# This is an example script demonstrating agent handoff using Groq LLM

from microagent import Microagent, Agent
from microagent.repl import run_demo_loop

client = Microagent(llm_type='groq')

english_agent = Agent(
    name="EnglishAgent",
    instructions="You only speak English.",
    model="llama3-groq-70b-8192-tool-use-preview",  # Correct Groq model
    tool_choice="auto"
)

spanish_agent = Agent(
    name="SpanishAgent",
    instructions="You only speak Spanish.",
    model="llama3-groq-70b-8192-tool-use-preview",  # Correct Groq model
    tool_choice="auto"
)

def transfer_to_spanish_agent():
    """Transfer spanish speaking users immediately."""
    return spanish_agent

english_agent.functions.append(transfer_to_spanish_agent)

def transfer_to_english_agent():
    """Transfer english speaking users immediately."""
    return english_agent

spanish_agent.functions.append(transfer_to_english_agent)

messages = [{"role": "user", "content": "Hola. ¿Como estás?"}]
response = client.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])

if __name__ == "__main__":
    run_demo_loop(english_agent, llm_type='groq')
