from langchain_openai import AzureChatOpenAI
from langchain.agents.load_tools import load_tools
from langchain.agents.initialize import initialize_agent
from langchain.agents.agent_types import AgentType
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["AZURE_OPENAI_API_KEY"] = os.environ.get('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://softtech-openai-ailab.openai.azure.com/"
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-02-01"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "gpt-4"


# Large language model
llm = AzureChatOpenAI(openai_api_version= os.environ["AZURE_OPENAI_API_VERSION"],
                                azure_deployment = "gpt-4")

# Tool integration
tools = load_tools(['wikipedia', 
                    'llm-math'], llm=llm)

# Initialization of the agent
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
                         handle_parsing_errors=True)

# Run the agent with a prompt
result = agent.run('What is the average age of a dog? Multiply the age by 3')