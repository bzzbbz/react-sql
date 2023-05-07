import ast
import json
import time
import gym
import requests
import pandas as pd
from pandasql import sqldf
from datasets import load_dataset
from consts import RANDOM_QUESTION_INDICES

# import wikipedia

def clean_str(p):
  return p.encode().decode("unicode-escape").encode("latin1").decode("utf-8")


class textSpace(gym.spaces.Space):
  def contains(self, x) -> bool:
    """Return boolean specifying if x is a valid member of this space."""
    return isinstance(x, str)


class SQLEnv(gym.Env):

  def __init__(self):
    """
      Initialize the environment.
    """
    super().__init__()
    self.obs = None  # current observation
    self.steps = 0  # current number of steps
    self.answer = None  # current answer from the agent
    self.observation_space = self.action_space = textSpace()
    self.data = load_dataset("wikisql")["test"][RANDOM_QUESTION_INDICES]
    self.data_idx = 0
    self.dfs = {}
    for data in self.data["table"]:
      d = {}
      for i, row in enumerate(data["rows"]):
          d[str(i)] = row
      
      _df = pd.DataFrame.from_dict(d, orient="index", columns=data["header"])
      
      for col, typ in zip(data["header"], data["types"]):
          if typ == "real":
              _df[col] = pd.to_numeric(_df[col].str.replace(',', ''), errors='coerce')
      self.dfs[data["id"]] = _df
    
  def _get_obs(self):
    return self.obs

  def _get_info(self):
    return {"steps": self.steps, "answer": self.answer}

  def reset(self, seed=None, return_info=False, options=None, idx=0):
    # We need the following line to seed self.np_random
    # super().reset(seed=seed)
    self.obs = ("Interact with SQL database using sql[] and "
                "finish[].\n")
    self.steps = 0
    self.data_idx = idx
    self.answer = None
    observation = self._get_obs()
    info = self._get_info()
    return (observation, info) if return_info else observation

  def sql_step(self, action):
    df = self.dfs[self.data["table"][self.data_idx]["id"]]
    # print(df)
    try:
        self.obs = sqldf(action).head().to_markdown(index=False)
    except:
        self.obs = "Invalid SQL command, please enter another query."
    # self.obs = sqldf(action).head().to_markdown(index=False)
  
  def step(self, action):
    reward = 0
    done = False
    action = action.strip()
    if self.answer is not None:  # already finished
      done = True
      return self.obs, reward, done, self._get_info()
    
    if action.startswith("sql[") and action.endswith("]"):
      query = action[len("sql["):-1]
      # entity_ = entity.replace(" ", "_")
      # search_url = f"https://en.wikipedia.org/wiki/{entity_}"
      self.sql_step(query)
    elif action.startswith("finish[") and action.endswith("]"):
      answer = action[len("finish["):-1]
      self.answer = answer
      done = True
      self.obs = f"Episode finished, reward = {reward}\n"
    else:
      self.obs = "Invalid action: {}".format(action)

    self.steps += 1

    return self.obs, reward, done, self._get_info()
  
  def get_time_info(self):
    speed = self.search_time / self.num_searches if self.num_searches else 0
    return {
        "call_speed": speed,
        "call_time": self.search_time,
        "num_calls": self.num_searches,
    }
  
  def update_data_idx(self, idx):
    self.data_idx = idx
