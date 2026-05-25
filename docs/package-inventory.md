# Package- und Tool-Inventar

Diese Datei buendelt die technischen Pakete aus README, lokalen Manifesten und Stack-Entscheidungen. Das README verweist nur noch auf diese Kategorien.

## 🖥️ Frontend, Desktop und Mobile

| Logo | Paket / Tool | Wird genutzt in | Zweck |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/react/61DAFB" width="22"> | `react` / `react-dom` | Cognitor, Dashboards | lokale Web-UIs |
| <img src="https://cdn.simpleicons.org/vite/646CFF" width="22"> | `vite` / `@vitejs/plugin-react` | Cognitor, Dashboard-Prototypen | schnelle lokale Builds |
| <img src="https://cdn.simpleicons.org/typescript/3178C6" width="22"> | `typescript` | Web, Tools, Voice Agent | Typisierung |
| <img src="https://www.google.com/s2/favicons?domain=lucide.dev&sz=64" width="22"> | `lucide-react` | UI-Apps | einheitliche Icons |
| <img src="https://cdn.simpleicons.org/tauri/24C8DB" width="22"> | `@tauri-apps/*` | Cognitor Tray | native macOS App |
| <img src="https://cdn.simpleicons.org/expo/000020" width="22"> | `expo` / `react-native` | Mobile Companion | mobile Agent-UX |
| <img src="https://www.google.com/s2/favicons?domain=playwright.dev&sz=64" width="22"> | `playwright` | Workspace | Browser-Validierung und Screenshots |

## 🤖 Agenten, APIs und Worker

| Logo | Paket / Tool | Wird genutzt in | Zweck |
|---|---|---|---|
| <img src="https://www.google.com/s2/favicons?domain=fastify.dev&sz=64" width="22"> | `fastify` / `@fastify/*` | Voice/API | HTTP, WebSocket, Static, Rate Limits |
| <img src="https://cdn.simpleicons.org/fastapi/009688" width="22"> | `fastapi` / `uvicorn` | Python Worker | typed HTTP Worker |
| <img src="https://www.google.com/s2/favicons?domain=prisma.io&sz=64" width="22"> | `prisma` | Voice Agent | strukturierter DB-Zugriff |
| <img src="https://cdn.simpleicons.org/zod/3E67B1" width="22"> | `zod` / `@trpc/*` | lokale APIs | typisierte Contracts |
| <img src="https://cdn.simpleicons.org/redis/DC382D" width="22"> | `ioredis` / `fastq` / `cron` | Jobs | Queues, Scheduler, Backpressure |
| <img src="https://cdn.simpleicons.org/rust/000000" width="22"> | `axum` / `tokio` / `tower` | Rust APIs | robuste lokale Gateways |

## 🎙️ Voice, Medien und ASR

| Logo | Paket / Tool | Wird genutzt in | Zweck |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/discord/5865F2" width="22"> | `eris` / `slash-create` / `discord.py` | Discord Voice Agent | Text/Voice Bot |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="22"> | `faster-whisper` / `sherpa-onnx` | Transcriber Worker | lokale Speech-to-Text Optionen |
| <img src="https://www.google.com/s2/favicons?domain=sharp.pixelplumbing.com&sz=64" width="22"> | `sharp` | Beeper/Matrix Proxy | Medien- und Avatar-Verarbeitung |
| <img src="https://www.google.com/s2/favicons?domain=yt-dlp.org&sz=64" width="22"> | `yt-dlp` | YouTube Importer | Medienmetadaten |

## 🧠 Daten, Knowledge und Lifelog

| Logo | Paket / Tool | Wird genutzt in | Zweck |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/postgresql/4169E1" width="22"> | Postgres / `pgvector` | Memory/RAG | Agent-State, Audit, Embeddings |
| <img src="https://www.google.com/s2/favicons?domain=activitywatch.net&sz=64" width="22"> | ActivityWatch | Presence/Lifelog | Fokus, Apps, Web, Timeline |
| <img src="https://cdn.simpleicons.org/obsidian/7C3AED" width="22"> | Obsidian Dataview / Git | Vault | Queries und Versionierung |
| <img src="https://cdn.simpleicons.org/python/3776AB" width="22"> | `click` / `httpx` / `pytest` / `ruff` | Importer | robuste lokale CLIs und Tests |

## 📬 Matrix, Bridges und Mail

| Logo | Paket / Tool | Wird genutzt in | Zweck |
|---|---|---|---|
| <img src="https://cdn.simpleicons.org/matrix/000000" width="22"> | Synapse / Tuwunel | Matrix Core | Homeserver |
| <img src="https://www.google.com/s2/favicons?domain=matrix.org&sz=64" width="22"> | `mautrix/python` / `mautrix-go` | Bot/Bridges | Matrix SDK und Appservices |
| <img src="https://www.google.com/s2/favicons?domain=pimalaya.org&sz=64" width="22"> | Himalaya / mbsync / notmuch | E-Mail | lokale Inbox und Suche |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="22"> | Mailpit | Mail Dev/Ops | sicherer lokaler SMTP-Test |

## 📊 Observability und Qualitaet

| Logo | Paket / Tool | Wird genutzt in | Zweck |
|---|---|---|---|
| <img src="https://www.google.com/s2/favicons?domain=opentelemetry.io&sz=64" width="22"> | OpenTelemetry Collector | Ops | Traces und Metriken |
| <img src="https://cdn.simpleicons.org/prometheus/E6522C" width="22"> | Prometheus | Ops | Metriken und Alerts |
| <img src="https://cdn.simpleicons.org/grafana/F46800" width="22"> | Loki / Grafana | Ops | Logs und Dashboards |
| <img src="https://cdn.simpleicons.org/sentry/362D59" width="22"> | `@sentry/node` | Node Services | Fehlerberichte |
