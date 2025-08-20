from modules.text_processor.core.ports.i_text_processor import ITextProcessor

class TextProcessor(ITextProcessor):
  def __init__(self, adapter: ITextProcessor):
    self.__adapter = adapter

  def process_text(self, input: str) -> str:
    return self.__adapter.process_text(input)