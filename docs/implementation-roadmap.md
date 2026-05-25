# 🛣️ Roadmap und Build-Plan

## 🧭 Phase 0: Entscheidungen

| Entscheidung | Default | Alternative |
|---|---|---|
| Homeserver | Synapse fuer sicheren Start | Tuwunel fuer leichten Greenfield-Stack |
| Client UX | Element Web + Cinny | Sable/Commet als zweite UX |
| Agenten | Ein Bot-Account | Appservice spaeter |
| Voice | Noch nicht im MVP | Discord Voice fuer schnellen Prototyp |
| Storage | Cloudflare R2 / S3 | MinIO nur auf separatem Storage-Node |
| Admin | Tailscale-only | Kein Public Admin |

## 🟢 Phase 1: Text-MVP

1. VPS/Dedicated mit Debian oder Ubuntu vorbereiten.
2. Tailscale installieren.
3. Matrix Homeserver deployen.
4. Element Web und Cinny/Sable bereitstellen.
5. Hermes/OpenClaw Matrix-Bot registrieren.
6. Bot hoert auf dedizierte Raeume:
   - `#agent-intake`
   - `#agent-research`
   - `#agent-ops`
   - `#agent-memory`
   - `#agent-alerts`
7. Bot prueft Rollen hart im Backend und erzeugt einen Run Contract mit Risiko, Tool Scope, Budget und Retention.
8. Job in Redis schreiben.
9. Worker fuehrt Hermes/OpenClaw Task aus und prueft vor jedem riskanten Tool Call erneut die Runtime Policy.
10. Ergebnis mit Job-ID, Trace-ID und Artefaktlinks in Matrix posten.

## 🛠️ Phase 1b: Matrix Admin und Wartung

1. Synapse-Admin oder `synadm` nur ueber Tailscale bereitstellen.
2. Admin-API-Zugriff trennen von normalen Bot-Accounts.
3. Media-Limits, Retention und Purge-Strategie dokumentieren.
4. Reports, Abuse, Bridge-Fehler und Background-Updates in `#agent-ops` spiegeln.
5. Prometheus-Metriken fuer Homeserver, DB, Background Updates und Federation erfassen.
6. URL-Previews, Guest Access, Registration, Auto-Join und Rate Limits bewusst setzen.

Mehr Details: [Matrix Ops Runbook](matrix-ops-runbook.md).

## 🔑 Phase 1c: Auth, MAS und Identitaeten

1. Matrix Authentication Service als OIDC-Zielbild dokumentieren.
2. Element X Login-Anforderungen und Secure Key Backup pruefen.
3. Admin-, Bot-, Agenten- und Menschen-Accounts trennen.
4. MAS als OAuth2/OIDC-Provider nach MSC3861 bewerten, inklusive Client-Kompatibilitaet, Account-Migration, Login-Flows und Admin-Recovery.
5. Kompatibilitaetslayer fuer Legacy-Clients erst nach erfolgreichem Text-MVP aktivieren.
6. Invite-, Registration-, 3PID-, Guest- und Auto-Join-Regeln pro Raumklasse festlegen.

## 🧠 Phase 2: Memory und Wissen

1. Postgres + pgvector bereitstellen.
2. Obsidian/Markdown Vault anbinden.
3. Memory-Typen definieren:
   - Decision
   - Project
   - Person
   - Meeting
   - Task
   - Source
   - Runbook
4. Agent darf zunaechst nur read-only suchen.
5. Schreibzugriff nur fuer dedizierte Memory-Raeume und mit Audit.

## 📊 Phase 2b: Trace Every Run

1. Jede Matrix-Anfrage bekommt `room_id`, `event_id`, `job_id` und `run_id`.
2. LLM-Aufrufe, MCP Calls, RAG-Retrieval, Tool Calls und Subagent-Handoffs als getrennte OTel-Spans erfassen.
3. Artefakte mit `artifact_id` in Postgres und S3/R2 verknuepfen.
4. Prompts, E-Mail-Inhalte, Tokens und private Texte vor Loki/Grafana redigieren.
5. Raum- und User-IDs in Metriken hashen; echte IDs nur in geschuetzten Audit-Tabellen speichern.
6. In `#agent-ops` nur Status, Kosten, Fehlerklasse und Link zum internen Trace posten.

## 📬 Phase 3: Bridges

Bridge-Reihenfolge:

