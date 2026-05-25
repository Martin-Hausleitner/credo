# GitHub-Repository-Matrix

Diese Matrix erweitert die lokale Repo-Inventur um Live-Metadaten von GitHub: Owner/Macher, Stars, Sprache, Sichtbarkeit, Kategorie und Credo-Wichtigkeit. Quelle sind alle GitHub-Links, die aktuell in README und `docs/` vorkommen.

Stand: 2026-05-26. Geprueft: **121** GitHub-Repositories, davon **120** per API erreichbar. Stars sind Momentaufnahmen aus der GitHub API.

## Legende

| Wichtigkeit | Bedeutung |
|---|---|
| 🔥 Core | Direkt fuer den Credo-MVP oder die zentrale Architektur notwendig. |
| ⭐ Wichtig | Sehr relevanter Baustein fuer Ausbau, eigene Repos oder klare Zielphase. |
| 🧩 Lokal beteiligt | Lokal vorhanden und praktisch wichtig, aber nicht zwingend Core. |
| 🔎 Referenz | Upstream, Vergleich, SDK, Client oder Implementierungsreferenz. |
| 📦 Lokal/Vendor | Installierte Skill-/Vendor-/Worktree-Referenz. |
| 🧪 Optional | Spaetere Idee, Experiment oder Randbaustein. |
| ⚠️ Unavailable | Link steht in der Doku, war aber per API nicht erreichbar. |

## Top nach GitHub-Stars

