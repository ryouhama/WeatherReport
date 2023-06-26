import requests
from typing import Any
from pydantic import Field, BaseModel


class OneCallApiParams(BaseModel):
    lat: float = Field(..., description='latitude of the location')
    lon: float = Field(..., description='longitude of the location')

    def __post_init__(self) -> None:
        self.lat = round(self.lat, 2)
        self.lon = round(self.lon, 2)

    def to_param(self) -> str:
        params = [
            f"lat={self.lat}",
            f"lon={self.lon}",
            "exclude=hourly,minutely,alerts",
            "units=metric",
            "lang=ja"
        ]
        return "&".join(params)


class OneCallApi:
    api_key: str
    url = "https://api.openweathermap.org/data/3.0/onecall"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get(self, params: OneCallApiParams) -> dict[str, Any]:
        response = requests.get(
            f"{self.url}?{params.to_param()}&appid={self.api_key}"
        )
        return OneCallApiJsonFormatter.format(response.json())


class OneCallApiJsonFormatter:
    @classmethod
    def format(cls, data: dict[str, Any]) -> dict[str, Any]:
        return {
            "lat": data["lat"],
            "lon": data["lon"],
            "timezone": data["timezone"],
            "timezone_offset": data["timezone_offset"],
            "current": cls.__format_to_weather_info(data["current"]),
            "daily": [
                cls.__format_to_weather_info(it)
                for it in data["daily"]
            ]
        }

    @classmethod
    def __format_to_weather_info(cls, data: dict[str, Any]) -> dict[str, Any]:
        return {
                key: value
                for key, value in data.items()
                if key not in [
                    "feels_like",
                    "pressure",
                    "dew_point",
                    "uvi",
                    "visibility",
                    "wind_speed",
                    "wind_gust",
                    "wind_deg"
                ]
            }
