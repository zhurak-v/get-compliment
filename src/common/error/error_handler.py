class ErrorHandler(Exception):
    def __init__(self, message: str, *, code: int = 500, context: dict = None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.context = context or {}

    def __str__(self) -> str:
        return f"[Error {self.code}] {self.message}"

    def to_dict(self) -> dict:
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "code": self.code,
            "context": self.context,
        }