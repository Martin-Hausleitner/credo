# Credo

**Credo** ist Martins Architekturdeck fuer einen selbst gehosteten Agent-Kommunikationsstack: **Matrix** als Raum-, Identity-, State- und Audit-Bus; **Hermes/OpenClaw/Codex** als Agent Runtime; **Postgres, Obsidian, ActivityWatch und lokale Skills** als Memory-, Kontext- und Tool-Schicht.

> 🎯 **MVP:** Synapse oder Tuwunel + Element/Cinny + Hermes Matrix-Bot + Redis + Postgres/pgvector + S3/R2 + Obsidian + ActivityWatch + Tailscale-only Admin.

![Credo logo board](assets/logo-board.svg)

## 🧭 Gesamtbild

```mermaid
flowchart TB
  Human["👤 Martin / Team"] --> UX

  subgraph UX["💬 01 Zugänge und UX"]
    Element["Element Web<br/>Admin + Debug"]
    ElementX["Element X<br/>Matrix 2.0 Pfad"]
    Cinny["Cinny / Sable / Commet<br/>Agent-Räume"]
    Chatwoot["Chatwoot<br/>Operator Inbox"]
    Cognitor["Cognitor<br/>Tray / Web / Mobile"]
  end

  subgraph Matrix["🟢 02 Matrix Kommunikationskern"]
    Homeserver["Synapse oder Tuwunel<br/>Rooms, State, Identity, Audit"]
    Rooms["Room Topology<br/>intake / research / ops / memory / alerts"]
    Admin["Admin + Ops<br/>synadm, reports, media, purges"]
  end

  subgraph Bridge["📬 03 Bridges und Inbox"]
    Mautrix["mautrix Bridges<br/>Telegram / WhatsApp / Signal / Slack"]
    Beeper["beeper-matrix-proxy"]
    Mail["Himalaya + Maildir + notmuch"]
  end

  subgraph Gateway["🚦 04 Gateway und Jobs"]
    Bot["Hermes Matrix Bot"]
    Policy["Policy Gate<br/>Rollen, Freigaben, Audit"]
    Queue["Redis Queue<br/>Job-ID, Retry, Backpressure"]
  end

  subgraph Runtime["🤖 05 Agent Runtime"]
    Hermes["Hermes Agent"]
    OpenClaw["OpenClaw / ClawHub"]
    Codex["Codex Computer Use"]
    Skills["Skills<br/>GitHub, Notion, E-Mail, Apple, Browser, MCP"]
  end

  subgraph Data["🧠 06 Daten und Memory"]
    Pg["Postgres + pgvector"]
    Supabase["Supabase optional"]
    S3["S3 / Cloudflare R2"]
    Vault["Obsidian + Git + Dataview"]
  end

  subgraph Context["🧩 07 Persönlicher Kontext"]
    AW["ActivityWatch"]
    Health["WHOOP / Apple Health / Screen Time"]
    Media["YouTube / Icons / Presence"]
  end

  subgraph Voice["🎙️ 08 Voice und RTC"]
    Discord["Discord Voice MVP"]
    ElementCall["Element Call"]
    LiveKit["LiveKit + lk-jwt-service"]
  end

  subgraph Ops["📊 09 Betrieb und Sicherheit"]
    OTel["OpenTelemetry"]
    Grafana["Prometheus + Loki + Grafana"]
    Tailnet["Tailscale-only Admin"]
    Resources["CPU / RAM / Storage Platzhalter"]
  end

  UX --> Homeserver --> Rooms --> Bot
  Admin --> Grafana
  Mautrix --> Homeserver
  Beeper --> Homeserver
  Mail --> Chatwoot
  Chatwoot --> Bot
  Bot --> Policy --> Queue --> Hermes
  Hermes --> OpenClaw
  Hermes --> Codex
  Hermes --> Skills
  Hermes --> Pg
  Hermes --> Supabase
  Hermes --> S3
  Hermes --> Vault
  Hermes --> AW
  Cognitor --> AW
  Health --> AW
  Media --> AW
  Discord --> Hermes
  Homeserver --> ElementCall --> LiveKit --> Hermes
  Hermes --> OTel --> Grafana --> Tailnet
  Resources --> Grafana
```

## 🧱 Stack-Kategorien

