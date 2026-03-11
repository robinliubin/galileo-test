# Galileo Evaluation — Scenario-Based Test Plan

## Scenario → Feature Coverage Matrix

### Scenario 1: Simple Chatbot Monitoring
**Story:** A developer builds a customer support chatbot with OpenAI and wants to monitor conversation quality in Galileo.

| Step | What the user does | Features covered |
|------|--------------------|-----------------|
| 1 | Bootstrap Galileo quickstart context (auto-creates project + log stream) | 1.1.1, 1.1.2, 12.1 |
| 2 | Initialize Galileo context | 1.2.4 (galileo_context.init) |
| 3 | Make OpenAI chat calls via wrapped client | 10.1.1 (OpenAI wrapper), 1.2.3 (auto-instrumentation) |
| 4 | Stream a response | 10.1.1b (streaming) |
| 5 | Run multi-turn conversation in a session | 1.1.3 (sessions), 1.1.4 (traces), 1.1.5 (LLM spans) |
| 6 | Enable response quality metrics | 2.3.2 (correctness), 2.3.3 (instruction adherence) |
| 7 | Enable safety metrics | 2.4.1 (PII), 2.4.4 (toxicity) |
| 8 | Tag traces with metadata | 1.1.10 (tags/metadata) |
| **Total** | | **~15 features** |

---

### Scenario 2: RAG Q&A Application
**Story:** A developer builds a document Q&A system. They retrieve chunks from a knowledge base and generate answers. They want to evaluate retrieval quality and catch hallucinations.

| Step | What the user does | Features covered |
|------|--------------------|-----------------|
| 1 | Bootstrap Galileo quickstart context (auto-creates project + log stream) | 1.1.1, 1.1.2 |
| 2 | Log RAG traces: retriever span → LLM span | 1.1.8 (retriever), 1.1.5 (LLM), 1.2.1 (manual logger) |
| 3 | Enable RAG metrics | 2.2.1 (chunk relevance), 2.2.2 (context relevance), 2.2.6 (context adherence), 2.2.7 (completeness) |
| 4 | Enable additional RAG metrics | 2.2.3 (context precision), 2.2.4 (precision@K), 2.2.5 (chunk attribution) |
| 5 | Create evaluation dataset | 5.1 (create dataset), 5.6 (add rows) |
| 6 | Run experiment comparing prompts | 4.1 (run_experiment), 4.6 (prompt templates) |
| 7 | Check ground truth adherence | 2.3.1 (ground truth adherence) |
| **Total** | | **~17 features** |

---

### Scenario 3: AI Agent with Tools
**Story:** A developer builds a multi-step AI agent that can search the web, query databases, and call APIs. They want to monitor agent decisions, tool usage, and overall efficiency.

| Step | What the user does | Features covered |
|------|--------------------|-----------------|
| 1 | Bootstrap Galileo quickstart context (auto-creates project + log stream) | 1.1.1, 1.1.2 |
| 2 | Log agent session with multiple turns | 1.1.3 (session), 1.1.6 (agent spans) |
| 3 | Log tool calls within agent | 1.1.7 (tool spans), 1.1.5 (LLM spans) |
| 4 | Nest spans in a workflow | 1.1.9 (workflow spans), 1.1.4 (traces) |
| 5 | Use @log decorator for agent functions | 1.2.2 (@log decorator) |
| 6 | Enable agentic metrics | 2.1.1 (action advancement), 2.1.3 (agent efficiency), 2.1.4 (agent flow) |
| 7 | Enable tool metrics | 2.1.6 (tool error), 2.1.7 (tool selection quality) |
| 8 | Enable reasoning metrics | 2.1.8 (reasoning coherence) |
| 9 | Session-level metrics | 2.1.2 (action completion), 2.1.5 (conversation quality), 2.1.9 (user intent change) |
| **Total** | | **~18 features** |

---

### Scenario 4: Prompt Engineering Lab
**Story:** A team wants to systematically compare different prompts and models for their application. They create datasets, run experiments, and compare results.

| Step | What the user does | Features covered |
|------|--------------------|-----------------|
| 1 | Bootstrap Galileo quickstart context (auto-creates project + log stream) | 1.1.1 |
| 2 | Create evaluation dataset | 5.1 (create dataset) |
| 3 | Add more test cases | 5.6 (add rows) |
| 4 | Create prompt template with variables | 6.1, 6.2, 6.3 (prompt templates) |
| 5 | Run experiment with prompt template | 4.1, 4.4 (run_experiment) |
| 6 | Run experiment with custom function | 4.4 (code-based experiment) |
| 7 | Configure model settings | 4.5 (PromptRunSettings) |
| 8 | Evaluate with BLEU/ROUGE | 2.6.1 (BLEU, ROUGE) |
| 9 | Evaluate tone | 2.6.2 (tone) |
| 10 | Check model confidence | 2.5.1 (perplexity), 2.5.2 (uncertainty) |
| **Total** | | **~15 features** |

---

### Scenario 5: Production Guardrails
**Story:** The app is going to production. The team sets up runtime protection to block toxic content, detect prompt injection, and flag PII before responses reach users.

| Step | What the user does | Features covered |
|------|--------------------|-----------------|
| 1 | Bootstrap Galileo quickstart context (auto-creates project + log stream) | 1.1.1 |
| 2 | Create toxicity guardrail stage | 7.1 (rules), 7.2 (rulesets), 7.3 (stages), 7.9 (toxicity) |
| 3 | Test passthrough on safe input | 7.4 (passthrough action) |
| 4 | Test override on toxic input | 7.5 (override action) |
| 5 | Create prompt injection stage | 7.11 (prompt injection guardrail) |
| 6 | Test injection detection | 7.11 |
| 7 | Create PII detection stage | 7.10 (PII guardrail) |
| 8 | Pause and resume a stage | 7.8 (pause/resume) |
| 9 | Invoke protect in a real LLM call flow | Combines 7.x with 10.1.1 |
| **Total** | | **~12 features** |

---

### Scenario 6: Custom Evaluation Pipeline
**Story:** A team has domain-specific quality requirements that built-in metrics don't cover. They create custom code-based scorers and wire them into their logging pipeline.

| Step | What the user does | Features covered |
|------|--------------------|-----------------|
| 1 | Bootstrap Galileo quickstart context (auto-creates project + log stream) | 1.1.1, 1.1.2 |
| 2 | Define custom code metric (local) | 3.11 (local code metric) |
| 3 | Enable custom metric on log stream | 13.1.6 (enable_metrics) |
| 4 | Use @log decorator to instrument functions | 1.2.2 (@log decorator) |
| 5 | Log traces with GalileoLogger | 1.2.1, 1.2.5 (manual logging) |
| 6 | Enable safety metrics alongside custom | 2.4.2 (prompt injection), 2.4.3 (sexism/bias) |
| 7 | List available scorers | 3.1a (list scorers) |
| 8 | Get distributed tracing headers | 1.1.11 (distributed tracing) |
| **Total** | | **~12 features** |

---

## Summary

| Scenario | Features | Makes real LLM calls? |
|----------|----------|----------------------|
| 1. Simple Chatbot | ~15 | Yes (OpenAI) |
| 2. RAG Application | ~17 | Yes (via experiment) |
| 3. AI Agent + Tools | ~18 | No (manual spans) |
| 4. Prompt Engineering | ~15 | Yes (via experiment) |
| 5. Production Guardrails | ~12 | No (invoke_protect) |
| 6. Custom Evaluation | ~12 | No (manual spans) |
| **Total unique** | **~85** | |
