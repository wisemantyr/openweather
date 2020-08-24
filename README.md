# Open Weather API Analysis
Matplotlib plots produced in a Jupyter Notebook using Python. Data obtained from the OpenWeather API. Cities were chosen from randomly generated latitude and longitude cooordinates using the random library. Data transformed and statistical analysis conducted with Pandas, NumPy, SciPy.

## WeatherPy Exercise Description

<i>In this example, you'll be creating a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator. To accomplish this, you'll be utilizing a simple Python library, the OpenWeatherMap API, and a little common sense to create a representative model of weather across world cities.</i>

<i>Your first objective is to build a series of scatter plots to showcase the following relationships:</i>
  - <i>Temperature (F) vs. Latitude </i>
  - <i> Humidity (%) vs. Latitude </i>
  - <i> Cloudiness (%) vs. Latitude </i>
  - <i> Wind Speed (mph) vs. Latitude </i>

<i>After each plot add a sentence or too explaining what the code is and analyzing.</i>

<i>Your next objective is to run linear regression on each relationship, only this time separating them into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude):</i>
  - <i> Northern Hemisphere - Temperature (F) vs. Latitude </i>
  - <i> Southern Hemisphere - Temperature (F) vs. Latitude </i>
  - <i> Northern Hemisphere - Humidity (%) vs. Latitude </i>
  - <i> Southern Hemisphere - Humidity (%) vs. Latitude </i>
  - <i> Northern Hemisphere - Cloudiness (%) vs. Latitude </i>
  - <i> Southern Hemisphere - Cloudiness (%) vs. Latitude </i>
  - <i> Northern Hemisphere - Wind Speed (mph) vs. Latitude </i>
  - <i> Southern Hemisphere - Wind Speed (mph) vs. Latitude </i>

<i>After each pair of plots explain what the linear regression is modelling such as any relationships you notice and any other analysis you may have.</i>

<i>Your final notebook must:</i>
  - <i>Randomly select at least 500 unique (non-repeat) cities based on latitude and longitude.</i>
  - <i>Perform a weather check on each of the cities using a series of successive API calls.</i>
  - <i>Include a print log of each city as it's being processed with the city number and city name.</i>
  - <i>Save a CSV of all retrieved data and a PNG image for each scatter plot.</i>
 
 ## VacationPy Exercise Description
<i>Now let's use your skills in working with weather data to plan future vacations. Use jupyter-gmaps and the Google Places API for this part of the assignment.</i>

1. <i> Create a heat map that displays the humidity for every city from WeatherPy.</i>
2. <i> Narrow down the DataFrame to find your ideal weather condition. </i>
3. <i> Using Google Places API to find the first hotel for each city located within 5000 meters of your coordinates. </i>
4. <i> Plot the hotels on top of the humidity heatmap with each pin containing the Hotel Name, City, and Country. </i>
