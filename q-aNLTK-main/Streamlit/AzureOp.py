import os
from openai import AzureOpenAI


def send_chat_message(messages):
    # Initialize the client using environment variables
    client = AzureOpenAI(
        api_key="724a9bfec68944fca09eaeb995b7014e",
        api_version="2024-02-01",
        azure_endpoint="https://dgopenaidev.openai.azure.com/"
    )

    response = client.chat.completions.create(
        model="DgOpenApiChat1Dev",
        messages=messages
    )

    return response


