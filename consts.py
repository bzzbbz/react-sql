EXAMPLE_REGULAR = """
EXAMPLE {i}:
Header: ['Player', 'No.', 'Nationality', 'Position', 'Years in Toronto', 'School/Club Team']
Question: [What is terrence ross' nationality]
Thought 1: I need to find the information related to terrence ross.
Action 1: sql[SELECT * FROM df WHERE UPPER([Player]) = UPPER("Terrence Ross")]
Observation 1: 
| Player        |   No. | Nationality   | Position   | Years in Toronto   | School/Club Team   |
|:--------------|------:|:--------------|:-----------|:-------------------|:-------------------|
| Terrence Ross |    31 | United States | Guard      | 2012-present       | Washington         |
Thought 2: Now I need to find the information in the “Nationality” column of terrence ross
Action 2: sql[SELECT [Nationality] FROM df WHERE UPPER([Player]) = UPPER("Terrence Ross")]
Observation 2: 
| Nationality   |
|:--------------|
| United States |
Thought 3: Finally, I need to get the information under Nationality and return the final answer.
Action 3: finish[United States]
"""

EXAMPLE_AND = """
EXAMPLE {i}:
Header: ['Scheme', 'Tariff code', 'BTs retail price (regulated)', 'Approx premium', 'Prefixes']
Question: [What prefixes are priced at pence per minute, fixed at all times with a premium of 3p/min?]
Thought 1: I need to find the rows in the table where the "Scheme" is "Pence per minute, fixed at all times," and the "Approx premium" is "3p/min".
Action 1: sql[SELECT * FROM df WHERE UPPER([Scheme]) = UPPER("Pence per minute, fixed at all times") AND UPPER([Approx premium]) = UPPER("3p/min")]
Observation 1: 
| Scheme                               | Tariff code   | BTs retail price (regulated)   | Approx premium   | Prefixes   |
|:-------------------------------------|:--------------|:-------------------------------|:-----------------|:-----------|
| Pence per minute, fixed at all times | g27           | 1.277p/min                     | 3p/min           | 0843, 0844 |
| Pence per minute, fixed at all times | g28           | 2.128p/min                     | 3p/min           | 0843, 0844 |
Thought 2: Now I need to extract the "Prefixes" column from the rows that match the criteria.
Action 2: sql[SELECT [Prefixes] FROM df WHERE [Scheme] = "Pence per minute, fixed at all times" AND [Approx premium] = "3p/min"]
Observation 2: 
| Prefixes   |
|:-----------|
| 0843, 0844 |
| 0843, 0844 |
Thought 3: Finally, I need to combine the prefixes from the selected rows and return the unique prefixes as the final answer.
Action 3: finish[0843, 0844]
"""

EXAMPLE_MAX = """
EXAMPLE {i}: 
Header: ['Year', 'Aircraft kilometers', 'Departures', 'Flying hours', 'Passengers', 'Seat factor', 'Employees', 'Profit/loss']
Question: [Of the years that had exactly 17096 departures, what is the greatest number of aircraft kilometers flown?]
Thought 1: I need to first find the years that had exactly 17096 departures
Action 1: sql[SELECT * FROM df WHERE [Departures] = 17096]
Observation 1:
|   Year |   Aircraft kilometers |   Departures |   Flying hours |   Passengers | Seat factor   |   Employees | Profit/loss        |
|-------:|----------------------:|-------------:|---------------:|-------------:|:--------------|------------:|:-------------------|
|   2002 |              37767709 |        17096 |          55970 |      1339779 | 66%           |        3008 | Loss 3,044,000 JOD |
Thought 2: Now I need to find the column that corresponds to the aircraft flown. I’ll need to use MAX to find the greatest number of this column.
Action 2: sql[SELECT max([Aircraft kilometers]) FROM df WHERE [Departures] = "17096"]
Observation 2:
|   max([Aircraft kilometers]) |
|-----------------------------:|
|                  3.77677e+07 |
Thought 3: Finally, I need to return the Aircraft kilometers as the final answer.
Action 3: finish[3.77677e+07]
"""

