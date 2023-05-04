import consts
# import sqlenv, wrappers
import json
from datasets import load_dataset
import pandas as pd
import pandasql as psql
from lib.query import Query


correct_answers = {}

selected_data = load_dataset("wikisql")["test"][consts.RANDOM_QUESTION_INDICES]

data_idx = 0

# def create_sql_query(sql_dict, table_headers):
#     table_name = "df"
#     select_col = sql_dict['sel']
#     agg_func = sql_dict['agg']
#     conditions = sql_dict['conds']

#     column_index = conditions['column_index'][0]
#     operator_index = conditions['operator_index'][0]
#     condition_value = conditions['condition'][0]

#     # Define aggregation functions mapping
#     AGG_FUNCTIONS = {0: "SELECT", 1: "AVG", 2: "MAX", 3: "MIN", 4: "COUNT", 5: "SUM"}

#     # Define operators mapping
#     OPERATORS = {0: "=", 1: ">", 2: "<", 3: ">=", 4: "<=", 5: "!="}

#     if agg_func == 0:
#         agg_str = AGG_FUNCTIONS[agg_func]
#     else:
#         agg_str = f"{AGG_FUNCTIONS[agg_func]}("
        
#     oper_str = OPERATORS[operator_index]

#     query = f"{agg_str} col_{select_col} FROM {table_name} WHERE col_{column_index} {oper_str} {condition_value}"
    
#     if agg_func != 0:
#         query += ")"

#     return query


# def fetch_answer(table_data, sql):
#     # Convert the table to a pandas dataframe
#     df = pd.DataFrame(table_data['rows'], columns=table_data['header'])

#     # Fetch the SQL query
#     print("This is the original SQL")
#     print(sql)
#     sql_query = create_sql_query(sql, table_data['header'])
#     print("This is the query i got back")
#     print(sql_query)

#     # Execute the SQL query
#     answer = psql.sqldf(sql_query, locals())
#     print("This is the answer")
#     print(answer)


for index in consts.RANDOM_QUESTION_INDICES:
    correct_answers[index] = {}

    # Fetch corresponding table
    correct_answers[index]["table"] = selected_data["table"][data_idx]

    # Fetch corresponding question
    correct_answers[index]["question"] = selected_data["question"][data_idx]

    # Fetch corresponding SQL
    correct_answers[index]["sql"] = selected_data["sql"][data_idx]
    # qg = Query.from_dict(selected_data["sql"][data_idx], ordered=False)
    # print("Whats this")
    # print(qg)

    # Execute the SQL query to get the expected answer
    # fetch_answer(selected_data["table"][data_idx], selected_data["sql"][data_idx])

    data_idx += 1

print(correct_answers)

# # write all results in >> correct_answers.json
with open("correct_answers2.json", "w") as f:
    json.dump(correct_answers, f)