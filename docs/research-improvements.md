# Research-Verbesserungen fuer Credo

Diese Datei verdichtet die neue Deep-Research-Runde fuer Credo. Sie ist absichtlich handlungsorientiert: Welche Ideen verbessern den Stack wirklich, welche bleiben spaeter, und was gehoert in README, Roadmap oder Runbooks?

## 🧭 Executive Synthesis

Credo sollte noch staerker als **Operating System fuer Agentenarbeit** formuliert werden:

```text
Matrix gibt Raeume, Identitaet, State und eine Audit-Timeline.
Hermes/OpenClaw/Codex fuehren Arbeit aus.
Redis entkoppelt lange Jobs.
Postgres/pgvector speichert State, kanonisches Audit, Memory und RAG.
Obsidian/Git bleibt menschliches Wissen und Review-Schicht.
ActivityWatch/Health/Presence liefern Kontext.
OTel/Grafana/Tailscale machen den Betrieb sichtbar und privat.
```

Die wichtigste Abstraktion ist: **jede Aktion hat einen Raum, eine Policy, einen Job, ein Artefakt und eine Spur**.

## 🧱 Neue Architektur-Prinzipien

| Prinzip | Bedeutung | Umsetzung in Credo |
|---|---|---|
| Room-first | Matrix-Raeume sind Arbeitskontexte, keine Chat-Spielerei | `#agent-intake`, `#agent-ops`, `#agent-research`, `#agent-memory`, `#agent-alerts` als feste Topologie |
| Policy before Tool | Kein LLM entscheidet Berechtigungen | Backend-Policy-Gate vor Redis/Worker und Runtime-Policy vor jedem riskanten Tool Call |
| Job over Chat | Lange Arbeit laeuft nicht im Matrix-Event-Handler | Matrix-Event erzeugt Job-ID, Redis haelt Queue, Worker schreibt Status zurueck |
| Artifact Ledger | Ergebnisse sind nicht nur Nachrichten | S3/R2 fuer Dateien, Postgres fuer Metadaten, Matrix fuer Audit-Link und Status-Timeline |
| Memory has Modes | Memory darf nicht einfach alles schreiben | read-only Default, dedizierte Memory-Raeume, Review vor persistenten Writes |
| Context is Local | Persoenliche Daten bleiben erst lokal | ActivityWatch, Obsidian, WHOOP/Apple/YouTube Importer vor Cloud-Dashboards |
| Trace every Run | Agentenlaeufe brauchen Debugbarkeit | OTel GenAI Spans fuer LLM, Tool, Agent und Subagent; redigierte Logs |
| Voice is Separate | Voice/RTC ist kein Text-MVP-Anhaengsel | Discord/OpenAI Realtime als Prototyp, MatrixRTC/LiveKit als eigene Phase |

## 🧩 Bessere README-Abstraktion

Das README sollte nicht versuchen, alle Tabellen direkt zu tragen. Die Startseite hat drei Jobs:

1. **North Star zeigen:** Was ist Credo?
2. **Architekturfluss zeigen:** Mensch -> Matrix -> Policy -> Jobs -> Agenten -> Memory/Ops.
3. **Zu Detaildokumenten routen:** Zielstack, Repos, GitHub-Matrix, Roadmap, Matrix-Ops, Ressourcen.

Die Details gehoeren in `docs/`, besonders:

| Thema | Datei |
|---|---|
| Stack-Entscheidung | [target-stack.md](target-stack.md) |
| Lokale Repos | [local-repositories.md](local-repositories.md) |
| GitHub-Repos + Stars | [github-repositories.md](github-repositories.md) |
| Matrix-Ops | [matrix-ops-runbook.md](matrix-ops-runbook.md) |
| Ressourcen | [resource-planning.md](resource-planning.md) |
| Research-Ideen | diese Datei |

## 🟢 Matrix und Homeserver

