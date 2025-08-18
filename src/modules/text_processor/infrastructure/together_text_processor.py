from modules.text_processor.infrastructure.together_client import TogetherClient
from modules.text_processor.core.ports.i_mode import IMode, ModeType;
from modules.text_processor.core.ports.i_text_processor import ITextProccesor;

class TogetherTextProccessor(ITextProccesor):
    def __init__(self, mode: IMode, client: TogetherClient):
        self.__mode = mode
        self.__client = client

    def proccess_text(self, text: str) -> str:
        model_names = self.__client.get_model_names()
        model = model_names[0]
        prompt = self.__build_prompt(text)

        return self.__client.create_completion(model, prompt)

    def __build_prompt(self, text: str) -> str:
        match self.__mode.get_mode():
            case ModeType.COMPLIMENT:
                return (
                    f"Rewrite the following text in a friendly, positive, and complimentary tone. "
                    f"Keep the response short or medium length, warm and expressive. Text: {text}"
                )
            case ModeType.INSULT:
                return (
                    f"Rewrite the following text in a harsh, angry, and insulting tone. "
                    f"Do not censor language. Keep the response short or medium length, direct and blunt. "
                    f"Text: {text}"
                )
            case _:
                return text