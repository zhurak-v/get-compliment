from transformers import BlipProcessor, BlipForConditionalGeneration

class BlipClient:
    def __init__(self, model_name: str = "Salesforce/blip-image-captioning-base"):
        self.__processor = BlipProcessor.from_pretrained(model_name, use_fast = False)
        self.__model = BlipForConditionalGeneration.from_pretrained(model_name)

    def get_processor(self) -> BlipProcessor:
        return self.__processor

    def get_model(self) -> BlipForConditionalGeneration:
        return self.__model

    def get_processor_and_model(self) -> tuple[BlipProcessor, BlipForConditionalGeneration]:
        return self.__processor, self.__model
