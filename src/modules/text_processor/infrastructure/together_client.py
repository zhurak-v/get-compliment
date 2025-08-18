from together import Together

priority_order = [
    "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    "deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
    "google/gemma-3-27b-it",
    "Qwen/Qwen3-32B-FP8",
    "lgai/exaone-3-5-32b-instruct",
    "lgai/exaone-deep-32b",
    "arcee-ai/AFM-4.5B",
    "togethercomputer/MoA-1-Turbo",
    "togethercomputer/MoA-1",
    "black-forest-labs/FLUX.1.1-pro",
    "black-forest-labs/FLUX.1-pro",
    "black-forest-labs/FLUX.1-dev-lora",
    "black-forest-labs/FLUX.1-dev",
    "black-forest-labs/FLUX.1-redux",
    "black-forest-labs/FLUX.1-kontext-pro",
    "black-forest-labs/FLUX.1-kontext-max",
    "black-forest-labs/FLUX.1-kontext-dev",
    "black-forest-labs/FLUX.1-schnell",
    "black-forest-labs/FLUX.1-schnell-Free",
    "black-forest-labs/FLUX.1-canny",
    "black-forest-labs/FLUX.1-depth"
]
class TogetherClient:
    def __init__(self, api_key: str):
        self.__client = Together(api_key=api_key)
        available_models = [
            model.id for model in self.__client.models.list()
            if all(getattr(model.pricing, key) == 0 for key in ("hourly", "base", "input", "output"))
        ]
        self.__model_names = [m for m in priority_order if m in available_models]

    def create_completion(self, model_name: str, prompt: str) -> str:
        response = self.__client.chat.completions.create(
            model = model_name,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
    
    def get_model_names(self):
        return self.__model_names