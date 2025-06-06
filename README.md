# API-INTEGRATION-AND-DATA-VISUALIZATIONS

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KAMIREDDY CHANDU SAI

*INTERN ID*: CT04DF282

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIOTION*:
This Python script is designed to retrieve real-time weather information for a specified city—Hyderabad in this case—using the OpenWeatherMap API, and then visually present some of the key weather parameters such as temperature and humidity. The program involves several important steps, starting from making a web request to processing the response and finally creating a graphical representation of the data.

First, the script sets up the necessary environment by importing essential libraries. These libraries enable it to send HTTP requests, handle data in tabular form, and generate visualizations. The program relies on a weather API key and the city name to dynamically construct the URL endpoint for accessing current weather data. The URL includes parameters for location, the API authentication token, and the unit system—metric units are used here to express temperature in degrees Celsius.

Once the URL is formed, the script sends a GET request to the API server. The response returned by the server is a JSON-formatted string, which the script then converts into a dictionary-like structure for easy data manipulation. The script checks the status of this response to ensure the request was successful before attempting to extract any data. If the response is positive, it proceeds to parse the main weather data points—specifically, the current temperature, humidity level, and a brief textual description of the weather conditions (such as “clear sky” or “scattered clouds”).

These extracted values are then displayed in the console as a simple textual report, providing an immediate overview of the current weather conditions for the city in question. This helps users quickly see the results without needing to analyze raw data.

To facilitate visualization, the script organizes the temperature and humidity values into a structured tabular format using a data manipulation library. This organization makes it straightforward to plot the data using visualization libraries that specialize in statistical graphics.

The visualization component generates a bar chart that clearly compares the temperature and humidity side by side. The chart is styled with a modern color palette to enhance readability and aesthetic appeal. It includes descriptive labels for both axes, a title reflecting the city name, and grid lines to help viewers interpret the values more precisely. This graphical representation allows for an intuitive and immediate understanding of the weather conditions, especially useful for presentations or reports.

In the event the API call fails—due to network issues, incorrect API keys, or invalid city names—the script is designed to handle these errors gracefully. Instead of crashing or producing confusing output, it prints an informative error message indicating the problem, which aids troubleshooting.

Overall, this script exemplifies how to combine data retrieval from online sources with data processing and visualization tools to create informative, user-friendly weather reports. It demonstrates important programming concepts such as API interaction, error handling, data manipulation, and graphical data presentation in a cohesive and practical manner.

The modular design of the program also means it can be easily adapted or expanded to include additional weather parameters (like wind speed or atmospheric pressure), or to fetch weather data for other cities. This makes it a versatile tool for both casual users interested in daily weather updates and developers learning how to integrate real-world data into Python applicationS

#OUTPUT

![Image](https://github.com/user-attachments/assets/3999a9ce-f737-4458-97c8-b2d1f2028d21)
