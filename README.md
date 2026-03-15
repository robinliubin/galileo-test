# Galileo SDK Learning Lab

An exploratory, educational project for learning the [Galileo](https://galileo.ai) AI observability platform through hands-on Jupyter notebooks.

## What This Repo Does

Each notebook in `agents/` is a self-contained scenario that teaches one area of the Galileo platform — from basic chatbot monitoring to production guardrails to human annotation workflows. Run the cells in order, read the explanations, and inspect the results in the Galileo Console.

## Prerequisites

- **Python 3.13** available on your system
- **[uv](https://docs.astral.sh/uv/)** installed for dependency and environment management
- A **Galileo account** — sign up at [galileo.ai](https://galileo.ai)
- An **OpenAI API key** — get one from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## Setup

```bash
# 1. Clone the repo and cd into it
git clone <repo-url> && cd galileo-test

# 2. Install dependencies and create .venv
uv sync

# 3. Copy the env template and fill in your API keys
cp .env.example .env
```

Your `.env` file needs:

```
GALILEO_API_KEY=your-galileo-key-here
OPENAI_API_KEY=your-openai-key-here
```

## Running the Notebooks

Open any notebook in **Jupyter** or **VS Code** and select the `.venv/bin/python` interpreter as the kernel (installed via `ipykernel` in `uv sync`).

```bash
# Or activate the environment in your shell
source .venv/bin/activate
```

### Notebook Scenarios

| # | Notebook | What You'll Learn | Makes LLM Calls? |
|---|----------|-------------------|-------------------|
| 1 | `agents/1_chatbot.ipynb` | Auto-instrumentation, streaming, sessions, quality & safety metrics | Yes (OpenAI) |
| 2 | `agents/2_rag.ipynb` | Retriever + LLM spans, RAG metrics, datasets, prompt experiments | Yes (via experiment) |
| 3 | `agents/3_tools.ipynb` | Agent/tool/workflow spans, @log decorator, agentic metrics | No (manual spans) |
| 4 | `agents/4_experiments.ipynb` | Datasets, prompt templates, experiment runs, BLEU/ROUGE/tone, confidence | Yes (via experiment) |
| 5 | `agents/5_guardrails.ipynb` | Protect stages, rulesets, toxicity/PII/injection detection | No (invoke_protect) |
| 6 | `agents/6_custom_eval.ipynb` | Custom Python metrics, safety metrics, available scorers, distributed tracing | No (manual spans) |
| 7 | `agents/7_annotations.ipynb` | Annotation templates, human ratings, review workflows | No (manual traces + API) |
| 8 | `agents/8_agent_control.ipynb` | Full agent lifecycle: observe spans, evaluate with agentic metrics, protect with guardrails | No (manual spans + invoke_protect) |

Each notebook:
- Loads credentials from `.env`
- Creates a Galileo project and log stream
- Walks through the scenario step by step with detailed explanations
- Includes a final cleanup cell to delete the demo project

**Run cells in order.** Notebooks create Galileo projects/log streams and may make live API calls.

## Documentation

| File | Contents |
|------|----------|
| `docs/terminology.md` | Core Galileo concepts — spans, traces, metrics, experiments, guardrails, etc. |
| `docs/scenarios.md` | Scenario-based test plan with feature coverage matrix |
| `docs/galileo-features.md` | Full Galileo platform feature checklist (148 features) |

## Running Scripts

```bash
uv run main.py
```

## Project Structure

```
├── agents/              # Jupyter notebooks (one per scenario)
│   ├── 1_chatbot.ipynb
│   ├── 2_rag.ipynb
│   ├── 3_tools.ipynb
│   ├── 4_experiments.ipynb
│   ├── 5_guardrails.ipynb
│   ├── 6_custom_eval.ipynb
│   ├── 7_annotations.ipynb
│   └── 8_agent_control.ipynb
├── docs/                # Reference documentation
│   ├── terminology.md
│   ├── scenarios.md
│   └── galileo-features.md
├── .env.example         # Template for API keys
├── pyproject.toml       # Python dependencies
└── uv.lock              # Locked dependency versions
```
