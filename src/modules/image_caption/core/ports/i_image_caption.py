from abc import ABC, abstractmethod

class IImageCaption(ABC):
    @abstractmethod
    def describe_image(self, url: str) -> str:
        pass
