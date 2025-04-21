"""
This service provides methods to interact with the OpenAI API.

It encapsulates OpenAI API calls and provides a clean interface
for making AI completion requests using Pydantic models for response parsing.
"""

import openai
from env import getenv
from typing import Type, TypeVar
from pydantic import BaseModel

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2025"
__license__ = "MIT"

T = TypeVar("T", bound=BaseModel)

API_KEY = getenv("OPENAI_API_KEY")
MODEL = getenv("OPENAI_MODEL", default="gpt-4o")  # or gpt-3.5-turbo, etc.

# Configure OpenAI globally
openai.api_key = API_KEY


class OpenAIService:
    """Service for interacting with OpenAI's API using chat completions."""

    _model: str = MODEL

    def __init__(self):
        pass

    def prompt(self, system_prompt: str, user_prompt: str, response_model: Type[T]) -> T:
        """Send a prompt to the OpenAI API and parse response into a Pydantic model."""
        response = openai.ChatCompletion.create(
            model=self._model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.7,
        )

        content = response["choices"][0]["message"]["content"]

        if not content:
            raise ValueError("No content returned from OpenAI API")

        return response_model.model_validate_json(content)
