# Galileo Platform Feature Evaluation Checklist

> Research compiled from https://v2docs.galileo.ai
> Date: 2026-03-10

## Evaluation Status Legend

| Status | Meaning |
|--------|---------|
| ⬜ | Not yet evaluated |
| 🔄 | In progress |
| ✅ | Evaluated - Working |
| ❌ | Evaluated - Issues found |
| ⏭️ | Skipped (not applicable) |

---

## 1. OBSERVABILITY (Logging & Tracing)

### 1.1 Hierarchical Logging Architecture
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 1.1.1 | Project creation and management | ⬜ | |
| 1.1.2 | Log stream creation and management | ⬜ | |
| 1.1.3 | Session grouping (multi-turn conversations) | ⬜ | |
| 1.1.4 | Trace creation (single request lifecycle) | ⬜ | |
| 1.1.5 | Span types: LLM spans | ⬜ | |
| 1.1.6 | Span types: Agent spans | ⬜ | |
| 1.1.7 | Span types: Tool spans | ⬜ | |
| 1.1.8 | Span types: Retriever spans | ⬜ | |
| 1.1.9 | Span types: Workflow spans | ⬜ | |
| 1.1.10 | Tags and metadata filtering | ⬜ | |
| 1.1.11 | Distributed tracing (Beta) | ⬜ | |

### 1.2 Logging Methods
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 1.2.1 | Manual logging via GalileoLogger | ⬜ | |
| 1.2.2 | Decorator-based logging (`@log`) | ⬜ | |
| 1.2.3 | Framework auto-instrumentation | ⬜ | |
| 1.2.4 | `galileo_context.init()` initialization | ⬜ | Already used in app.py |
| 1.2.5 | `GalileoLogger` direct usage | ⬜ | |

### 1.3 Console Visualization
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 1.3.1 | Flowchart visualization of traces | ⬜ | |
| 1.3.2 | Messages tab (conversation format) | ⬜ | |
| 1.3.3 | Condense Steps toggle | ⬜ | |
| 1.3.4 | Latency inspection per span | ⬜ | |
| 1.3.5 | Tool calls as separate spans | ⬜ | |

---

## 2. EVALUATION METRICS

### 2.1 Agentic Metrics (9 metrics)
| # | Metric | Scope | Status | Notes |
|---|--------|-------|--------|-------|
| 2.1.1 | Action Advancement | Trace | ⬜ | Whether each action moves toward goal |
| 2.1.2 | Action Completion | Session | ⬜ | Whether agent accomplished all objectives |
| 2.1.3 | Agent Efficiency | Session | ⬜ | Efficient execution path |
| 2.1.4 | Agent Flow | Session | ⬜ | Correctness of agentic trajectory |
| 2.1.5 | Conversation Quality | Session | ⬜ | Binary user satisfaction |
| 2.1.6 | Tool Error | Tool span | ⬜ | Tool execution failure detection |
| 2.1.7 | Tool Selection Quality | LLM span | ⬜ | Appropriateness of tool choices |
| 2.1.8 | Reasoning Coherence | LLM span | ⬜ | Logical consistency of reasoning |
| 2.1.9 | User Intent Change | Session | ⬜ | Detects goal shifts |

### 2.2 RAG Metrics (7 metrics)
| # | Metric | Status | Notes |
|---|--------|--------|-------|
| 2.2.1 | Chunk Relevance | ⬜ | Individual chunk usefulness |
| 2.2.2 | Context Relevance (Query Adherence) | ⬜ | Overall retrieval relevance |
| 2.2.3 | Context Precision | ⬜ | Relevant chunks weighted by position |
| 2.2.4 | Precision @ K | ⬜ | Relevant chunk % in top K |
| 2.2.5 | Chunk Attribution Utilization | ⬜ | Response uses/cites chunks |
| 2.2.6 | Context Adherence | ⬜ | Anti-hallucination metric |
| 2.2.7 | Completeness | ⬜ | Coverage of available context |

### 2.3 Response Quality Metrics (3 metrics)
| # | Metric | Status | Notes |
|---|--------|--------|-------|
| 2.3.1 | Ground Truth Adherence | ⬜ | Alignment with known answers |
| 2.3.2 | Correctness (Factuality) | ⬜ | Factual accuracy |
| 2.3.3 | Instruction Adherence | ⬜ | Whether model followed instructions |

### 2.4 Safety & Compliance Metrics (4 metrics)
| # | Metric | Status | Notes |
|---|--------|--------|-------|
| 2.4.1 | PII / CPNI / PHI Detection | ⬜ | Sensitive data detection |
| 2.4.2 | Prompt Injection Detection | ⬜ | Adversarial prompt detection |
| 2.4.3 | Sexism / Bias Detection | ⬜ | Gender/demographic bias |
| 2.4.4 | Toxicity Detection | ⬜ | Harmful content detection |

