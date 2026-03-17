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
| 1.2.6 | Batch logging mode | ⬜ | |
| 1.2.7 | OpenAI streaming support | ⬜ | |

### 1.3 Console Visualization
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 1.3.1 | Flowchart visualization of traces | ⬜ | |
| 1.3.2 | Messages tab (conversation format) | ⬜ | |
| 1.3.3 | Condense Steps toggle | ⬜ | |
| 1.3.4 | Latency inspection per span | ⬜ | |
| 1.3.5 | Tool calls as separate spans | ⬜ | |
| 1.3.6 | Session overview dashboard | ⬜ | |
| 1.3.7 | Agent execution graph visualization | ⬜ | |
| 1.3.8 | Log stream data export (CSV/JSON) | ⬜ | |
| 1.3.9 | Column-based filtering in log streams | ⬜ | |

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
| 3.14 | Fine-tuned evaluation models | ⬜ | Custom fine-tuned metric models |
| 3.15 | Scorer feedback mechanism | ⬜ | Feedback on metric scorer accuracy |
| 3.16 | Code metrics at specific span levels (LLM, Tool, Retriever, Agent, Workflow, Trace, Session) | ⬜ | |

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
| 4.9 | Experiment results export and charts | ⬜ | |
| 4.10 | Re-run experiments with different model parameters | ⬜ | |

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
| 5.8 | Copy log data to dataset | ⬜ | |

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
| 8.8 | Job monitoring and progress tracking | ⬜ | Background job status |

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
| 12.6 | Organization creation and management | ⬜ | |
| 12.7 | Organization permissions | ⬜ | |
| 12.8 | SSO authentication (Enterprise) | ⬜ | |
| 12.9 | User onboarding flow | ⬜ | |

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
| 13.1.10 | Batch logging mode | ⬜ | |
| 13.1.11 | Future SDK object model (Project, Dataset, Experiment, Prompt, LogStream, Metric classes) | ⬜ | Next-gen API |

### 13.2 TypeScript SDK
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 13.2.1 | `wrapOpenAI()` | ⬜ | |
| 13.2.2 | Dataset client | ⬜ | |
| 13.2.3 | Projects client | ⬜ | |
| 13.2.4 | Scorers client | ⬜ | |
| 13.2.5 | Logger client | ⬜ | |
| 13.2.6 | Complex trace graph creation | ⬜ | |
| 13.2.7 | LangChain callback handler | ⬜ | |
| 13.2.8 | Log stream management | ⬜ | |

---

## 14. AGENT CONTROL (Runtime Guardrails Platform)

> Agent Control is a standalone open-source platform for adding runtime guardrails to AI agents.
> Repo: https://github.com/agentcontrol/agent-control

### 14.1 Agent Control Core
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.1.1 | agent_control.init() initialization | ⬜ | Register agent with server |
| 14.1.2 | @control() decorator | ⬜ | Protect any async function |
| 14.1.3 | Control definition (scope + selector + evaluator + action) | ⬜ | Core data model |
| 14.1.4 | AgentControlClient HTTP client | ⬜ | Direct API interaction |
| 14.1.5 | Server health check | ⬜ | Verify connectivity |
| 14.1.6 | Background policy refresh | ⬜ | Auto-refresh controls cache |

### 14.2 Built-in Evaluators
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.2.1 | Regex evaluator | ⬜ | Pattern matching (SSN, PII, prompt injection) |
| 14.2.2 | List evaluator | ⬜ | Value matching (banned terms, allowlists) |
| 14.2.3 | JSON evaluator | ⬜ | Schema validation, field constraints, type checks |
| 14.2.4 | SQL evaluator | ⬜ | Query validation, operation blocking, table access |
| 14.2.5 | Luna-2 evaluator (Galileo) | ⬜ | AI-powered toxicity, injection detection |

### 14.3 Actions and Error Handling
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.3.1 | Deny action | ⬜ | Hard block, raises ControlViolationError |
| 14.3.2 | Steer action | ⬜ | Corrective guidance, raises ControlSteerError |
| 14.3.3 | Warn action | ⬜ | Log warning, continue execution |
| 14.3.4 | Log action | ⬜ | Observability only |
| 14.3.5 | Allow action | ⬜ | Explicit pass-through |
| 14.3.6 | ControlViolationError handling | ⬜ | Graceful deny recovery |
| 14.3.7 | ControlSteerError handling | ⬜ | Steering context interpretation |

### 14.4 Agent and Control Management
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.4.1 | Register agent via SDK | ⬜ | agent_control.init() or agents API |
| 14.4.2 | Create controls via SDK | ⬜ | controls.create_control() |
| 14.4.3 | Associate controls with agent | ⬜ | agents.add_agent_control() |
| 14.4.4 | List agent controls | ⬜ | agents.list_agent_controls() |
| 14.4.5 | Create policy | ⬜ | policies.create_policy() |
| 14.4.6 | Add controls to policy | ⬜ | policies.add_control_to_policy() |
| 14.4.7 | Assign policy to agent | ⬜ | policies.assign_policy_to_agent() |

### 14.5 Scope and Selector Configuration
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.5.1 | Pre-execution scope (stages: ["pre"]) | ⬜ | Check inputs before execution |
| 14.5.2 | Post-execution scope (stages: ["post"]) | ⬜ | Check outputs after execution |
| 14.5.3 | Step type filtering (tool, llm) | ⬜ | Target specific step types |
| 14.5.4 | Step name filtering | ⬜ | Target specific named functions |
| 14.5.5 | Selector path expressions | ⬜ | Extract data (input, output, input.field) |

### 14.6 Framework Integrations
| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 14.6.1 | LangChain integration | ⬜ | SQL agent protection |
| 14.6.2 | CrewAI integration | ⬜ | Multi-agent guardrails |
| 14.6.3 | Google ADK integration | ⬜ | Callback and decorator patterns |
| 14.6.4 | Strands Agents integration | ⬜ | Steering handler |

---

## 15. AUTO-TUNE

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 15.1 | Auto-tune with preset metrics | ⬜ | Automated metric optimization |
| 15.2 | Auto-tune with custom metrics | ⬜ | |

---

## 16. PLAYGROUND

| # | Feature | Status | Notes |
|---|---------|--------|-------|
| 16.1 | Interactive playground for LLM testing | ⬜ | |

---

## Summary

| Category | Total Features | Evaluated | Passing | Failing |
|----------|---------------|-----------|---------|---------|
| Observability | 22 | 0 | 0 | 0 |
| Evaluation Metrics | 31 | 0 | 0 | 0 |
| Custom Metrics | 16 | 0 | 0 | 0 |
| Experiments | 10 | 0 | 0 | 0 |
| Datasets | 8 | 0 | 0 | 0 |
| Prompt Management | 5 | 0 | 0 | 0 |
| Runtime Protection | 13 | 0 | 0 | 0 |
| Alerts & Monitoring | 8 | 0 | 0 | 0 |
| Annotations | 7 | 0 | 0 | 0 |
| Integrations | 18 | 0 | 0 | 0 |
| Luna-2 Model | 4 | 0 | 0 | 0 |
| Access Control | 9 | 0 | 0 | 0 |
| SDK Features | 19 | 0 | 0 | 0 |
| Agent Control | 34 | 0 | 0 | 0 |
| Auto-Tune | 2 | 0 | 0 | 0 |
| Playground | 1 | 0 | 0 | 0 |
| **TOTAL** | **207** | **0** | **0** | **0** |
