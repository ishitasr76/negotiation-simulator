"""
This service provides methods to interact with the OpenAI API.

It encapsulates OpenAI API calls and provides a clean interface
for making AI completion requests using Pydantic models for response parsing.
"""

from env import getenv
from typing import Type, TypeVar
from pydantic import BaseModel
from openai import OpenAI
from openai.types.chat import ChatCompletion

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2025"
__license__ = "MIT"

T = TypeVar("T", bound=BaseModel)

# Load API key and model from environment
API_KEY = getenv("OPENAI_API_KEY")
MODEL = getenv("OPENAI_MODEL", default="gpt-4o")


class OpenAIService:
    """Service for interacting with OpenAI's chat API using a reusable client."""

    def __init__(self):
        self._client = OpenAI(api_key=API_KEY)
        self._model = MODEL

    def prompt(self, system_prompt: str, user_prompt: str, response_model: Type[T]) -> T:
        """Send a system/user prompt and return parsed model of the response."""
        response: ChatCompletion = self._client.chat.completions.create(
            model=self._model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content
        if not content:
            raise ValueError("OpenAI returned an empty response.")

        return response_model.model_validate_json(content)
