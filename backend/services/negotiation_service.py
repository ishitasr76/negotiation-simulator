from typing import Annotated
from fastapi import Depends
from ..env import get_session
from openai import OpenAIService
from ..models.negotiation import NegotiationInput, NegotiationOutput

class NegotiationService:
    def __init__(
        self,
        openai_svc: Annotated[OpenAIService, Depends(OpenAIService)],
    ):
        self._openai_svc = openai_svc

    def generate_negotiation_summary(self, input_data: NegotiationInput) -> NegotiationOutput:
        scenario = input_data.scenario
        stakeholders = input_data.stakeholders
        negotiation_type = input_data.negotiation_type
        frameworks = input_data.frameworks

        system_prompt = (
            "You are a negotiation simulator assistant that generates mock negotiation summaries "
            "based on scenario details, stakeholder roles, and philosophical frameworks."
        )

        user_prompt = f"""
        Scenario: {scenario}

        Stakeholders:
        {chr(10).join([f"- {s['name']} ({s['role']}): {s['description']}" for s in stakeholders])}

        Negotiation Type: {negotiation_type}
        Philosophical Frameworks: {', '.join(frameworks)}

        Please generate a summary of how this negotiation might unfold. Be thoughtful.
        """

        response = self._openai_svc.prompt(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            response_model=NegotiationOutput
        )

        return response