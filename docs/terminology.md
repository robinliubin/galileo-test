# Galileo Terminology & Core Concepts

A beginner-friendly guide to the terms, data model, and patterns used throughout the Galileo SDK and these notebooks.

---

## The Galileo Data Model

Galileo organizes your LLM observability data in a hierarchy:

```
Organization
 └── Project
      └── Log Stream
           └── Session (optional)
                └── Trace
                     └── Span
                          └── Nested Span (optional)
```

---

## Projects

**What:** A top-level container in Galileo — like a repository for one application or use case.

**Why:** Projects keep data from different apps separated. Each project has its own log streams, datasets, experiments, guardrail stages, and annotation templates.

**When to create a new project:** One project per application or team. For example, `customer-support-bot` and `internal-qa-tool` would be separate projects.

```python
galileo_context.init(project="my-chatbot")
```

---

## Log Streams

**What:** A named feed of traces within a project — like a topic or channel.

**Why:** Log streams let you separate data within the same project. Common uses: one stream per environment (dev, staging, prod), per feature, or per experiment type.

**Key behavior:**
- Metrics are configured **per log stream** — different streams can have different metrics enabled
- Each `enable_metrics()` call **replaces** the stream's entire metric set

```python
galileo_context.init(project="my-chatbot", log_stream="production")
```

---

## Sessions

**What:** A logical grouping of traces that belong to one conversation or user interaction.

**Why:** Without sessions, each LLM call appears as an isolated trace. Sessions let you see the full multi-turn conversation thread and enable session-level metrics (conversation quality, action completion).

**When to use:** Any multi-turn interaction — chatbots, agents with multiple steps, wizard-style workflows.

```python
galileo_context.start_session(name="user-session-42")
# ... multiple LLM calls ...
galileo_context.flush()  # sends all traces in the session
```

---

## Traces

**What:** One end-to-end request through your application — from user input to final output.

**Why:** A trace captures the complete picture of a single interaction: what the user asked, what your app did, and what it returned. Traces are the primary unit you inspect in the Galileo Console.

