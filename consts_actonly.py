EXAMPLE_REGULAR_A = """
EXAMPLE {i}:
Header: ['Player', 'No.', 'Nationality', 'Position', 'Years in Toronto', 'School/Club Team']
Question: [What is terrence ross' nationality]
Action 1: sql[SELECT * FROM df WHERE UPPER([Player]) = UPPER("Terrence Ross")]
Observation 1: 
| Player        |   No. | Nationality   | Position   | Years in Toronto   | School/Club Team   |
|:--------------|------:|:--------------|:-----------|:-------------------|:-------------------|
| Terrence Ross |    31 | United States | Guard      | 2012-present       | Washington         |
Action 2: sql[SELECT [Nationality] FROM df WHERE UPPER([Player]) = UPPER("Terrence Ross")]
Observation 2: 
| Nationality   |
|:--------------|
| United States |
Action 3: finish[United States]
"""

EXAMPLE_AND_A = """
EXAMPLE {i}:
Header: ['Scheme', 'Tariff code', 'BTs retail price (regulated)', 'Approx premium', 'Prefixes']
Question: [What prefixes are priced at pence per minute, fixed at all times with a premium of 3p/min?]
Action 1: sql[SELECT * FROM df WHERE UPPER([Scheme]) = UPPER("Pence per minute, fixed at all times") AND UPPER([Approx premium]) = UPPER("3p/min")]
Observation 1: 
| Scheme                               | Tariff code   | BTs retail price (regulated)   | Approx premium   | Prefixes   |
|:-------------------------------------|:--------------|:-------------------------------|:-----------------|:-----------|
| Pence per minute, fixed at all times | g27           | 1.277p/min                     | 3p/min           | 0843, 0844 |
| Pence per minute, fixed at all times | g28           | 2.128p/min                     | 3p/min           | 0843, 0844 |
Action 2: sql[SELECT [Prefixes] FROM df WHERE [Scheme] = "Pence per minute, fixed at all times" AND [Approx premium] = "3p/min"]
Observation 2: 
| Prefixes   |
|:-----------|
| 0843, 0844 |
| 0843, 0844 |
Action 3: finish[0843, 0844]
"""

EXAMPLE_MAX_A = """
EXAMPLE {i}: 
Header: ['Year', 'Aircraft kilometers', 'Departures', 'Flying hours', 'Passengers', 'Seat factor', 'Employees', 'Profit/loss']
Question: [Of the years that had exactly 17096 departures, what is the greatest number of aircraft kilometers flown?]
Action 1: sql[SELECT * FROM df WHERE [Departures] = "17096"]
Observation 1:
|   Year |   Aircraft kilometers |   Departures |   Flying hours |   Passengers | Seat factor   |   Employees | Profit/loss        |
|-------:|----------------------:|-------------:|---------------:|-------------:|:--------------|------------:|:-------------------|
|   2002 |              37767709 |        17096 |          55970 |      1339779 | 66%           |        3008 | Loss 3,044,000 JOD |
Action 2: sql[SELECT max([Aircraft kilometers]) FROM df WHERE [Departures] = "17096"]
Observation 2:
|   max([Aircraft kilometers]) |
|-----------------------------:|
|                  3.77677e+07 |
Action 3: finish[3.77677e+07]
"""

EXAMPLE_COUNT_A = """
EXAMPLE {i}: 
Header: ['N°', 'Television service', 'Country', 'Language', 'Content', 'DAR', 'HDTV', 'Package/Option']
Question: [How many television services are there where n°is greater than 856.0?]
Action 1: sql[SELECT * FROM df WHERE [N°] > 856.0]
Observation 1:
|   N° | Television service   | Country   | Language   | Content   | DAR   | HDTV   | Package/Option   |
|-----:|:---------------------|:----------|:-----------|:----------|:------|:-------|:-----------------|
|  857 | Sender Neu Jerusalem | Germany   | German     | religione | 4:3   | no     | no ( FTA )       |
|  858 | TRSP                 | Italy     | Italian    | religione | 4:3   | no     | no ( FTA )       |
Action 2: sql[SELECT COUNT([Television service]) FROM df WHERE [N°] > "856.0"]
Observation 2:
|   COUNT([Television service]) |
|------------------------------:|
|                             2 |
Action 3: finish[2]
"""

EXAMPLE_AVG_A = """
EXAMPLE {i}: 
Header: ['Rank', 'Nation', 'Gold', 'Silver', 'Bronze', 'Total']
Question: [Name the average bronze for total less than 3]
Action 1: sql[SELECT * FROM df WHERE [Total] < 3]
Observation 1:
|   Rank | Nation      |   Gold |   Silver |   Bronze |   Total |
|-------:|:------------|-------:|---------:|---------:|--------:|
|      8 | Isle of Man |      1 |        0 |        0 |       1 |
|      9 | Guernsey    |      0 |        2 |        0 |       2 |
|     10 | Swaziland   |      0 |        1 |        0 |       1 |
|     12 | Malawi      |      0 |        0 |        2 |       2 |
|     13 | Botswana    |      0 |        0 |        1 |       1 |
Action 2: sql[SELECT AVG([Bronze]) FROM df WHERE [Total] < 3]
Observation 2:
|   AVG([Bronze]) |
|----------------:|
|        0.714286 |
Action 3: finish[0.714286]
"""