import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api_key = '987106004b82154021206c799447e119'  # Your API key
city = 'Hyderabad'

# Correct URL with proper f-string variable usage
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    # Extract relevant data
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

    # Create a simple DataFrame for visualization
    weather_df = pd.DataFrame({
        'Metric': ['Temperature (°C)', 'Humidity (%)'],
        'Value': [temperature, humidity]
    })

    # Create a bar plot using Seaborn
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Metric', y='Value', data=weather_df, palette='viridis')
    plt.title(f'Current Weather in {city}')
    plt.xlabel('Weather Metric')
    plt.ylabel('Value')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

else:
    print(f"Error fetching data: {data.get('message', 'Unknown error')}")
