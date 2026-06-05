# Malicious Skill And Agent Static Audit

Status: FLAG
Date: 2026-06-03
Strategy stages: malicious-skill-agent-audit, installed-agent-skill-validation

## Scope

This audit checked installed skill manifests and runtime entry points for suspicious behavior categories:

- outbound HTTP/network execution
- shell execution patterns
- secret/key material references
- local file writes
- runtime adapter privilege expansion
- command execution APIs
- persistence/startup hooks

Primary surfaces inspected:

- `.agents/skills/**/SKILL.md`
- `.codex/skills/**/SKILL.md`
- `.claude/skills/**/SKILL.md`
- `.github/skills/**/SKILL.md`
- `tools/arcanum`

## Evidence Command

```bash
rg -n "curl|wget|fetch\(|axios|Invoke-WebRequest|http://|https://|api_key|token|secret|password|private_key|BEGIN .*PRIVATE|\.env|id_rsa|chmod|rm -rf|nc |netcat|powershell|osascript|sh -lc|cmd /C|eval\(|child_process|subprocess|Command::new|fs::write|writeFile|OpenOptions|startup|profile" .agents .codex .claude .github/skills tools/arcanum
```

## Findings

### F-101: No Direct Private Key Material Observed

Verdict: PASS

The observed static pattern scan did not surface committed private key blocks, `id_rsa` material, or clear secret exfiltration snippets in the visible output. Many `secret`, `token`, and `password` hits were safety instructions telling agents not to store or expose credentials.

### F-102: Bootstrap Skill Contains Network-Shell Install Examples

Verdict: FLAG

`.github/skills/arcanum-spell-arcanum-bootstrap/SKILL.md` contains remote install examples using `curl` from GitHub piped into `bash`. This may be expected bootstrap documentation, but it is a high-risk pattern and must be permission-gated, source-pinned, and explicitly allowlisted.

Required development handoff:

```text
$invoke handoff use context builder to prepare development for network-shell pattern allowlist for installed skills
```

### F-103: Runtime Adapter Profiles Need Purpose-To-Permission Classification

Verdict: FLAG

`tools/arcanum` contains adapter profile handling and profile-writing behavior, including references to adapter modes such as Codex execution profiles. This is expected runtime behavior, not evidence of malicious activity by itself, but it is a privileged control surface.

Required development handoff:

```text
$invoke handoff use context builder to prepare development for high-privilege runtime adapter policy classification
```

### F-104: Local Write Behavior Exists In Runtime Tooling

Verdict: FLAG

`tools/arcanum` writes runtime adapter/profile data and uses temporary-file behavior. This should be represented in a capability permission matrix so validators can distinguish expected writes from suspicious writes.

Required development handoff:

```text
$invoke handoff use context builder to prepare development for runtime local-write permission matrix
```

### F-105: Audit Coverage Is Static And Partial

Verdict: FLAG

This audit used static search over visible installed manifests and `tools/arcanum`. It did not recursively execute or parse every script/template under generated development trees, and it did not perform AST-level or data-flow analysis. A deterministic hostile-content scanner is required before installed skills can be treated as trusted inputs.

Required development handoff:

```text
$invoke handoff use context builder to prepare development for installed agent hostile-content scanner
```

## Maturity Assessment

Malicious skill/agent audit is at Level 1: mapped.

It is not yet Level 2 because detection is pattern-based, manual, and partial. Level 2 requires a repeatable scanner with allowlists, denylist severity, structured findings, and policy exceptions for expected runtime/bootstrap behavior.

## Result

No direct malicious payload was confirmed in the inspected output. The audit did identify multiple high-risk classes that need deterministic controls before this security-agent project can safely install, generate, or execute new skills at scale.
