from modules.image_caption.core.ports.i_image_caption import IImageCaption

class ImageCaption(IImageCaption):
    def __init__(self, adapter: IImageCaption):
        self.__adapter = adapter

    def describe_image(self, url: str) -> str:
        return self.__adapter.describe_image(url)
