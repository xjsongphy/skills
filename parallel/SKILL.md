---
name: parallel
description: Use when processing multiple independent tasks with bounded concurrency to manage resource limits, avoid rate limits, or prevent system overload
---

# Parallel Pool Management

## Overview
Manage a pool of subagents with a precise concurrency limit, dispatching new tasks immediately as slots free up. Unlike fire-all-at-once approaches, this maintains steady parallelism without overwhelming systems.

## When to Use

✅ **Use when:**
- Processing 5+ independent tasks (chapters, files, API calls, etc.)
- Need to limit concurrent execution (API rate limits, memory constraints, system overload)
- Want parallelism benefits without fire-all-at-once resource spikes
- Tasks can complete incrementally (don't need all results simultaneously)

❌ **Don't use when:**
- Tasks have sequential dependencies or shared state
- Only 1-4 tasks (just dispatch them directly)
- Need all results simultaneously before proceeding (use `superpowers:dispatching-parallel-agents` instead)

## Core Pattern

### Pool Management Algorithm

```
1. INITIALIZE: Set concurrency limit (default 3), create task queue
2. DISPATCH: Fire min(limit, queue_size) subagents initially
3. WAIT: Monitor for ANY completion (not polling - check notification)
4. REFILL: When slot frees, immediately dispatch next task from queue
5. REPEAT: Until queue empty AND all slots free
```

**Critical**: Refill slots **immediately when ANY completes**, not "wait for all then dispatch next batch."

### Implementation Pattern

```javascript
// Pool state management
const limit = 3;  // or custom limit from args
const queue = [...tasks];       // remaining tasks
const running = new Set();      // currently-executing agent IDs
const results = [];             // collected results

// Step 1: Initial dispatch (fill pool to limit)
for (let i = 0; i < Math.min(limit, queue.length); i++) {
  const task = queue.shift();
  const agent = dispatchAgent(task);
  running.add(agent.id);
}

// Step 2: Monitor and refill loop
while (running.size > 0) {
  // Wait for ANY completion to finish
  const completed = awaitNextCompletion(running);

  // Free the slot
  running.delete(completed.agentId);
  results.push(completed.result);

  // Refill immediately if queue has tasks
  if (queue.length > 0) {
    const next = queue.shift();
    const nextAgent = dispatchAgent(next);
    running.add(nextAgent.id);
  }
}

// running.size === 0 and queue.length === 0 means done
```

### Error Handling

When a task fails, the slot must still free:

```javascript
try {
  const result = await agentCompletion;
  results.push({success: true, data: result});
} catch (error) {
  results.push({success: false, error: error.message});
  // Slot still freed - running.delete() happens regardless
}

// Decide: retry (add back to queue) or log and skip?
if (shouldRetry(task, error)) {
  queue.push(task);  // will be re-dispatched
}
```

**Principle**: Failures are local. One task failing doesn't block the queue. Free the slot, decide retry/skip, continue.

## Quick Reference

| Operation | Pattern |
|-----------|---------|
| Use default limit (3) | Initialize with `limit = 3` |
| Specify custom limit | `limit = 5` (or from args) |
| Track running state | `Set<agentId>` for O(1) add/remove/lookup |
| Refill on completion | `if (queue.length > 0) dispatchNext()` |
| Handle failure | `try/catch`, free slot regardless, decide retry |

## Common Mistakes

| Mistake | Why It's Wrong | Fix |
|---------|-----------------|-----|
| Fire all tasks at once | Violates limit, overwhelms system | Dispatch only `min(limit, queue.length)` initially |
| Batch-wait (wait ALL, then next) | Inefficient - slots sit idle | Refill **immediately when ANY slot frees** |
| No running state tracking | Can't enforce limit | Always maintain `Set<agentId>` of running agents |
| Forget to free slot on error | Pool eventually stalls | `running.delete()` in `finally` block or outside try/catch |
| Don't handle failures | Queue blocks on first error | Wrap in try/catch, log, free slot, continue |
| Polling for completions | Wastes cycles, inefficiency | Use notification-based "await next completion" |

## Self-Check Questions

Before using this pattern:

- [ ] Are tasks truly independent? (no shared state, no sequential dependencies)
- [ ] Do I need a concurrency limit? (rate limits, resource constraints, system stability)
- [ ] Do I have 5+ tasks? (otherwise just dispatch directly)
- [ ] Can I process incrementally? (don't need all results before proceeding)
- [ ] Will I track running state? (Set of agent IDs)

## Comparison to Related Skills

- **`superpowers:dispatching-parallel-agents`**: Fire ALL agents at once in one block. Use when you need all results simultaneously and have no rate limits.
- **`superpowers:subagent-driven-development`**: Sequential execution (one task at a time). Use when tasks might conflict or need careful integration.
- **`parallel` (this skill)**: Bounded pool with steady refill. Use when you need parallelism with resource constraints.

## Why This Matters

Without pool management, agents either:
- **Fire all at once** → 50 concurrent agents overwhelm APIs, exhaust memory, trigger rate limits
- **Process sequentially** → 50 tasks take 50x longer than necessary

Pool management gives you **controlled parallelism**: steady throughput without resource spikes.