| Kategorie | Logos | Was es macht | Haupt-Dokument |
|---|---|---|---|
| 🟢 Kommunikation | <img src="https://cdn.simpleicons.org/matrix/000000" width="22"> <img src="https://cdn.simpleicons.org/element/0DBD8B" width="22"> | Matrix-Räume, Nutzer, State, Federation, Audit, Clients | [Zielstack](docs/target-stack.md) |
| 📬 Inbox und Bridges | <img src="https://www.google.com/s2/favicons?domain=chatwoot.com&sz=64" width="22"> <img src="https://www.google.com/s2/favicons?domain=pimalaya.org&sz=64" width="22"> | E-Mail, Beeper, Telegram, WhatsApp, Signal, Operator-Inbox | [Matrix Ops Runbook](docs/matrix-ops-runbook.md) |
| 🤖 Agent Runtime | <img src="https://www.google.com/s2/favicons?domain=nousresearch.com&sz=64" width="22"> <img src="https://www.google.com/s2/favicons?domain=openclawdoc.com&sz=64" width="22"> <img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="22"> | Hermes, OpenClaw, Codex, Skills, Subagents, Computer Use | [Hermes Skills](docs/hermes-skills.md) |
| 🧠 Daten und Memory | <img src="https://cdn.simpleicons.org/postgresql/4169E1" width="22"> <img src="https://cdn.simpleicons.org/redis/DC382D" width="22"> <img src="https://cdn.simpleicons.org/supabase/3FCF8E" width="22"> | Jobs, Agent-State, Audit, RAG, Artefakte, interne Dashboards | [Ressourcenplanung](docs/resource-planning.md) |
| 🧩 Wissen und Kontext | <img src="https://cdn.simpleicons.org/obsidian/7C3AED" width="22"> <img src="https://www.google.com/s2/favicons?domain=activitywatch.net&sz=64" width="22"> <img src="https://cdn.simpleicons.org/apple/000000" width="22"> | Obsidian Vault, ActivityWatch, WHOOP, Apple, YouTube, Presence | [Repo-Landkarte](docs/repository-map.md) |
| 🎙️ Voice und RTC | <img src="https://cdn.simpleicons.org/discord/5865F2" width="22"> <img src="https://www.google.com/s2/favicons?domain=livekit.io&sz=64" width="22"> | Discord Voice MVP, Element Call, LiveKit, OpenAI Realtime | [Architekturfluesse](docs/architecture-flows.md) |
| 📊 Betrieb | <img src="https://cdn.simpleicons.org/grafana/F46800" width="22"> <img src="https://cdn.simpleicons.org/prometheus/E6522C" width="22"> <img src="https://cdn.simpleicons.org/tailscale/242424" width="22"> | Logs, Metriken, Alerts, Tailscale-only Admin, Redaction | [Build-Plan](docs/implementation-roadmap.md) |

## ✅ Kurzurteil

Matrix ist **nicht** das Agent-Framework und auch **nicht** die interne Queue.

| Schicht | Entscheidung |
|---|---|
| 🟢 Matrix | Kommunikations-, Raum-, Identity-, State- und Audit-Schicht |
| 🚦 Redis/Worker | echte Job-Ausführung, Retries, Backpressure und Status |
| 🤖 Hermes/OpenClaw/Codex | Agent Runtime, Skills, Tools, Memory, Automationen |
| 🧠 Postgres/pgvector | Core Memory, Audit, Agent-State und RAG |
| 🧩 ActivityWatch/Obsidian/Cognitor | persönlicher Kontext, Wissen, Lifelog und Dashboards |
| 🎙️ LiveKit/Discord Voice | separater späterer Voice-/Realtime-Strang |

**Synapse** ist der konservative Produktionsstart. **Tuwunel** ist der interessante Greenfield-Test, wenn RAM, S3 und schlanke Ops wichtiger sind. **Supabase** ist sinnvoll fuer schnelle interne Dashboards/Auth/Realtime, aber nicht als Ersatz fuer Core-Postgres + pgvector.

## 🏆 Bester Zielstack

| Kategorie | Gewinner | Gedacht fuer | Status |
|---|---|---|---|
| 🟢 Kommunikationskern | Synapse oder Tuwunel | Rooms, State, Federation, Audit | MVP-Entscheidung |
| 🚀 Deployment | matrix-docker-ansible-deploy | Homeserver, TLS, TURN, Clients, Bridges | empfohlen |
| 💬 UX | Element Web + Cinny/Sable + Element X | Admin, Alltag, Matrix-2.0, Agent-Räume | empfohlen |
| 📬 Inbox | Chatwoot + Himalaya + Maildir/notmuch | E-Mail, Beeper, Agent-Ops | aktiv/lokal |
| 🤖 Runtime | Hermes + OpenClaw + Codex | Skills, Subagents, Tools, Computer Use | Core |
| 🚦 Jobs | Redis Queue + Worker | Job-ID, Backpressure, Retry | Core |
| 🧠 Memory | Postgres + pgvector | Agent-State, Audit, RAG | Core |
| ⚡ App Layer | Supabase optional | Dashboard, Auth, Realtime, Studio | optional |
| 🗄️ Artefakte | S3 / Cloudflare R2 | Medien, Exporte, Reports | Core |
| 🧩 Wissen | Obsidian + Git + Dataview | Knowledge Vault und Audit Trail | aktiv |
| 📈 Kontext | ActivityWatch + Importer | Fokus, Health, Medien, Presence | aktiv |
| 🎙️ Voice | Discord MVP, später Element Call + LiveKit | niedrige Latenz, Calls, Streaming | später |
| 📊 Ops | OTel + Prometheus + Loki + Grafana | Logs, Metriken, Alerts | Core |
| 🔐 Admin | Tailscale | private Admin- und Dashboard-Schicht | Core |

