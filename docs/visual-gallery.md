# Visual Gallery und Diagramme

Diese Datei ist die visuelle Schnellspur fuer Credo: mehr Screenshots, mehr Mermaid-Diagramme und staerker abstrahierte Karten. Die grossen Inventare bleiben in den spezialisierten Dateien, hier geht es um Orientierung.

## Stack Planes

![Credo Stack Planes](../assets/credo-planes.svg)

## Screen Gallery

| Bereich | Preview | Rolle in Credo |
|---|---|---|
| Hermes Desktop Chat | <img src="https://raw.githubusercontent.com/fathah/hermes-desktop/main/previews/chat.png" width="260"> | lokale Agent-Schaltzentrale fuer Chat, Tool-Fortschritt und Sessions |
| Hermes Desktop Skills | <img src="https://raw.githubusercontent.com/fathah/hermes-desktop/main/previews/skills.png" width="260"> | sichtbares Skill-Management fuer Hermes/OpenClaw-nahe Workflows |
| Hermes Desktop Gateway | <img src="https://raw.githubusercontent.com/fathah/hermes-desktop/main/previews/gateway.png" width="260"> | Messaging-Gateways als Desktop-konfigurierbare Oberflaeche |
| Hermes Desktop Schedules | <img src="https://raw.githubusercontent.com/fathah/hermes-desktop/main/previews/schedules.png" width="260"> | Cron-/Automationsansicht fuer wiederkehrende Agentenarbeit |
| Element Web | <img src="https://opengraph.githubassets.com/Credo/element-hq/element-web" width="260"> | Matrix-Referenzclient fuer Admin, Debugging und Kompatibilitaet |
| Cinny | <img src="https://opengraph.githubassets.com/Credo/cinnyapp/cinny" width="260"> | schnelle Agent-Raum-UX |
| OpenClaw | <img src="https://opengraph.githubassets.com/Credo/openclaw/openclaw" width="260"> | lokale Skills, Tools und Automationen |
| Supabase | <img src="https://opengraph.githubassets.com/Credo/supabase/supabase" width="260"> | optionaler Dashboard/Auth/Realtime-Beschleuniger |

## Layer Abstraction

```mermaid
flowchart TB
  NorthStar["Credo<br/>Agent Work OS"] --> Rooms["Rooms<br/>Matrix Context"]
  Rooms --> Contract["Run Contract<br/>risk + tools + budget + memory"]
  Contract --> Jobs["Jobs<br/>Redis + Worker"]
  Jobs --> Runtime["Runtime<br/>Hermes + OpenClaw + Codex"]
  Runtime --> Knowledge["Knowledge<br/>Postgres + Obsidian + ActivityWatch"]
  Runtime --> Artifacts["Artifacts<br/>S3/R2 + checksums"]
  Runtime --> Ops["Ops<br/>OTel + Grafana + Tailscale"]
```

## Control Surfaces

```mermaid
flowchart LR
  Martin["Martin"] --> MatrixClient["Element / Cinny<br/>room first"]
  Martin --> HermesDesktop["Hermes Desktop<br/>local control"]
  Martin --> Cognitor["Cognitor<br/>personal context"]
  Martin --> Obsidian["Obsidian<br/>review layer"]
  MatrixClient --> Matrix["Matrix Rooms"]
  HermesDesktop --> Hermes["Hermes API<br/>local or remote"]
  Cognitor --> ActivityWatch["ActivityWatch"]
  Obsidian --> Vault["Git-backed Vault"]
  Matrix --> Hermes
  Hermes --> Vault
  Hermes --> ActivityWatch
```

## Library Map

