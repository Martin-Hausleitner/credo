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
| Hermes Desktop | Agent Desktop | Native GUI fuer Hermes-Installation, lokale/remote API, Skills, Memory, Sessions, Schedules und Gateways | Kein Matrix-Client-Ersatz, muss in Policy/Trace-Modell eingebunden werden | Sehr interessant als lokale Control-Surface fuer Martin | [hermes-desktop](https://github.com/fathah/hermes-desktop) |

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

## GPL-3.0-Kopplungsgrenze und Voice-/TTS-Adapter

OpenHuman steht unter **GPL-3.0**. Damit diese Lizenz nicht den ganzen Credo-Stack ansteckt, ist die Kopplung bewusst eine **Prozess- und Protokollgrenze**, kein Linking.

| Aspekt | Regel | Folge |
|---|---|---|
| Prozess | OpenHuman laeuft als eigener Tauri-Prozess, nicht in den Credo-Core gelinkt | kein gemeinsames Binary, keine Derivative-Work-Kopplung |
| Schnittstelle | Kopplung nur ueber Netz/IPC: MCP, HTTP oder Matrix-Events | austauschbar, sprach-/lizenzneutral |
| Daten | Vault-Chunks und Connector-Outputs sind Daten, kein Code | GPL betrifft OpenHuman selbst, nicht die Inhalte im Gate |
| Distribution | wird OpenHuman mitverteilt, gilt GPL-3.0 fuer dieses Artefakt; Credo-Core behaelt seine eigene Lizenz | klare Trennung je Artefakt im Repo-/Build-Manifest |

Praktisch heisst das: der Credo-Core ruft OpenHuman nie als Bibliothek auf, sondern spricht ausschliesslich ueber definierte Endpunkte mit ihm. So bleibt die GPL-Pflicht auf den OpenHuman-Node begrenzt.

Voice/TTS laeuft ueber einen **austauschbaren Adapter**, damit der proprietaere ElevenLabs-Pfad jederzeit gegen OSS getauscht werden kann. Adapter-Vertrag: `stt(audio) -> text`, `tts(text) -> audio`, plus Capability-/Lizenz-Flag.

| Adapter | Lizenz | Rolle | Einsatz |
|---|---|---|---|
| ElevenLabs TTS | proprietaer | hohe Stimmqualitaet | Default nur bei explizit erlaubtem External-Write-Gate |
| Piper | MIT | lokales OSS-TTS | OSS-Fallback, Edge-tauglich |
| Coqui TTS | MPL-2.0 | OSS-TTS mit Voice-Cloning | OSS-Alternative fuer Self-Hosting |
| Whisper / faster-whisper | MIT | lokales STT | OSS-Default fuer Spracherkennung |

Regel: Der Adapter waehlt per Config; proprietaere Backends sind nie Default-on, sondern nur nach expliziter Freigabe, und jeder ausgehende Synthese-Call laeuft durch das External-Write-Gate mit Audit.

Mehr Details: [openhuman-integration.md](openhuman-integration.md), [Voice-Skills](hermes-skills.md#openhuman-core-tools-als-risikoklassifizierte-skills). Quellen: [OpenHuman](https://github.com/tinyhumansai/openhuman), [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html), [Piper](https://github.com/rhasspy/piper), [Coqui TTS](https://github.com/coqui-ai/TTS).

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
| Hermes Desktop | Desktop Companion fuer Hermes Agent | Lokale Control-Surface fuer Provider, Chat, Sessions, Memory, Skills, Tools, Schedules und Messaging Gateways | [hermes-desktop](https://github.com/fathah/hermes-desktop) |
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
| Lokale Agent Workbench | Hermes Desktop + Hermes Agent + OpenClaw + Tailscale | Wenn Martin eine native Schaltzentrale fuer Provider, Skills, Sessions, Memory und Gateways will |
| Ressourcen-Stack | Tuwunel + Element Web + Sable/Cinny + R2 + Postgres | Wenn 8GB/256GB und S3 wichtig sind |
| Universal Messenger | Synapse/Tuwunel + mautrix WhatsApp/Telegram/Signal + Bridge Manager | Wenn externe Messenger wichtig sind |
| Voice MVP | Discord.py + OpenAI Realtime + Hermes Tools + pgvector | Wenn schnell sprechender Agent gebraucht wird |
| Sovereign Voice | Element Call + LiveKit + LiveKit Agents | Wenn alles in Matrix/selbstgehostet bleiben soll |
| Knowledge Stack | Obsidian + Git + Dataview + Smart Connections + pgvector | Wenn Memory/Docs zentral sind |