| Logo | Repo | Macher | Stars | Sprache | Wichtigkeit | Credo-Zusammenhang |
|---|---|---|---:|---|---|---|
| <img src="https://github.com/openclaw.png?size=32" width="24"> | [openclaw/openclaw](https://github.com/openclaw/openclaw) | [openclaw](https://github.com/openclaw) | 374,620 | TypeScript | 🔥 Core | Lokaler Skill-, Tool- und Agentenlayer. |
| <img src="https://github.com/obra.png?size=32" width="24"> | [obra/superpowers](https://github.com/obra/superpowers) | [obra](https://github.com/obra) | 206,254 | Shell | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. |
| <img src="https://github.com/NousResearch.png?size=32" width="24"> | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | [NousResearch](https://github.com/NousResearch) | 167,171 | Python | 🔥 Core | Agent-Orchestrator fuer Sessions, Skills, Memory und Automationen. |
| <img src="https://github.com/anthropics.png?size=32" width="24"> | [anthropics/skills](https://github.com/anthropics/skills) | [anthropics](https://github.com/anthropics) | 140,665 | Python | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. |
| <img src="https://github.com/supabase.png?size=32" width="24"> | [supabase/supabase](https://github.com/supabase/supabase) | [supabase](https://github.com/supabase) | 103,009 | TypeScript | 🔥 Core | Optionaler Dashboard/Auth/Realtime-Beschleuniger. |
| <img src="https://github.com/redis.png?size=32" width="24"> | [redis/redis](https://github.com/redis/redis) | [redis](https://github.com/redis) | 74,546 | C | 🔥 Core | Queue, Cache, Job-Status und Backpressure. |
| <img src="https://github.com/grafana.png?size=32" width="24"> | [grafana/grafana](https://github.com/grafana/grafana) | [grafana](https://github.com/grafana) | 73,991 | TypeScript | 🔥 Core | Observability fuer Logs, Metriken, Traces und Alerts. |
| <img src="https://github.com/wshobson.png?size=32" width="24"> | [wshobson/agents](https://github.com/wshobson/agents) | [wshobson](https://github.com/wshobson) | 35,940 | Python | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. |
| <img src="https://github.com/tailscale.png?size=32" width="24"> | [tailscale/tailscale](https://github.com/tailscale/tailscale) | [tailscale](https://github.com/tailscale) | 31,931 | Go | 🔥 Core | Private Admin-Schicht fuer interne Dashboards und APIs. |
| <img src="https://github.com/chatwoot.png?size=32" width="24"> | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | [chatwoot](https://github.com/chatwoot) | 29,725 | Ruby | 🔥 Core | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. |
| <img src="https://github.com/wandb.png?size=32" width="24"> | [wandb/openui](https://github.com/wandb/openui) | [wandb](https://github.com/wandb) | 22,331 | TypeScript | 🧪 Optional | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. |
| <img src="https://github.com/pgvector.png?size=32" width="24"> | [pgvector/pgvector](https://github.com/pgvector/pgvector) | [pgvector](https://github.com/pgvector) | 21,469 | C | 🔥 Core | Embedding-Suche und RAG direkt in Postgres. |
| <img src="https://github.com/postgres.png?size=32" width="24"> | [postgres/postgres](https://github.com/postgres/postgres) | [postgres](https://github.com/postgres) | 21,021 | C | 🔥 Core | Core-Datenbank fuer Agent-State, Audit und App-Daten. |
| <img src="https://github.com/vercel-labs.png?size=32" width="24"> | [vercel-labs/skills](https://github.com/vercel-labs/skills) | [vercel-labs](https://github.com/vercel-labs) | 20,036 | TypeScript | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. |
| <img src="https://github.com/livekit.png?size=32" width="24"> | [livekit/livekit](https://github.com/livekit/livekit) | [livekit](https://github.com/livekit) | 18,886 | Go | ⭐ Wichtig | Voice/RTC/Streaming-Strang fuer spaetere MatrixRTC-Phase. |
| <img src="https://github.com/ActivityWatch.png?size=32" width="24"> | [ActivityWatch/activitywatch](https://github.com/ActivityWatch/activitywatch) | [ActivityWatch](https://github.com/ActivityWatch) | 17,674 | Python | 🔥 Core | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. |
| <img src="https://github.com/Rapptz.png?size=32" width="24"> | [Rapptz/discord.py](https://github.com/Rapptz/discord.py) | [Rapptz](https://github.com/Rapptz) | 16,069 | Python | 🔎 Referenz | Voice-, Recording-, ASR- oder Audio-Agent-Referenz. |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/element-web](https://github.com/element-hq/element-web) | [element-hq](https://github.com/element-hq) | 13,137 | TypeScript | 🔥 Core | Referenzclient fuer Admin, Debugging und Kompatibilitaet. |
| <img src="https://github.com/jackyzha0.png?size=32" width="24"> | [jackyzha0/quartz](https://github.com/jackyzha0/quartz) | [jackyzha0](https://github.com/jackyzha0) | 12,277 | TypeScript | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. |
| <img src="https://github.com/Vinzent03.png?size=32" width="24"> | [Vinzent03/obsidian-git](https://github.com/Vinzent03/obsidian-git) | [Vinzent03](https://github.com/Vinzent03) | 11,040 | TypeScript | 🔥 Core | Knowledge Vault, Markdown-Abfragen und Git-Audit. |
| <img src="https://github.com/vrtmrz.png?size=32" width="24"> | [vrtmrz/obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync) | [vrtmrz](https://github.com/vrtmrz) | 10,977 | TypeScript | 🔎 Referenz | Knowledge Vault, Markdown-Abfragen und Git-Audit. |
| <img src="https://github.com/livekit.png?size=32" width="24"> | [livekit/agents](https://github.com/livekit/agents) | [livekit](https://github.com/livekit) | 10,681 | Python | ⭐ Wichtig | Voice/RTC/Streaming-Strang fuer spaetere MatrixRTC-Phase. |
| <img src="https://github.com/blacksmithgu.png?size=32" width="24"> | [blacksmithgu/obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview) | [blacksmithgu](https://github.com/blacksmithgu) | 8,990 | TypeScript | 🔥 Core | Knowledge Vault, Markdown-Abfragen und Git-Audit. |
| <img src="https://github.com/openclaw.png?size=32" width="24"> | [openclaw/clawhub](https://github.com/openclaw/clawhub) | [openclaw](https://github.com/openclaw) | 8,764 | TypeScript | 🔥 Core | Lokaler Skill-, Tool- und Agentenlayer. |
| <img src="https://github.com/remotely-save.png?size=32" width="24"> | [remotely-save/remotely-save](https://github.com/remotely-save/remotely-save) | [remotely-save](https://github.com/remotely-save) | 7,531 | TypeScript | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. |

## Kategorien

| Kategorie | Repos | Core/Wichtig |
|---|---:|---:|
| 🟢 Matrix / Messaging | 40 | 28 |
| 🤖 Agents / Skills | 18 | 9 |
| 🧑‍💻 Coding Agents | 1 | 1 |
| 📈 ActivityWatch / Health / Context | 9 | 7 |
| 🧠 Knowledge / Obsidian | 7 | 3 |
| 🎙️ Voice / Audio / RTC | 5 | 3 |
| 📊 Ops / Observability | 2 | 2 |
| 💼 Business / Finance | 4 | 0 |
| 🧪 Web / Product / UI | 6 | 0 |
| 🌐 Browser / Proxy / Scraping | 4 | 0 |
| 🍎 Apple / Device | 3 | 0 |
| 🔬 Other / Research | 18 | 9 |
| 📦 Local / Vendor / References | 4 | 0 |

## 🟢 Matrix / Messaging

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/element-web](https://github.com/element-hq/element-web) | [element-hq](https://github.com/element-hq) | 13,137 | TypeScript | public | 🔥 Core | Referenzclient fuer Admin, Debugging und Kompatibilitaet. | cognitor-widget-sharing.md, Matrix Map, Service-Katalog, Vergleich |
| <img src="https://github.com/spantaleev.png?size=32" width="24"> | [spantaleev/matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy) | [spantaleev](https://github.com/spantaleev) | 6,370 | Jinja | public | 🔥 Core | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/synapse](https://github.com/element-hq/synapse) | [element-hq](https://github.com/element-hq) | 4,227 | Python | public | 🔥 Core | Konservativer Matrix-Homeserver fuer den MVP. | Matrix Map, Service-Katalog, Vergleich |
| <img src="https://github.com/cinnyapp.png?size=32" width="24"> | [cinnyapp/cinny](https://github.com/cinnyapp/cinny) | [cinnyapp](https://github.com/cinnyapp) | 3,673 | TypeScript | public | 🔥 Core | Discord-artige Matrix-UX fuer Agentenraeume. | Matrix Map, Service-Katalog, Vergleich |
| <img src="https://github.com/matrix-org.png?size=32" width="24"> | [matrix-org/matrix-rust-sdk](https://github.com/matrix-org/matrix-rust-sdk) | [matrix-org](https://github.com/matrix-org) | 2,133 | Rust | public | 🔥 Core | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | cognitor-widget-sharing.md, Matrix Map |
| <img src="https://github.com/matrix-construct.png?size=32" width="24"> | [matrix-construct/tuwunel](https://github.com/matrix-construct/tuwunel) | [matrix-construct](https://github.com/matrix-construct) | 2,119 | Rust | public | 🔥 Core | Leichter Homeserver-Kandidat fuer RAM/S3-orientierten Betrieb. | Matrix Map, Service-Katalog, Vergleich |
| <img src="https://github.com/matrix-org.png?size=32" width="24"> | [matrix-org/matrix-spec](https://github.com/matrix-org/matrix-spec) | [matrix-org](https://github.com/matrix-org) | 306 | HTML | public | 🔥 Core | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/python](https://github.com/mautrix/python) | [mautrix](https://github.com/mautrix) | 242 | Python | public | 🔥 Core | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map |
| <img src="https://github.com/SableClient.png?size=32" width="24"> | [SableClient/Sable](https://github.com/SableClient/Sable) | [SableClient](https://github.com/SableClient) | 212 | TypeScript | public | 🔥 Core | Discord-artige Matrix-UX fuer Agentenraeume. | Matrix Map, Service-Katalog, Vergleich |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/Credo](https://github.com/Martin-Hausleitner/Credo) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | - | private | 🔥 Core | Zentrales Architekturdeck und Repo fuer den Credo-Stack. | README, lokal, Matrix Map, Repo-Map, Service-Katalog |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/element-x-android](https://github.com/element-hq/element-x-android) | [element-hq](https://github.com/element-hq) | 2,169 | Kotlin | public | ⭐ Wichtig | Matrix-2.0 Mobile-Pfad mit Rust SDK, Sliding Sync und OIDC. | Matrix Map, Vergleich |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/whatsapp](https://github.com/mautrix/whatsapp) | [mautrix](https://github.com/mautrix) | 1,779 | Go | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map, Vergleich |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/telegram](https://github.com/mautrix/telegram) | [mautrix](https://github.com/mautrix) | 1,689 | Go | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map, Vergleich |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/element-desktop](https://github.com/element-hq/element-desktop) | [element-hq](https://github.com/element-hq) | 1,488 | TypeScript | public, archived | ⭐ Wichtig | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map, Vergleich |
| <img src="https://github.com/matrix-org.png?size=32" width="24"> | [matrix-org/matrix-spec-proposals](https://github.com/matrix-org/matrix-spec-proposals) | [matrix-org](https://github.com/matrix-org) | 1,225 | - | public | ⭐ Wichtig | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/element-call](https://github.com/element-hq/element-call) | [element-hq](https://github.com/element-hq) | 952 | TypeScript | public | ⭐ Wichtig | Voice/RTC/Streaming-Strang fuer spaetere MatrixRTC-Phase. | Matrix Map, Vergleich |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/dendrite](https://github.com/element-hq/dendrite) | [element-hq](https://github.com/element-hq) | 919 | Go | public | ⭐ Wichtig | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map, Vergleich |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/element-x-ios](https://github.com/element-hq/element-x-ios) | [element-hq](https://github.com/element-hq) | 861 | Swift | public | ⭐ Wichtig | Matrix-2.0 Mobile-Pfad mit Rust SDK, Sliding Sync und OIDC. | Matrix Map, Vergleich |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/signal](https://github.com/mautrix/signal) | [mautrix](https://github.com/mautrix) | 647 | Go | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map, Vergleich |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/discord](https://github.com/mautrix/discord) | [mautrix](https://github.com/mautrix) | 459 | Go | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map, Vergleich |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/meta](https://github.com/mautrix/meta) | [mautrix](https://github.com/mautrix) | 373 | Go | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map, Vergleich |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/matrix-authentication-service](https://github.com/element-hq/matrix-authentication-service) | [element-hq](https://github.com/element-hq) | 253 | Rust | public | ⭐ Wichtig | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/gmessages](https://github.com/mautrix/gmessages) | [mautrix](https://github.com/mautrix) | 147 | Go | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map, Vergleich |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/slack](https://github.com/mautrix/slack) | [mautrix](https://github.com/mautrix) | 97 | Go | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map, Vergleich |
| <img src="https://github.com/matrix-org.png?size=32" width="24"> | [matrix-org/matrix-widget-api](https://github.com/matrix-org/matrix-widget-api) | [matrix-org](https://github.com/matrix-org) | 92 | TypeScript | public | ⭐ Wichtig | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | cognitor-widget-sharing.md, Matrix Map |
| <img src="https://github.com/element-hq.png?size=32" width="24"> | [element-hq/lk-jwt-service](https://github.com/element-hq/lk-jwt-service) | [element-hq](https://github.com/element-hq) | 89 | Go | public | ⭐ Wichtig | Voice/RTC/Streaming-Strang fuer spaetere MatrixRTC-Phase. | Matrix Map, Vergleich |
| <img src="https://github.com/mautrix.png?size=32" width="24"> | [mautrix/manager](https://github.com/mautrix/manager) | [mautrix](https://github.com/mautrix) | 48 | TypeScript | public | ⭐ Wichtig | Bridge-, Bot- oder SDK-Pfad fuer Matrix-Appservices. | Matrix Map |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/beeper-matrix-proxy](https://github.com/Martin-Hausleitner/beeper-matrix-proxy) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 2 | Go | public | ⭐ Wichtig | Bridge-Referenz fuer Beeper/Matrix-Portale und Appservice-Betrieb. | lokal, Matrix Map, Repo-Map, Service-Katalog |
| <img src="https://github.com/beeper.png?size=32" width="24"> | [beeper/bridge-manager](https://github.com/beeper/bridge-manager) | [beeper](https://github.com/beeper) | 1,335 | Go | public | 🧩 Lokal beteiligt | Bridge-Referenz fuer Beeper/Matrix-Portale und Appservice-Betrieb. | lokal, Repo-Map |
| <img src="https://github.com/krille-chan.png?size=32" width="24"> | [krille-chan/fluffychat](https://github.com/krille-chan/fluffychat) | [krille-chan](https://github.com/krille-chan) | 2,815 | Dart | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map, Vergleich |
| <img src="https://github.com/Nheko-Reborn.png?size=32" width="24"> | [Nheko-Reborn/nheko](https://github.com/Nheko-Reborn/nheko) | [Nheko-Reborn](https://github.com/Nheko-Reborn) | 2,423 | C++ | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map, Vergleich |
| <img src="https://github.com/maubot.png?size=32" width="24"> | [maubot/maubot](https://github.com/maubot/maubot) | [maubot](https://github.com/maubot) | 877 | Python | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |
| <img src="https://github.com/cinnyapp.png?size=32" width="24"> | [cinnyapp/cinny-desktop](https://github.com/cinnyapp/cinny-desktop) | [cinnyapp](https://github.com/cinnyapp) | 784 | JavaScript | public | 🔎 Referenz | Discord-artige Matrix-UX fuer Agentenraeume. | Matrix Map, Vergleich |
| <img src="https://github.com/ConduitIO.png?size=32" width="24"> | [ConduitIO/conduit](https://github.com/ConduitIO/conduit) | [ConduitIO](https://github.com/ConduitIO) | 597 | Go | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map, Vergleich |
| <img src="https://github.com/etkecc.png?size=32" width="24"> | [etkecc/synapse-admin](https://github.com/etkecc/synapse-admin) | [etkecc](https://github.com/etkecc) | 406 | TypeScript | public | 🔎 Referenz | Konservativer Matrix-Homeserver fuer den MVP. | Matrix Map |
| <img src="https://github.com/matrix-construct.png?size=32" width="24"> | [matrix-construct/construct](https://github.com/matrix-construct/construct) | [matrix-construct](https://github.com/matrix-construct) | 395 | C++ | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map, Vergleich |
| <img src="https://github.com/the-draupnir-project.png?size=32" width="24"> | [the-draupnir-project/Draupnir](https://github.com/the-draupnir-project/Draupnir) | [the-draupnir-project](https://github.com/the-draupnir-project) | 235 | TypeScript | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |
| <img src="https://github.com/etkecc.png?size=32" width="24"> | [etkecc/baibot](https://github.com/etkecc/baibot) | [etkecc](https://github.com/etkecc) | 227 | Rust | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |
| <img src="https://github.com/matrix-org.png?size=32" width="24"> | [matrix-org/synapse-s3-storage-provider](https://github.com/matrix-org/synapse-s3-storage-provider) | [matrix-org](https://github.com/matrix-org) | 197 | Python | public | 🔎 Referenz | Konservativer Matrix-Homeserver fuer den MVP. | Matrix Map |
| <img src="https://github.com/matrix-org.png?size=32" width="24"> | [matrix-org/matrix-appservice-bridge](https://github.com/matrix-org/matrix-appservice-bridge) | [matrix-org](https://github.com/matrix-org) | 182 | TypeScript | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map |

## 🤖 Agents / Skills

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/openclaw.png?size=32" width="24"> | [openclaw/openclaw](https://github.com/openclaw/openclaw) | [openclaw](https://github.com/openclaw) | 374,620 | TypeScript | public | 🔥 Core | Lokaler Skill-, Tool- und Agentenlayer. | Service-Katalog, Vergleich |
| <img src="https://github.com/NousResearch.png?size=32" width="24"> | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | [NousResearch](https://github.com/NousResearch) | 167,171 | Python | public | 🔥 Core | Agent-Orchestrator fuer Sessions, Skills, Memory und Automationen. | Service-Katalog, Vergleich |
| <img src="https://github.com/openclaw.png?size=32" width="24"> | [openclaw/clawhub](https://github.com/openclaw/clawhub) | [openclaw](https://github.com/openclaw) | 8,764 | TypeScript | public | 🔥 Core | Lokaler Skill-, Tool- und Agentenlayer. | Vergleich |
| <img src="https://github.com/livekit.png?size=32" width="24"> | [livekit/agents](https://github.com/livekit/agents) | [livekit](https://github.com/livekit) | 10,681 | Python | public | ⭐ Wichtig | Voice/RTC/Streaming-Strang fuer spaetere MatrixRTC-Phase. | Matrix Map, Vergleich |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/discord-voice-obsidian-agent](https://github.com/Martin-Hausleitner/discord-voice-obsidian-agent) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | TypeScript | private | ⭐ Wichtig | Knowledge Vault, Markdown-Abfragen und Git-Audit. | lokal, Matrix Map, Repo-Map, Service-Katalog |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/martins-awesome-skills](https://github.com/Martin-Hausleitner/martins-awesome-skills) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | public | ⭐ Wichtig | Eigene public-safe Hermes/OpenClaw Skill-Sammlung. | lokal, Matrix Map, Repo-Map, Service-Katalog |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/openclaw-apple-findmy-skill](https://github.com/Martin-Hausleitner/openclaw-apple-findmy-skill) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | public | ⭐ Wichtig | Lokaler Skill-, Tool- und Agentenlayer. | lokal, Repo-Map |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/openclaw-workspace](https://github.com/Martin-Hausleitner/openclaw-workspace) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | private | ⭐ Wichtig | Lokaler Skill-, Tool- und Agentenlayer. | lokal, Repo-Map |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/sonar-skills](https://github.com/Martin-Hausleitner/sonar-skills) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | - | public | ⭐ Wichtig | Voice-, Recording-, ASR- oder Audio-Agent-Referenz. | lokal |
| <img src="https://github.com/farzaa.png?size=32" width="24"> | [farzaa/clicky](https://github.com/farzaa/clicky) | [farzaa](https://github.com/farzaa) | 6,112 | Swift | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/moritzWa.png?size=32" width="24"> | [moritzWa/cronus](https://github.com/moritzWa/cronus) | [moritzWa](https://github.com/moritzWa) | 116 | TypeScript | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/fintaro-ai.png?size=32" width="24"> | [fintaro-ai/Fintaro-Agent](https://github.com/fintaro-ai/Fintaro-Agent) | [fintaro-ai](https://github.com/fintaro-ai) | 0 | Python | private | 🧩 Lokal beteiligt | Business-, Finance-, Gateway- oder Creator-Tooling im erweiterten Portfolio. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/eins](https://github.com/Martin-Hausleitner/eins) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | - | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/Fintaro-Agent](https://github.com/servas-ai/Fintaro-Agent) | [servas-ai](https://github.com/servas-ai) | 0 | Python | private | 🧩 Lokal beteiligt | Business-, Finance-, Gateway- oder Creator-Tooling im erweiterten Portfolio. | lokal |
| <img src="https://github.com/openai.png?size=32" width="24"> | [openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents) | [openai](https://github.com/openai) | 6,877 | TypeScript | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Service-Katalog, Vergleich |
| <img src="https://github.com/snyk.png?size=32" width="24"> | [snyk/agent-scan](https://github.com/snyk/agent-scan) | [snyk](https://github.com/snyk) | 2,472 | Python | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Vergleich |
| <img src="https://github.com/joelhooks.png?size=32" width="24"> | [joelhooks/agent-secrets](https://github.com/joelhooks/agent-secrets) | [joelhooks](https://github.com/joelhooks) | 78 | Go | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Vergleich |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/hermes-agent](https://github.com/Martin-Hausleitner/hermes-agent) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | private | 🧪 Optional | Agent-Orchestrator fuer Sessions, Skills, Memory und Automationen. | Repo-Map |

## 🧑‍💻 Coding Agents

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/codex-computer-use-eu-activate](https://github.com/Martin-Hausleitner/codex-computer-use-eu-activate) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 1 | Shell | public | ⭐ Wichtig | Native UI-Automation und Codex-Computer-Use-Aktivierung. | lokal, Repo-Map |

## 📈 ActivityWatch / Health / Context

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/ActivityWatch.png?size=32" width="24"> | [ActivityWatch/activitywatch](https://github.com/ActivityWatch/activitywatch) | [ActivityWatch](https://github.com/ActivityWatch) | 17,674 | Python | public | 🔥 Core | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | Service-Katalog |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/aw-activitywatch-stack](https://github.com/Martin-Hausleitner/aw-activitywatch-stack) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | public | ⭐ Wichtig | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/aw-importer-apple-health](https://github.com/Martin-Hausleitner/aw-importer-apple-health) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | public | ⭐ Wichtig | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/aw-importer-apple-screentime](https://github.com/Martin-Hausleitner/aw-importer-apple-screentime) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | public | ⭐ Wichtig | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | lokal, Repo-Map |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/aw-importer-whoop](https://github.com/Martin-Hausleitner/aw-importer-whoop) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | public | ⭐ Wichtig | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | lokal, Repo-Map |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/aw-importer-youtube](https://github.com/Martin-Hausleitner/aw-importer-youtube) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | JavaScript | public | ⭐ Wichtig | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | lokal, Repo-Map |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/aw-john-harris-wifi](https://github.com/Martin-Hausleitner/aw-john-harris-wifi) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | private | ⭐ Wichtig | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | lokal, Repo-Map |
| <img src="https://github.com/antonpk1.png?size=32" width="24"> | [antonpk1/excalidraw-mcp-app](https://github.com/antonpk1/excalidraw-mcp-app) | [antonpk1](https://github.com/antonpk1) | 4,544 | TypeScript | public | 🧩 Lokal beteiligt | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/excalidraw-mcp-app](https://github.com/Martin-Hausleitner/excalidraw-mcp-app) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | - | public | 🧪 Optional | Lifelog, Fokus, Health, Medien- oder Presence-Kontext. | Repo-Map |

## 🧠 Knowledge / Obsidian

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/Vinzent03.png?size=32" width="24"> | [Vinzent03/obsidian-git](https://github.com/Vinzent03/obsidian-git) | [Vinzent03](https://github.com/Vinzent03) | 11,040 | TypeScript | public | 🔥 Core | Knowledge Vault, Markdown-Abfragen und Git-Audit. | Vergleich |
| <img src="https://github.com/blacksmithgu.png?size=32" width="24"> | [blacksmithgu/obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview) | [blacksmithgu](https://github.com/blacksmithgu) | 8,990 | TypeScript | public | 🔥 Core | Knowledge Vault, Markdown-Abfragen und Git-Audit. | Service-Katalog, Vergleich |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/obsidian-notion-ui-customization](https://github.com/Martin-Hausleitner/obsidian-notion-ui-customization) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | - | public | ⭐ Wichtig | Knowledge Vault, Markdown-Abfragen und Git-Audit. | lokal, Repo-Map |
| <img src="https://github.com/jackyzha0.png?size=32" width="24"> | [jackyzha0/quartz](https://github.com/jackyzha0/quartz) | [jackyzha0](https://github.com/jackyzha0) | 12,277 | TypeScript | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Vergleich |
| <img src="https://github.com/vrtmrz.png?size=32" width="24"> | [vrtmrz/obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync) | [vrtmrz](https://github.com/vrtmrz) | 10,977 | TypeScript | public | 🔎 Referenz | Knowledge Vault, Markdown-Abfragen und Git-Audit. | Vergleich |
| <img src="https://github.com/remotely-save.png?size=32" width="24"> | [remotely-save/remotely-save](https://github.com/remotely-save/remotely-save) | [remotely-save](https://github.com/remotely-save) | 7,531 | TypeScript | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Vergleich |
| <img src="https://github.com/brianpetro.png?size=32" width="24"> | [brianpetro/obsidian-smart-connections](https://github.com/brianpetro/obsidian-smart-connections) | [brianpetro](https://github.com/brianpetro) | 5,037 | JavaScript | public | 🔎 Referenz | Knowledge Vault, Markdown-Abfragen und Git-Audit. | Vergleich |

## 🎙️ Voice / Audio / RTC

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/livekit.png?size=32" width="24"> | [livekit/livekit](https://github.com/livekit/livekit) | [livekit](https://github.com/livekit) | 18,886 | Go | public | ⭐ Wichtig | Voice/RTC/Streaming-Strang fuer spaetere MatrixRTC-Phase. | Matrix Map, Service-Katalog, Vergleich |
| <img src="https://github.com/livekit.png?size=32" width="24"> | [livekit/egress](https://github.com/livekit/egress) | [livekit](https://github.com/livekit) | 336 | Go | public | ⭐ Wichtig | Voice/RTC/Streaming-Strang fuer spaetere MatrixRTC-Phase. | Matrix Map, Vergleich |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/Sonar](https://github.com/Martin-Hausleitner/Sonar) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Swift | public | ⭐ Wichtig | Voice-, Recording-, ASR- oder Audio-Agent-Referenz. | lokal |
| <img src="https://github.com/CraigChat.png?size=32" width="24"> | [CraigChat/craig](https://github.com/CraigChat/craig) | [CraigChat](https://github.com/CraigChat) | 525 | TypeScript | public | 🧩 Lokal beteiligt | Voice-, Recording-, ASR- oder Audio-Agent-Referenz. | lokal |
| <img src="https://github.com/Rapptz.png?size=32" width="24"> | [Rapptz/discord.py](https://github.com/Rapptz/discord.py) | [Rapptz](https://github.com/Rapptz) | 16,069 | Python | public | 🔎 Referenz | Voice-, Recording-, ASR- oder Audio-Agent-Referenz. | Vergleich |

## 📊 Ops / Observability

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/grafana.png?size=32" width="24"> | [grafana/grafana](https://github.com/grafana/grafana) | [grafana](https://github.com/grafana) | 73,991 | TypeScript | public | 🔥 Core | Observability fuer Logs, Metriken, Traces und Alerts. | Service-Katalog |
| <img src="https://github.com/tailscale.png?size=32" width="24"> | [tailscale/tailscale](https://github.com/tailscale/tailscale) | [tailscale](https://github.com/tailscale) | 31,931 | Go | public | 🔥 Core | Private Admin-Schicht fuer interne Dashboards und APIs. | Service-Katalog |

## 💼 Business / Finance

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/OFAuth-org.png?size=32" width="24"> | [OFAuth-org/onlyfans-sdk-typescript](https://github.com/OFAuth-org/onlyfans-sdk-typescript) | [OFAuth-org](https://github.com/OFAuth-org) | 1 | TypeScript | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/MoneyMaker.Workspace](https://github.com/servas-ai/MoneyMaker.Workspace) | [servas-ai](https://github.com/servas-ai) | 1 | C# | private | 🧩 Lokal beteiligt | Business-, Finance-, Gateway- oder Creator-Tooling im erweiterten Portfolio. | lokal |
| <img src="https://github.com/fintaro-ai.png?size=32" width="24"> | [fintaro-ai/fintaro-logo-maker](https://github.com/fintaro-ai/fintaro-logo-maker) | [fintaro-ai](https://github.com/fintaro-ai) | 0 | TypeScript | public | 🧩 Lokal beteiligt | Business-, Finance-, Gateway- oder Creator-Tooling im erweiterten Portfolio. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/onlyapi](https://github.com/servas-ai/onlyapi) | [servas-ai](https://github.com/servas-ai) | 0 | Rust | private | 🧩 Lokal beteiligt | Business-, Finance-, Gateway- oder Creator-Tooling im erweiterten Portfolio. | lokal |

## 🧪 Web / Product / UI

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/erginstudio.png?size=32" width="24"> | [erginstudio/website-clone](https://github.com/erginstudio/website-clone) | [erginstudio](https://github.com/erginstudio) | 0 | HTML | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/company-network-viz](https://github.com/Martin-Hausleitner/company-network-viz) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | TypeScript | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/angebot-servas.ai-generator](https://github.com/servas-ai/angebot-servas.ai-generator) | [servas-ai](https://github.com/servas-ai) | 0 | TypeScript | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/ergin.studio-clone](https://github.com/servas-ai/ergin.studio-clone) | [servas-ai](https://github.com/servas-ai) | 0 | HTML | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/Roadmap-Builder-v2](https://github.com/servas-ai/Roadmap-Builder-v2) | [servas-ai](https://github.com/servas-ai) | 0 | TypeScript | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/wandb.png?size=32" width="24"> | [wandb/openui](https://github.com/wandb/openui) | [wandb](https://github.com/wandb) | 22,331 | TypeScript | public | 🧪 Optional | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | cognitor-widget-sharing.md |

## 🌐 Browser / Proxy / Scraping

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/patrik-proxy-research](https://github.com/servas-ai/patrik-proxy-research) | [servas-ai](https://github.com/servas-ai) | 0 | - | private | 🧩 Lokal beteiligt | Proxy-, Browser- oder Scraping-Referenz. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/proxychecker](https://github.com/servas-ai/proxychecker) | [servas-ai](https://github.com/servas-ai) | 0 | Python | private | 🧩 Lokal beteiligt | Proxy-, Browser- oder Scraping-Referenz. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/browser-use-mcp-plus](https://github.com/Martin-Hausleitner/browser-use-mcp-plus) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | public | 🧪 Optional | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Repo-Map |
| <img src="https://github.com/router-for-me.png?size=32" width="24"> | `router-for-me/CLIProxyAPIPlus` | [router-for-me](https://github.com/router-for-me) | n/a | - | not reachable | ⚠️ Unavailable | Proxy-, Browser- oder Scraping-Referenz. | lokal |

## 🍎 Apple / Device

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/timi2506.png?size=32" width="24"> | [timi2506/iphone-mirroring-eu-activate](https://github.com/timi2506/iphone-mirroring-eu-activate) | [timi2506](https://github.com/timi2506) | 136 | Python | public | 🧩 Lokal beteiligt | Apple-/iPhone-Mirroring-/Device-Referenz. | lokal |
| <img src="https://github.com/Pauli1Go.png?size=32" width="24"> | [Pauli1Go/iphone-mirroring-eu-enabler](https://github.com/Pauli1Go/iphone-mirroring-eu-enabler) | [Pauli1Go](https://github.com/Pauli1Go) | 88 | Python | public | 🧩 Lokal beteiligt | Apple-/iPhone-Mirroring-/Device-Referenz. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/iphone-mirroring-eu-guide](https://github.com/Martin-Hausleitner/iphone-mirroring-eu-guide) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Shell | public | 🧩 Lokal beteiligt | Apple-/iPhone-Mirroring-/Device-Referenz. | lokal |

## 🔬 Other / Research

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/supabase.png?size=32" width="24"> | [supabase/supabase](https://github.com/supabase/supabase) | [supabase](https://github.com/supabase) | 103,009 | TypeScript | public | 🔥 Core | Optionaler Dashboard/Auth/Realtime-Beschleuniger. | Service-Katalog |
| <img src="https://github.com/redis.png?size=32" width="24"> | [redis/redis](https://github.com/redis/redis) | [redis](https://github.com/redis) | 74,546 | C | public | 🔥 Core | Queue, Cache, Job-Status und Backpressure. | Service-Katalog |
| <img src="https://github.com/chatwoot.png?size=32" width="24"> | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | [chatwoot](https://github.com/chatwoot) | 29,725 | Ruby | public | 🔥 Core | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Service-Katalog |
| <img src="https://github.com/pgvector.png?size=32" width="24"> | [pgvector/pgvector](https://github.com/pgvector/pgvector) | [pgvector](https://github.com/pgvector) | 21,469 | C | public | 🔥 Core | Embedding-Suche und RAG direkt in Postgres. | Service-Katalog |
| <img src="https://github.com/postgres.png?size=32" width="24"> | [postgres/postgres](https://github.com/postgres/postgres) | [postgres](https://github.com/postgres) | 21,021 | C | public | 🔥 Core | Core-Datenbank fuer Agent-State, Audit und App-Daten. | Service-Katalog |
| <img src="https://github.com/pimalaya.png?size=32" width="24"> | [pimalaya/himalaya](https://github.com/pimalaya/himalaya) | [pimalaya](https://github.com/pimalaya) | 6,262 | Rust | public | 🔥 Core | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Service-Katalog |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/cognitor-launcher](https://github.com/Martin-Hausleitner/cognitor-launcher) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Shell | private | ⭐ Wichtig | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal, Repo-Map, Service-Katalog |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/mac-ai-dev-setup](https://github.com/Martin-Hausleitner/mac-ai-dev-setup) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | JavaScript | private | ⭐ Wichtig | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal, Repo-Map |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/mac-ram-rescue](https://github.com/Martin-Hausleitner/mac-ram-rescue) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Swift | private | ⭐ Wichtig | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal, Repo-Map |
| <img src="https://github.com/elder-plinius.png?size=32" width="24"> | [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | [elder-plinius](https://github.com/elder-plinius) | 6,757 | TypeScript | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/mac4n6.png?size=32" width="24"> | [mac4n6/APOLLO](https://github.com/mac4n6/APOLLO) | [mac4n6](https://github.com/mac4n6) | 645 | Python | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/rustem.png?size=32" width="24"> | [rustem/sense](https://github.com/rustem/sense) | [rustem](https://github.com/rustem) | 3 | Python | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/Martin-Hausleitner.png?size=32" width="24"> | [Martin-Hausleitner/clogwork](https://github.com/Martin-Hausleitner/clogwork) | [Martin-Hausleitner](https://github.com/Martin-Hausleitner) | 0 | Python | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/servas-ai.png?size=32" width="24"> | [servas-ai/tokenrouter-workspace](https://github.com/servas-ai/tokenrouter-workspace) | [servas-ai](https://github.com/servas-ai) | 0 | HTML | private | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/NousResearch.png?size=32" width="24"> | [NousResearch/atropos](https://github.com/NousResearch/atropos) | [NousResearch](https://github.com/NousResearch) | 1,228 | Python | public | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Vergleich |
| <img src="https://github.com/commetchat.png?size=32" width="24"> | [commetchat/commet](https://github.com/commetchat/commet) | [commetchat](https://github.com/commetchat) | 1,017 | Dart | public | 🔎 Referenz | Discord-artige Matrix-UX fuer Agentenraeume. | Matrix Map, Vergleich |
| <img src="https://github.com/girlbossceo.png?size=32" width="24"> | [girlbossceo/conduwuit](https://github.com/girlbossceo/conduwuit) | [girlbossceo](https://github.com/girlbossceo) | 21 | Rust | public, archived | 🔎 Referenz | Upstream-, Tooling- oder Vergleichsreferenz fuer den Credo-Stack. | Matrix Map, Vergleich |
| <img src="https://github.com/beeper.png?size=32" width="24"> | [beeper/platform-imessage](https://github.com/beeper/platform-imessage) | [beeper](https://github.com/beeper) | 14 | Swift | public | 🔎 Referenz | Bridge-Referenz fuer Beeper/Matrix-Portale und Appservice-Betrieb. | Matrix Map, Vergleich |

## 📦 Local / Vendor / References

| Logo | Repo | Macher | Stars | Sprache | Sichtbarkeit | Wichtigkeit | Credo-Zusammenhang | Quelle |
|---|---|---|---:|---|---|---|---|---|
| <img src="https://github.com/obra.png?size=32" width="24"> | [obra/superpowers](https://github.com/obra/superpowers) | [obra](https://github.com/obra) | 206,254 | Shell | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/anthropics.png?size=32" width="24"> | [anthropics/skills](https://github.com/anthropics/skills) | [anthropics](https://github.com/anthropics) | 140,665 | Python | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/wshobson.png?size=32" width="24"> | [wshobson/agents](https://github.com/wshobson/agents) | [wshobson](https://github.com/wshobson) | 35,940 | Python | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |
| <img src="https://github.com/vercel-labs.png?size=32" width="24"> | [vercel-labs/skills](https://github.com/vercel-labs/skills) | [vercel-labs](https://github.com/vercel-labs) | 20,036 | TypeScript | public | 🧩 Lokal beteiligt | Lokal vorhandenes Repo, das als Credo-Baustein oder Referenz erhalten bleibt. | lokal |

## ⚠️ Nicht erreichbar

| Repo | Fehler | Quelle |
|---|---|---|
| `router-for-me/CLIProxyAPIPlus` | gh: Not Found (HTTP 404) | lokal |

## Pflegehinweise

- Neue GitHub-Links zuerst in der passenden Fachdatei eintragen; diese Matrix kann danach neu generiert oder manuell erweitert werden.
- Stars sind nur ein Popularitaetsindikator. Die Credo-Wichtigkeit bewertet, ob ein Repo fuer Martins Stack praktisch wichtig ist.
- Owner-Avatare dienen als robuste Logos, weil Produktlogos/Favicons und GitHub OpenGraph-Previews bei grossen Tabellen drosseln koennen.
