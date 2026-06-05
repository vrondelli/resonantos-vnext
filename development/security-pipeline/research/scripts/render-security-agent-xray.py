#!/usr/bin/env python3
"""Render the ResonantOS security-agent research x-ray HTML page."""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "development/security-pipeline/research/security-agent-xray.html"
STRATEGY = ROOT / "development/security-pipeline/research/SECURITY-AGENT-RESEARCH-STRATEGY.md"
DISPATCH = ROOT / "development/security-pipeline/research/security-agent-research.dispatch.json"
PROFILER = Path("/mnt/c/Users/vlad_/.codex/attachments/4c725bc6-1aeb-4727-b2e9-683be907dbd4/pasted-text.txt")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def pretty_json(path: Path) -> str:
    return json.dumps(json.loads(read(path)), indent=2)


def source_block(title: str, description: str, text: str, open_by_default: bool = False) -> str:
    open_attr = " open" if open_by_default else ""
    return f"""
      <details class="source-block"{open_attr}>
        <summary>
          <span>{esc(title)}</span>
          <small>{esc(description)}</small>
        </summary>
        <pre>{esc(text)}</pre>
      </details>
    """


strategy_text = read(STRATEGY)
dispatch_text = pretty_json(DISPATCH)
profiler_text = read(PROFILER)

