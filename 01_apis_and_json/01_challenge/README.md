Let's create a weather **[CLI](https://en.wikipedia.org/wiki/Command-line_interface)** utilizing the OpenWeatherMap API you saw in exercise 3. The user flow should be as follows (in pseudo-code):

1. Start the app with **`python weather.py`**
2. Prompt the user to enter a city name
3. If the city is unknown to the API, display an error message and return to step 2.
4. Retrieve and display the weather forecast for the next 5 days (date, weather, and maximum temperature in °C)
5. Return to step 2 (loop to request a new city)
6. Use **`Ctrl+C`** at any time to exit the program

The actual execution should resemble:

```python
> python weather.py
City?
> london
Here's the weather in London
2020-09-30: Heavy Rain 16.4°C
2020-10-01: Light Rain 15.1°C
2020-10-02: Heavy Rain 13.4°C
2020-10-03: Heavy Rain 14.3°C
2020-10-04: Heavy Rain 14.6°C
City?
> 
```

create a file called **`weather.py`** and create the following three functions:

- **`search_city(query)`**
- **`weather_forecast(lat, lon)`**
- **`main()`**

Implement them **in the specified order**. Make sure to check their functionality as you go along by running the program in the CLI with **`python weather.py`** .

1. Begin with the **`search_city`** function, which should return a **`dictionary`** containing comprehensive information about the city, including **`lat`** and **`lon`**.
2. Proceed to the **`weather_forecast`** function, which accepts the city's **`lat`** and **`lon`** as arguments and returns a five-day forecast (ensure the function returns a **`list`** of dictionaries). **NOTE**: OpenWeatherMap provides a forecast for every 3 hours, so you will need to refine the results to display only one forecast per day.
3. Complete the challenge by coding the **`main`** function, which will be executed when you run the **`weather.py`** file from the terminal. Determine which functions should be called within **`main`** and the appropriate order.

**City List**

After **`step 3`**, if the user input is ambiguous (i.e., several cities are returned from the search), display the options and prompt the user to select one by index, as shown below:

```
City?
> Pari
1. Paris,FR
2. Paris,FR
3. Paris,FR
4. Pari,IT
5. Puri,IN
Multiple matches found, which city did you mean?
> 1
2022-09-26: Clouds (12°C)
2022-09-27: Clouds (10°C)
2022-09-28: Rain (12°C)
2022-09-29: Clouds (11°C)
2022-09-30: Clear (10°C)
```

💡 **Hint 1:** The built-in **[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)** function could be helpful.

💡 **Hint 2:** By default, the API does not return multiple options for a given query **`q`**. Add the **`limit=`** parameter to your URL to ensure that the API returns the specified number of options (e.g.  `**https://api.openweathermap.org/geo/1.0/direct?q=Barcelona&limit=5&appid=XXXXXXXXXXX**` will return 5 options for Barcelona, if available).