### 2.5 Model Confidence Metrics (2 metrics)
| # | Metric | Status | Notes |
|---|--------|--------|-------|
| 2.5.1 | Prompt Perplexity | ⬜ | Prompt difficulty for model |
| 2.5.2 | Uncertainty | ⬜ | Model confidence in response |

### 2.6 Expression & Readability (2 metrics)
| # | Metric | Status | Notes |
|---|--------|--------|-------|
| 2.6.1 | BLEU & ROUGE scores | ⬜ | Text generation quality |
| 2.6.2 | Tone assessment | ⬜ | Emotional tone alignment |

### 2.7 Text-to-SQL Metrics (4 metrics)
| # | Metric | Status | Notes |
|---|--------|--------|-------|
| 2.7.1 | SQL Correctness | ⬜ | Syntactic validity |
| 2.7.2 | SQL Adherence | ⬜ | Semantic alignment with intent |
| 2.7.3 | SQL Injection Detection | ⬜ | Security vulnerability detection |
| 2.7.4 | SQL Efficiency | ⬜ | Performance anti-patterns |

---

## 3. CUSTOM METRICS

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 3.1 | Custom LLM-as-a-Judge metrics | ⬜ | Natural language evaluation prompts |
| 3.2 | Output types: Boolean | ⬜ | |
| 3.3 | Output types: Categorical | ⬜ | |
| 3.4 | Output types: Count | ⬜ | |
| 3.5 | Output types: Discrete | ⬜ | |
| 3.6 | Output types: Percentage | ⬜ | |
| 3.7 | Chain-of-thought reasoning | ⬜ | |
| 3.8 | Multi-judge averaging | ⬜ | |
| 3.9 | Prompt Assist (AI-generated prompts) | ⬜ | |
| 3.10 | Custom code-based metrics (registered) | ⬜ | Org-wide, server-side |
| 3.11 | Custom code-based metrics (local) | ⬜ | Project-specific, client-side |
| 3.12 | Composite metrics | ⬜ | Reference other metric results |
| 3.13 | Metric version management | ⬜ | History and rollback |

---

## 4. EXPERIMENTS

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 4.1 | Run prompts against datasets | ⬜ | |
| 4.2 | Side-by-side experiment comparison (up to 5) | ⬜ | |
| 4.3 | Console-based experiment execution | ⬜ | |
| 4.4 | Code-based experiment execution (`run_experiment`) | ⬜ | |
| 4.5 | Model configuration (temp, top_p, etc.) | ⬜ | |
| 4.6 | Prompt templates with `{{variable}}` syntax | ⬜ | |
| 4.7 | Batch execution ("Run All") | ⬜ | |
| 4.8 | Historical tracking | ⬜ | |

---

## 5. DATASETS

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 5.1 | Create dataset via SDK | ⬜ | |
| 5.2 | Create dataset via file upload (CSV, JSON) | ⬜ | Console feature |
| 5.3 | Synthetic data generation | ⬜ | |
| 5.4 | Dataset versioning | ⬜ | |
| 5.5 | Organization-wide sharing | ⬜ | |
| 5.6 | Add/extend rows | ⬜ | |
| 5.7 | Derive datasets from logs | ⬜ | |

---

## 6. PROMPT MANAGEMENT

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 6.1 | Create prompt templates | ⬜ | |
| 6.2 | Mustache-style variable templating | ⬜ | |
| 6.3 | Multi-message templates (system/user roles) | ⬜ | |
| 6.4 | Template search and listing | ⬜ | |
| 6.5 | Integration with experiments | ⬜ | |

---

## 7. RUNTIME PROTECTION (Guardrails)

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 7.1 | Rule creation (metric + operator + value) | ⬜ | |
| 7.2 | Ruleset creation (AND logic) | ⬜ | |
| 7.3 | Stage configuration (prioritized rulesets) | ⬜ | |
| 7.4 | Passthrough action | ⬜ | |
| 7.5 | Override action | ⬜ | |
| 7.6 | Central stages (org-wide) | ⬜ | |
| 7.7 | Local stages (app-team managed) | ⬜ | |
| 7.8 | Pause/resume without redeployment | ⬜ | |
| 7.9 | Toxicity guardrail | ⬜ | |
| 7.10 | PII guardrail | ⬜ | |
| 7.11 | Prompt injection guardrail | ⬜ | |
| 7.12 | Context adherence guardrail | ⬜ | |
| 7.13 | Custom code metric guardrail | ⬜ | |

---

