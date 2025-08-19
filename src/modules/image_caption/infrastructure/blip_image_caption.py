from PIL import Image
import requests
import torch

from modules.image_caption.core.ports.i_image_caption import IImageCaption
from modules.image_caption.infrastructure.blip_client import BlipClient

class BlipImageCaption(IImageCaption):
    def __init__(self):
        self.__device = "cuda" if torch.cuda.is_available() else "cpu"
        self.__processor, self.__model = BlipClient().get_processor_and_model()
        self.__model = self.__model.to(self.__device)

    def describe_image(self, url: str) -> str:
        image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
        inputs = self.__processor(image, return_tensors="pt")
        inputs = { k: v.to(self.__device) for k, v in inputs.items() }

        with torch.no_grad():
            output_ids = self.__model.generate(
                **inputs,
                max_length=10,
                num_beams=5,
                no_repeat_ngram_size=2,
                early_stopping=True,
                do_sample=True,
                temperature=0.8,
                top_k=50,
                top_p=0.9,
                num_return_sequences=3,
                length_penalty=1.0,
                repetition_penalty=1.2,
            )

        return self.__processor.decode(output_ids[0], skip_special_tokens=True)
