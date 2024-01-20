import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  // State to store the weather status
  const [status, setStatus] = useState('Checking Weather...');

  // useEffect hook to fetch data when the component mounts
  useEffect(() => {
    // Function to fetch weather data
    const fetchData = async () => {
      try {
        // Making a GET request to the '/check-weather' endpoint
        const response = await axios.get('/check-weather');
        // Updating the status state with the fetched data
        setStatus(response.data);
      } catch (error) {
        // Handling errors and updating the status state
        console.error(error);
        setStatus('Error checking weather');
      }
    };

    // Calling the fetchData function
    fetchData();
  }, []); // Empty dependency array ensures the useEffect runs only once on mount

  // JSX to render the component
  return (
    <div>
      {/* Header */}
      <h1>Music App</h1>

      {/* Displaying the weather status */}
      <p>Status: {status}</p>
    </div>
  );
};

export default App;
