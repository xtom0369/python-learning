#! /usr/bin/env python
# -*- coding:utf-8 -*-

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New Yory'
cities['OR'] = 'Portland'

# print some cities
print(f"""

{'_' * 10}
NY State has : {cities['NY']}
OR State has : {cities['OR']}

""")

# print some states
print(f"""

{'_' * 10}
Michigan has : {cities[states['Michigan']]}
Florida State has : {cities[states['Florida']]}

""")

# print every state abbreviation
print(f"{'_' * 10}")
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

# print every cities in state
print(f"{'_' * 10}")
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print(f"{'_' * 10}")
for state, abbrev in states.items():
    print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")

# safely get a abbreviation by state that might not be there
print(f"{'_' * 10}")
state = states.get("Texas", None)

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is : {city}")



