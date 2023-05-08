from consts import *
import json
from datasets import load_dataset
from lib.query import Query
from lib.dbengine import DBEngine
from lib.query import Query
import argparse
import pickle

def is_float(x):
    try:
        y = float(x)
        return True
    except:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db_file", type=str, default="./data/test.db")
    parser.add_argument("--ordered", action="store_true")
    parser.add_argument("--res_file", type=str, default="./results/results_standard_all_003.pkl")
    args = parser.parse_args()
    
    data = load_dataset("wikisql")["test"][RANDOM_QUESTION_INDICES]
    correct_answers = []
    data_idx = 0
    engine = DBEngine(args.db_file)
    mistakes = []
    preds = pickle.load(open(args.res_file, 'rb'))
    

    num_mistakes = i = 0
    mistakes_text = ""
    for idx, q, d, s, pred in zip(RANDOM_QUESTION_INDICES, data["question"], data["table"], data["sql"], preds):
        query = Query.from_dict(s, ordered=args.ordered)
        res = engine.execute_query(d['id'], query, lower=True)[0]
        p = pred["answer"]
        mistake = False
        if is_float(p):
            try:
                mistake = abs(float(res) - float(p)) > 1e-5
            except:
                mistake = True
        else:
            mistake = str(p).lower().strip() != str(res).lower().strip()
        if mistake:
            mistakes.append({
                "question": q,
                "question_idx": idx,
                "data_idx": i,
                "gt": res,
                "pred": p,
            })
            mistakes_text += f"""
"question": {q}
"question_idx": {idx}
"data_idx": {i}
"gt": {res}
"pred": {p}
            """
            num_mistakes += 1
        i += 1
        
    with open("mistakes.txt", 'w') as f:
        f.write(mistakes_text)

    with open("./results/correct_answers.pkl", 'wb') as f:
        pickle.dump(mistakes, f)
    
    print("accuracy: {acc}".format(acc=100 - num_mistakes))
    

