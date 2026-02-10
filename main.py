#project for simple AI agent using openAI api
# langchain is a framework for building AI agents that can interact with various tools and APIs. 
# In this example, we will create a simple agent that can answer questions using the OpenAI API.
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
# langgraph is a library that provides prebuilt agents and tools for building AI applications.
from langgraph.prebuilt import creat_react_agent
# dotenv module is used to load environment variables from a .env file. This is useful for keeping sensitive information like API keys out of your code.
from dotenv import load_dotenv

# looks in the folder for the .env file and loads the environment variables defined in it into the system's environment variables. This allows you to access those variables in your code using os.environ or similar methods.
load_dotenv()

def main():
    # temperature is a parameter that controls the randomness of the model's output. A temperature of 0 means that the model will always choose the most likely next word, while higher temperatures will allow for more diverse and creative responses.
    model = ChatOpenAI(temperature = 0)

    #below array of tools will hold list of tools that the agent can use to answer questions.
    tools = []

    # creates agent that will use the above defined model and tools to answer questions automatically. The creat_react_agent function is a helper function that sets up the agent with the specified model and tools, allowing it to interact with them to generate responses.
    agent_executor = creat_react_agent(model, tools)

    print("Hello! I am a simple AI agent. Ask me anything!")
    print("Type 'exit' to quit.")
    print("What can I help you with today?")

    # Keep looping so long as user keeps interacting with the agent. The loop will continue until the user types 'exit', at which point the program will break out of the loop and end.
    while True:
        # .strip() is used to remove any leading or trailing whitespace from the user's input, ensuring that the input is clean and free of unnecessary spaces before it is processed by the agent.
        user_input = input("\nYou: ").strip() 

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        print("nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            # chunks are parts of a response from the agent. the below checks if there is any messages within any of those chunks
            if "agent" in chunk and "messages" in chunk["agent"]:
                # will stream the responses from the agent in real-time, allowing the user to see the response as it is generated. The loop iterates through each message in the chunk and prints its content without adding a new line after each message, creating a continuous stream of output.
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()  # Print a newline after the response is complete

 # executes the main function when the script is run directly. Allows the code to be imported as a module without executing the main function, while still allowing it to run when the script is executed directly.
if __name__ == "__main__":
    main()