EXAMPLE_COUNT = """
EXAMPLE {i}: 
Header: ['N°', 'Television service', 'Country', 'Language', 'Content', 'DAR', 'HDTV', 'Package/Option']
Question: [How many television services are there where n°is greater than 856.0?]
Thought 1: I need to first find the rows in the table where "n°" is greater than 856.0.
Action 1: sql[SELECT * FROM df WHERE [N°] > 856.0]
Observation 1:
|   N° | Television service   | Country   | Language   | Content   | DAR   | HDTV   | Package/Option   |
|-----:|:---------------------|:----------|:-----------|:----------|:------|:-------|:-----------------|
|  857 | Sender Neu Jerusalem | Germany   | German     | religione | 4:3   | no     | no ( FTA )       |
|  858 | TRSP                 | Italy     | Italian    | religione | 4:3   | no     | no ( FTA )       |
Thought 2: Now I need to find the column that corresponds to Television service. I’ll need to use COUNT to know how many Televesion service there are.
Action 2: sql[SELECT COUNT([Television service]) FROM df WHERE [N°] > "856.0"]
Observation 2:
|   COUNT([Television service]) |
|------------------------------:|
|                             2 |
Thought 3: Finally, I need to return the count of Television service as the final answer.
Action 3: finish[2]
"""

EXAMPLE_AVG = """
EXAMPLE {i}: 
Header: ['Rank', 'Nation', 'Gold', 'Silver', 'Bronze', 'Total']
Question: [Name the average bronze for total less than 3]
Thought 1: I need to first find the rows in the table where "Total" is less than 3.
Action 1: sql[SELECT * FROM df WHERE [Total] < 3]
Observation 1:
|   Rank | Nation      |   Gold |   Silver |   Bronze |   Total |
|-------:|:------------|-------:|---------:|---------:|--------:|
|      8 | Isle of Man |      1 |        0 |        0 |       1 |
|      9 | Guernsey    |      0 |        2 |        0 |       2 |
|     10 | Swaziland   |      0 |        1 |        0 |       1 |
|     12 | Malawi      |      0 |        0 |        2 |       2 |
|     13 | Botswana    |      0 |        0 |        1 |       1 |
Thought 2: Now I need to find the column that corresponds to Bronze. I’ll need to use AVG to get the average.
Action 2: sql[SELECT AVG([Bronze]) FROM df WHERE [Total] < 3]
Observation 2:
|   AVG([Bronze]) |
|----------------:|
|        0.714286 |
Thought 3: Finally, I need to return the average of Bronze as the final answer.
Action 3: finish[0.714286]
"""

EXAMPLE_EMPTY = """
EXAMPLE {i}:"""

RANDOM_QUESTION_INDICES = [
    654,
    1241,
    5014,
    7894,
    9763,
    14396,
    14355,
    7133,
    2737,
    5410,
    8402,
    10036,
    4671,
    8972,
    10363,
    15119,
    13728,
    14368,
    12058,
    8082,
    3433,
    8467,
    4428,
    8819,
    15500,
    885,
    8840,
    6794,
    2081,
    4610,
    3365,
    5050,
    10229,
    14432,
    1318,
    7272,
    15217,
    10476,
    11830,
    407,
    5425,
    4210,
    7419,
    11732,
    9924,
    15021,
    8902,
    7460,
    13204,
    11120,
    9992,
    14336,
    14468,
    8637,
    15650,
    13968,
    15035,
    10159,
    12041,
    6910,
    11797,
    1200,
    8466,
    6348,
    844,
    7308,
    14036,
    7190,
    14537,
    3367,
    6542,
    13276,
    3598,
    10399,
    4881,
    11009,
    14171,
    1838,
    14749,
    6159,
    122,
    15197,
    777,
    7712,
    14367,
    3950,
    3491,
    3250,
    12712,
    3106,
    15721,
    9421,
    97,
    1102,
    11861,
    9465,
    12801,
    3452,
    10104,
    2873,
]
