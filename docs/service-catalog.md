# Service-Katalog: Icons, Screenshots, Webseiten und GitHub

Dieser Katalog ist die schnelle visuelle Karte: welches Programm ist was, wo ist die Website, wo ist GitHub, und was macht es in unserem Stack. Die Screenshot-Spalte nutzt bewusst stabile GitHub-OpenGraph-Previews oder offizielle Website-/Favicon-Assets, damit GitHub die Seite direkt rendern kann.

## Kernservices

| Icon | Screenshot / Preview | Service | Website | GitHub | Was es bei uns macht |
|---|---|---|---|---|---|
| <img src="https://www.google.com/s2/favicons?domain=matrix.org&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/element-hq/synapse" width="220"> | Matrix / Synapse | [matrix.org](https://matrix.org) | [element-hq/synapse](https://github.com/element-hq/synapse) | Konservativer Homeserver fuer maximale Kompatibilitaet, Admin-API, Bridges und Clients. |
| <img src="https://www.google.com/s2/favicons?domain=matrix.org&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/matrix-construct/tuwunel" width="220"> | Tuwunel | [matrix.org ecosystem](https://matrix.org/ecosystem/servers/) | [matrix-construct/tuwunel](https://github.com/matrix-construct/tuwunel) | Ressourcenschonender Greenfield-Homeserver fuer den 8GB/S3-orientierten Stack. |
| <img src="https://www.google.com/s2/favicons?domain=element.io&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/element-hq/element-web" width="220"> | Element Web | [element.io](https://element.io) | [element-hq/element-web](https://github.com/element-hq/element-web) | Referenzclient fuer Admin, Debugging, Features und Kompatibilitaet. |
| <img src="https://www.google.com/s2/favicons?domain=cinny.in&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/cinnyapp/cinny" width="220"> | Cinny | [cinny.in](https://cinny.in) | [cinnyapp/cinny](https://github.com/cinnyapp/cinny) | Schneller, ruhiger Webclient fuer Agent-Raeume und Discord-artige Channel-UX. |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/SableClient/Sable" width="220"> | Sable | [GitHub](https://github.com/SableClient/Sable) | [SableClient/Sable](https://github.com/SableClient/Sable) | Cinny-Fork fuer mehr QoL, Power-UX und experimentelle Komfortfeatures. |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/NousResearch/hermes-agent" width="220"> | Hermes Agent | [GitHub](https://github.com/NousResearch/hermes-agent) | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Haupt-Orchestrator fuer Agenten, Skills, Subagents, Memory, Gateway-Plattformen und Automationen. |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/openclaw/openclaw" width="220"> | OpenClaw | [GitHub](https://github.com/openclaw/openclaw) | [openclaw/openclaw](https://github.com/openclaw/openclaw) | Lokaler Tool-, Skill- und Automationslayer fuer persoenliche Agent-Faehigkeiten. |
| <img src="https://www.google.com/s2/favicons?domain=supabase.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/supabase/supabase" width="220"> | Supabase | [supabase.com](https://supabase.com) | [supabase/supabase](https://github.com/supabase/supabase) | Optionaler Beschleuniger fuer interne Hermes-Agent-Dashboards: Postgres, Auth, Realtime, Storage und Edge Functions. |
| <img src="https://www.google.com/s2/favicons?domain=postgresql.org&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/postgres/postgres" width="220"> | Postgres | [postgresql.org](https://www.postgresql.org) | [postgres/postgres](https://github.com/postgres/postgres) | Persistente DB fuer Audit, Agent-Jobs, Memory-Metadaten und App-Daten. |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/pgvector/pgvector" width="220"> | pgvector | [GitHub](https://github.com/pgvector/pgvector) | [pgvector/pgvector](https://github.com/pgvector/pgvector) | Vektor- und Embedding-Suche direkt in Postgres fuer RAG/Memory. |
| <img src="https://www.google.com/s2/favicons?domain=redis.io&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/redis/redis" width="220"> | Redis | [redis.io](https://redis.io) | [redis/redis](https://github.com/redis/redis) | Queue, Cache und Entkopplung zwischen Matrix Gateway und Agent-Workern. |
| <img src="https://www.google.com/s2/favicons?domain=cloudflare.com&sz=64" width="32"> | <img src="https://www.google.com/s2/favicons?domain=cloudflare.com&sz=128" width="80"> | Cloudflare R2 / S3 | [Cloudflare R2](https://www.cloudflare.com/developer-platform/products/r2/) | n/a | Artefakte, Medien, Exporte und grosse Dateien ohne lokales Storage-Volllaufen. |

## Agenten, Inbox und Knowledge

| Icon | Screenshot / Preview | Service | Website | GitHub | Was es bei uns macht |
|---|---|---|---|---|---|
| <img src="https://www.google.com/s2/favicons?domain=chatwoot.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/chatwoot/chatwoot" width="220"> | Chatwoot | [chatwoot.com](https://www.chatwoot.com) | [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | Operator-Inbox fuer E-Mail, Chat, Beeper/Matrix und Agent-Ops. |
| <img src="https://www.google.com/s2/favicons?domain=pimalaya.org&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/pimalaya/himalaya" width="220"> | Himalaya | [pimalaya.org](https://pimalaya.org) | [pimalaya/himalaya](https://github.com/pimalaya/himalaya) | E-Mail CLI fuer Lesen, Suchen, Antworten, Weiterleiten und Agent-Triage. |
| <img src="https://www.google.com/s2/favicons?domain=obsidian.md&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/blacksmithgu/obsidian-dataview" width="220"> | Obsidian + Dataview | [obsidian.md](https://obsidian.md) | [obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview) | Local-first Memory, Projektwissen, Properties, Tasks und strukturierte Queries. |
| <img src="https://www.google.com/s2/favicons?domain=activitywatch.net&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/ActivityWatch/activitywatch" width="220"> | ActivityWatch | [activitywatch.net](https://activitywatch.net) | [ActivityWatch/activitywatch](https://github.com/ActivityWatch/activitywatch) | Lokaler Fokus-, App-, Web- und Lifelog-Kontext fuer Agenten. |
| <img src="https://www.google.com/s2/favicons?domain=livekit.io&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/livekit/livekit" width="220"> | LiveKit | [livekit.io](https://livekit.io) | [livekit/livekit](https://github.com/livekit/livekit) | Spaeterer Voice/RTC/Streaming-Strang fuer MatrixRTC und Voice Agents. |
| <img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/openai/openai-realtime-agents" width="220"> | OpenAI Realtime Agents | [OpenAI Voice Agents](https://platform.openai.com/docs/guides/voice-agents) | [openai-realtime-agents](https://github.com/openai/openai-realtime-agents) | Schnellster Voice-MVP fuer niedrige Latenz, Tool Calls und Barge-in. |
| <img src="https://www.google.com/s2/favicons?domain=grafana.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/grafana/grafana" width="220"> | Grafana | [grafana.com](https://grafana.com) | [grafana/grafana](https://github.com/grafana/grafana) | Tailscale-only Dashboard fuer Agenten, Bridges, Kosten, Queues und Host-Health. |
| <img src="https://www.google.com/s2/favicons?domain=tailscale.com&sz=64" width="32"> | <img src="https://opengraph.githubassets.com/matrix-hermes-agent-stack/tailscale/tailscale" width="220"> | Tailscale | [tailscale.com](https://tailscale.com) | [tailscale/tailscale](https://github.com/tailscale/tailscale) | Private Admin- und Observability-Schicht ohne Public Dashboards. |

## Eigene GitHub-Anker

| Projekt | GitHub | Was es bei uns macht |
|---|---|---|
| Matrix Hermes Agent Stack | [matrix-hermes-agent-stack](https://github.com/Martin-Hausleitner/matrix-hermes-agent-stack) | Dieses Architekturdeck und Runbook. |
| Cognitor Launcher | [cognitor-launcher](https://github.com/Martin-Hausleitner/cognitor-launcher) | Persoenliche Web-/Tray-/Mobile-Agent-Oberflaechen. |
| Beeper Matrix Proxy | [beeper-matrix-proxy](https://github.com/Martin-Hausleitner/beeper-matrix-proxy) | Beeper/BIPA als Matrix-Portale und Bridge-Referenz. |
| Martins Awesome Skills | [martins-awesome-skills](https://github.com/Martin-Hausleitner/martins-awesome-skills) | Public-safe Skill-Sammlung fuer Hermes/OpenClaw. |
| Discord Voice Obsidian Agent | [discord-voice-obsidian-agent](https://github.com/Martin-Hausleitner/discord-voice-obsidian-agent) | Schneller Voice-Agent-Prototyp und Obsidian-Anbindung. |
| OpenClaw Hermes Email Control | local workspace | Operator-Inbox, E-Mail, Chatwoot und Himalaya-Workflows. |

## Supabase-Einordnung

Supabase ist sinnvoll, wenn wir schnell interne Apps fuer Hermes-Agenten bauen wollen: Dashboard, Auth, Row-Level-Security, Realtime-Status, einfache Storage-Uploads und Edge Functions. Fuer den Kernbetrieb bleibt **plain Postgres + pgvector** die robusteste Minimalvariante. Supabase ersetzt keine Matrix-Homeserver-Datenbank und sollte fuer Agent-Memory nur separat verwendet werden.

| Variante | Empfehlung |
|---|---|
| Supabase Cloud | Gut fuer schnelle interne Dashboards und Prototypen; private Agent-Daten nur bewusst und mit Redaction. |
| Self-hosted Supabase | Sinnvoll, wenn Auth/Realtime/Studio wirklich gebraucht werden; mehr Ops-Last als plain Postgres. |
| Plain Postgres + pgvector | Default fuer MVP: weniger bewegliche Teile, leichter zu sichern, leichter zu backuppen. |
