

**README.md**

**Comprehensive Travel Planning Service**
=====================================

Overview
--------

This project provides a comprehensive service that encompasses two primary functionalities: internet search and mathematical calculations. The service is designed to assist with hotel selection and cost estimation, ensuring the best possible experience for travelers.

Functionality
------------

### Internet Search

The `SearchTools` class utilizes the Serper API to search the internet, constructing a URL and payload, sending a POST request, and returning the top search results.

### Mathematical Calculations

The `CalculatorTools` class leverages the `eval` function to evaluate mathematical expressions, returning the result or an error message if the syntax is invalid.

### Task Generation

The service generates task descriptions based on input parameters such as:

* Origin
* Cities
* Travel date
* Number of nights
* Requirements
* Price range

### Hotel Cost Calculation

The service calculates the total cost of stay for each hotel option, including a detailed cost breakdown and travel expenses calculation.

### Hotel Evaluation and Recommendation

The service evaluates hotel options based on factors like:

* Location
* Amenities
* Cost-effectiveness

It compares top choices and recommends the best hotel that meets the traveler's preferences and budget.

### Justification and Reporting

The service provides comprehensive reports, including justifications for the recommended hotel, to ensure the best possible experience for the traveler.

Usage
-----

To use this service, simply import the required classes and call the relevant methods with the necessary input parameters.

**Example:**
```python
from SearchTools import SearchTools
from CalculatorTools import CalculatorTools
from TaskGenerator import TaskGenerator
from HotelCostCalculator import HotelCostCalculator
from HotelEvaluator import HotelEvaluator

# Initialize classes
search_tools = SearchTools()
calculator_tools = CalculatorTools()
task_generator = TaskGenerator()
hotel_cost_calculator = HotelCostCalculator()
hotel_evaluator = HotelEvaluator()

# Generate task description
task_description = task_generator.generate_task_description(origin="New York", cities=["Paris", "London"], travel_date="2023-06-01", num_nights=5, requirements=["free breakfast", "gym"], price_range=[100, 200])

# Calculate hotel costs
hotel_costs = hotel_cost_calculator.calculate_hotel_costs(task_description)

# Evaluate and recommend hotel
recommended_hotel = hotel_evaluator.evaluate_and_recommend_hotel(hotel_costs)

# Generate report
report = hotel_evaluator.generate_report(recommended_hotel)

print(report)
```

Requirements
------------

* Serper API key
* Python 3.x

License
-------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

Acknowledgments
--------------

This project would not have been possible without the Serper API and the Python programming language.