from modules.text_processor.core.ports.i_mode import IMode, ModeType

class Mode(IMode):
  def __init__(self, variant: ModeType):
        self.__mode: ModeType = variant

  def get_mode(self) -> ModeType:
    return self.__mode

  def set_mode(self, variant: ModeType) -> None:
    self.__mode = variant