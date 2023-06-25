from pydantic import Field, BaseModel
from enum import Enum


class WeatherUnit(str, Enum):
    """
    天気の単位
    """
    celcius = "celcius"
    fahrenheit = "fahrenheit"


class WeatherInputSchema(BaseModel):
    """
    天気情報取得の入力パラメータ
    """
    location: str = Field(..., description='city_and_state')
    unit: WeatherUnit
