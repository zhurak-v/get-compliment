from application.core.ports.i_get_compliment import IGetCompliment
from modules.text_processor.core.ports.i_mode import ModeType

class GetCompliment(IGetCompliment):
    def __init__(self, adapter: IGetCompliment):
        self.__adapter = adapter

    def get_mode(self) -> ModeType:
        return self.__adapter.get_mode()

    def set_mode(self, variant: ModeType) -> None:
        self.__adapter.set_mode(variant)

    def describe_image(self, url: str) -> str:
        return self.__adapter.describe_image(url)