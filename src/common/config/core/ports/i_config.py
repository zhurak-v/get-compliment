from typing import TypeVar, Generic, Type
from abc import ABC, abstractmethod

T = TypeVar('T', str, int, float, bool)

class IConfig(Generic[T], ABC): 
  @abstractmethod
  def get_or_throw(self, key: str, type: Type[T]) -> T:
    pass