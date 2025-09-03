from agents import Agent
from my_config.gemini_confg import MODEL
from data_schema.myDataSchema import MyDataType

guardrail_agent = Agent(
    name="Hotel guardrail for Hotel Sanata",
    instructions="Check queries for hotel sannata",
    model=MODEL,
    output_type=MyDataType
)