## 8. ALERTS & MONITORING

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 8.1 | Metric-based alerts (cost, correctness, etc.) | ⬜ | |
| 8.2 | Aggregation functions (avg, min, max, count, sum) | ⬜ | |
| 8.3 | Configurable thresholds and time windows | ⬜ | |
| 8.4 | Email notifications | ⬜ | |
| 8.5 | Slack webhook notifications | ⬜ | |
| 8.6 | Default system metrics (Status Code, Cost, Latency) | ⬜ | |
| 8.7 | Trends dashboard (widgets and sections) | ⬜ | |

---

## 9. ANNOTATIONS & HUMAN FEEDBACK

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 9.1 | Categories annotation (multi-select) | ⬜ | |
| 9.2 | Score annotation (0-N) | ⬜ | |
| 9.3 | Star annotation (1-5) | ⬜ | |
| 9.4 | Text annotation (freeform) | ⬜ | |
| 9.5 | Thumbs Up/Down annotation | ⬜ | |
| 9.6 | Annotation Queues (Enterprise Beta) | ⬜ | |
| 9.7 | Export annotations as columns | ⬜ | |

---

## 10. INTEGRATIONS

### 10.1 LLM Provider SDKs
| # | Integration | Mechanism | Status | Notes |
|---|------------|-----------|--------|-------|
| 10.1.1 | OpenAI SDK (Python) | Native wrapper | ⬜ | Already tested in app.py |
| 10.1.2 | OpenAI SDK (TypeScript) | Native wrapper | ⬜ | |
| 10.1.3 | Azure OpenAI | Native wrapper | ⬜ | |
| 10.1.4 | Anthropic | Manual span logging | ⬜ | |
| 10.1.5 | Google Gemini | SDK integration | ⬜ | |
| 10.1.6 | AWS Bedrock | API config | ⬜ | |
| 10.1.7 | Mistral | SDK integration | ⬜ | |
| 10.1.8 | NVIDIA NIM | Console config | ⬜ | |

### 10.2 Framework Integrations
| # | Integration | Mechanism | Status | Notes |
|---|------------|-----------|--------|-------|
| 10.2.1 | LangChain (Callback) | GalileoCallback | ⬜ | |
| 10.2.2 | LangGraph (Middleware) | GalileoMiddleware | ⬜ | |
| 10.2.3 | CrewAI | Event listener | ⬜ | |
| 10.2.4 | OpenAI Agents SDK | Trace processor | ⬜ | |
| 10.2.5 | Google ADK | Native plugin | ⬜ | |
| 10.2.6 | Vercel AI SDK | OpenTelemetry | ⬜ | |
| 10.2.7 | Microsoft Agent Framework | OpenTelemetry | ⬜ | |
| 10.2.8 | Strands Agents | OpenTelemetry | ⬜ | |

### 10.3 Universal Standards
| # | Integration | Status | Notes |
|---|------------|--------|-------|
| 10.3.1 | OpenTelemetry/OpenInference | ⬜ | Generic integration path |
| 10.3.2 | Custom model integration (JSON config) | ⬜ | |

---

## 11. LUNA-2 EVALUATION MODEL (Enterprise)

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 11.1 | Luna-2 3B model | ⬜ | ~125x cheaper than GPT-4o |
| 11.2 | Luna-2 8B model | ⬜ | |
| 11.3 | Fine-tuning with labeled samples | ⬜ | ~4,000 samples needed |
| 11.4 | 128k token context window | ⬜ | |

---

## 12. PROJECTS & ACCESS CONTROL

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 12.1 | Project creation/deletion | ⬜ | |
| 12.2 | Collaborator management | ⬜ | |
| 12.3 | Role-based access (Admin/Manager/User/Read-only) | ⬜ | |
| 12.4 | Group management (Enterprise) | ⬜ | |
| 12.5 | API key management | ⬜ | |

---

## 13. SDK FEATURES

### 13.1 Python SDK
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 13.1.1 | `galileo_context.init()` | ⬜ | |
| 13.1.2 | `GalileoLogger` manual logging | ⬜ | |
| 13.1.3 | `@log` decorator | ⬜ | |
| 13.1.4 | `run_experiment()` | ⬜ | |
| 13.1.5 | `create_dataset()` / dataset CRUD | ⬜ | |
| 13.1.6 | `enable_metrics()` | ⬜ | |
| 13.1.7 | `create_custom_llm_metric()` | ⬜ | |
| 13.1.8 | `ainvoke_protect()` (guardrails) | ⬜ | |
| 13.1.9 | Metric sampling configuration | ⬜ | |

