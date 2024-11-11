from .needs_auth.Openai import Openai
import requests as _requests
import secrets as _secrets

class PollinationsAI(Openai):
  label = "Pollinations AI"
  url = "https://pollinations.ai/"
  working = True
  needs_auth = False
  supports_message_history = True
  supports_system_message = True
  default_model = "openai"
  models = [i["name"] for i in _requests.get("https://text.pollinations.ai/models").json()]
  model_aliases = {
    "gpt-4o": "openai",
    "gpt-4o-mini": "openai"
  }
  @classmethod
  async def create_async_generator(
        cls,
        **kwargs
    ) -> AsyncResult:
      kwargs["api_key"] = _secrets.token_hex(16)
      kwargs["api_base"] = "https://text.pollinations.ai/openai"
      return await super().create_async_generator(cls, **kwargs)
