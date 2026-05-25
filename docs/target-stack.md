# Zielstack nach Kategorien

Diese Datei ist die ausfuehrliche Sicht auf den Credo-Zielstack. Das README zeigt nur die Startkarte; hier steht, wofuer jede Kategorie gedacht ist und welche Komponenten zusammengehoeren.

## 🧭 Architekturfluss

```text
Mensch / Team
  -> Matrix Clients
  -> Matrix Homeserver
  -> Bot Gateway + Policy Gate
  -> Redis Jobs
  -> Hermes / OpenClaw / Codex
  -> Memory, Wissen, Artefakte, Kontext
  -> Ergebnis zurueck in Matrix
```

## 🟢 Kommunikationskern

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/matrix/000000" width="24"> | Matrix | Raum-, State-, Identity- und Audit-Bus | Core |
| <img src="https://www.google.com/s2/favicons?domain=matrix.org&sz=64" width="24"> | Synapse | kompatibler Produktionsstart, Admin-API, Bridges | Default, wenn Stabilitaet zaehlt |
| <img src="https://www.google.com/s2/favicons?domain=matrix.org&sz=64" width="24"> | Tuwunel | leichter Greenfield-Homeserver, RAM/S3/OIDC-Test | Testen, wenn Ressourcen knapp sind |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="24"> | matrix-docker-ansible-deploy | reproduzierbares Deployment mit TLS, TURN, Clients, Bridges | Runbook-Basis |

## 💬 Zugange und UX

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/element/0DBD8B" width="24"> | Element Web | Admin, Debugging, Referenzclient | immer bereitstellen |
| <img src="https://cdn.simpleicons.org/element/0DBD8B" width="24"> | Element X | Matrix-2.0-Pfad mit Rust SDK, Sliding Sync, OIDC, MatrixRTC | mobile Zukunft, aber Accounts vorsichtig planen |
| <img src="https://www.google.com/s2/favicons?domain=cinny.in&sz=64" width="24"> | Cinny | ruhige, schnelle Agent-Raum-UX | bevorzugte Alltags-Web-UX |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="24"> | Sable / Commet | alternative Discord-artige oder Multi-Account-UX | beobachten/testen |

**Hinweis:** Element X iOS ist fuer mehrere Accounts heikel. Logout kann lokale Kryptodaten loeschen; Secure Key Backup muss vor ernsthafter Nutzung sauber stehen.

## 📬 Bridges und Inbox

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://www.google.com/s2/favicons?domain=matrix.org&sz=64" width="24"> | mautrix Bridges | Telegram, WhatsApp, Signal, Slack nach Matrix | Phase 3 |
| <img src="https://www.google.com/s2/favicons?domain=beeper.com&sz=64" width="24"> | Beeper / beeper-matrix-proxy | Beeper/BIPA-Portale als Matrix-Raeume | lokale Referenz |
| <img src="https://www.google.com/s2/favicons?domain=chatwoot.com&sz=64" width="24"> | Chatwoot | Operator-Inbox fuer Chat, E-Mail, Agent-Ops | sehr sinnvoll |
| <img src="https://www.google.com/s2/favicons?domain=pimalaya.org&sz=64" width="24"> | Himalaya + Maildir + notmuch | E-Mail lesen, suchen, triagieren, auditieren | Core Skill-Pfad |
| <img src="https://www.google.com/s2/favicons?domain=instagram.com&sz=64" width="24"> | Meta/Instagram Bridges | riskante spaetere Spezialphase | nur VM/Proxy/Kill-Switch |

## 🤖 Agent Runtime

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://www.google.com/s2/favicons?domain=nousresearch.com&sz=64" width="24"> | Hermes Agent | Orchestrierung, Sessions, Memory, Automationen | Core |
| <img src="https://www.google.com/s2/favicons?domain=openclawdoc.com&sz=64" width="24"> | OpenClaw | lokale Skills, Tooling, Automationen | Core |
| <img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="24"> | Codex | coding agent, Computer Use, Validierung | Core fuer lokale Arbeit |
| <img src="https://cdn.simpleicons.org/github/181717" width="24"> | GitHub Skills | Issues, PRs, Repos, Reviews, Releases | installiert |
| <img src="https://cdn.simpleicons.org/notion/000000" width="24"> | Notion Skill | Notion lesen, suchen, strukturieren | installiert |
| <img src="https://cdn.simpleicons.org/apple/000000" width="24"> | Apple Skills | Notes, Reminders, iMessage, Find My | installiert |

## 🧠 Daten, Memory und Artefakte

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/redis/DC382D" width="24"> | Redis | Queue, Backpressure, Job-Status | Core |
| <img src="https://cdn.simpleicons.org/postgresql/4169E1" width="24"> | Postgres | Agent-State, Audit, App-Daten | Core |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="24"> | pgvector | semantische Suche und RAG | Core |
| <img src="https://cdn.simpleicons.org/supabase/3FCF8E" width="24"> | Supabase | schnelle Dashboards, Auth, Realtime, Studio | optional, nicht Core-DB-Ersatz |
| <img src="https://www.google.com/s2/favicons?domain=cloudflare.com&sz=64" width="24"> | S3 / Cloudflare R2 | Artefakte, Exporte, Matrix-Medien | Core |

## 🧩 Wissen und Kontext

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/obsidian/7C3AED" width="24"> | Obsidian + Git | local-first Knowledge Vault und Audit | Core |
| <img src="https://www.google.com/s2/favicons?domain=activitywatch.net&sz=64" width="24"> | ActivityWatch | Fokus, App/Web-Zeit, Timeline | Core Kontext |
| <img src="https://www.google.com/s2/favicons?domain=whoop.com&sz=64" width="24"> | WHOOP Importer | Schlaf, Recovery, Training | Kontext |
| <img src="https://cdn.simpleicons.org/apple/000000" width="24"> | Apple Health / Screen Time | Device- und Health-Kontext | Kontext |
| <img src="https://cdn.simpleicons.org/youtube/FF0000" width="24"> | YouTube Importer | Mediennutzung und Watch Sessions | Kontext |

## 🎙️ Voice und Realtime

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/discord/5865F2" width="24"> | Discord Voice MVP | schneller Voice-Prototyp ausserhalb MatrixRTC | zuerst testen |
| <img src="https://cdn.simpleicons.org/element/0DBD8B" width="24"> | Element Call | MatrixRTC Frontend | spaeter |
| <img src="https://www.google.com/s2/favicons?domain=livekit.io&sz=64" width="24"> | LiveKit | SFU, Agents, Egress, Realtime Media | spaeter |
| <img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="24"> | OpenAI Realtime | niedrige Latenz, Tool Calls, Barge-in | schneller Voice-Pfad |

## 📊 Betrieb und Sicherheit

| Logo | Komponente | Zweck | Empfehlung |
|---|---|---|---|
| <img src="https://www.google.com/s2/favicons?domain=opentelemetry.io&sz=64" width="24"> | OpenTelemetry | Traces/Metriken mit Redaction | Core |
| <img src="https://cdn.simpleicons.org/prometheus/E6522C" width="24"> | Prometheus | Metriken und Alerts | Core |
| <img src="https://cdn.simpleicons.org/grafana/F46800" width="24"> | Loki + Grafana | Logs und Dashboards | Core |
| <img src="https://cdn.simpleicons.org/tailscale/242424" width="24"> | Tailscale | private Admin-Schicht | Core |
