from consts import *
import json
from datasets import load_dataset
from lib.query import Query
from lib.dbengine import DBEngine
from lib.query import Query
import argparse
import pickle
import pandas as pd

if __name__ == "__main__":    
    # dataset= load_dataset("wikisql")["test"]
    # Simple = AND = MAX = COUNT = AVG = 0
    # for idx in RANDOM_QUESTION_INDICES:
    #     hr = dataset["sql"][idx]["human_readable"]
    #     if "AND" in hr:
    #         AND += 1
    #     if "MAX" in hr:
    #         MAX += 1
    #     if "COUNT" in hr:
    #         COUNT += 1
    #     if "AVG" in hr:
    #         AVG += 1
    #     if dataset["sql"][idx]["agg"] == 0:
    #         Simple += 1
            
    # print(Simple, AND, MAX, COUNT, AVG)
            
    idx = 14396
    data_idx = 5
    results = pickle.load(open("./results/results_react_all_003.pkl", 'rb'))
    dataset= load_dataset("wikisql")["test"]
    data = dataset["table"][idx]
    res = results[data_idx]["traj"]


    d = {}
    for i, row in enumerate(data["rows"]):
        d[str(i)] = row
    
    df = pd.DataFrame.from_dict(d, orient="index", columns=data["header"])
    
    for col, typ in zip(data["header"], data["types"]):
        if typ == "real":
            df[col] = pd.to_numeric(df[col].str.replace(',', ''), errors='coerce')
    
    print(res)
    print(dataset["sql"][idx]["human_readable"])
    print(df)

        
