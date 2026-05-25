# Architekturfluesse

Das README enthaelt die grosse Gesamtkarte. Hier liegen die Detailfluesse fuer Betrieb, Daten und Repos.

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
  ElementCall["Element Call"] --> LiveKit["LiveKit + lk-jwt-service"]
  LiveKit --> VoiceWorker
  VoiceWorker --> Hermes["Hermes / OpenClaw"]
  Hermes --> Tools["Tools / Skills"]
  Hermes --> Matrix["Matrix Room Summary"]
  Hermes --> Obsidian["Obsidian Notes"]
```