### 13.2 TypeScript SDK
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 13.2.1 | `wrapOpenAI()` | ⬜ | |
| 13.2.2 | Dataset client | ⬜ | |
| 13.2.3 | Projects client | ⬜ | |
| 13.2.4 | Scorers client | ⬜ | |
| 13.2.5 | Logger client | ⬜ | |

---

## 14. AGENT CONTROL

### 14.1 Agent Observability
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.1.1 | Agent span creation and nesting | ⬜ | AgentSpan for decision-making steps |
| 14.1.2 | Tool span creation and nesting | ⬜ | ToolSpan for function/API invocations |
| 14.1.3 | Workflow span orchestration | ⬜ | WorkflowSpan for named pipelines |
| 14.1.4 | Session-based agent conversation grouping | ⬜ | Bundle multi-turn agent interactions |
| 14.1.5 | @log decorator for agent/tool/workflow | ⬜ | Auto-span creation from Python functions |
| 14.1.6 | Flowchart visualization of agent traces | ⬜ | Console tree view of span hierarchy |

### 14.2 Agent Framework Integrations
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.2.1 | OpenAI Agents SDK (GalileoTracingProcessor) | ⬜ | Auto-captures agent events, tool calls, handoffs |
| 14.2.2 | LangChain/LangGraph (GalileoCallback) | ⬜ | Callback-based, supports multi-agent graphs |
| 14.2.3 | Strands Agents (OpenTelemetry) | ⬜ | OTel with GalileoSpanProcessor |
| 14.2.4 | Microsoft Agent Framework (OpenTelemetry) | ⬜ | OTel integration |
| 14.2.5 | MCP Server tool call logging | ⬜ | Manual tool span logging for MCP calls |

### 14.3 Agent Evaluation Metrics
| # | Metric | Scope | Status | Notes |
|---|--------|-------|--------|-------|
| 14.3.1 | Action Advancement | Trace | ⬜ | Does each step advance toward the goal? |
| 14.3.2 | Action Completion | Session | ⬜ | Did agent accomplish all objectives? |
| 14.3.3 | Agent Efficiency | Session | ⬜ | Minimal redundant steps/tool calls? |
| 14.3.4 | Agent Flow | Session | ⬜ | Validates trajectory against test conditions |
| 14.3.5 | Reasoning Coherence | LLM span | ⬜ | Logical consistency of reasoning |
| 14.3.6 | Tool Error Detection | Tool span | ⬜ | API failures, parameter errors, timeouts |
| 14.3.7 | Tool Selection Quality | LLM span | ⬜ | Correct tool with correct arguments? |
| 14.3.8 | Conversation Quality | Session | ⬜ | User satisfaction signal |
| 14.3.9 | User Intent Change | Session | ⬜ | Detects goal shifts during session |

### 14.4 Agent Guardrails (Runtime Protection)
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.4.1 | Agentic metric rules in Protect stages | ⬜ | action_advancement, action_completion as rules |
| 14.4.2 | Tool reliability rules | ⬜ | tool_errors, tool_selection_quality as rules |
| 14.4.3 | Circular tool detection patterns | ⬜ | Prevent infinite loops in agent workflows |
| 14.4.4 | Agent response override on violation | ⬜ | Block or replace unsafe agent outputs |

### 14.5 Agent Reliability Patterns
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.5.1 | Hierarchical span creation patterns | ⬜ | entrypoint → workflow → tool → session |
| 14.5.2 | Session context tracking | ⬜ | conversationHistory, toolsUsed, metrics |
| 14.5.3 | Response caching for tool calls | ⬜ | Reduce redundant API calls |
| 14.5.4 | Dataset-driven agent testing | ⬜ | pytest + run_experiment for agents |

---

## Summary

| Category | Total Features | Evaluated | Passing | Failing |
|----------|---------------|-----------|---------|---------|
| Observability | 16 | 0 | 0 | 0 |
| Evaluation Metrics | 31 | 0 | 0 | 0 |
| Custom Metrics | 13 | 0 | 0 | 0 |
| Experiments | 8 | 0 | 0 | 0 |
| Datasets | 7 | 0 | 0 | 0 |
| Prompt Management | 5 | 0 | 0 | 0 |
| Runtime Protection | 13 | 0 | 0 | 0 |
| Alerts & Monitoring | 7 | 0 | 0 | 0 |
| Annotations | 7 | 0 | 0 | 0 |
| Integrations | 18 | 0 | 0 | 0 |
| Luna-2 Model | 4 | 0 | 0 | 0 |
| Access Control | 5 | 0 | 0 | 0 |
| SDK Features | 14 | 0 | 0 | 0 |
| Agent Control | 24 | 0 | 0 | 0 |
| **TOTAL** | **172** | **0** | **0** | **0** |
