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
