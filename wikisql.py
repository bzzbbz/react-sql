from datasets import load_dataset
from consts import RANDOM_QUESTION_INDICES

dataset = load_dataset('wikisql')
print(str(dataset["test"][0]["table"]["header"]))