import unittest
from weather import search_city, weather_forecast

class TestWeatherCLI(unittest.TestCase):

    def test_search_city_returns_dict(self):
        city = 'New York'
        result = search_city(city)
        self.assertIsInstance(result, dict)

    def test_search_city_has_lat_lon(self):
        city = 'New York'
        result = search_city(city)
        self.assertIn('lat', result)
        self.assertIn('lon', result)

    def test_weather_forecast_returns_list(self):
        dummy_lat, dummy_lon = 40.7128, -74.0060
        result = weather_forecast(dummy_lat, dummy_lon)
        self.assertIsInstance(result, list)

    def test_weather_forecast_list_non_empty(self):
        dummy_lat, dummy_lon = 40.7128, -74.0060
        result = weather_forecast(dummy_lat, dummy_lon)
        self.assertTrue(len(result) > 0)

    def test_weather_forecast_each_entry_is_dict(self):
        dummy_lat, dummy_lon = 40.7128, -74.0060
        result = weather_forecast(dummy_lat, dummy_lon)
        for entry in result:
            self.assertIsInstance(entry, dict)

if __name__ == '__main__':
    unittest.main()