html_body = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>ResonantOS Security Agent X-Ray</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #16202a;
      --muted: #5e6b78;
      --line: #d8dee6;
      --panel: #ffffff;
      --soft: #f4f7fa;
      --blue: #1769aa;
      --green: #16734d;
      --red: #b33a3a;
      --amber: #a66a00;
      --violet: #6a4aa0;
      --shadow: 0 10px 30px rgba(18, 28, 38, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background: #eef2f6;
      line-height: 1.55;
    }}
    header {{
      padding: 44px min(6vw, 72px) 30px;
      background: linear-gradient(135deg, #f8fbfd 0%, #e8f1f8 58%, #f4efe2 100%);
      border-bottom: 1px solid var(--line);
    }}
    .eyebrow {{
      margin: 0 0 10px;
      color: var(--blue);
      font-weight: 700;
      letter-spacing: 0;
      text-transform: uppercase;
      font-size: 0.78rem;
    }}
    h1 {{
      max-width: 1040px;
      margin: 0;
      font-size: clamp(2rem, 4vw, 4.2rem);
      line-height: 1.02;
      letter-spacing: 0;
    }}
    .lead {{
      max-width: 900px;
      margin: 18px 0 0;
      color: #314253;
      font-size: clamp(1.02rem, 1.5vw, 1.22rem);
    }}
    main {{ padding: 28px min(6vw, 72px) 64px; }}
    section {{
      max-width: 1220px;
      margin: 0 auto 28px;
    }}
    h2 {{
      margin: 0 0 14px;
      font-size: 1.35rem;
      letter-spacing: 0;
    }}
    h3 {{
      margin: 0 0 8px;
      font-size: 1.02rem;
      letter-spacing: 0;
    }}
    p {{ margin: 0 0 12px; }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(12, minmax(0, 1fr));
      gap: 14px;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      box-shadow: var(--shadow);
    }}
    .span-4 {{ grid-column: span 4; }}
    .span-6 {{ grid-column: span 6; }}
    .span-8 {{ grid-column: span 8; }}
    .span-12 {{ grid-column: span 12; }}
    .tagrow {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
    }}
    .tag {{
      display: inline-flex;
      align-items: center;
      min-height: 28px;
      padding: 4px 9px;
      border-radius: 999px;
      background: #e8f0f7;
      color: #24445f;
      font-size: 0.86rem;
      font-weight: 650;
    }}
    .callout {{
      border-left: 4px solid var(--blue);
      padding: 13px 15px;
      background: #f7fafc;
      border-radius: 0 8px 8px 0;
    }}
    .callout.warning {{ border-left-color: var(--amber); }}
    .callout.danger {{ border-left-color: var(--red); }}
    .lane-list {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
    }}
    .lane-list li {{
      padding: 12px;
      background: var(--soft);
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    .lane-list strong {{ display: block; margin-bottom: 4px; }}
    .dag {{
      overflow-x: auto;
      padding-bottom: 8px;
    }}
    .flow {{
      min-width: 960px;
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 12px;
      align-items: stretch;
    }}
    .node {{
      background: #f9fbfd;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      min-height: 92px;
      position: relative;
    }}
    .node::after {{
      content: "→";
      position: absolute;
      right: -12px;
      top: 38px;
      color: var(--muted);
      font-weight: 700;
    }}
    .node:last-child::after {{ content: ""; }}
    .node .n {{ font-weight: 800; color: var(--blue); display: block; margin-bottom: 4px; }}
    .node small {{ color: var(--muted); }}
    .dag-svg {{
      min-width: 1080px;
      width: 100%;
      height: auto;
      display: block;
      background: #f8fbfd;
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    .dag-svg text {{
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      letter-spacing: 0;
    }}
    .svg-title {{ font-size: 16px; font-weight: 800; fill: #16202a; }}
    .svg-label {{ font-size: 13px; font-weight: 750; fill: #16202a; }}
    .svg-small {{ font-size: 11px; fill: #5e6b78; }}
    .svg-node {{ fill: #ffffff; stroke: #c9d4df; stroke-width: 1.4; }}
    .svg-core {{ fill: #e8f1f8; stroke: #1769aa; }}
    .svg-risk {{ fill: #fff4e0; stroke: #a66a00; }}
    .svg-agent {{ fill: #e9f6ef; stroke: #16734d; }}
    .svg-gate {{ fill: #f9e8e8; stroke: #b33a3a; }}
    .svg-final {{ fill: #efeaf8; stroke: #6a4aa0; }}
    .svg-edge {{ stroke: #7c8b99; stroke-width: 1.5; fill: none; marker-end: url(#arrow); }}
    .svg-faint {{ stroke: #aab6c2; stroke-width: 1.1; fill: none; marker-end: url(#arrow); }}
    .surface-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
    }}
    .surface {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      background: #fff;
    }}
    .surface b {{ display: block; margin-bottom: 5px; color: #21313f; }}
    .surface span {{ color: var(--muted); font-size: 0.92rem; }}
    .risk-high {{ border-left: 4px solid var(--red); }}
    .risk-med {{ border-left: 4px solid var(--amber); }}
    .risk-gov {{ border-left: 4px solid var(--violet); }}
    .risk-agent {{ border-left: 4px solid var(--green); }}
    .matrix {{
      width: 100%;
      border-collapse: collapse;
      overflow: hidden;
      border-radius: 8px;
    }}
    .matrix th, .matrix td {{
      padding: 10px 12px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
    }}
    .matrix th {{ background: #eaf0f5; }}
    .matrix tr:last-child td {{ border-bottom: 0; }}
    details.source-block {{
      background: #0f1720;
      color: #d9e2ec;
      border-radius: 8px;
      margin-bottom: 14px;
      border: 1px solid #243242;
      overflow: hidden;
    }}
    details.source-block summary {{
      cursor: pointer;
      padding: 14px 16px;
      background: #172231;
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: center;
    }}
    details.source-block summary span {{ font-weight: 800; }}
    details.source-block summary small {{ color: #a8b6c5; }}
    pre {{
      margin: 0;
      padding: 16px;
      overflow: auto;
      white-space: pre-wrap;
      word-break: break-word;
      font-size: 0.86rem;
      line-height: 1.45;
    }}
    .footer-note {{
      color: var(--muted);
      font-size: 0.92rem;
    }}
    @media (max-width: 900px) {{
      .span-4, .span-6, .span-8 {{ grid-column: span 12; }}
      .lane-list, .surface-grid {{ grid-template-columns: 1fr; }}
      header, main {{ padding-left: 18px; padding-right: 18px; }}
    }}
  </style>
</head>
<body>
  <header>
    <p class="eyebrow">ResonantOS vNext Security Agent Research</p>
    <h1>A governed map from attack surfaces to safe security skills.</h1>
    <p class="lead">This x-ray distills the security-agent research strategy into a readable architecture: what the app exposes, how the research DAG works, which specialized skills are planned, and where active red-team work is gated. Full source documents are included at the end for deep review.</p>
  </header>

  <main>
    <section class="grid">
      <div class="panel span-8">
        <h2>Distilled Explanation</h2>
        <p>The security agent is not a single scanner. It is a governed research program that first maps architecture and trust boundaries, then fans out into specialist skills, then turns validated findings into deterministic checks.</p>
        <div class="callout warning">
          <strong>Important boundary:</strong> the strategy authorizes research, mapping, static scans, and safe fixtures by default. Active exploitation, destructive probing, live network scans, credential mutation, persistence simulation, or external-provider calls require explicit approval.
        </div>
        <div class="tagrow">
          <span class="tag">architecture first</span>
          <span class="tag">DAG research</span>
          <span class="tag">surface specialists</span>
          <span class="tag">safe tests first</span>
          <span class="tag">approval-gated red team</span>
          <span class="tag">pipeline promotion</span>
        </div>
      </div>
      <div class="panel span-4">
        <h2>Target Boundary</h2>
        <p>ResonantOS vNext: Tauri desktop app, React/Vite webview, Rust backend, browser-first Node bridge, side-panel browser extension, Electron alternative host, local memory service, provider APIs, local subprocesses, and installed agent skills.</p>
      </div>
    </section>

    <section class="panel">
      <h2>Research DAG</h2>
      <div class="dag">
        <svg class="dag-svg" viewBox="0 0 1160 720" role="img" aria-labelledby="dag-title dag-desc">
          <title id="dag-title">Security-agent research DAG</title>
          <desc id="dag-desc">A directed graph showing context recovery, architecture mapping, threat modeling, specialist fanout, validation gates, safe tests, optional red-team approval, maturity scoring, and pipeline handoff.</desc>
          <defs>
            <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
              <path d="M0,0 L8,3 L0,6 Z" fill="#7c8b99"></path>
            </marker>
          </defs>

          <text class="svg-title" x="36" y="36">Architecture-first security research graph</text>
          <text class="svg-small" x="36" y="58">The plan maps trust boundaries before tests, then promotes only validated checks.</text>

          <rect class="svg-node svg-core" x="40" y="92" width="170" height="76" rx="8"></rect>
          <text class="svg-label" x="60" y="122">S0 Recover Context</text>
          <text class="svg-small" x="60" y="145">reviewer + profiler + pipeline</text>

          <rect class="svg-node svg-core" x="270" y="92" width="180" height="76" rx="8"></rect>
          <text class="svg-label" x="290" y="122">S1 Architecture Map</text>
          <text class="svg-small" x="290" y="145">assets, flows, trust boundaries</text>

          <rect class="svg-node svg-core" x="510" y="92" width="180" height="76" rx="8"></rect>
          <text class="svg-label" x="530" y="122">S2 Vector Catalog</text>
          <text class="svg-small" x="530" y="145">safe, approval, blocked tags</text>

          <rect class="svg-node svg-agent" x="750" y="70" width="190" height="64" rx="8"></rect>
          <text class="svg-label" x="770" y="98">S4 Agentic Intel</text>
          <text class="svg-small" x="770" y="120">worms, memory poisoning, tool abuse</text>

          <rect class="svg-node svg-risk" x="750" y="166" width="190" height="64" rx="8"></rect>
          <text class="svg-label" x="770" y="194">S3 Specialist Fanout</text>
          <text class="svg-small" x="770" y="216">17 surface and agent lanes</text>

          <rect class="svg-node" x="70" y="286" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="88" y="316">Tauri IPC + CSP</text>
          <rect class="svg-node" x="282" y="286" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="300" y="316">Bridge + Extension</text>
          <rect class="svg-node" x="494" y="286" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="512" y="316">Electron IPC</text>
          <rect class="svg-node" x="706" y="286" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="724" y="316">Local Listeners</text>
          <rect class="svg-node" x="918" y="286" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="936" y="316">Agent Skill Safety</text>

          <rect class="svg-node" x="70" y="374" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="88" y="406">Secrets + Data</text>
          <rect class="svg-node" x="282" y="374" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="300" y="406">Provider Network</text>
          <rect class="svg-node" x="494" y="374" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="512" y="406">Native + Terminal</text>
          <rect class="svg-node" x="706" y="374" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="724" y="406">Supply + Release</text>
          <rect class="svg-node" x="918" y="374" width="180" height="54" rx="8"></rect>
          <text class="svg-label" x="936" y="406">External Integrations</text>

          <rect class="svg-node" x="80" y="514" width="190" height="70" rx="8"></rect>
          <text class="svg-label" x="100" y="542">S5 Tool + Skill Design</text>
          <text class="svg-small" x="100" y="564">prefer existing tools</text>

          <rect class="svg-node svg-agent" x="325" y="514" width="190" height="70" rx="8"></rect>
          <text class="svg-label" x="345" y="542">S6-S7 Skill Validation</text>
          <text class="svg-small" x="345" y="564">runtime + malicious audit</text>

          <rect class="svg-node svg-core" x="570" y="514" width="190" height="70" rx="8"></rect>
          <text class="svg-label" x="590" y="542">S8 Safe Tests</text>
          <text class="svg-small" x="590" y="564">fixtures, static scans, local checks</text>

          <rect class="svg-node svg-gate" x="815" y="496" width="210" height="60" rx="8"></rect>
          <text class="svg-label" x="835" y="524">S9 Approval Gate</text>
          <text class="svg-small" x="835" y="546">active red-team only if approved</text>

          <rect class="svg-node svg-final" x="815" y="594" width="210" height="60" rx="8"></rect>
          <text class="svg-label" x="835" y="622">S10-S11 Maturity + CI</text>
          <text class="svg-small" x="835" y="644">score, gaps, observe/warn/block</text>

          <path class="svg-edge" d="M210 130 H270"></path>
          <path class="svg-edge" d="M450 130 H510"></path>
          <path class="svg-edge" d="M690 130 C716 130 722 102 750 102"></path>
          <path class="svg-edge" d="M690 130 C720 130 720 198 750 198"></path>
          <path class="svg-edge" d="M845 230 V260"></path>
          <path class="svg-faint" d="M845 260 C845 276 160 260 160 286"></path>
          <path class="svg-faint" d="M845 260 C845 276 372 260 372 286"></path>
          <path class="svg-faint" d="M845 260 C845 276 584 260 584 286"></path>
          <path class="svg-faint" d="M845 260 C845 276 796 260 796 286"></path>
          <path class="svg-faint" d="M845 260 C845 276 1008 260 1008 286"></path>
          <path class="svg-faint" d="M845 260 C845 360 160 354 160 374"></path>
          <path class="svg-faint" d="M845 260 C845 360 372 354 372 374"></path>
          <path class="svg-faint" d="M845 260 C845 360 584 354 584 374"></path>
          <path class="svg-faint" d="M845 260 C845 360 796 354 796 374"></path>
          <path class="svg-faint" d="M845 260 C845 360 1008 354 1008 374"></path>

          <path class="svg-edge" d="M584 428 C584 472 175 470 175 514"></path>
          <path class="svg-edge" d="M270 549 H325"></path>
          <path class="svg-edge" d="M515 549 H570"></path>
          <path class="svg-edge" d="M760 549 H815"></path>
          <path class="svg-edge" d="M920 556 V594"></path>
          <path class="svg-edge" d="M760 584 C790 624 800 624 815 624"></path>
        </svg>
      </div>
    </section>

    <section class="grid">
      <div class="panel span-6">
        <h2>Explanation Lanes</h2>
        <ul class="lane-list">
          <li><strong>Surface</strong>What systems, modes, and entrypoints exist.</li>
          <li><strong>Properties</strong>Single-user desktop posture, local state, token models, no TLS on loopback.</li>
          <li><strong>Components</strong>Tauri, Electron, browser-first bridge, extension, memory service, provider clients, agents.</li>
          <li><strong>Flows</strong>IPC calls, bridge routes, provider prompts, local file scans, subprocess launches.</li>
          <li><strong>Dependencies</strong>npm, Cargo, provider APIs, GitHub Actions, Arcanum skills, local CLIs.</li>
          <li><strong>Risk Questions</strong>What can cross trust boundaries, gain tool access, leak data, or become a CI check.</li>
        </ul>
      </div>
      <div class="panel span-6">
        <h2>Promotion Logic</h2>
        <table class="matrix">
          <tr><th>Level</th><th>Meaning</th></tr>
          <tr><td>0 Unknown</td><td>Surface exists but is not mapped or tested.</td></tr>
          <tr><td>1 Mapped</td><td>Assets, flows, boundaries, and vectors are documented.</td></tr>
          <tr><td>2 Guarded</td><td>Controls are documented and at least one deterministic test exists.</td></tr>
          <tr><td>3 Stress-tested</td><td>Safe simulations or fuzz/property tests exercise abuse paths.</td></tr>
          <tr><td>4 Managed</td><td>Checks run in CI or repeatable harnesses with owners and evidence.</td></tr>
        </table>
      </div>
    </section>

    <section class="panel">
      <h2>Specialist Skill Families</h2>
      <div class="surface-grid">
        <div class="surface risk-high"><b>Tauri IPC Boundary</b><span>128 commands, capability gates, CSP-null escalation paths.</span></div>
        <div class="surface risk-high"><b>Webview CSP & Injection</b><span>React rendering, markdown, XSS backstop, frontend-to-core path.</span></div>
        <div class="surface risk-high"><b>Native Loading & Terminal</b><span>PTY shell, sh -lc/cmd /C, libloading, env-driven native bridge.</span></div>
        <div class="surface risk-med"><b>Browser-First Bridge</b><span>Bridge token, capability tokens, route tiers, side-panel extension.</span></div>
        <div class="surface risk-med"><b>Electron IPC</b><span>Renderer-to-main invoke mirror, sandbox posture, local servers.</span></div>
        <div class="surface risk-med"><b>Local Listener Topology</b><span>Loopback services, memory host override, no TLS, rate-limit gaps.</span></div>
        <div class="surface risk-med"><b>Provider Network</b><span>Configurable base URLs, hardcoded LAN endpoint, SSRF and quota concerns.</span></div>
        <div class="surface risk-agent"><b>Agent Skill Malware Analysis</b><span>Suspicious scripts, secret reads, network egress, persistence, tool mismatch.</span></div>
        <div class="surface risk-agent"><b>Agentic Attack Intelligence</b><span>Prompt-injection worms, memory poisoning, goal hijack, approval bypass.</span></div>
        <div class="surface risk-gov"><b>Disclosure & Release Trust</b><span>SECURITY.md, code signing, notarization, SBOM, provenance.</span></div>
        <div class="surface risk-med"><b>Secrets & Data Lifecycle</b><span>Plaintext secrets, env forwarding, logs, retention, SQLite encryption gaps.</span></div>
        <div class="surface risk-med"><b>Supply Chain</b><span>npm, Cargo, GitHub Actions, vitest CVE, cargo audit, action hardening.</span></div>
      </div>
    </section>

    <section class="grid">
      <div class="panel span-6">
        <h2>What Is Already Known</h2>
        <p>The current evidence already identifies high-signal risk areas: CSP is disabled, addon capability state is unsigned JSON, provider secrets need stronger file permissions/encryption, bridge route tiers need review, Electron mode needs its own IPC boundary, and installed skills/agents need hostile-content review.</p>
      </div>
      <div class="panel span-6">
        <h2>What Comes Next</h2>
        <p>The first practical slice should validate the installed skill surfaces, then start with the Tauri IPC boundary and webview CSP path. Those two determine how hard it is for injected or malicious content to reach powerful local capabilities.</p>
      </div>
      <div class="panel span-12">
        <h2>Development Handoff Rule</h2>
        <p>Whenever research finds something that needs development, route it through an invoke handoff first. The handoff must use context-builder to prepare the smallest sufficient implementation context before any code change or new check is built.</p>
        <pre>$invoke handoff use context builder to prepare development for &lt;finding-or-surface&gt;</pre>
      </div>
    </section>

    <section class="panel">
      <h2>Full Documents</h2>
      <p class="footer-note">These are embedded as escaped text for offline review. They are not executed, fetched, or rendered through remote services.</p>
      {source_block("Security Agent Research Strategy", "Primary distilled strategy document", strategy_text, True)}
      {source_block("Dispatch Route JSON", "Validated dispatch-spec route", dispatch_text)}
      {source_block("Threat Model Profiler Run", "Profiler evidence used to extend the strategy", profiler_text)}
    </section>
  </main>
</body>
</html>
"""

OUT.write_text(html_body, encoding="utf-8")
print(OUT)