## 📚 Detail-Dokumente

| Dokument | Inhalt |
|---|---|
| [docs/target-stack.md](docs/target-stack.md) | Ausfuehrlicher Zielstack nach Kategorien mit Logos und Empfehlungen |
| [docs/service-catalog.md](docs/service-catalog.md) | Service-Katalog mit Icons, Webseiten, GitHub-Links und Previews |
| [docs/matrix-ops-runbook.md](docs/matrix-ops-runbook.md) | Synapse/Tuwunel, Admin, Security, MatrixRTC und Bridge-Ops |
| [docs/resource-planning.md](docs/resource-planning.md) | CPU/RAM/Storage/Bandbreiten-Platzhalter |
| [docs/package-inventory.md](docs/package-inventory.md) | Package- und Tool-Inventar nach Kategorien |
| [docs/repository-map.md](docs/repository-map.md) | Eigene und externe Repos nach Rolle im Stack |
| [docs/architecture-flows.md](docs/architecture-flows.md) | Runtime-, Knowledge-, Inbox- und Voice-Flows |
| [docs/hermes-skills.md](docs/hermes-skills.md) | Installierte Hermes-Skills nach Kategorien |
| [docs/matrix-repositories.md](docs/matrix-repositories.md) | Matrix-Repositories, Clients, Bridges, SDKs, RTC |
| [docs/implementation-roadmap.md](docs/implementation-roadmap.md) | Roadmap, Phasen, Security-Regeln und Definition of Done |
| [docs/stack-comparison.md](docs/stack-comparison.md) | Vergleichstabelle der Stack-Optionen |
| [docs/architecture.mmd](docs/architecture.mmd) | Mermaid-Quellgraph |

## 🛣️ MVP Scope

1. 🟢 Matrix Homeserver aufsetzen.
2. 💬 Element Web + Cinny/Sable bereitstellen.
3. 🤖 Hermes/OpenClaw Matrix-Bot registrieren.
4. 🚦 Matrix-Nachrichten in Redis-Jobs verwandeln.
5. 🧠 Postgres + pgvector fuer Memory/RAG anbinden.
6. 🗄️ S3/R2 fuer Artefakte und grosse Dateien verwenden.
7. 📊 Redigierte Logs/Metriken intern sichtbar machen.
8. 🔐 Admin und Observability nur ueber Tailscale exponieren.

## ⏳ Nicht in den MVP

| Thema | Warum warten? |
|---|---|
| 🔒 E2EE Recording | Bots brauchen echte Teilnehmer-Keys; hoher Engineering-Aufwand |
| 🎥 4K60 MatrixRTC | Bandbreite, Codecs, Simulcast und Browser-Limits machen es teuer |
| 🧱 Eigener Matrix Client | Zu viel UI-/Crypto-/Sync-Komplexitaet |
| 📱 Meta/Instagram Bridges | Ban-, Proxy-, Session- und Cookie-Risiko |
| 🗝️ Agenten mit Admin-Tokens | Nur in eng begrenzten Ops-Raeumen mit Audit |
| ☸️ Kubernetes | Fuer den Start Overkill; Ansible + Docker ist passender |

## 🧼 Pflege-Regeln

- Neue Services zuerst in [docs/service-catalog.md](docs/service-catalog.md) eintragen.
- Neue lokale Packages in [docs/package-inventory.md](docs/package-inventory.md) kategorisieren.
- Neue eigene Repos in [docs/repository-map.md](docs/repository-map.md) einordnen.
- Architekturveraenderungen im README-Diagramm und in [docs/architecture.mmd](docs/architecture.mmd) synchron halten.
- Keine Tokens, Roh-Exports, personenbezogenen Chat-Inhalte oder privaten Credentials einchecken.

## 🔗 Repo-Hinweis

[Credo](https://github.com/Martin-Hausleitner/Credo) fasst die ausgewerteten Notion-Unterlagen, lokalen Repo-Infos und Stack-Reviews als private Architektur-Spezifikation zusammen. Es enthaelt keine Notion-Tokens, keine Roh-Exports und keine privaten Credentials.
