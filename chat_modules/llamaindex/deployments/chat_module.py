from llama_index.llms.ollama import Ollama
from typing import Union
from chat_modules.llamaindex.base_chat_module import StandardlizedChatModule
from system_components import Logger

class OllamaChatModule(StandardlizedChatModule):
    def __init__(self,
                 model_name: Union[str, None] = "zephyr",
                 temperature: float = 0.8,
                 max_tokens :int = 512
                 ):
        """Define embedding service with specified params"""
        super().__init__(temperature = temperature,max_tokens = max_tokens)
        # Set model
        self._model_name = model_name
        self._chat_model = Ollama(model=self._model_name, temperature=self.temperature)

        # Status
        Logger.info(f"Launch Chat Model with temperature {self.temperature}")