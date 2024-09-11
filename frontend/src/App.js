import React, { useState } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');
  const [mappedData, setMappedData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const onDrop = acceptedFiles => {
    const uploadedFile = acceptedFiles[0];
    setFile(uploadedFile);
    setFileName(uploadedFile.name);


    alert(`File uploaded: ${uploadedFile.name}`);

  };

  const handleSubmit = async () => {
    if (!file) {
      setError('Please upload a CSV file first.');
      return;
    }

    setLoading(true);
    setMappedData(null);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
    
      const response = await axios.post('http://localhost:8000/api/uploadcsv/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

 
      const parsedOutput = response.data.output
        .split('\n')
        .map(row => row.split('|').map(cell => cell.trim())); 

      const headerRemovedData = parsedOutput.slice(1);

      setMappedData(headerRemovedData);
      setLoading(false);
    } catch (err) {
      console.error('Error processing CSV:', err);

      if (err.response && err.response.data && err.response.data.error) {
        setError(err.response.data.error);
      } else {
        setError('There was an error processing the CSV file.');
      }

      setLoading(false);
    }
  };

  const { getRootProps, getInputProps } = useDropzone({
    onDrop,
    accept: '.csv',
  });

  const handleChooseFilesClick = () => {
    document.getElementById('file-input').click();
  };

  return (
    <div className="container">
      <div className="dropzone-container">
          <h3>Csv-Uploader</h3>
        <div
          className="dropzone"
          {...getRootProps()}
        >
          <input {...getInputProps()} id="file-input" style={{ display: 'none' }} />
          <p>Drag and drop your CSV file here</p>
        </div>
        <div className="dropzone-content">
          <button
            type="button"
            onClick={handleChooseFilesClick}
          >
            Choose Files
          </button>
          {fileName && <p className="uploaded-file">Uploaded file: {fileName}</p>}
          {file && (
            <button className="btn btn-primary" style={{ backgroundColor: '#041512', borderColor: '#041512' }} onClick={handleSubmit}>
              Submit
            </button>
          )}
        </div>
      </div>
      <div className="main-content">
        {loading && <p>Processing file, please wait...</p>}
        {error && <p className="text-danger">{error}</p>}
        {mappedData && (
          <div>
            <h2>Mapped Data</h2>
            <table className="table table-bordered">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Class</th>
                  <th>School</th>
                  <th>State</th>
                </tr>
              </thead>
              <tbody>
                {mappedData.map((row, index) => (
                  <tr key={index}>
                    <td>{row[0]}</td>
                    <td>{row[1]}</td>
                    <td>{row[2]}</td>
                    <td>{row[3]}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
