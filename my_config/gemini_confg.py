from decouple import config
# Update the import path below to the correct location of AsyncOpenAI and OpenAIChatCompletionsModel
# For example, if they are in a file named my_agents.py in the same directory, use:
# from my_agents import AsyncOpenAI, OpenAIChatCompletionsModel

from my_agent import AsyncOpenAI, OpenAIChatCompletionsModel


key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")


gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=gemini_client, temperature=0.2, max_tokens=10)