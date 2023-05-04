import ast
import json
import time
import gym
import requests
import pandas as pd
from pandasql import sqldf

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
    # self.page = None  # current Wikipedia page
    self.obs = None  # current observation
    # self.lookup_keyword = None  # current lookup keyword
    # self.lookup_list = None  # list of paragraphs containing current lookup keyword
    # self.lookup_cnt = None  # current lookup index
    self.steps = 0  # current number of steps
    self.answer = None  # current answer from the agent
    self.observation_space = self.action_space = textSpace()
    # self.search_time = 0
    # self.num_searches = 0
    
  def _get_obs(self):
    return self.obs

  def _get_info(self):
    return {"steps": self.steps, "answer": self.answer}

  def reset(self, seed=None, return_info=False, options=None):
    # We need the following line to seed self.np_random
    # super().reset(seed=seed)
    self.obs = ("Interact with SQL database using sql[] and "
                "finish[].\n")
    # self.page = None
    # self.lookup_keyword = None
    # self.lookup_list = None
    # self.lookup_cnt = None
    self.steps = 0
    self.answer = None
    observation = self._get_obs()
    info = self._get_info()
    return (observation, info) if return_info else observation

  def sql_step(self, query, df):
    pysqldf = lambda q: sqldf(q, locals())
    try:
        self.obs = pysqldf(query).head().to_markdown(index=False)
    except:
        self.obs = "Invalid SQL command, please enter another query."    
  
  def step(self, action, df):
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
      self.sql_step(df, query, df)
    elif action.startswith("finish[") and action.endswith("]"):
      answer = action[len("finish["):-1]
      self.answer = answer
      done = True
      self.obs = f"Episode finished, reward = {reward}\n"
    elif action.startswith("think[") and action.endswith("]"):
      self.obs = "Nice thought."
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
