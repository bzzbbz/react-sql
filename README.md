# ReAct Prompting on WikiSQL

GPT-3 prompting code for ICLR 2023 paper [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629).

## Setup
You need to first have an OpenAI API key and store it in the environment variable ``OPENAI_API_KEY`` (see [here](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)).

Package requirement: ``openai`` and ``datasets``.

## Experiments
Run ``wikisql.ipynb``. As WikiSQL have large test sets, we only run 100 random examples (see notebooks).


|                    | text-davinci-002 | text-davinci-003 |
|--------------------|-------------------------------|----------------------------|
| ReAct  | 0.14                         | 0.10                       |
| Act-only | 0.08                          | 0.06                         |
| Chain-of-thought | 0.56                          | 0.55                         |
| Standard prompting | 0.58                         | 0.61                         |

## Citation

```bibtex
@inproceedings{yao2023react,
  title = {{ReAct}: Synergizing Reasoning and Acting in Language Models},
  author = {Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
  booktitle = {International Conference on Learning Representations (ICLR) },
  year = {2023},
  html = {https://arxiv.org/abs/2210.03629},
}
```
