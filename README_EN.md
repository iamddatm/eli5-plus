# ELI5+

[中文](README.md)

> ELI5 makes a topic easy to follow. ELI5+ helps you truly understand it.

ELI5+ is an open-source skill for AI agents. It turns complex topics into accurate, visual, progressively layered standalone HTML explainers for non-specialists. The goal is a useful mental model, not merely a simplified definition.

## Walkthrough and examples

For a detailed Chinese walkthrough of the design, generated results, and usage, read [ELI5+ detailed walkthrough and examples on WeChat](https://mp.weixin.qq.com/s/X95JKZzp0wVZqdZKaOcXQQ).

## What it does

- Builds intuition before introducing the real mechanism.
- Uses concrete scenarios, examples, and analogies with explicit limits.
- Expresses structure, flow, comparison, and state through meaningful visuals.
- Explains important constraints, tradeoffs, failure modes, and misconceptions.
- Produces responsive, self-contained HTML that works offline.
- Checks desktop and mobile rendering when browser tooling is available.

The guiding idea is: **large visuals, little text; one focus per section; less memorization, more intuition.**

## When to use it

Use ELI5+ for abstract concepts, mechanisms, workflows, easily confused ideas, and topics that benefit from a path from intuition to accurate detail.

It is not intended for ultra-brief summaries or expert-first, paper-style technical deep dives.

## Installation

### Ask an agent to install it (recommended)

If your agent supports skills, give it this repository URL or local directory and use a prompt such as:

```text
Install the ELI5+ skill from this repository. The skill is located at skills/eli5-plus. Follow your agent's skill installation conventions, then verify that the skill can be discovered and invoked.
```

### Manual installation

Copy `skills/eli5-plus` into the skills directory used by your agent. Directory locations and loading behavior vary, so follow the conventions of your agent.

For example, with Codex, run the following command from the repository root:

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/eli5-plus ~/.codex/skills/eli5-plus
```

Restart the agent or begin a new task so it can discover the skill. If a skill with the same name already exists, back it up or compare the directories before replacing it. Agents that do not support a compatible `SKILL.md` format may require a small adaptation.

## Usage

Invocation syntax depends on the agent. The most portable option is to name ELI5+ directly in the request:

```text
Use ELI5+ to explain LLMs
Use ELI5+ to explain RAG with diagrams
```

Agents that support the `$skill-name` syntax can also invoke it explicitly:

```text
$eli5-plus LLM
$eli5-plus Explain RAG with diagrams
$eli5-plus Why can a smaller model learn from a larger model through distillation?
```

Agents with automatic skill discovery may select it from a matching ordinary request. The primary deliverable is a standalone `.html` file in the workspace, not a long block of raw HTML in chat.

## Compatibility

The core behavior is defined entirely in `skills/eli5-plus/SKILL.md` and does not require a specific MCP server, plugin, or remote service. `agents/openai.yaml` only provides optional interface metadata for Codex/OpenAI clients; other agents can ignore it.

## ELI5 vs. ELI5+

| | ELI5 | ELI5+ |
|---|---|---|
| Goal | Make it easy to follow | Build a transferable mental model |
| Content | Core idea and a simple analogy | Intuition, mechanism, examples, boundaries, and tradeoffs |
| Medium | Mostly text | Visual-first, with meaningful motion when useful |
| Accuracy | May simplify aggressively | Simple without distortion; analogy limits are explicit |
| Deliverable | Usually a short answer | A complete standalone HTML page |

## Design principles

1. **Intuition before mechanism**: explain what it is and why it exists before the implementation details.
2. **Concrete before abstract**: prefer scenarios, examples, and analogies, without treating an analogy as the real mechanism.
3. **Connected knowledge**: make conditions, processes, and outcomes visible instead of listing isolated facts.
4. **Visuals carry meaning**: use structure, relationships, flow, and state rather than turning prose into decorative cards.
5. **Accuracy comes first**: preserve constraints, assumptions, tradeoffs, and source boundaries that affect the conclusion.
6. **Adapt to the topic**: do not force every concept into the same page template.

See [skills/eli5-plus/SKILL.md](skills/eli5-plus/SKILL.md) for the complete behavior contract.

## Repository layout

```text
.
├── .github/workflows/validate.yml
├── scripts/validate_skill.py
└── skills/eli5-plus
    ├── SKILL.md
    └── agents/openai.yaml    # optional Codex/OpenAI client metadata
```

## Local validation

```bash
python3 scripts/validate_skill.py
```

The validator uses only the Python standard library. It checks the skill layout, frontmatter, UI metadata, and common repository debris. It does not replace realistic topic generation or browser-based visual review.

## Contributing

Issues and pull requests are welcome. Changes to the behavior contract should ideally include a realistic use case and explain the generation or comprehension failure they address. This helps keep the skill focused instead of accumulating universal rules for isolated pages.

## License

[MIT](LICENSE)

This is an independent open-source project.
