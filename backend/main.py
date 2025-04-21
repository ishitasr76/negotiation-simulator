from fastapi import FastAPI, Body, Depends
from typing import Annotated
from models.negotiation import NegotiationInput, NegotiationOutput
from services.openai import OpenAIService, openai_client

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from NegotiationSim"}


@app.post("/negotiation", response_model=NegotiationOutput)
def handle_negotiation(
    input_data: Annotated[
        NegotiationInput,
        Body(description="Negotiation scenario input")
    ],
    openai_svc: Annotated[OpenAIService, Depends(openai_client)],
):
    """Handles a negotiation request and returns a generated mock negotiation result."""
    return openai_svc.generate_negotiation_summary(input_data, openai_svc)
