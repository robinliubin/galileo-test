# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## What This Repo Is

An exploratory, educational project for learning the Galileo SDK (`galileo`) through hands-on Jupyter notebooks. Reference docs: https://v2docs.galileo.ai/getting-started/quickstart

## Methodology

This repo follows a structured approach to learning and evaluating the Galileo platform:

1. **Extract features** — Fetch the Galileo v2 docs, catalog every platform capability into a feature checklist (`docs/galileo-features.md`, 148 features across 13 categories)
2. **Design scenarios** — Group features into realistic use cases that a developer would actually build (`docs/scenarios.md`, 7 scenarios covering ~92 features)
3. **Define terminology** — Extract core concepts and explain them for beginners (`docs/terminology.md` — spans, traces, metrics, experiments, guardrails, annotations)
4. **Build notebooks** — For each scenario, create a self-contained Jupyter notebook under `agents/` in an exploratory, educational format so a new user with zero Galileo knowledge can follow along and learn the platform step by step

### Why This Order Matters

Features → Scenarios → Terminology → Notebooks. You can't write good tutorials without first understanding the full feature surface. You can't design good scenarios without grouping features into coherent use cases. And you can't write beginner-friendly notebooks without first defining the vocabulary.

## Architecture

- **`agents/*.ipynb`** — Jupyter notebooks, one per scenario. Each is a self-contained entry point with detailed markdown explanations before every code cell.
- **`docs/`** — Reference documentation (feature checklist, scenario plan, terminology guide).
- **`.env`** — API keys (`GALILEO_API_KEY`, `OPENAI_API_KEY`). Not committed. See `.env.example`.

## Setup

This project uses **uv** for dependency management. See `README.md` for full setup instructions.

```bash
uv sync            # install dependencies
cp .env.example .env  # add API keys
```

## Galileo SDK Patterns

- **OpenAI**: Auto-instruments via `galileo.openai` wrapper + `galileo_context.init()` — no manual span logging needed.
- **Anthropic**: Requires manual span logging with `GalileoLogger` — `start_trace()`, `add_llm_span()`, `conclude()`, `flush()`.
- **Metrics**: Configured per log stream via `enable_metrics()`. Each call replaces the full metric set.
- **Experiments**: Run a prompt template or Python function over a dataset, score every row.
- **Guardrails**: Runtime protection via `invoke_protect()` with stages, rulesets, and actions.
- All traces are viewable in the Galileo Console at the project/log-stream URLs printed after execution.

## Notebook Conventions

- Every code cell has a preceding markdown cell explaining what it does and why
- Notebooks assume the reader knows nothing about Galileo
- Each notebook creates its own Galileo project and includes a cleanup cell at the end
- Notebooks are numbered to suggest a learning order (1–7)
