from crewai import Crew
from textwrap import dedent
from agents import HotelPlannerAgents
from tasks import HotelTasks
from dotenv import load_dotenv
#import agentops
import os
import logging

logging.basicConfig(level=logging.DEBUG)
load_dotenv('.env')

class HotelCrew:

  def __init__(self, origin, cities, travel_date, number_of_nights, requirements, price_range):

    self.origin = origin
    self.cities = cities
    self.travel_date = travel_date
    self.number_of_nights = number_of_nights
    self.requirements = requirements
    self.price_range = price_range

  def run(self):

    agents = HotelPlannerAgents()
    tasks = HotelTasks()

    city_selector_agent = agents.city_selection_agent()
    hotel_information_finder_agent = agents.hotel_information_agent()
    economist_agent = agents.price_filter()
    hotel_selector_agent = agents.best_hotel_selector()

    identify_task = tasks.identify_task(
      city_selector_agent,
      self.origin,
      self.cities,
      self.travel_date,
      self.number_of_nights,
      self.requirements,
      self.price_range
    )

    gather_task = tasks.gather_hotels_information(
      hotel_information_finder_agent,
      self.origin,
      self.cities,
      self.travel_date,
      self.number_of_nights,
      self.requirements,
      self.price_range
    )

    expenses_task = tasks.expenses_task(
      economist_agent, 
      self.origin,
      self.cities,
      self.travel_date,
      self.number_of_nights,
      self.requirements,
      self.price_range
    )

    selection_task = tasks.choose_hotel_task(
        hotel_selector_agent,
        self.origin,
        self.cities,
        self.travel_date,
        self.number_of_nights,
        self.requirements,
        self.price_range
    )

    crew = Crew(
      agents=[
        city_selector_agent, hotel_information_finder_agent, economist_agent, hotel_selector_agent
      ],
      tasks=[identify_task, gather_task, expenses_task, selection_task],

      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Hotel Finder Crew")
  print('-------------------------------')

  origin = 'Istanbul'
  cities = 'Antalya, Rome'
  travel_date = '30th of August'
  number_of_nights = '3'
  requirements = 'adult only and close to the sea'
  price_range = 'under 1000 dollars total'

  #agentops.init(api_key=os.environ.get('AGENT_OPS_KEY'))

  #agentops.start_session()

  hotel_crew = HotelCrew(origin, cities, travel_date, number_of_nights, requirements, price_range)
  result = hotel_crew.run()
  print("\n\n########################")
  print("## Here is you Trip Plan")
  print("########################\n")
  print(result)

  file_path = '/mnt/keremaydin/crewAI/result.txt'

  with open(file_path, "w") as file:
    # Write the string to the file
    file.write(result)

  #agentops.end_session("Success")



