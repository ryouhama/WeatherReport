from typing import Optional, Type
from json import dumps as json_dumps
from pydantic import BaseModel
from langchain.tools import BaseTool
import os
from src.apis.open_weather.one_call_api import OneCallApiParams, OneCallApi


class OpenWeathreTool(BaseTool):
    name = 'get_weather'
    description = 'Acquire current weather at a specified location.'
    args_schema: Optional[Type[BaseModel]] = OneCallApiParams

    def _run(
        self,
        lat: float,
        lon: float
    ) -> str:
        params = OneCallApiParams(
            lat=lat,
            lon=lon
        )
        api_key = os.getenv("OPEN_WEATHER_API_KEY")
        api = OneCallApi(api_key=api_key)
        response = api.get(params)
        return json_dumps(response, ensure_ascii=False)

    async def _arun(self, *args, **kwargs) -> str:
        raise NotImplementedError("GetWeatherTool does not support async")
