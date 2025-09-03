from agents import Agent
from my_config.gemini_confg import MODEL


hotel_assistant=Agent(
    name="Hotel customer care",
    instructions="""
You are helpful hotel customer care assistant, hotel total room 200.
-Hotel name is Hotel sanata.
-Hotel Owner name is Mr. Ratan Lal
-20 rooms are not available for public, Its for special guest.

""",
model=MODEL,
)


