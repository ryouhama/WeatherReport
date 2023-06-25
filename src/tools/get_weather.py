from typing import Optional, Type
from json import dumps as json_dumps
from pydantic import BaseModel
from langchain.tools import BaseTool
from src.models.weather import WeatherInputSchema, WeatherUnit


class GetWeatherTool(BaseTool):
    name = 'get_weather'
    description = 'Acquire current weather at a specified location.'
    args_schema: Optional[Type[BaseModel]] = WeatherInputSchema

    def _run(
        self,
        location: str,
        unit: str = WeatherUnit.celcius.value
    ) -> str:
        weather_info = {
            "location": location,
            "temperature": "72",
            "unit": unit,
            "forecast": ["sunny", "windy"],
        }
        return json_dumps(weather_info)

    async def _arun(self, location: str, unit: str) -> str:
        raise NotImplementedError("GetWeatherTool does not support async")
