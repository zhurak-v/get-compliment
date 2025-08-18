from abc import ABC, abstractmethod

class ITextProccesor(ABC): 
  @abstractmethod
  def proccess_text(self, input: str) -> str:
    pass