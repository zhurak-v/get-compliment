from modules.image_caption.core.ports.i_image_caption import IImageCaption
from modules.text_processor.core.ports.i_mode import IMode
from abc import ABC

class IGetCompliment(IImageCaption, IMode, ABC):
    pass