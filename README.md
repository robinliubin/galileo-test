# Galileo Scenario Agents

This repo contains Galileo scenario agents in Python under `agents/` and matching runnable notebooks under `agents/*.ipynb`.

## Prerequisites

- `uv` installed
- Python 3.13 available to `uv`
- Required Galileo and OpenAI credentials saved in `.env`

## Set Up The Environment With `uv`

From the repo root:

```bash
uv sync
```

This creates `.venv/` and installs all project dependencies, including `ipykernel` for notebooks.

If you want to activate the environment in your shell:

```bash
source .venv/bin/activate
```

You can also run commands without activating it:

```bash
uv run python main.py list
uv run python evaluator.py --list
```

## Use The Notebooks

The generated notebooks are:

- `agents/chatbot.ipynb`
- `agents/rag.ipynb`
- `agents/tools.ipynb`
- `agents/experiments.ipynb`
- `agents/guardrails.ipynb`
- `agents/custom_eval.ipynb`

Each notebook:

- loads credentials from `.env`
- instantiates one agent
- exposes the scenario steps as separate cells
- includes a final cleanup cell

Open a notebook in Jupyter or VS Code and select the interpreter from:

```text
.venv/bin/python
```

If your notebook client asks for a kernel, use the environment created by `uv sync`. The project includes `ipykernel`, so the `.venv` interpreter is notebook-ready.

## Regenerate The Notebooks

If you update any agent in `agents/*.py`, regenerate the companion notebooks with:

```bash
python scripts/generate_agent_notebooks.py
```

## Notes

- Run notebook cells in order.
- The notebooks will create Galileo projects/log streams and may make live API calls.
- Use the final cleanup cell when you are done with a scenario.
