from abc import ABC, abstractmethod
from enum import Enum

class ModeType(str, Enum):
    COMPLIMENT = "COMPLIMENT"
    INSULT = "INSULT"

class IMode(ABC): 
  @abstractmethod
  def get_mode(self) -> ModeType:
    pass

  @abstractmethod
  def set_mode(self, variant: ModeType) -> None:
    pass