| Idee | Empfehlung |
|---|---|
| Synapse als Ops-Default | Synapse bleibt der Produktionspfad, weil Admin-API, Worker-Modell, Bridges und Tooling am reifsten sind. |
| Tuwunel als Lean-Test | Tuwunel bleibt Greenfield-Kandidat fuer niedrige RAM-/S3-Anforderungen, aber nicht alleiniger MVP-Anker. |
| MAS/OIDC frueh planen | Matrix Authentication Service wird als OAuth2/OIDC-Pfad wichtig fuer Element X und moderne Auth. Nicht sofort Core-MVP, aber als Phase 1c mit Client-Kompatibilitaet, Account-Migration, Login-Flows und Admin-Recovery vormerken. |
| Workers nicht zu frueh | Erst ein sauberer kleiner Synapse-Start; Worker-Modell vorbereiten, aber erst bei echter Last aktivieren. |
| Admin-API isolieren | Synapse Admin, `synadm`, Reports, Media Purges und User-Operationen nur ueber Tailscale und Ops-Raeume. |

Quellen: [Synapse docs](https://element-hq.github.io/synapse/), [Synapse Admin API](https://github.com/element-hq/synapse/tree/develop/docs/admin_api), [Element MAS docs](https://docs.element.io/latest/element-server-suite-pro/configuring-components/configuring-matrix-authentication-service/).

## 🎙️ MatrixRTC und Voice

| Idee | Empfehlung |
|---|---|
| Voice nicht in Text-MVP ziehen | Erst Text-/Job-Orchestrierung stabilisieren. |
| Discord/OpenAI Realtime als schneller Prototyp | Damit niedrige Latenz, Barge-in und Tool Calls getestet werden koennen, ohne MatrixRTC zu blockieren. |
| Element Call + LiveKit spaeter sauber | MatrixRTC braucht Element Call, LiveKit, `lk-jwt-service`, `.well-known` Foci, Reverse-Proxy-Routen und dedizierte Port-/Firewall-Planung. |
| Recording trennen | E2EE Recording bleibt spaeter und braucht eigene Key-/Teilnehmerstrategie. |

MatrixRTC-Checkliste:

- Homeserver-Features fuer Element Call bewusst planen: MSC-Flags, `max_event_delay_duration`, Rate Limits und OpenID/Federation Listener.
- `.well-known/matrix/client` mit RTC Foci setzen, besonders `org.matrix.msc4143.rtc_foci`.
- Reverse Proxy fuer `/livekit/jwt` und `/livekit/sfu` dokumentieren.
- LiveKit API/WebSocket `7880` hinter TLS/LB, ICE/TCP `7881`, ICE/UDP `50000-60000` oder UDP mux `7882` einplanen.
- Hermes nicht als impliziten LiveKit-Endpunkt sehen: ein Voice-Agent ist ein eigener LiveKit Participant.

Quellen: [Element Call self-hosting](https://github.com/element-hq/element-call/blob/livekit/docs/self-hosting.md), [lk-jwt-service](https://github.com/element-hq/lk-jwt-service), [LiveKit](https://github.com/livekit/livekit).

## 🤖 Agent Runtime und Skills

| Idee | Empfehlung |
|---|---|
| Skill Registry statt Skill-Liste | Skills nach Risiko, Datenzugriff und Freigabegrad gruppieren. |
| MCP-Tools als untrusted behandeln | Jeder MCP-Server bekommt Scope, Manifest, erlaubte Pfade und Audit. |
| Subagenten als Worker-Typ | Subagents sollen Jobs mit eigener Run-ID, Artefaktpfad und OTel Trace bekommen. |
| Computer Use nur mit visueller Validierung | UI-Automation darf nicht nur "erfolgreich geklickt" melden, sondern Screenshot/DOM/Status pruefen. |

MCP-Security-Checkliste:

- Server-Identitaet und Version pinnen.
- Manifest vor Aktivierung reviewen.
- Pro Server getrennte Credentials und minimale OAuth-/API-Scopes nutzen.
- Filesystem-, Netzwerk- und Shell-Zugriff allowlisten.
- Keine ambient Secrets aus `.env`, Shell oder Keychain in untrusted Tools geben.
- Tool Output vor Prompt-Wiedereinspeisung sanitizen.
- Prompt-Injection aus Webseiten, E-Mail, Notion und Matrix als Daten behandeln, nicht als Anweisung.
- Jeden Tool Call mit `run_id`, `approval_id`, `tool_version`, Inputs-Klasse und Ergebnisstatus auditieren.

Quellen: [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices), [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/).

## 🧠 Memory, RAG und Knowledge

| Idee | Empfehlung |
|---|---|
| Memory in drei Stufen | Ephemeral Run Context, Reviewed Project Memory, Long-term Canonical Memory. |
| Obsidian bleibt Review-Layer | Agenten duerfen Vorschlaege schreiben, aber kuratierte Memory bleibt menschlich lesbar in Markdown/Git. |
| Postgres/pgvector als Runtime-Memory | Jobs, Embeddings, Runs, Artefakt-Metadaten und Retrieval gehoeren in Postgres. |
| Supabase optional | Gute interne App-/Auth-/Realtime-Schicht, aber nicht Ersatz fuer Core-DB. |

## 📊 Observability und Betrieb

| Idee | Empfehlung |
|---|---|
| OTel zuerst denken | Jeder Agentenlauf hat `run_id`, `room_id`, `job_id`, `tool_name`, `approval_id`, `artifact_id`. |
| GenAI-Spans einplanen | `agent.run`, `llm.request`, `tool.call`, `mcp.call`, `rag.retrieve`, `memory.write_proposal`, `approval.request`, `subagent.run`, `artifact.write`. |
| Redaction Pipeline | Prompts, Tokens, E-Mail-Inhalte und personenbezogene Daten vor Loki/Grafana redigieren. |
| Replay-Ansicht spaeter | Ein Run sollte aus Matrix-Link, Artefakten, OTel Trace und Logs rekonstruierbar sein. |

Raum- und User-IDs gehoeren nicht roh in hochkardinale Metriken. Metrics nutzen gehashte stabile IDs; echte IDs bleiben in geschuetzten Audit-Tabellen oder redigierten Logs.

Quellen: [OpenTelemetry GenAI SemConv](https://opentelemetry.io/docs/specs/semconv/gen-ai/), [OpenTelemetry GenAI Observability](https://opentelemetry.io/blog/2026/genai-observability/), [Prometheus OTLP guide](https://prometheus.io/docs/guides/opentelemetry/).

## 🔐 Security Upgrades

| Risiko | Gegenmassnahme |
|---|---|
| Tool Poisoning / falsche Tools | Signierte Skill-Manifeste, feste Tool-IDs, Review bei neuen Skills |
| Secret Leakage | Kein Secret in Matrix, Logs, Screenshots oder Prompt-Artefakten |
| Broad MCP Tokens | Pro Tool minimaler Scope und getrennte Credentials |
| Riskante Bridges | VM, Proxy-Konzept, Kill-Switch und eigene DB pro Bridge |
| Admin-Token Missbrauch | Admin-APIs nie in normalen Agentenraeumen, nur Ops-Policy |
| Memory Poisoning | Write-Gates, Quellenlink, Review-Status und Loeschpfad |
| Externe Side Effects | Gates fuer `read-only`, `local-write`, `external-write`, `money/account-impacting`, `public/posting` |

## 🚀 Naechste konkrete Verbesserungen

| Prioritaet | Verbesserung | Ziel-Datei |
|---:|---|---|
| 1 | Runtime Policy Enforcement und Run Contract in Implementierung ueberfuehren | [target-stack.md](target-stack.md) |
| 2 | MatrixRTC-Checkliste in Ops-Runbook mit Ports, Foci und Proxy-Routen vertiefen | [matrix-ops-runbook.md](matrix-ops-runbook.md) |
| 3 | Skills nach Risiko-/Freigabeklassen gruppieren | [hermes-skills.md](hermes-skills.md) |
| 4 | Service-Katalog fuer mobile GitHub-Ansicht in Katalog + Galerie splitten | [service-catalog.md](service-catalog.md) |
| 5 | Repo-Inventare mit Kategorie-Ankern und Update-Datum versehen | [github-repositories.md](github-repositories.md) |
