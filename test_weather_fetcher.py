import unittest
from src.weather_fetcher import get_weather

class TestWeatherfetcher(unittest.TestCase):
    def test_get_weather(self):
        temp,description = get_weather()


        self.assertIsInstance(temp, (int,float), "Temperature should be number")
        self.assertIsInstance(description , str, "weather description")

    
if __name__ == '__main__':
    unittest.main()