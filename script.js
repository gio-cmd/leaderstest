const cityInput = document.getElementById('cityInput'); // Get the city input element
const apiKey = '95da03f5bd59f14f34ca3e257b952f8f'; // API key
const weatherData = document.getElementById('weatherData'); // Get the weather data element
const weatherImage = document.getElementById('weatherImage'); // Get the weather image element

// Object mapping weather descriptions to image URLs
const weatherImages = {
    'clear sky': 'clear.png',
    'few clouds': 'clouds.png',
    'scattered clouds': 'drizzle.png',
    'broken clouds': 'https://example.com/broken-clouds.jpg',
    'shower rain': 'https://example.com/shower-rain.jpg',
    'rain': 'https://example.com/rain.jpg',
    'thunderstorm': 'https://example.com/thunderstorm.jpg',
    'snow': 'https://example.com/snow.jpg',
    'mist': 'https://example.com/mist.jpg'
};

async function getWeather() { // Create a main function
    try {
        const city = cityInput.value; // Get the inputted city value
        const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`; // API URL
        const response = await fetch(url); // Fetch the result of the input, also use await to wait for the response
        const data = await response.json(); // Transform data into JSON
        if (data.cod == 200) { // Check if the successful response returned
            const weatherDescription = data.weather[0].description;
            const imageUrl = weatherImages[weatherDescription] || 'https://example.com/default-weather.jpg';

            weatherData.innerHTML = `
                <p>City: ${data.name}</p>
                <p>Temperature: ${data.main.temp} Celsius</p>
                <p>Weather: ${weatherDescription}</p>
            `;
            
            weatherImage.src = imageUrl;
            weatherImage.style.display = 'block';
        } else {
            weatherData.innerHTML = `<p>${data.message}</p>`;
            weatherImage.style.display = 'none';
        }
    } catch (error) {
        weatherData.innerHTML = `<p>Error while getting data</p>`;
        weatherImage.style.display = 'none';
    }
}

document.getElementById('getWeatherButton').addEventListener('click', getWeather);