1. Telegram
2. WhatsApp
3. Signal
4. Slack
5. Discord bot/guild
6. Meta/Instagram nur mit Proxy-/VM-Konzept

Regeln:

- Keine Consumer-Cookies zentral speichern.
- Keine User-Token-Puppeting als Default.
- Pro Bridge eigener Appservice-Token und eigene DB.
- Riskante Bridges in VM mit Kill-Switch.
- Meta/Instagram nur als spaetere Spezialphase mit Provisioning API, Session-Watchdog, Proxy-/VM-Konzept und klarer Abschaltung.

## 🎙️ Phase 4: RTC und Voice

1. Element Call + LiveKit + lk-jwt-service einrichten.
2. `.well-known/matrix/client` mit RTC Foci setzen.
3. Reverse-Proxy-Routen `/livekit/jwt` und `/livekit/sfu` dokumentieren.
4. LiveKit API/WebSocket `7880` hinter TLS/LB, ICE/TCP `7881`, ICE/UDP `50000-60000` oder UDP mux `7882` planen.
5. Homeserver-Settings fuer MatrixRTC pruefen: MSC-Flags, `max_event_delay_duration`, Rate Limits und OpenID/Federation Listener.
6. Erst 1080p/1440p stabilisieren.
7. 4K/Ultrawide nur als separates Profil.
8. Recording nur ohne E2EE oder mit eigenem Recorder-Teilnehmer.
9. AI Voice zuerst ausserhalb MatrixRTC testen.
10. Fuer MatrixRTC `org.matrix.msc4143.rtc_foci`, `lk-jwt-service`, TURN/TLS und LiveKit UDP-Portbereich vorbereiten.
11. `LIVEKIT_FULL_ACCESS_HOMESERVERS` hart begrenzen.
12. Discord/OpenAI Realtime als schnellen Voice-MVP getrennt vom MatrixRTC-Produktionspfad behandeln.

## 📊 Phase 5: Observability

1. OTel Collector lokal.
2. Redaction vor zentraler Speicherung.
3. Prometheus + Loki + Grafana intern.
4. Alerts fuer:
   - Tool-Call-Spikes
   - Kosten-Spikes
   - Rate-Limits
   - Bridge-Login-Fehler
   - Queue-Stau
   - Agent-Loop-Verdacht

## 🧮 Ressourcenplatzhalter

Die konkrete Dimensionierung lebt in [resource-planning.md](resource-planning.md). Die wichtigsten Kategorien:

| Kategorie | Komponenten |
|---|---|
| 🟢 Kommunikationskern | Synapse, Tuwunel, Clients |
| 📬 Bridges | mautrix Bridges, Beeper, Chatwoot, Maildir |
| 🤖 Agenten | Hermes, OpenClaw, Codex Worker |
| 🧠 Daten | Postgres, pgvector, Redis, S3/R2 |
| 🎙️ Realtime | LiveKit, TURN, Voice Worker |
| 📊 Betrieb | OTel, Prometheus, Loki, Grafana, Tailscale |

## 🔐 Security-Regeln

| Regel | Umsetzung |
|---|---|
| LLM entscheidet keine Berechtigungen | Rollencheck im Bot/Backend |
| Admin-APIs nie public | Tailscale-only |
| Destruktive Tools brauchen Freigabe | Permission Manifest + Audit |
| Keine Tokens in Logs | Redaction Layer |
| Agenten sind scoped | Pro Raum eigene Session/Policy |
| Memory Writes sind auditierbar | Git/DB History + Matrix Link |
| Matrix-Admin ist getrennt | Kein Admin-Token in normalen Agent-Raeumen |
| URL-Previews sind bewusst | Externe Fetches und IP-Leakage vermeiden |
| Element X nutzt sauberes Backup | Secure Key Backup vor produktiver Multi-Device-/Mobile-Nutzung |

## ✅ Definition of Done fuer MVP

- Ein Mensch kann in Matrix eine Aufgabe stellen.
- Bot antwortet mit Job-ID.
- Hermes/OpenClaw fuehrt einen echten Task aus.
- Ergebnis landet im selben Raum.
- Artefakte liegen in S3/R2.
- Memory kann read-only durchsucht werden.
- Rollencheck verhindert Ops-Tools fuer normale Raeume.
- Logs sind redigiert.
- Alles ist ueber Tailscale administrierbar.
