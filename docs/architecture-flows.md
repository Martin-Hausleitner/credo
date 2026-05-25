# Architekturfluesse

Das README enthaelt die grosse Gesamtkarte. Hier liegen die Detailfluesse fuer Betrieb, Daten und Repos.

Weitere visuelle Karten und Screenshot-Galerien liegen in [visual-gallery.md](visual-gallery.md).

## 🧭 Runtime Flow

```mermaid
flowchart LR
  Human["Human"] --> Client["Element / Cinny / Sable"]
  Client --> Matrix["Matrix Homeserver"]
  Matrix --> Bot["Hermes Matrix Bot"]
  Bot --> Policy["Policy Gate"]
  Policy --> Redis["Redis Job Queue"]
  Redis --> Worker["Hermes / OpenClaw / Codex Worker"]
  Worker --> Tools["Skills + MCP + Computer Use"]
  Worker --> Memory["Postgres + pgvector"]
  Worker --> Vault["Obsidian + Git"]
  Worker --> Artifacts["S3 / R2"]
  Worker --> Matrix
```

## 🖥️ Control Surface Flow

```mermaid
flowchart LR
  Human["Human"] --> MatrixClient["Element / Cinny"]
  Human --> Desktop["Hermes Desktop"]
  Human --> ObsidianUI["Obsidian"]
  MatrixClient --> Room["Matrix Room"]
  Desktop --> HermesAPI["Hermes API<br/>local 127.0.0.1:8642 or remote"]
  Room --> Bot["Hermes Matrix Bot"]
  Bot --> Queue["Redis Job"]
  HermesAPI --> Queue
  Queue --> Worker["Hermes / OpenClaw / Codex"]
  Worker --> Result["Matrix Result + Artifacts"]
  Worker --> ObsidianUI
```

## 🚦 Policy + Run Contract Flow

```mermaid
flowchart TB
  Event["Matrix Event<br/>room_id + event_id"] --> Intent["Intent Parser"]
  Intent --> Policy["Policy Gate<br/>actor_id + room policy + tool scope"]
  Policy -->|allowed| Job["Redis Job<br/>job_id + run_id"]
  Policy -->|needs approval| Approval["Approval Room<br/>human confirms"]
  Policy -->|denied| Denied["Matrix Denial<br/>reason + audit"]
  Approval --> Job
  Job --> Worker["Hermes / OpenClaw / Codex Worker"]
  Worker --> RuntimePolicy["Runtime Policy<br/>per MCP / skill / browser / email / GitHub call"]
  RuntimePolicy --> Tools["Scoped Tool Call"]
  Worker --> Trace["OTel Trace<br/>LLM + RAG + tool + subagent spans"]
  Worker --> Artifacts["S3/R2 Artifacts<br/>artifact_id"]
  Worker --> Memory["Memory Mode<br/>read-only / proposed / approved"]
  Tools --> Trace
  Trace --> Ops["Grafana / Loki / Prometheus"]
  Artifacts --> Result["Matrix Result<br/>summary + links"]
  Memory --> Result
```

## 🧠 Knowledge Flow

```mermaid
flowchart TB
  Activity["ActivityWatch / WHOOP / Screen Time / YouTube"] --> Context["Context Normalization"]
  Obsidian["Obsidian Vault"] --> Context
  Notion["Notion Research Pages"] --> Context
  Context --> Memory["Postgres + pgvector"]
  Context --> Vault["Markdown + Git"]
  Memory --> Agent["Hermes Agent"]
  Vault --> Agent
  Agent --> Matrix["Matrix Result Rooms"]
```

## 📬 Inbox Flow

```mermaid
flowchart LR
  Mail["E-Mail"] --> Himalaya["Himalaya / Maildir / notmuch"]
  Chat["Beeper / Matrix"] --> Chatwoot["Chatwoot Inbox"]
  Bridges["mautrix Bridges"] --> Matrix["Matrix"]
  Himalaya --> Agent["Hermes Agent"]
  Chatwoot --> Agent
  Matrix --> Agent
  Agent --> Approval["Approval Gate"]
  Approval --> Action["Reply / Issue / PR / Reminder"]
```

## 🎙️ Voice Flow

```mermaid
flowchart LR
  Discord["Discord Voice MVP"] --> VoiceWorker["Voice Worker / ASR"]
  ElementCall["Element Call Client"] --> LKJWT["lk-jwt-service<br/>Matrix OpenID -> LiveKit JWT"]
  Homeserver["Matrix Homeserver"] --> LKJWT
  LKJWT --> LiveKit["LiveKit SFU"]
  ElementCall --> LiveKit
  LiveKitAgent["Hermes Voice Agent<br/>LiveKit Participant"] --> LiveKit
  LiveKitAgent --> VoiceWorker
  VoiceWorker --> Hermes["Hermes / OpenClaw"]
  Hermes --> Tools["Tools / Skills"]
  Hermes --> Matrix["Matrix Room Summary"]
  Hermes --> Obsidian["Obsidian Notes"]
```
