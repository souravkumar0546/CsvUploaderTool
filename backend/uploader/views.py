import requests
import csv
from io import StringIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings


GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'
GEMINI_API_KEY = settings.API_KEY  # Replace with your actual Gemini API key

@csrf_exempt
@require_POST
def upload_csv(request):
    # Get the CSV file from the request
    file = request.FILES.get('file')

    if not file:
        return JsonResponse({'error': 'No file provided. Please upload a CSV file.'}, status=400)

    # Read the CSV file content as raw text
    try:
        csv_file_content = file.read().decode('utf-8')
    except UnicodeDecodeError:
        return JsonResponse({'error': 'File encoding is not supported. Please upload a UTF-8 encoded CSV file.'}, status=400)

    # Process CSV data
    csv_file = StringIO(csv_file_content)
    reader = csv.reader(csv_file)

    rows = []
    max_columns = 10

    for row in reader:
        processed_row = [cell.strip() for cell in row]
        if any(processed_row):
            processed_row = processed_row[:max_columns]
            rows.append(processed_row)

    # Create the formatted CSV data for Gemini
    formatted_data = '\n'.join([','.join(row) for row in rows])

    # Construct prompt for Gemini API
    prompt = f"""Hi Gemini, map the CSV data to this output structure:
The output structure is:
Name | Class | School | State
Each class entry should be a separate row, even if the Name, School, or State are repeated.

Example csv:
First Name,Last Name,Class 1,Class 2,School,Location
Beth,Smith,English,Math,Harvard,Boston
Rahul,Shankar,Physics,Chemistry,Stanford,Palo Alto

Gemini's output(only this):
Name | Class | School | State
Beth Smith | English | Harvard | MA
Beth Smith | Math | Harvard | MA
Rahul Shankar | Physics | Stanford | CA
Rahul Shankar | Chemistry | Stanford | CA

Here is the CSV data:
{formatted_data}

Gemini's output (only this):
Name | Class | School | State"""
    
    # Call the Gemini API
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            json=payload,
            headers=headers
        )
        
        response.raise_for_status()

        response_data = response.json()

        

        # Check if 'candidates' exists in the response
        if 'candidates' in response_data and response_data['candidates']:
            gemini_output = response_data['candidates'][0]['content']['parts'][0]['text']
            # Validate if the response starts with the expected header
            if gemini_output.strip().startswith("Name | Class | School | State"):
                # Check if there's any actual data after the header
                if len(gemini_output.strip().split('\n')) > 1:
                    return JsonResponse({"output": gemini_output})
                else:
                    return JsonResponse({'error': 'Gemini response is empty. No data to populate.'}, status=400)
            else:
                return JsonResponse({'error': 'Invalid data structure in Gemini response. Expected format: Name | Class | School | State.'}, status=400)
        else:
            return JsonResponse({'error': 'Invalid response structure from Gemini API. Response does not contain expected data.'}, status=500)

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return JsonResponse({'error': f'API request failed: {str(e)}. Please try again later.'}, status=500)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}.'}, status=500)
