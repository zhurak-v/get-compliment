# EXAMPLE

from modules.text_processor.core.services.text_proccessor import TextProccessor
from modules.text_processor.infrastructure.together_text_processor import TogetherTextProccessor
from modules.text_processor.infrastructure.together_client import TogetherClient
from modules.text_processor.core.services.mode import Mode
from modules.text_processor.core.ports.i_mode import ModeType;
from common.config.infrastructure.instance import config

together_client = TogetherClient(config.get_or_throw("TOGETHER_API_KEY", str))
mode = Mode()
together_adapter = TogetherTextProccessor(mode, together_client)
text_processor = TextProccessor(together_adapter)

print(text_processor.proccess_text("Hello"))

mode.set_mode(ModeType.INSULT)
print(text_processor.proccess_text("Hello"))