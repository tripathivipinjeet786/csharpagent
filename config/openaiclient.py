import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI


load_dotenv(find_dotenv())

class AzureAIClients:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.deployment_name = os.getenv(
            "AZURE_OPENAI_DEPLOYMENT",
            "gpt-5.2"
        )

        if not self.endpoint:
            raise ValueError(
                "AZURE_OPENAI_ENDPOINT is not configured"
            )

        if not self.api_key:
            raise ValueError(
                "AZURE_OPENAI_API_KEY is not configured"
            )

        self.openai_client = AsyncOpenAI(
            base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )

    def get_openai_client(self) -> AsyncOpenAI:
        return self.openai_client

    def get_deployment_name(self) -> str:
        return self.deployment_name