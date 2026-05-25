# Ressourcenplanung

Diese Tabelle ist absichtlich als Platzhalter vorbereitet. Martin kann hier spaeter CPU-Kerne, RAM, Storage und Bandbreite pro Baustein eintragen.

| Kategorie | Komponente | CPU-Kerne | RAM | Storage | Netzwerk | Notizen |
|---|---|---:|---:|---:|---:|---|
| 🟢 Kommunikationskern | Synapse | TBD | TBD | TBD | TBD | Kompatibilitaet, Admin-API, Bridges, Postgres-I/O, Media Retention. |
| 🟢 Kommunikationskern | Tuwunel | TBD | TBD | TBD | TBD | Greenfield-Test fuer niedrigen RAM, S3 und OIDC. |
| 💬 Zugange | Element Web / Cinny / Sable | TBD | TBD | TBD | TBD | Web-Clients koennen leicht getrennt vom Homeserver liegen. |
| 📬 Bridges | mautrix Telegram/WhatsApp/Signal/Slack | TBD | TBD | TBD | TBD | Pro Bridge eigene DB und eigener Appservice-Token. |
| 🤖 Agent Runtime | Hermes / OpenClaw / Codex Worker | TBD | TBD | TBD | TBD | Nach Tool-Last, Modell-Last und parallelen Jobs dimensionieren. |
| 🧠 Daten | Postgres + pgvector | TBD | TBD | TBD | TBD | Core Memory separat von Matrix-Datenbank planen. |
| 🧠 Daten | Redis | TBD | TBD | TBD | TBD | Queue-Stau und Retry-Last beobachten. |
| 🧠 Daten | S3 / Cloudflare R2 | n/a | n/a | TBD | TBD | Artefakte, Exporte, Matrix-Medien, Backups. |
| 🎙️ Voice | LiveKit + TURN | TBD | TBD | TBD | TBD | Bandbreite ist der Engpass, besonders bei 4K/Ultrawide. |
| 📊 Ops | OTel + Prometheus + Loki + Grafana | TBD | TBD | TBD | TBD | Retention, Redaction und Dashboard-Zugriff festlegen. |
| 🔐 Private Admin | Tailscale / Reverse Proxy | TBD | TBD | TBD | TBD | Admin-APIs nicht public exponieren. |

## Dimensionierungsnotizen

- Matrix ist ein langlebiger Raum- und State-Dienst; CPU ist oft weniger kritisch als Datenbank-I/O, Media Storage und Backups.
- Voice/RTC muss getrennt geplant werden, weil Netzwerk, TURN und Simulcast schneller limitieren als reine CPU.
- Agent Worker duerfen horizontal wachsen, solange Redis, Rate Limits und Freigabe-Policy sauber bleiben.
- Supabase wird nur dimensioniert, wenn es wirklich als Dashboard/Auth/Realtime-Layer betrieben wird.

## Ausbauprofile

| Profil | Grober Korridor | Ziel | Aktivieren | Noch nicht aktivieren |
|---|---|---|---|---|
| 🧪 Lab | 2-4 vCPU, 8-16 GB RAM, 100-250 GB SSD | lokales Testen und Doku validieren | README, GitHub-Matrix, lokale Inventur, einzelne Worker | Federation, Bridges, Voice |
| 🚀 MVP | 4-8 vCPU, 16-32 GB RAM, 250-500 GB SSD + S3/R2 | Text- und Job-Orchestrierung | Matrix, Element/Cinny, Bot, Redis, Postgres/pgvector, S3/R2, Tailscale | MatrixRTC, Meta-Bridges, E2EE Recording |
| 🏠 Personal OS | 6-12 vCPU, 32-64 GB RAM, 500 GB-1 TB SSD + S3/R2 | Alltagstauglicher persoenlicher Kontext | Obsidian, ActivityWatch, WHOOP/Apple/YouTube Importer, Cognitor | Multi-Tenant-Team-Betrieb |
| 🎙️ Voice Lab | 4-8 vCPU, 16-32 GB RAM, gute Upstream-Bandbreite | niedrige Latenz testen | Discord/OpenAI Realtime, ASR Worker, Obsidian Summaries | produktive MatrixRTC Calls |
| 📞 RTC | 8-16 vCPU, 32-64 GB RAM, hohe UDP-Bandbreite | Matrix-native Calls | Element Call, LiveKit, lk-jwt-service, TURN/TLS, Foci | 4K/Ultrawide als Default |
| 🏢 Team | 12+ vCPU, 64+ GB RAM, getrennte DB/Storage-Nodes | mehrere Menschen und Rollen | MAS/OIDC, Rollenmodell, Bridge-Policies, Audit Dashboards | ungepruefte Memory Writes |

Diese Werte sind Startkorridore, keine Sizing-Garantie. Matrix-Datenbank, Bridge-Last, Media Retention, OTel-Retention und parallele Agentenlaeufe koennen die reale Groesse staerker treiben als reine User-Zahl.
