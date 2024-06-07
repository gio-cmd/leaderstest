const cityInput = document.getElementById('cityInput'); // Get the city input element
const apiKey = '95da03f5bd59f14f34ca3e257b952f8f'; // API key
const weatherData = document.getElementById('weatherData'); // Get the weather data element

async function getWeather() { // Create a main function
    try {
        const city = cityInput.value; // Get the inputted city value
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`; // API URL
        const response = await fetch(url); // Fetch the result of the input, also use await to wait for the response
        const data = await response.json(); // Transform data into JSON
        if (data.cod == 200) { // Check if the successful response returned
            weatherData.innerHTML = `
                <p>City: ${data.name}</p>
                <p>Temperature: ${data.main.temp} Celsius</p>
                <p>Weather: ${data.weather[0].description}</p>
            `;
        } else {
            weatherData.innerHTML = `<p>${data.message}</p>`;
        }
    } catch (error) {
        weatherData.innerHTML = `<p>Error while getting data</p>`;
    }
}

document.getElementById('getWeatherButton').addEventListener('click', getWeather);