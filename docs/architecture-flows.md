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

## 🧬 OpenHuman Edge Identity + Write-Gate Flow

Der OpenHuman-Desktop ist ein **Edge-Node mit eigener Identitaet**: ein Ed25519 Device Key, nicht der menschliche Account. Jede Edge-Aktion (Memory-Vorschlag, Connector-Write) wird mit diesem Key signiert und muss durch das Write-Gate, bevor sie kanonisch wird.

```mermaid
flowchart TB
  OH["OpenHuman Edge Node<br/>Ed25519 Device Key"] --> Sign["Sign Action<br/>payload + node_id + nonce"]
  Sign --> Gate["Write-Gate<br/>verify sig + memory_mode + risk class"]
  Gate -->|sig invalid| Reject["Reject + Audit<br/>reason + node_id"]
  Gate -->|valid · low risk| Quorum["m-of-n Quorum<br/>device keys"]
  Gate -->|valid · high risk| Human["Approval Room<br/>human confirm"]
  Human --> Quorum
  Quorum --> Persist["pgvector + Postgres Audit<br/>run_id + approval_id + source_hash"]
  Persist --> Anchor["IPFS Anchor + Matrix Audit-Link"]
```

Identitaets- und Gate-Regeln:

1. Der OpenHuman-Node erhaelt bei Provisionierung einen eigenen Ed25519 Device Key, getrennt vom Menschen- und Bot-Account.
2. Jede Edge-Aktion traegt `node_id`, Payload-Hash und Nonce und wird signiert; das Gate verifiziert die Signatur vor jeder Policy-Pruefung.
3. Ungueltige oder unbekannte Signaturen werden verworfen und mit `node_id` und Grund auditiert.
4. Low-Risk-Writes laufen ueber das m-of-n Quorum der Device Keys; High-Risk-Writes brauchen zusaetzlich eine menschliche Freigabe im Approval-Raum.
5. Persistente Writes landen in pgvector plus Postgres-Audit (`run_id`, `approval_id`, `source_hash`) und werden ueber IPFS + Matrix verankert.
6. Key-Rotation und Revocation laufen ueber denselben Quorum-Pfad; ein revozierter Node-Key kann keine neuen Writes mehr signieren.

Mehr Details: [openhuman-integration.md](openhuman-integration.md), [target-stack.md](target-stack.md#-memory-bruecke-openhuman-vault--write-gate--pgvector). Quellen: [OpenHuman](https://github.com/tinyhumansai/openhuman), [libsodium Ed25519](https://doc.libsodium.org/public-key_cryptography/public-key_signatures).

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
