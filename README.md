# Whiskey Exporters

## Introduction 

Imagine you are working at the Department for Business and Trade supporting export analysts. 
The Data engineering team has built a tool for them (for simplicity in this scenario) as a python module, 
a command line application called `wexp` (Whiskey Exporter tool).

The `wexp` command line tool is used by analysts to quickly check information about whiskey exporters. 
In production, it has information about over 100 countries and hundreds of thousands of individual whiskey exports from the UK. 
But this data is not available in the development environment. 
We have only a few records (you can see them in the data folder).

`wexp` uses a DuckDB backend, and the [DuckDB Python API](https://duckdb.org/docs/stable/clients/python/dbapi.html) to interact with it.

The analysts have asked for a few improvements, which we will go over during the interview. 

We recommend using [GitHub Codespaces](https://github.com/features/codespaces) to do this, but you are allowed to use other code editors. Typically, the interviewer will start the codespace, then the interviewee will join via liveshare. However, this is not a hard and fast rule. We recommend that you get familiar with GitHub Codespaces and `wexp` prior to the interview. You will **not** be allowed to use AI code assistants such as GitHub Copilot. However you are free to search online to help you find the most appropriate solution.

## Setup

- Log into [GitHub Codespaces](https://github.com/codespaces)
- Clone the repository `uktrade-recruitment/data-engineer-derec`
- Leave the default options as-is

GitHub will take a few seconds to spin up your codespace. GitHub will provide users in the free plan 120 core hours or 60 hours of run time on a 2 core codespace, so you should't be charged unless you already use GitHub Codespaces for personal use.

The repository uses [uv](https://docs.astral.sh/uv/) as a python package manager. Run the following commands to setup the python environment:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
uv sync
```

You are now ready to use `wexp`. Try a few commands:

```
python wexp test
python wexp show countries
```

Good luck with the interview!
