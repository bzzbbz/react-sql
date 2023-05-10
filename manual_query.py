import pandas as pd
from pandasql import sqldf
from datasets import load_dataset
from consts import *

if __name__ == "__main__":
    # idx = RANDOM_QUESTION_INDICES[6]
    # dataset= load_dataset("wikisql")["test"]
    # data = dataset["table"][idx]

    data = { "header": [ "Rank", "Nation", "Gold", "Silver", "Bronze", "Total" ], "page_title": "1986 Commonwealth Games", "page_id": "1006029", "types": [ "text", "text", "real", "real", "real", "real" ], "id": "2-1006029-1", "section_title": "Medals by country", "caption": "Medals by country", "rows": [ [ "1", "England", "52", "43", "49", "144" ], [ "2", "Canada", "51", "34", "31", "116" ], [ "3", "Australia", "40", "46", "35", "121" ], [ "4", "New Zealand", "8", "16", "14", "38" ], [ "5", "Wales", "6", "5", "12", "23" ], [ "6", "Scotland", "3", "12", "18", "33" ], [ "7", "Northern Ireland", "2", "4", "9", "15" ], [ "8", "Isle of Man", "1", "0", "0", "1" ], [ "9", "Guernsey", "0", "2", "0", "2" ], [ "10", "Swaziland", "0", "1", "0", "1" ], [ "11", "Hong Kong", "0", "0", "3", "3" ], [ "12", "Malawi", "0", "0", "2", "2" ], [ "13", "Botswana", "0", "0", "1", "1" ], [ "13", "Jersey", "0", "0", "1", "1" ], [ "13", "Singapore", "0", "0", "1", "1" ], [ "Total", "Total", "163", "163", "176", "502" ] ], "name": "" }



    d = {}
    for i, row in enumerate(data["rows"]):
        d[str(i)] = row
    
    df = pd.DataFrame.from_dict(d, orient="index", columns=data["header"])
    
    for col, typ in zip(data["header"], data["types"]):
        if typ == "real":
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
    
    print(df)
    pysqldf = lambda q: sqldf(q, globals())

    print(data["header"])
    query = """SELECT * FROM df WHERE [Total] < "3\""""
    print(pysqldf(query).to_markdown(index=False))
        
