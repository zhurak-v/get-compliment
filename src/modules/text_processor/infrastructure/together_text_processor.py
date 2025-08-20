from modules.text_processor.infrastructure.together_client import TogetherClient
from modules.text_processor.core.ports.i_mode import IMode, ModeType
from modules.text_processor.core.ports.i_text_processor import ITextProcessor

class TogetherTextProcessor(ITextProcessor):
    def __init__(self, mode: IMode, client: TogetherClient):
        self.__mode = mode
        self.__client = client

    def process_text(self, text: str) -> str:
        model_names = self.__client.get_model_names()
        prompt = self.__build_prompt(text)

        last_error = None
        for model in model_names:
            try:
                return self.__client.create_completion(model, prompt)
            except Exception as err:
                last_error = err
                continue

        raise RuntimeError(f"All models failed. Last error: {last_error}")

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