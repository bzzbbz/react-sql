EXAMPLE_REGULAR_S = """
EXAMPLE {i}:
Header: ['Player', 'No.', 'Nationality', 'Position', 'Years in Toronto', 'School/Club Team']
Question: [What is terrence ross' nationality]
Action 1: finish[United States]
Observation 1: none
"""

EXAMPLE_AND_S = """
EXAMPLE {i}:
Header: ['Scheme', 'Tariff code', 'BTs retail price (regulated)', 'Approx premium', 'Prefixes']
Question: [What prefixes are priced at pence per minute, fixed at all times with a premium of 3p/min?]
Action 1: finish[0843, 0844]
Observation 1: none
"""

EXAMPLE_MAX_S = """
EXAMPLE {i}: 
Header: ['Year', 'Aircraft kilometers', 'Departures', 'Flying hours', 'Passengers', 'Seat factor', 'Employees', 'Profit/loss']
Question: [Of the years that had exactly 17096 departures, what is the greatest number of aircraft kilometers flown?]
Action 1: finish[37767709]
Observation 1: none
"""

EXAMPLE_COUNT_S = """
EXAMPLE {i}: 
Header: ['N°', 'Television service', 'Country', 'Language', 'Content', 'DAR', 'HDTV', 'Package/Option']
Question: [How many television services are there where n° is greater than 856.0?]
Action 1: finish[2]
Observation 1: none
"""

EXAMPLE_AVG_S = """
EXAMPLE {i}: 
Header: ['Rank', 'Nation', 'Gold', 'Silver', 'Bronze', 'Total']
Question: [Name the average bronze for total less than 3]
Action 1: finish[0.714286]
Observation 1: none
"""