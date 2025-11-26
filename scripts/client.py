import os
from dotenv import load_dotenv
import requests
class Client:
    def __init__(self):
        load_dotenv()
        self.__api_key = os.getenv("WEATHERAPI_KEY")
        self.__base_url = "http://api.weatherapi.com/v1"
        self.__method = {"current": "/current.json", "forecast": "/forecast.json"}

    def prepare_url(self, endpoint: str, query: str, day: int = None) -> str:
        if endpoint == "forecast":
            return f"{self.__base_url}{self.__method[endpoint]}?key={self.__api_key}&q={query}&days={day}"
        else:
            return f"{self.__base_url}{self.__method[endpoint]}?key={self.__api_key}&q={query}"

    def send_request(self, url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()