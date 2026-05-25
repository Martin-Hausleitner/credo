# Ausfuehrliche Stack-Vergleichstabelle

## Entscheidungsmatrix

| Kategorie | Option | Staerke | Schwaeche | Empfehlung | GitHub |
|---|---|---|---|---|---|
| Homeserver | Tuwunel | Sehr leicht, Rust, native S3-Richtung, ideal fuer knappe Server | Juenger als Synapse, weniger klassisch bewaehrt | Gewinner fuer Greenfield/8GB-Stack | [matrix-construct/tuwunel](https://github.com/matrix-construct/tuwunel) |
| Homeserver | Synapse | Referenz, beste Kompatibilitaet, Admin-API, Bridges | RAM/DB schwerer, mehr Ops-Last | Gewinner fuer konservativen Produktivstart | [element-hq/synapse](https://github.com/element-hq/synapse) |
| Homeserver | Dendrite | Go, effizienter als Synapse | Feature-/Push-/Reife-Luecken | Beobachten, nicht MVP-Core | [element-hq/dendrite](https://github.com/element-hq/dendrite) |
| Homeserver | Conduit | Sehr leicht | Stagnation/Abandonware-Risiko | Nicht als Core | [ConduitIO/conduit](https://github.com/ConduitIO/conduit) |
| Homeserver | Conduwuit | Conduit-Fork, leicht | Unklare Zukunft/Reife | Nur Test | [girlbossceo/conduwuit](https://github.com/girlbossceo/conduwuit) |
| Homeserver | Construct | Sehr leicht, C++ | Wenig Automatisierung, Spezialwissen | Nicht MVP | [matrix-construct/construct](https://github.com/matrix-construct/construct) |

## Clients

| Client | Rolle | Staerke | Schwaeche | Empfehlung | GitHub |
|---|---|---|---|---|---|
| Element Web | Referenz-Webclient | Kompatibilitaet, Admin, Debugging, Integrationen | Schwerer, weniger frisch | Pflicht-Fallback/Admin | [element-web](https://github.com/element-hq/element-web) |
| Element Desktop | Desktop-Fallback | Verpacktes Element Web, einfach fuer Nutzer | Electron/Chromium, kein nativer Encoder-Vorteil | Optional | [element-desktop](https://github.com/element-hq/element-desktop) |
| Element X iOS | Mobile Hauptaccount | Schnell, Matrix 2.0, Sliding Sync/OIDC-Zukunft | iOS Multi-Account fehlt | iPhone fuer Hauptkonto | [element-x-ios](https://github.com/element-hq/element-x-ios) |
| Element X Android | Mobile | Zukunftsclient, Android Multi-Account experimentell | Noch nicht voll Feature-komplett | Android testen | [element-x-android](https://github.com/element-hq/element-x-android) |
| Cinny | Haupt-Web UX | Schnell, klar, Discord-artiger | Weniger Enterprise-Fallback als Element | Sehr gut fuer Agent-Raeume | [cinny](https://github.com/cinnyapp/cinny), [cinny-desktop](https://github.com/cinnyapp/cinny-desktop) |
| Sable | Cinny-Fork/QoL | QoL, Cosmetics, experimenteller | Fork-Risiko | Top fuer Power-UX | [Sable](https://github.com/SableClient/Sable) |
| Commet | Discord-artiger Client | Multi-Account als Designziel | Reife pruefen | Interessant als Alternative | [commet](https://github.com/commetchat/commet) |
| FluffyChat | Casual/Mobile | Freundlich, plattformuebergreifend | Nicht Power-Agent-Client | Gut fuer Gaeste/Familie | [fluffychat](https://github.com/krille-chan/fluffychat) |
| Nheko | Power/Desktop | Schnell, nativ, technisch | UX weniger mainstream | Debug/Power-User | [nheko](https://github.com/Nheko-Reborn/nheko) |

## RTC, Voice und Streaming

| Komponente | Rolle | Staerke | Risiko | Empfehlung | GitHub |
|---|---|---|---|---|---|
| Element Call | MatrixRTC Frontend | Matrix-native Calls, LiveKit-Strang | Media-Quality noch jung | Spaeterer Call-Stack | [element-call](https://github.com/element-hq/element-call) |
| LiveKit | SFU/Realtime Media | Stark, skalierbar, Egress/Agents | Eigener Ops-Strang | Beste Wahl fuer RTC | [livekit](https://github.com/livekit/livekit) |
| lk-jwt-service | MatrixRTC LiveKit Auth | Verbindet MatrixRTC mit LiveKit | Konfig-Aufwand | Pflicht fuer Element Call + LiveKit | [lk-jwt-service](https://github.com/element-hq/lk-jwt-service) |
| LiveKit Egress | Recording ohne E2EE | Sauber fuer S3/MP4/HLS | Mit E2EE nicht dekodierbar | Nur fuer unverschluesselte Recording-Raeume | [egress](https://github.com/livekit/egress) |
| LiveKit Agents | Voice Agents | Provider-Mix STT/LLM/TTS | MatrixRTC-E2EE bleibt hart | Spaeter fuer Matrix Voice | [livekit/agents](https://github.com/livekit/agents) |
| OpenAI Realtime | Voice MVP | Niedrige Latenz, Tool Calls | Cloud-Audio, Kosten | Discord Voice MVP | [openai-realtime-agents](https://github.com/openai/openai-realtime-agents) |
| discord.py | Discord Voice Gateway | Schnell produktiv | Discord-Abhaengigkeit | Schnellster Voice-Pfad | [discord.py](https://github.com/Rapptz/discord.py) |

## Bridges

| Bridge | Ziel | Reife | Risiko | Empfehlung | GitHub |
|---|---|---|---|---|---|
| mautrix/whatsapp | WhatsApp | Aktiv, Go, bridgev2 | Session invalidation | Frueh aktivieren, wenn noetig | [whatsapp](https://github.com/mautrix/whatsapp) |
| mautrix/telegram | Telegram | Aktiv, Go rewrite | Niedrig bis mittel | Gute erste Bridge | [telegram](https://github.com/mautrix/telegram) |
| mautrix/signal | Signal | Aktiv, libsignal | Kryptografisch/operativ komplex | Gut, aber sauber planen | [signal](https://github.com/mautrix/signal) |
| mautrix/discord | Discord | Aktiv | User-token puppeting ToS-riskant | Nur Bot/Guild sauber nutzen | [discord](https://github.com/mautrix/discord) |
| mautrix/slack | Slack | Aktiv | Workspace Policies | Fuer Team-Interop | [slack](https://github.com/mautrix/slack) |
| mautrix/gmessages | Google Messages | Aktiv | Google/Android Session | Optional | [gmessages](https://github.com/mautrix/gmessages) |
| mautrix/meta | Instagram/Facebook | Aktiv, aber fragil | Hoch: Ban, Proxy, Cookies | Erst nach VM/Proxy-Konzept | [meta](https://github.com/mautrix/meta) |
| beeper/platform-imessage | iMessage | Aktiv, macOS Relay | Apple-Hardware noetig | Spezialfall | [platform-imessage](https://github.com/beeper/platform-imessage) |

## Agent Runtime, Skills und Security

| Komponente | Rolle | Empfehlung | GitHub |
|---|---|---|---|
| Hermes Agent | Orchestrator, Gateway, Skills, Memory, Subagents | Kernruntime fuer Agenten | [hermes-agent](https://github.com/NousResearch/hermes-agent) |
| OpenClaw | Lokale Agent-/Skill-Umgebung | Lokale Tool-Ausfuehrung und Skills | [openclaw](https://github.com/openclaw/openclaw) |
| ClawHub | Skill Registry/Katalog | Versionierung, Trust, Install-Layer | [clawhub](https://github.com/openclaw/clawhub) |
| agent-secrets | Secret Handling | Keine Tokens in Skills | [agent-secrets](https://github.com/joelhooks/agent-secrets) |
| agent-scan | Security Scan | Skill-/Agent-Risiken pruefen | [agent-scan](https://github.com/snyk/agent-scan) |
| Atropos | Agent Evals | Regressionen/Evals fuer Skills | [atropos](https://github.com/NousResearch/atropos) |

## Knowledge und Memory

| Komponente | Rolle | Empfehlung | GitHub |
|---|---|---|---|
| Obsidian Markdown | Local-first Knowledge Base | Beste mensch/agentenlesbare Memory-Basis | n/a |
| Dataview | Abfragen ueber Markdown/YAML | Sehr nuetzlich fuer strukturierte Memory | [obsidian-dataview](https://github.com/blacksmithgu/obsidian-dataview) |
| Smart Connections | Vault-RAG | Semantische Suche direkt im Vault | [smart-connections](https://github.com/brianpetro/obsidian-smart-connections) |
| Obsidian Git | Versionierung | Audit-Trail fuer Agent-Aenderungen | [obsidian-git](https://github.com/Vinzent03/obsidian-git) |
| Self-hosted LiveSync | Multi-Device Sync | Fast realtime, aber mehr Ops | [obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync) |
| Remotely Save | S3/WebDAV Sync | Simpler Sync/Backup | [remotely-save](https://github.com/remotely-save/remotely-save) |
| Quartz | Publish/Wiki | Vault als Docs-Site | [quartz](https://github.com/jackyzha0/quartz) |

## Klare Stack-Varianten

| Variante | Stack | Wann nehmen? |
|---|---|---|
| Konservativer Start | Synapse + Element Web + Cinny + Hermes Bot + Redis + Postgres + R2 | Wenn Kompatibilitaet wichtiger ist als RAM |
| Ressourcen-Stack | Tuwunel + Element Web + Sable/Cinny + R2 + Postgres | Wenn 8GB/256GB und S3 wichtig sind |
| Universal Messenger | Synapse/Tuwunel + mautrix WhatsApp/Telegram/Signal + Bridge Manager | Wenn externe Messenger wichtig sind |
| Voice MVP | Discord.py + OpenAI Realtime + Hermes Tools + pgvector | Wenn schnell sprechender Agent gebraucht wird |
| Sovereign Voice | Element Call + LiveKit + LiveKit Agents | Wenn alles in Matrix/selbstgehostet bleiben soll |
| Knowledge Stack | Obsidian + Git + Dataview + Smart Connections + pgvector | Wenn Memory/Docs zentral sind |