**What's inside a trace:**
- An **input** (the user's question or request)
- An **output** (the final answer or response)
- One or more **spans** (the individual steps that happened)
- **Metrics** (automated scores like correctness, toxicity, etc.)
- **Metadata** (tags, timestamps, token counts)

```python
logger.start_trace(input="What is Galileo?")
# ... add spans ...
logger.conclude(output="Galileo is an AI observability platform.")
logger.flush()
```

---

## Spans

**What:** A unit of work inside a trace. Each span represents one discrete operation — an LLM call, a tool invocation, a document retrieval, etc.

**Why:** Spans give you visibility into **what happened inside** a trace. A trace tells you "the user asked X and got Y." Spans tell you "the app first searched the database, then called the LLM, then formatted the response." This granularity is essential for debugging, optimization, and understanding complex LLM pipelines.

### Span Types

Galileo supports 5 span types, each representing a different kind of operation:

| Span Type | What It Represents | When to Use | Example |
|-----------|-------------------|-------------|---------|
| **LLM** | A call to a language model | Every LLM API call (OpenAI, Anthropic, etc.) | `chat.completions.create()` |
| **Retriever** | A search/retrieval operation | Fetching documents from a vector DB, search engine, or knowledge base | Querying Pinecone, Elasticsearch, or a local document store |
| **Tool** | A tool or function invocation | Any external action the agent takes — API calls, database queries, calculations | `search_flights()`, `send_email()`, `run_sql()` |
| **Agent** | An agent's decision-making step | When an AI agent reasons about what to do next | "I should search for flights, then compare prices" |
| **Workflow** | A named pipeline or orchestration step | Grouping related sub-operations into a logical unit | "ItineraryWorkflow" containing research + booking + confirmation |

### Span Nesting

Spans can be **nested** to show parent-child relationships:

```
Trace: "Plan a trip to Tokyo"
 └── Workflow Span: "TripPlanningWorkflow"
      ├── Agent Span: "ResearchAgent"
      │    ├── Tool Span: search_flights()
      │    └── Tool Span: search_hotels()
      ├── LLM Span: "Summarize options"
      └── Tool Span: book_flight()
```

In the Galileo Console, nested spans appear as an expandable tree view, letting you drill into each step.

### How to Create Spans

**Auto-instrumentation (easiest):** Use Galileo's wrapped OpenAI client — LLM spans are created automatically.

```python
from galileo.openai import openai
client = openai.OpenAI()
# Every call is auto-logged as an LLM span
response = client.chat.completions.create(model="gpt-4o-mini", messages=[...])
```

**@log Decorator (recommended for custom functions):** Decorate your Python functions to auto-create spans.

```python
from galileo.decorator import log as galileo_log

@galileo_log(span_type="tool")
def search_flights(origin, destination):
    return api.search(origin, destination)

@galileo_log(span_type="agent")
def travel_agent(query):
    flights = search_flights("SFO", "NRT")  # nested tool span
    return f"Found {len(flights)} flights"
```

**Manual logging (full control):** Use `GalileoLogger` to create spans with explicit parameters.

```python
logger = GalileoLogger(project="my-app", log_stream="dev")
logger.start_trace(input="user question")
logger.add_retriever_span(input="query", output=["doc1", "doc2"])
logger.add_llm_span(
    input=[Message(role=MessageRole.user, content="question")],
    output=Message(role=MessageRole.assistant, content="answer"),
    model="gpt-4o-mini",
)
logger.conclude(output="final answer")
logger.flush()
```

---

## Metrics

**What:** Automated scorers that evaluate your traces along quality, safety, and performance dimensions.

**Why:** Manually reviewing every LLM response doesn't scale. Metrics let you automatically score thousands of traces and surface the ones that need attention.

### Metric Categories

| Category | Examples | Use Case |
|----------|----------|----------|
| **Response Quality** | Correctness, Instruction Adherence, Ground Truth Adherence | Is the LLM accurate and following instructions? |
| **RAG Quality** | Context Adherence, Chunk Relevance, Completeness, Context Precision | Is the retrieval system finding good documents? Is the LLM using them? |
| **Agentic** | Action Advancement, Agent Efficiency, Tool Selection Quality, Agent Flow | Is the agent making good decisions and using tools well? |
| **Safety** | Toxicity, PII Detection, Prompt Injection, Sexism/Bias | Is the content safe, compliant, and appropriate? |
| **Confidence** | Perplexity, Uncertainty | How confident is the model in its output? |
| **Expression** | BLEU, ROUGE, Tone | Does the output match a reference style or tone? |
| **Custom** | Any Python function you write | Domain-specific scoring (e.g., "response must be under 200 chars") |

### How Metrics Work

1. **Enable metrics on a log stream** — this tells Galileo which scorers to run
2. **Log traces** — send data to that log stream
3. **Galileo scores the traces** — metrics appear as columns in the Console
4. **Review results** — sort, filter, and drill into low-scoring traces

```python
from galileo.log_streams import enable_metrics
from galileo import GalileoMetrics

enable_metrics(
    project_name="my-chatbot",
    log_stream_name="production",
    metrics=[
        GalileoMetrics.correctness,
        GalileoMetrics.input_toxicity,
        GalileoMetrics.output_pii,
    ],
)
```

**Important:** Each `enable_metrics()` call **replaces** the entire metric set for that log stream. Always include all the metrics you want active in a single call.

---

## Datasets

**What:** A collection of input/output test pairs used for experiments.

**Why:** Datasets let you systematically evaluate your prompts and models across many examples instead of testing one question at a time.

**Structure:**
- `input` — the question or prompt (fed to the template)
- `output` — the expected/reference answer (used by metrics like Ground Truth Adherence, BLEU, ROUGE)

```python
from galileo.datasets import create_dataset

ds = create_dataset(
    name="qa-test-set",
    content=[
        {"input": "What is Galileo?", "output": "An AI observability platform."},
        {"input": "What is RAG?", "output": "Retrieval-Augmented Generation."},
    ],
    project_name="my-project",
)
```

---

## Experiments

**What:** A systematic way to run a prompt or function over an entire dataset and score every result.

**Why:** Instead of manually testing "does my prompt work for this one question?", experiments answer "how does my prompt perform across 50 diverse questions?" They let you compare prompt versions, model settings, and approaches with evidence.

**Components:**
- **Dataset** — the test cases to run against
- **Prompt Template** or **Function** — what to run on each test case
- **Metrics** — how to score the results
- **PromptRunSettings** — model configuration (temperature, max_tokens, model_alias)

```python
from galileo.experiments import run_experiment, PromptRunSettings

run_experiment(
    experiment_name="baseline-v1",
    dataset="qa-test-set",
    prompt_template=my_template,
    metrics=[GalileoMetrics.correctness, GalileoMetrics.ground_truth_adherence],
    prompt_settings=PromptRunSettings(model_alias="GPT-4o mini", temperature=0.3),
    project="my-project",
)
```

---

## Guardrails (Galileo Protect)

**What:** Runtime safety checks that evaluate content against rules and take action when violations are detected.

**Why:** Guardrails protect your users and your app. They intercept requests or responses and can block, override, or flag unsafe content — before it reaches the user or the LLM.

### Key Concepts

| Term | What It Means |
|------|--------------|
| **Stage** | A named checkpoint (e.g., "toxicity-filter") that you invoke at runtime |
| **Ruleset** | A set of rules + an action. Rules within a ruleset use AND logic |
| **Rule** | A condition: `metric` `operator` `value` (e.g., `input_toxicity >= 0.5`) |
| **Action** | What happens when triggered — e.g., `OverrideAction` replaces the content |
| **Payload** | The input/output being checked |
| **invoke_protect()** | Sends a payload through a stage and returns the result |

### Execution Statuses

| Status | Meaning |
|--------|---------|
| `not_triggered` | Content passed all rules — safe to proceed |
| `triggered` | A rule was violated — the action (e.g., override) was applied |
| `error` | Something went wrong (e.g., wrong metric for the payload type) |

```python
from galileo import invoke_protect, Payload

result = invoke_protect(
    payload=Payload(input="user message here"),
    stage_name="toxicity-filter",
    project_name="my-project",
)
if result.status == "triggered":
    return result.action_result["value"]  # return the safe override message
```

---

## Annotations

**What:** Human feedback attached to traces — ratings, tags, notes, and approval signals.

**Why:** Automated metrics are great for scale, but some qualities can only be judged by humans: empathy, brand voice, policy compliance, nuanced correctness. Annotations let reviewers score traces directly.

### Annotation Types

| Type | What It Captures | Example |
|------|-----------------|---------|
| **Score** | Numeric rating (min to max) | Helpfulness: 4 out of 5 |
| **Star** | 1-5 star rating | Tone quality: ★★★★☆ |
| **Tags** | Categorical labels (multi-select) | Issues: `too_vague`, `missing_empathy` |
| **Text** | Free-form reviewer note | "Add empathy before stating the refund policy" |
| **Like/Dislike** | Binary thumbs up/down | Ship to production? 👎 |

### Workflow

1. **Create annotation templates** — reusable review forms (e.g., "Rate helpfulness 1-5")
2. **Log traces** — get some data worth reviewing
3. **Submit ratings** — attach human feedback to specific traces (via Console UI or API)
4. **Export** — use annotated data to improve prompts or build training datasets

---

## Distributed Tracing

**What:** Connecting spans from multiple microservices into a single end-to-end trace.

**Why:** In production, your LLM app often involves multiple services: an API gateway, a retriever service, an LLM service, a post-processing service. Distributed tracing lets all services contribute spans to the same trace, so you see the full picture.

**How it works:**
1. Service A creates a trace and gets tracing headers
2. Service A passes headers to Service B via HTTP
3. Service B uses the headers to attach its spans to the same trace

```python
# Service A
logger = GalileoLogger(project="my-app", log_stream="prod", mode="distributed")
logger.start_trace(input="user query")
headers = logger.get_tracing_headers()
# Pass headers to Service B: {"X-Galileo-Trace-ID": "...", "X-Galileo-Parent-ID": "..."}
```

---

## Logging Methods Comparison

Galileo offers three ways to log traces, each suited to different situations:

| Method | Best For | Effort | Control |
|--------|----------|--------|---------|
| **Auto-instrumentation** (`galileo.openai`) | OpenAI apps — just swap the import | Minimal | Low — spans created automatically |
| **@log Decorator** (`@galileo_log`) | Custom Python functions — decorate and forget | Low | Medium — you choose span types |
| **Manual Logging** (`GalileoLogger`) | Full control — any provider, any structure | High | Full — you define every span |

### Decision Guide

```
Are you using OpenAI?
 ├── Yes → Use auto-instrumentation (galileo.openai)
 └── No
      ├── Do you have Python functions to instrument?
      │    └── Yes → Use @log decorator
      └── Need full control or using Anthropic/other?
           └── Use GalileoLogger manually
```

---

## The `flush()` Pattern

**What:** `galileo_context.flush()` or `logger.flush()` sends all buffered traces to Galileo's servers.

**Why:** Galileo buffers traces locally for performance. Without flushing, your traces stay in memory and never reach the server. Think of it like `git push` — your work exists locally until you push.

**When to flush:**
- After completing a logical unit of work (one request, one conversation)
- At the end of a session
- Before your program exits

**When NOT to flush:**
- After every single LLM call in a multi-turn session (this creates separate traces instead of one conversation)

---

## Agent Control

### What is Agent Control?

Agent Control is not a single Galileo feature — it's the combination of three capabilities applied to AI agents:

1. **Observe** — Capture every agent decision, tool call, and LLM interaction as structured spans
2. **Evaluate** — Score agent behavior with 9 purpose-built agentic metrics
3. **Protect** — Apply runtime guardrails using agentic metric rules

### Agent-Specific Span Patterns

The typical span hierarchy for an agent:

```
Session: "user-conversation-42"
 └── Trace: "Plan a trip to Tokyo"
      └── Agent Span: "TravelPlannerAgent" (decision-making)
           ├── Tool Span: search_flights() (action)
           ├── Tool Span: search_hotels() (action)
           └── LLM Span: "Summarize options" (generation)
```

### Agent Framework Integrations

| Framework | Integration Method | Auto-captures |
|-----------|-------------------|---------------|
| OpenAI Agents SDK | GalileoTracingProcessor | Agent events, tool calls, handoffs |
| LangChain/LangGraph | GalileoCallback | Full agent graph, multi-agent routing |
| Strands Agents | OpenTelemetry (GalileoSpanProcessor) | Built-in telemetry |
| Microsoft Agent Framework | OpenTelemetry (GalileoSpanProcessor) | LLM I/O with sensitive data option |
| MCP Servers | Manual logger.add_tool_span() | Tool call inputs/outputs |

### Agent Reliability Patterns

- **Circular tool detection**: Monitor for alternating/repeating tool call patterns that indicate infinite loops
- **Session context tracking**: Maintain conversation history, tools used, and execution metrics across turns
- **Response caching**: Cache frequently accessed tool results to reduce redundant API calls
- **Dataset-driven testing**: Use pytest + run_experiment to systematically test agent behavior

---

## Glossary Quick Reference

| Term | One-Line Definition |
|------|-------------------|
| **Project** | Top-level container for one app or use case |
| **Log Stream** | Named feed of traces within a project |
| **Session** | Group of traces forming one conversation |
| **Trace** | One end-to-end request (input → output) |
| **Span** | One operation within a trace (LLM call, tool call, etc.) |
| **Metric** | Automated scorer that evaluates traces |
| **Dataset** | Collection of test input/output pairs |
| **Experiment** | Runs a prompt over a dataset and scores results |
| **Guardrail** | Runtime safety check (stage + rulesets + actions) |
| **Annotation** | Human feedback attached to a trace |
| **flush()** | Sends buffered traces to Galileo's servers |
| **Auto-instrumentation** | Automatic trace logging via a wrapped client |
| **@log Decorator** | Turns a Python function into a Galileo span |
| **Distributed Tracing** | Connecting spans from multiple services into one trace |
| **Agent Control** | Observe + Evaluate + Protect applied to AI agents |
| **Agent Framework Integration** | Auto-instrumentation for agent frameworks (OpenAI Agents, LangGraph, etc.) |
| **Circular Tool Detection** | Pattern to prevent infinite loops in agent tool call sequences |
| **Agentic Metrics** | 9 purpose-built metrics for evaluating agent behavior |
