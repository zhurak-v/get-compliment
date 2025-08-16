import os
from typing import TypeVar, Type, cast
from dotenv import load_dotenv
from common.config.core.ports.i_config import IConfig
from common.error.error_handler import ErrorHandler

T = TypeVar('T', str, int, float, bool)

class Config(IConfig[T]):
  def __init__(self, env_path: str):
    load_dotenv(env_path)
    self.__env = os.environ
    
  def __cast(self, value: str, type: Type[T], key: str) -> T:
    try:
      if type == str:
        return cast(T, value)
      if type == int:
        return cast(T, int(value))
      if type == float:
        return cast(T, float(value))
      if type == bool:
        lowered = value.lower()
        if lowered in ['true', '1', 'yes', 'on']:
          return cast(T, True)
        elif lowered in ['false', '0', 'no', 'off']:
          return cast(T, False)
        else:
            raise ErrorHandler(
              f"Cannot cast value '{value}' to bool",
              code=422,
              context={"key": key, "value": value}
            )
      raise ErrorHandler(
        f"Unsupported type: {type}",
        code=500,
        context={"key": key, "type": str(type)}
      )
    except ValueError as err:
      raise ErrorHandler(
        f"Cannot cast value '{value}' to {type.__name__}",
          code=422,
          context={"key": key, "value": value}
      ) from err
    
  def get_or_throw(self, key: str, type: Type[T]) -> T:
    value = self.__env.get(key)
    if value is None:
      raise ErrorHandler(
        f"Environment variable '{key}' is not set",
        code=500,
        context={"key": key}
      )
    return self.__cast(value, type, key)
    
