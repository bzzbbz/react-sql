import pandas as pd
from pandasql import sqldf
from datasets import load_dataset
from consts import *

if __name__ == "__main__":
    # data = { "header": [ "Year", "Aircraft kilometers", "Departures", "Flying hours", "Passengers", "Seat factor", "Employees", "Profit/loss" ], "page_title": "Royal Jordanian", "page_id": "", "types": [ "real", "real", "real", "real", "real", "text", "real", "text" ], "id": "1-105344-2", "section_title": "Statistics", "caption": "Financial and operational statistics", "rows": [ [ "2002", "37767709", "17096", "55970", "1339779", "66%", "3008", "Loss 3,044,000 JOD" ], [ "2003", "36933462", "16202", "54972", "1404588", "68%", "3162", "Loss 9,753,000 JOD" ], [ "2004", "44557377", "19148", "66004", "1736637", "71%", "3313", "Profit 15,327,000 JOD" ], [ "2005", "45557377", "20777", "68883", "1821329", "69%", "3557", "Profit 20,516,000 JOD" ], [ "2006", "52274917", "25661", "77374", "2004559", "66%", "3799", "Profit 6,135,000 JOD" ], [ "2007", "56055803", "30244", "88378", "2288000", "71%", "4275", "Profit 24,111,000 JOD" ], [ "2008", "64379058", "34285", "101381", "2701000", "72%", "4507", "Loss 23,400,000 JOD" ], [ "2009", "66017391", "35715", "105579", "2668590", "68%", "4399", "Profit 28,614,000 JOD" ] ], "name": "table_105344_2" }
    idx = RANDOM_QUESTION_INDICES[6]
    dataset= load_dataset("wikisql")["test"]
    data = dataset["table"][idx]

    d = {}
    for i, row in enumerate(data["rows"]):
        d[str(i)] = row
    
    df = pd.DataFrame.from_dict(d, orient="index", columns=data["header"])
    
    for col, typ in zip(data["header"], data["types"]):
        if typ == "real":
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
        
    pysqldf = lambda q: sqldf(q, globals())
    
    # SELECT COUNT Tariff code FROM table WHERE BTs retail price (regulated) = 2p/min or inclusive"
    # query = 'SELECT * FROM df WHERE [BTs retail price (regulated)] = "2p/min or inclusive"'
    # df = pysqldf(query)
    # query = 'SELECT [Tariff code] FROM df'
    # df = pysqldf(query)
    # print(pysqldf(query))
    query = "SELECT [Opponent] FROM df WHERE [Record] = '43-56'"
    print(pysqldf(query).to_markdown(index=False))
    

    # print(df)
    
