---
name: pi
description: "Delegate coding and repository tasks to Pi, select an available model, monitor its run, inspect its result, and review the changes without implementing them yourself. Use when the user asks Codex to use Pi as the executor."
---

# Delegate work to Pi

Use the installed Pi CLI to execute the user's task. Codex owns scoping, model selection, progress tracking, and independent review; Pi owns implementation. Do not edit Pi's implementation yourself. If review finds a problem, send Pi a focused correction request and review the new diff.

## Before starting

- Run `pi --help` when the installed CLI's interface is uncertain. The installed version's help is authoritative.
- Capture the actual pre-run baseline before Pi starts, not only file status. Keep these outputs for the post-run review:

  ```sh
  git status --short --branch
  git diff --binary
  git diff --cached --binary
  git ls-files --others --exclude-standard
  ```

  Preserve the contents of any already-untracked file Pi may need to edit. Include existing user changes in the brief as protected work; ask Pi to limit its edits to the requested files and leave unrelated changes untouched.
- Use an explicit model when the user names one. Otherwise inspect available models and choose a capable option that fits the task's difficulty and cost. Do not assume a provider or model ID from memory.
- Before launching Pi, inspect project-local `.pi` settings and resources and project `.agents/skills` in the working directory or its ancestors. For an untrusted or externally sourced repository, use `--no-approve` unless the task needs reviewed project resources. Grant trust with `--approve` only after intentionally reviewing those resources. Project trust controls resource loading; it does not sandbox Pi or its tools. In print, JSON, and RPC modes, make the trust decision explicitly because the built-in prompt cannot appear. `AGENTS.md` and `CLAUDE.md` load independently of project trust; use `--no-context-files` only when deliberately excluding repository instructions.
- Give Pi the task, relevant constraints, and a concrete completion condition. Tell it to report changed files, checks run, failures, and any remaining uncertainty.

## Find models without exposing credentials

Start with Pi's current catalog; filter only when a requested provider or model needs narrowing:

```sh
pi --list-models
pi --list-models <search>
```

This lists models available to the current Pi environment, including provider, model ID, context window, output limit, reasoning support, and image support. The optional argument is a fuzzy search, not a provider selector. Use the exact provider and model ID shown when launching Pi.

Resolve Pi's agent directory from `PI_CODING_AGENT_DIR` when set; otherwise use `~/.pi/agent`. For the configured default, read only non-secret settings fields such as `defaultProvider`, `defaultModel`, and `defaultThinkingLevel` from `<agent-dir>/settings.json`. For custom model entries, inspect only provider names and model `id`/`name` fields in `<agent-dir>/models.json`; never print the whole file because it can contain literal credentials or private endpoints. If needed, check a known provider without displaying or refreshing credentials:

```sh
pi auth check --provider <provider-id> --json --no-refresh
```

This reports readiness and auth type. Never use `pi auth print-api-key`, `pi auth print-bearer-token`, `pi auth check --credentials`, or print `<agent-dir>/auth.json`. Do not dump environment values; checking whether a provider is ready is sufficient.

The interactive picker is `/model` (also `Ctrl+L`); `Ctrl+P` cycles available models. Use `--provider <id> --model <id>` for a reproducible run. Add `--thinking <level>` (`off`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`) when useful; Pi clamps it to the model's supported levels. `--model <provider>/<id>:<thinking>` is also supported by current Pi versions.

## Run and monitor

For a one-shot task where progress matters, run from the target repository with explicit model selection and JSON event output:

```sh
pi --no-approve --provider <provider-id> --model <model-id> --mode json -- "<task brief>"
```

Use `--approve` instead only for intentionally trusted project resources. Keep stdout attached to the running process so progress remains visible. If the command runner returns a process ID, poll that same process until it exits; do not start a duplicate run because output paused briefly. Capture the `id` from the first JSON record (`type: "session"`) as the exact Pi session to use for corrections. JSON events useful for progress include `message_update`, `tool_execution_start`, `tool_execution_update`, `tool_execution_end`, retry/compaction events, and `agent_settled`. `agent_end` alone is not always final because recovery or queued work can follow.

Choose the output mode to fit the task:

- Interactive `pi`: follow the transcript and tool calls in the TUI; use `/session` for session details and `Escape` to stop.
- `--print`: one-shot final assistant text only; useful when live progress is unnecessary.
- `--mode json`: one-shot JSONL event stream; inspect the final `message_end` and wait for `agent_settled`. A model error/abort can appear in JSON while the process exit status is still zero, so inspect the final events.
- `--mode rpc`: long-lived JSONL command/event protocol when a client must send follow-up commands and track events. Keep reading stdout through `agent_settled`; use RPC only when continuing interaction is needed.

Pi saves sessions by default. Use `--name` to label a run and `/session` or `--export` to inspect/export it. `--continue` selects the current project's most recent session, which may belong to another task; use the captured session ID for review corrections. Use `--no-session` only when the user wants an ephemeral run.

## Review Pi's result

After Pi exits, compare the new status and tracked patches with the saved pre-run status, unstaged patch, and staged patch. Compare any pre-existing untracked files Pi touched with their saved contents. Attribute only the changes made after the baseline to Pi; inspect every such change and verify the requested behavior. Run the relevant checks when the user asks for verification or the task requires them. Do not accept Pi's completion summary as a substitute for reviewing the workspace, and do not stage, commit, push, or publish unless the user explicitly requested that action. If Pi changed unrelated files, preserve them and report the scope issue; do not silently revert them.

If review finds a problem, send a focused correction to the exact same Pi session, then review the new changes against the original baseline again:

```sh
pi --no-approve --session <captured-session-id> --mode json -- "Review found these issues: <specific corrections>"
```

Keep the same trust decision as the initial run. Do not implement the correction yourself or rely on `--continue` when the exact session ID is available.

## Official references

- [Command Line](https://pi.dev/docs/latest/cli) — flags, model selection, sessions, and tools.
- [CLI Integration](https://pi.dev/docs/latest/cli-integration) — print, JSON, and RPC modes.
- [JSON Event Stream](https://pi.dev/docs/latest/json) — progress events and completion semantics.
- [Choose a Model](https://pi.dev/docs/latest/models) — model selection and provider setup.
- [Provider Authentication](https://pi.dev/docs/latest/providers) — credential sources and safe provider readiness checks.
- [Run Pi Safely](https://pi.dev/docs/latest/security) — project trust and non-interactive trust decisions.
- [Configuration](https://pi.dev/docs/latest/configuration) — agent directory and project resources.
