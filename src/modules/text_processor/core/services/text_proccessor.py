from modules.text_processor.core.ports.i_text_processor import ITextProccesor

class TextProccessor(ITextProccesor):
  def __init__(self, adapter: ITextProccesor):
    self.__adapter = adapter

  def proccess_text(self, input: str) -> str:
    return self.__adapter.proccess_text(input)