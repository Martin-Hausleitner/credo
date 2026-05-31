# Matrix Ops Runbook

Diese Datei sammelt die aus Notion nachgezogenen Matrix-Ops-Punkte. Sie ist kein finales Deployment-Handbuch, sondern die Checkliste fuer die naechste konkrete Implementierung.

## 🟢 Homeserver-Entscheidung

| Thema | Synapse | Tuwunel |
|---|---|---|
| Ziel | kompatibler Produktionsstart | leichter Greenfield-Test |
| Staerke | Admin-API, Tools, Bridges, bekannte Ops-Pfade | niedriger Ressourcenbedarf, S3/OIDC-Fokus |
| Risiko | mehr RAM/I/O/Ops-Last | weniger breite Produktionshistorie |
| Empfehlung | Default, wenn es funktionieren muss | parallel evaluieren, wenn Ressourcen knapp sind |

## 🛠️ Synapse Admin und Wartung

| Bereich | Was pruefen |
|---|---|
| User und Rooms | Admin-API, `synadm`, Synapse-Admin UI, Server Notices |
| Media | Upload-Limits, Retention, Purges, S3-Provider, Quotas |
| Reports | Abuse/Spam/Bridge-Fehler in dedizierte Ops-Raeume spiegeln |
| Background Updates | Fortschritt in Prometheus/Grafana sichtbar machen |
| Federation | Signing Keys, Server Name, `.well-known`, TLS und DNS sauber dokumentieren |

## 🔐 Security und Auth

| Bereich | Regel |
|---|---|
| Admin | Admin-APIs nur ueber Tailscale oder private Netze |
| Registrierung | 3PID/E-Mail, Invite Policy und Auto-Join-Raeume bewusst setzen |
| Guests | Guest Access aus, ausser fuer bewusst isolierte Test-Raeume |
| OIDC/MAS | fuer Element X und Matrix-2.0-Pfad frueh einplanen |
| URL Previews | IP-Leakage und externe Fetches bewusst konfigurieren |
| Retention | Raum- und Medien-Retention pro Raumklasse definieren |
| Rollen | LLM entscheidet keine Berechtigungen; Backend prueft hart |

## 🎙️ MatrixRTC / LiveKit Checkliste

| Bereich | Notiz |
|---|---|
| `.well-known/matrix/client` | `org.matrix.msc4143.rtc_foci` fuer LiveKit-Foci setzen |
| Auth | `lk-jwt-service` zwischen MatrixRTC und LiveKit betreiben |
| Homeserver Access | erlaubte Homeserver in `LIVEKIT_FULL_ACCESS_HOMESERVERS` begrenzen |
| Netzwerk | TURN/TLS 443 und LiveKit UDP-Portbereich planen |
| Matrix MSCs | MSC3266, MSC4143, MSC4222 und Event Delay Settings beobachten |
| Recording | E2EE Recording nicht in MVP; spaeter nur mit klarer Teilnehmer-/Key-Strategie |

## 🌉 Bridge Ops

| Bridge | Empfehlung |
|---|---|
| Telegram | zuerst testen, gute Nutzbarkeit |
| WhatsApp | danach, Session- und Device-Handling beachten |
| Signal | danach, separate DB und Backups |
| Slack | optional, eher Team-/Workspace-Kontext |
| Discord | lieber Bot/Guild sauber als riskantes Puppeting |
| Meta/Instagram | nur spaeter mit VM, Proxy, Kill-Switch, Provisioning API und Session-Watchdog |

## 🧩 Composio-Untrusted-Regime und OSS-Bridge-Migration

OpenHuman bringt 118+ OAuth-Integrationen ueber den **Composio**-Connector mit. Composio ist managed/proprietaer und damit der **Edge-Default**, aber niemals vertrauenswuerdig: jeder Connector laeuft im **MCP-Untrusted-Regime**. Native OSS-Bridge oder eigene MCP-Integration bleibt je Connector das **Migrationsziel**, nicht der Sofort-Ersatz.

Untrusted-Regeln fuer jeden Composio-Connector:

1. Eigene, minimal gescopte Credentials je Connector — keine ambient Secrets aus `.env`, Shell oder Keychain.
2. Connector-Output ist Daten, nicht Anweisung: vor Prompt-Wiedereinspeisung sanitizen (Prompt-Injection-Schutz).
3. Schreibende Aktionen nur ueber das Write-Gate mit `memory_mode`/Risiko-Klasse und Freigabe.
4. Jeder Connector-Call wird mit `run_id`, `approval_id`, `connector`, Scope-Klasse und Ergebnisstatus auditiert.
5. Riskante Connectors laufen isoliert (VM/Proxy-Konzept), mit Kill-Switch und eigener Retention.

Migrationsziel je Connector-Klasse (Composio managed → OSS-Ziel):

| Connector-Klasse | Composio (Edge-Default) | OSS-Migrationsziel | Trigger fuer Migration |
|---|---|---|---|
| Chat / Messaging | Telegram, WhatsApp, Signal, Slack, Discord | native mautrix-Bridge je Netz | sobald Bridge stabil + auditiert |
| Mail | Gmail/Outlook via Composio | Maildir + notmuch + Mail-MCP | sobald lokaler Mail-Pfad steht |
| Kalender | Google/Outlook Calendar | cal.rs + CalDAV-MCP | sobald cal.rs produktiv |
| Dev / Issues | GitHub, Notion, Linear | native GitHub-/Notion-MCP-Skill | sobald Skill risikoklassifiziert |
| Storage / Files | Drive, Dropbox | MinIO / R2 + S3-MCP | sobald Artefakt-Ledger steht |

So bleibt der Edge sofort nutzbar, aber jede Integration hat einen klaren Pfad raus aus managed/proprietaer hin zu OSS unter Credos Gates.

Mehr Details: [openhuman-integration.md](openhuman-integration.md), [Research: MCP-Security](research-improvements.md), [target-stack.md](target-stack.md). Quellen: [Composio](https://github.com/ComposioHQ/composio), [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices).