```mermaid
flowchart TB
  subgraph Desktop["Desktop + Web UI"]
    Electron["Electron"]
    Vite["Vite"]
    React["React"]
    Tailwind["Tailwind"]
    Lucide["Lucide Icons"]
    SQLite["better-sqlite3"]
  end

  subgraph Runtime["Agent Runtime"]
    Hermes["Hermes Agent"]
    OpenClaw["OpenClaw"]
    MCP["MCP Servers"]
    FastAPI["FastAPI / uvicorn"]
    Fastify["Fastify"]
  end

  subgraph Jobs["Jobs + Data"]
    Redis["Redis / ioredis"]
    Postgres["Postgres"]
    Pgvector["pgvector"]
    R2["S3 / Cloudflare R2"]
  end

  subgraph Ops["Ops"]
    OTel["OpenTelemetry"]
    Prometheus["Prometheus"]
    Loki["Loki"]
    Grafana["Grafana"]
    Tailscale["Tailscale"]
  end

  Electron --> React --> Vite
  React --> Lucide
  Electron --> SQLite
  Electron --> Hermes
  Hermes --> OpenClaw --> MCP
  Hermes --> FastAPI
  Hermes --> Fastify
  Hermes --> Redis --> Postgres --> Pgvector
  Hermes --> R2
  Hermes --> OTel --> Prometheus --> Grafana
  OTel --> Loki --> Grafana
  Grafana --> Tailscale
```

## Policy Ladder

```mermaid
stateDiagram-v2
  [*] --> ReadOnly
  ReadOnly --> LocalWrite: reviewed local artifact
  LocalWrite --> ExternalWrite: approval_id required
  ExternalWrite --> AccountImpact: money, account, repo, inbox
  AccountImpact --> PublicPosting: public release or outbound message
  PublicPosting --> [*]

  ReadOnly: read-only\nsearch, summarize, inspect
  LocalWrite: local-write\nfiles, notes, drafts
  ExternalWrite: external-write\nGitHub, Notion, Matrix, email draft send
  AccountImpact: account-impacting\nbilling, secrets, admin APIs
  PublicPosting: public/posting\nrelease, social, public repo
```

## Data Shape

```mermaid
erDiagram
  MATRIX_EVENT ||--o| RUN_CONTRACT : creates
  RUN_CONTRACT ||--|| REDIS_JOB : enqueues
  REDIS_JOB ||--|| AGENT_RUN : executes
  AGENT_RUN ||--o{ TOOL_CALL : contains
  AGENT_RUN ||--o{ ARTIFACT : writes
  AGENT_RUN ||--o{ MEMORY_PROPOSAL : proposes
  AGENT_RUN ||--|| TRACE : emits
  ARTIFACT }o--|| STORAGE_OBJECT : points_to
  MEMORY_PROPOSAL }o--|| OBSIDIAN_NOTE : reviewed_into
```

## Deployment Plane

```mermaid
flowchart TB
  Public["Public Plane"] --> Proxy["Reverse Proxy / TLS"]
  Proxy --> Matrix["Matrix Client/Federation"]
  Proxy --> Bridges["Selected Bridges"]
  Proxy --> ElementCall["Element Call / LiveKit paths"]

  Tailnet["Tailscale Admin Plane"] --> Grafana["Grafana / Loki / Prometheus"]
  Tailnet --> AdminAPI["Synapse Admin API"]
  Tailnet --> DB["Postgres / Redis"]
  Tailnet --> Supabase["Supabase Studio optional"]
  Tailnet --> S3Admin["S3/R2 Admin"]

  Matrix --> Bot["Hermes Matrix Bot"]
  Bot --> Jobs["Redis Jobs"]
  Jobs --> Worker["Hermes/OpenClaw/Codex Worker"]
  Worker --> DB
  Worker --> S3Admin
```

## Visual Reading Order

| Reihenfolge | Datei | Warum |
|---:|---|---|
| 1 | [README.md](../README.md) | North Star, Zielstack und MVP-Scope |
| 2 | [visual-gallery.md](visual-gallery.md) | Bilder, Diagramme und abstrakte Layer |
| 3 | [target-stack.md](target-stack.md) | konkrete Stack-Entscheidung |
| 4 | [architecture-flows.md](architecture-flows.md) | Runtime-, Policy-, Knowledge-, Inbox- und Voice-Flows |
| 5 | [package-inventory.md](package-inventory.md) | Libraries, Frameworks und Tools |
