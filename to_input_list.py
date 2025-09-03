from decouple import config
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner

key = config("GEMINI_API_KEY")

gemini_client = AsyncOpenAI(api_key=key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

MODEL = OpenAIChatCompletionsModel(model="gemini-2.5-flash",openai_client=gemini_client)

agent = Agent(name="HelloAgent", instructions="You answer user query", model=MODEL)

result = Runner.run_sync(agent, "What is Leaning tower of pisa")

inputdata = result.to_input_list()

print(result.final_output)
