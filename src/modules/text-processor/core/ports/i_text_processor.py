from abc import ABC, abstractmethod

class ITextProccesor(ABC): 
  @abstractmethod
  def proccess_text(input: str) -> str:
    pass