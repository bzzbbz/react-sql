import pandas as pd
from pandasql import sqldf
from datasets import load_dataset
from consts import *

if __name__ == "__main__":
    # idx = RANDOM_QUESTION_INDICES[6]
    # dataset= load_dataset("wikisql")["test"]
    # data = dataset["table"][idx]

    data = { "header": [ "N°", "Television service", "Country", "Language", "Content", "DAR", "HDTV", "Package/Option" ], "page_title": "Television in Italy", "page_id": "", "types": [ "real", "text", "text", "text", "text", "text", "text", "text" ], "id": "1-15887683-15", "section_title": "Religious", "caption": "Religious", "rows": [ [ "850", "Telepace", "Italy", "Italian", "religione", "16:9", "no", "no ( FTA )" ], [ "851", "Daystar Television Network", "Italy", "English", "religione", "4:3", "no", "no ( FTA )" ], [ "852", "Padre Pio TV", "Italy", "Italian", "religione", "4:3", "no", "no ( FTA )" ], [ "853", "The Word Network", "United Kingdom", "English", "religione", "4:3", "no", "no ( FTA )" ], [ "854", "Inspiration", "United Kingdom", "English", "religione", "4:3", "no", "no ( FTA )" ], [ "855", "EWTN", "United Kingdom", "English", "religione", "4:3", "no", "no ( FTA )" ], [ "856", "TBNE", "Italy", "Italian", "religione", "4:3", "no", "no ( FTA )" ], [ "857", "Sender Neu Jerusalem", "Germany", "German", "religione", "4:3", "no", "no ( FTA )" ], [ "858", "TRSP", "Italy", "Italian", "religione", "4:3", "no", "no ( FTA )" ] ], "name": "table_15887683_15" }


    d = {}
    for i, row in enumerate(data["rows"]):
        d[str(i)] = row
    
    df = pd.DataFrame.from_dict(d, orient="index", columns=data["header"])
    
    for col, typ in zip(data["header"], data["types"]):
        if typ == "real":
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
    
    print(df)
    pysqldf = lambda q: sqldf(q, globals())
    
    # SELECT COUNT Tariff code FROM table WHERE BTs retail price (regulated) = 2p/min or inclusive"
    # query = 'SELECT * FROM df WHERE [BTs retail price (regulated)] = "2p/min or inclusive"'
    # df = pysqldf(query)
    # query = 'SELECT [Tariff code] FROM df'
    # df = pysqldf(query)
    # print(pysqldf(query))
    print(data["header"])
    query = """SELECT * FROM df WHERE [N°] > "856.0\""""
    print(pysqldf(query).to_markdown(index=False))
    

    # print(df)
    
