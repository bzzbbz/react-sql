EXAMPLE_REGULAR_T = """
EXAMPLE {i}:
Header: ['Player', 'No.', 'Nationality', 'Position', 'Years in Toronto', 'School/Club Team']
Question: [What is terrence ross' nationality]
Thought 1: Let's think step-by-step. Terrence Ross is American, so the answer is United States.
Action 1: finish[United States]
Observation 1: none
"""

EXAMPLE_AND_T = """
EXAMPLE {i}:
Header: ['Scheme', 'Tariff code', 'BTs retail price (regulated)', 'Approx premium', 'Prefixes']
Question: [What prefixes are priced at pence per minute, fixed at all times with a premium of 3p/min?]
Thought 1: Let's think step-by-step. The prefixes that are priced at pence per minute, fixed at all times are both 0843, 0844. Both prefixes are also fixed at all times with a premiuum of 3p/min. I need to combine the prefixes to return a unique prefix as the final answer, so the answer is 0843, 0844.
Action 1: finish[0843, 0844]
Observation 1: none
"""

EXAMPLE_MAX_T = """
EXAMPLE {i}: 
Header: ['Year', 'Aircraft kilometers', 'Departures', 'Flying hours', 'Passengers', 'Seat factor', 'Employees', 'Profit/loss']
Question: [Of the years that had exactly 17096 departures, what is the greatest number of aircraft kilometers flown?]
Thought 1: Let's think step-by-step. 2002 is only one year that had exactly 17096 departures. The number of aircraft kilometers folwon is 37767709, so the answer is 37767709.
Action 1: finish[37767709]
Observation 1: none
"""

EXAMPLE_COUNT_T = """
EXAMPLE {i}: 
Header: ['N°', 'Television service', 'Country', 'Language', 'Content', 'DAR', 'HDTV', 'Package/Option']
Question: [How many television services are there where n° is greater than 856.0?]
Thought: Let's think step-by-step. Sender Neu Jerusalem and TRSP have n° greater than 856.0, so the answer is 2.
Action 1: finish[2]
Observation 1: none
"""

EXAMPLE_AVG_T = """
EXAMPLE {i}: 
Header: ['Rank', 'Nation', 'Gold', 'Silver', 'Bronze', 'Total']
Question: [Name the average bronze for total less than 3]
Thought 1: Let's think step-by-step. There are six nations with less than 3 bronze. The average of them is 0.714286, so the answer is 0.714286.
Action 1: finish[0.714286]
Observation 1: none
"""