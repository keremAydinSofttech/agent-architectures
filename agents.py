from crewai import Agent
from langchain.llms import OpenAI
from tools import CalculatorTools, SearchTools
from langchain_openai import AzureChatOpenAI
import os
#from agentops.agent import track_agent

os.environ["AZURE_OPENAI_API_KEY"] = os.environ.get('AZURE_OPENAI_API_KEY')
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://softtech-openai-ailab.openai.azure.com/"
os.environ["AZURE_OPENAI_API_VERSION"] = "2024-02-01"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "gpt-4"

class HotelPlannerAgents():

    #@track_agent(name='CitySelectionAgent')
    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the best city based on weather, season, and prices',
            backstory=
            'An expert in analyzing travel data to pick ideal destinations',
            tools=[
                SearchTools.search_internet,
            ],
            llm=AzureChatOpenAI(openai_api_version= os.environ["AZURE_OPENAI_API_VERSION"],
                                azure_deployment = "gpt-4"),
            verbose=True)
    #@track_agent(name='HotelInformationAgent')
    def hotel_information_agent(self):  
        return Agent(  
            role='Hotel Information Specialist',  
            goal='Provide detailed information about hotels, their attributes, and pricing',  
            backstory="""A specialist with a comprehensive database of hotel features,  
            prices, and availability, equipped to assist travelers in making informed decisions""",  
            tools=[  
                SearchTools.search_internet,  
            ],  
            llm=AzureChatOpenAI(openai_api_version= os.environ["AZURE_OPENAI_API_VERSION"],
                                azure_deployment = "gpt-4"),  
            verbose=True)  
    #@track_agent(name='HotelSelectorAgent')
    def best_hotel_selector(self):  
        return Agent(  
            role='Hotel Selection Specialist',  
            goal='Choose the best hotel that fits the customer’s requirements',  
            backstory=  
            'An expert in hospitality who can match accommodations to customer preferences for comfort, amenities, and experiences',  
            tools=[  
                SearchTools.search_internet,  
            ],  
            llm=AzureChatOpenAI(openai_api_version= os.environ["AZURE_OPENAI_API_VERSION"],
                                azure_deployment = "gpt-4"),  
            verbose=True) 

    #@track_agent(name='EconomistAgent')
    def price_filter(self):  
        return Agent(  
            role='Hotel Price Analyst',  
            goal='Filter hotels to find the best options within the customer’s budget',  
            backstory=  
            'Specialized in price analysis and budget-friendly travel solutions, adept at finding the best value for money',  
            tools=[  
                SearchTools.search_internet,  
                CalculatorTools.calculate,
            ],  
            llm=AzureChatOpenAI(openai_api_version= os.environ["AZURE_OPENAI_API_VERSION"],
                                azure_deployment = "gpt-4"),  
            verbose=True) 