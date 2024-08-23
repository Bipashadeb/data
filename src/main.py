from weather_fetcher import get_weather
from outfit_recommender import recommender_outfit

def main():
    try:
        temp, weather_desc = get_weather()
        outfit = recommender_outfit(temp, weather_desc)
        print(f"The temperature is {temp}°C with {weather_desc}.")
        print(f"Recommended outfit: {outfit}")
    except Exception as e:
        print(e)

if __name__=="__main__":
    main()