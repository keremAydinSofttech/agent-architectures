from crewai import Task
from textwrap import dedent
from datetime import date


class HotelTasks():

    def identify_task(self, agent, origin, cities, travel_date, number_of_nights, requirements, price_range):  
        return Task(description=dedent(f"""  
            Analyze and select the best city for the trip based   
            on specific criteria such as weather patterns, seasonal  
            events, and hotel costs. This task involves comparing  
            multiple cities, considering factors like current weather  
            conditions, upcoming cultural or seasonal events, and  
            overall hotel expenses.   
                
            Your final answer must be a detailed  
            report on the chosen city, and everything you found out  
            about it, including the actual average price range of hotels, weather   
            forecast and attractions.  
            If you do your BEST WORK, I'll tip you $100!  

            Traveling from: {origin}  
            City Options: {cities}  
            Travel Date: {travel_date}  
            Number of nights: {number_of_nights}
            Traveler requirements: {requirements}  
            Price range: {price_range}  
            """),  
                agent=agent,  
                expected_output="A detailed report on the chosen city including hotel costs, travel costs, weather forecast, and attractions.") 

    def gather_hotels_information(self, agent, origin, cities, travel_date, number_of_nights, requirements, price_range):  
        return Task(description=dedent(f"""  
            Research and compile a comprehensive list of hotels within {cities} that   
            align with the specified traveler requirements and fall within the given   
            price range. This task involves collecting detailed information on each   
            hotel's location, pricing during the {travel_date}, available amenities,   
            and booking availability.   
                
            The final deliverable should be an organized list or table that includes   
            hotel names, addresses, price per night, amenities, proximity to major   
            attractions, and any other relevant information that will help in making   
            an informed decision.  
                
            Traveling from: {origin}  
            City Options: {cities}  
            Travel Date: {travel_date}  
            Number of nights: {number_of_nights}
            Traveler requirements: {requirements}  
            Price range: {price_range} 
            """),  
                agent=agent,  
                expected_output="An organized list or table of hotels including names, addresses, pricing, amenities, and proximity to attractions.")  

    def expenses_task(self, agent, origin, cities, travel_date, number_of_nights, requirements, price_range):  
        return Task(description=dedent(f"""  
            Calculate the total expenses for staying at each of the provided hotels,   
            taking into account the length of stay and the number of guests. Include   
            in your calculation the cost of the hotel room per night, any additional   
            fees (such as resort fees or taxes), and the estimated travel expenses   
            to and from the hotel.  

            The final deliverable should be a detailed breakdown of the total cost   
            for each hotel option, including a line-item description of all charges   
            and the grand total for the entire stay at each hotel. Additionally,   
            calculate the travel expenses based on the provided information.  
                
            Traveling from: {origin}  
            City Options: {cities}  
            Travel Date: {travel_date}  
            Number of nights: {number_of_nights}
            Traveler requirements: {requirements}  
            Price range: {price_range} 
            """),  
                agent=agent,  
                expected_output="A detailed cost breakdown for each hotel option and the total travel expenses.") 

    def choose_hotel_task(self, agent, origin, cities, travel_date, number_of_nights, requirements, price_range):  
        return Task(description=dedent(f"""  
            Evaluate all the provided hotel options along with the calculated total   
            expenses to select the best hotel that meets the traveler's preferences   
            and budget. Consider factors such as location, amenities, hotel quality,   
            and the overall cost-effectiveness of the stay.  
  
            The final deliverable should be a comprehensive report that includes a   
            comparison of the top hotel choices, highlighting the advantages and   
            disadvantages of each, and ultimately recommending the best hotel. Justify   
            your recommendation based on how well it aligns with the traveler's   
            preferences and the value for money offered.  
              
            Traveling from: {origin}  
            City Options: {cities}  
            Travel Date: {travel_date}  
            Number of nights: {number_of_nights}
            Traveler requirements: {requirements}  
            Price range: {price_range}   
          """),  
              agent=agent,  
              expected_output="A comprehensive report recommending the best hotel with a justification based on traveler preferences and overall value.")   
