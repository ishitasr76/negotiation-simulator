from fastapi import APIRouter, Depends
from ..models.negotiation import NegotiationInput, NegotiationOutput
from ..services.negotiation_service import generate_negotiation_response
from ..services.openai import OpenAIService, openai_client
from openai import AzureOpenAI

router = APIRouter()

@router.post("/negotiation", response_model=NegotiationOutput)
def handle_negotiation(
    input_data: NegotiationInput,
    client: AzureOpenAI = Depends(openai_client)
):
    """Route that accepts negotiation input and returns a generated response."""
    service = OpenAIService(client)
    return generate_negotiation_response(input_data, service)
