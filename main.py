# Update the import path if "agents" is a local module, or install it if it's external.
# Example for local module:
from agents import Runner, set_tracing_disabled
# Or, if "agents.py" is in the same directory:
# from agents import Runner, set_tracing_disable
from my_agent.hotel_assistant import hotel_assistant
from my_agent.guardrail_agents import guardrail_agent




set_tracing_disabled(True)




res = Runner.run_sync(
    starting_agent=guardrail_agent,
    input="What is the owner name of hotel sannata?"
)