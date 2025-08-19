# EXAMPLE

from modules.text_processor.core.services.text_proccessor import TextProccessor
from modules.text_processor.infrastructure.together_text_processor import TogetherTextProccessor
from modules.text_processor.infrastructure.together_client import TogetherClient
from modules.text_processor.core.services.mode import Mode
from modules.text_processor.core.ports.i_mode import ModeType;
from modules.image_caption.infrastructure.blip_image_caption import BlipImageCaption
from modules.image_caption.core.services.image_caption import ImageCaption
from common.config.infrastructure.instance import config

# together_client = TogetherClient(config.get_or_throw("TOGETHER_API_KEY", str))
# mode = Mode()
# together_adapter = TogetherTextProccessor(mode, together_client)
# text_processor = TextProccessor(together_adapter)

# print(text_processor.proccess_text("Hello"))

# mode.set_mode(ModeType.INSULT)
# print(text_processor.proccess_text("Hello"))

blip_adapter = BlipImageCaption()
image_caption = ImageCaption(blip_adapter)

print(image_caption.describe_image("https://www.wikihow.com/images/thumb/f/f9/Playfully-Tease-Girls-Step-13.jpg/v4-728px-Playfully-Tease-Girls-Step-13.jpg.webp"))
