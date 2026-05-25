# Roadmap und Build-Plan

## Phase 0: Entscheidungen

| Entscheidung | Default | Alternative |
|---|---|---|
| Homeserver | Synapse fuer sicheren Start | Tuwunel fuer leichten Greenfield-Stack |
| Client UX | Element Web + Cinny | Sable/Commet als zweite UX |
| Agenten | Ein Bot-Account | Appservice spaeter |
| Voice | Noch nicht im MVP | Discord Voice fuer schnellen Prototyp |
| Storage | Cloudflare R2 / S3 | MinIO nur auf separatem Storage-Node |
| Admin | Tailscale-only | Kein Public Admin |

## Phase 1: Text-MVP

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
7. Bot prueft Rollen hart im Backend.
8. Job in Redis schreiben.
9. Worker fuehrt Hermes/OpenClaw Task aus.
10. Ergebnis mit Job-ID und Artefaktlinks in Matrix posten.

## Phase 2: Memory und Wissen

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

## Phase 3: Bridges

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

## Phase 4: RTC und Voice

1. Element Call + LiveKit + lk-jwt-service einrichten.
2. `.well-known/matrix/client` mit RTC Foci setzen.
3. Erst 1080p/1440p stabilisieren.
4. 4K/Ultrawide nur als separates Profil.
5. Recording nur ohne E2EE oder mit eigenem Recorder-Teilnehmer.
6. AI Voice zuerst ausserhalb MatrixRTC testen.

## Phase 5: Observability

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

## Security-Regeln

| Regel | Umsetzung |
|---|---|
| LLM entscheidet keine Berechtigungen | Rollencheck im Bot/Backend |
| Admin-APIs nie public | Tailscale-only |
| Destruktive Tools brauchen Freigabe | Permission Manifest + Audit |
| Keine Tokens in Logs | Redaction Layer |
| Agenten sind scoped | Pro Raum eigene Session/Policy |
| Memory Writes sind auditierbar | Git/DB History + Matrix Link |

## Definition of Done fuer MVP

- Ein Mensch kann in Matrix eine Aufgabe stellen.
- Bot antwortet mit Job-ID.
- Hermes/OpenClaw fuehrt einen echten Task aus.
- Ergebnis landet im selben Raum.
- Artefakte liegen in S3/R2.
- Memory kann read-only durchsucht werden.
- Rollencheck verhindert Ops-Tools fuer normale Raeume.
- Logs sind redigiert.
- Alles ist ueber Tailscale administrierbar.
