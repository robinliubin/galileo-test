# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python test project for learning the Galileo SDK (`galileo`). Uses Galileo's observability platform to log and trace LLM calls. Reference docs: https://v2docs.galileo.ai/getting-started/quickstart

## Setup

This project uses **uv** for dependency and environment management.

```bash
# Install dependencies and create .venv (from pyproject.toml + uv.lock)
uv sync

# Add new dependencies
uv add <package>

# Copy and fill in API keys
cp .env.example .env
```

Both `GALILEO_API_KEY` and the `OPENAI_API_KEY` are required in `.env`.

## Running

```bash
uv run main.py
```

## Architecture

- All notebooks (`.ipynb` files) are located in the `agents/` folder. These serve as entry points, where Galileo context is initialized, LLM calls are made, and traces are logged.
- **`.env`** — API keys (not committed). See `.env.example` for required variables.

## Galileo SDK Patterns

- **OpenAI**: Galileo auto-instruments via `galileo_context.init()` — no manual span logging needed.
- **Anthropic**: Requires manual span logging with `logger.start_trace()`, `logger.add_llm_span()`, `logger.conclude()`, and `logger.flush()`.
- All traces are viewable in the Galileo console at the project/log-stream URLs printed after execution.
