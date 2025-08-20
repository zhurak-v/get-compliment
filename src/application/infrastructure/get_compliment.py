from application.core.ports.i_get_compliment import IGetCompliment
from modules.image_caption.core.services.image_caption import ImageCaption
from modules.image_caption.infrastructure.blip_image_caption import BlipImageCaption
from modules.text_processor.core.ports.i_mode import ModeType
from modules.text_processor.core.ports.i_text_processor import ITextProcessor
from modules.text_processor.core.services.mode import Mode, IMode
from modules.text_processor.core.services.text_processor import TextProcessor
from modules.text_processor.infrastructure.together_client import TogetherClient
from modules.text_processor.infrastructure.together_text_processor import TogetherTextProcessor
from common.config.infrastructure.instance import config

class GetComplimentService(IGetCompliment):
    def __init__(self):
        together_api_key = config.get_or_throw("TOGETHER_API_KEY", str)
        together_client = TogetherClient(together_api_key)
        variant: ModeType = ModeType.COMPLIMENT
        self.__mode: IMode = Mode(variant)
        together_text_processor: ITextProcessor = TogetherTextProcessor(self.__mode, together_client)
        self.__text_processor = TextProcessor(together_text_processor)
        blip_image_caption = BlipImageCaption()
        self.__image_caption = ImageCaption(blip_image_caption)


    def get_mode(self) -> ModeType:
        return self.__mode.get_mode()

    def set_mode(self, variant: ModeType) -> None:
        self.__mode.set_mode(variant)

    def describe_image(self, url: str) -> str:
        caption: str = self.__image_caption.describe_image(url)
        return self.__text_processor.process_text(caption)

