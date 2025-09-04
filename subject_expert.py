from strands import Agent
from strands_tools import current_time, http_request
import logging


# Enable debug logging for Strands
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# Create a basic agent with a specialized system prompt
subject_expert = Agent(
    system_prompt="""You are a Computer Science Subject Expert specializing
    in explaining technical concepts clearly and concisely. Your expertise
    covers programming languages, data structures, algorithms, computer
    architecture, and software engineering principles.
    
    When explaining concepts:
    1. Start with a clear, concise definition
    2. Provide short, but relevant examples to illustrate the concept
    3. Explain practical applications where applicable
    4. Avoid unnecessary jargon, but introduce important terminology
    5. Consider the learner's perspective and make complex topics accessible
    
    Your goal is to help learners build a solid understanding of computer
    science fundamentals.
    """,
    tools = [current_time, http_request]
)

# The response will be automatically printed by the Agent class
# response = subject_expert("Explain the concept of recursion in programming.")


def interactive_session():
    while True:
        user_input = input("\nYour question? ")

        if user_input.lower() in ["exit", "quit", "q", "bye"]:
            print("Goodbye!")
            break

        print("\nThinking")
        subject_expert(user_input)


if __name__ == "__main__":
    interactive_session()