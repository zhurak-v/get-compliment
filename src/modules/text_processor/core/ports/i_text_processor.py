from abc import ABC, abstractmethod

class ITextProcessor(ABC):
  @abstractmethod
  def process_text(self, caption: str) -> str:
    pass