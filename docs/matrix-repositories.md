# 🟢 Matrix-Repository-Map fuer Credo

Diese Map fuehrt die Matrix-bezogenen Entscheidungen in Credo auf die konkreten Upstream-Repositories zurueck. Sie trennt Core-Server, Clients, SDKs, Bridges, RTC und Ops, damit spaetere Implementierungsschritte nicht im Architekturtext verschwimmen.

## 🧱 Core und Server

| Repo | Rolle in Credo | Bewertung | GitHub |
|---|---|---|---|
| Synapse | konservativer Referenz-Homeserver | beste Kompatibilitaet, Admin-API, Bridges | [element-hq/synapse](https://github.com/element-hq/synapse) |
| Tuwunel | leichter Greenfield-Homeserver | stark fuer knappe Ressourcen und S3-orientierten Betrieb | [matrix-construct/tuwunel](https://github.com/matrix-construct/tuwunel) |
| Dendrite | alternativer Go-Homeserver | beobachten, nicht Core-MVP | [element-hq/dendrite](https://github.com/element-hq/dendrite) |
| Conduit | leichter Rust-Homeserver | nicht als Core wegen Reife-/Stagnationsrisiko | [ConduitIO/conduit](https://github.com/ConduitIO/conduit) |
| Conduwuit | Conduit-Fork | Testkandidat, nicht MVP | [girlbossceo/conduwuit](https://github.com/girlbossceo/conduwuit) |
| Construct | C++ Homeserver | technisch spannend, aber Spezialbetrieb | [matrix-construct/construct](https://github.com/matrix-construct/construct) |
| Matrix Spec | Protokollreferenz | normative Basis fuer Federation, Rooms, Events, Widgets und RTC | [matrix-org/matrix-spec](https://github.com/matrix-org/matrix-spec) |
| Matrix Spec Proposals | MSCs fuer neue Features | wichtig fuer MatrixRTC, Sliding Sync, Auth und Widgets | [matrix-org/matrix-spec-proposals](https://github.com/matrix-org/matrix-spec-proposals) |

## 💬 Clients

| Repo | Rolle in Credo | Bewertung | GitHub |
|---|---|---|---|
| Element Web | Referenz-/Admin-Webclient | Pflicht-Fallback fuer Debugging und Kompatibilitaet | [element-hq/element-web](https://github.com/element-hq/element-web) |
| Element Desktop | Desktop-Fallback | Electron-Wrapper, praktisch aber kein nativer Vorteil | [element-hq/element-desktop](https://github.com/element-hq/element-desktop) |
| Element X iOS | Mobile Hauptaccount | schnell, aber Multi-Account auf iOS bleibt kritisch | [element-hq/element-x-ios](https://github.com/element-hq/element-x-ios) |
| Element X Android | Mobile Android | Zukunftsclient, Multi-Account experimenteller | [element-hq/element-x-android](https://github.com/element-hq/element-x-android) |
| Cinny | primaerer UX-Webclient | schnelle, klare Agent-Raum-UX | [cinnyapp/cinny](https://github.com/cinnyapp/cinny) |
| Cinny Desktop | Desktop-Verpackung fuer Cinny | optional | [cinnyapp/cinny-desktop](https://github.com/cinnyapp/cinny-desktop) |
| Sable | Cinny-Fork | Power-UX/QoL, aber Fork-Risiko | [SableClient/Sable](https://github.com/SableClient/Sable) |
| Commet | alternativer Matrix-Client | Multi-Account-orientiert, beobachten | [commetchat/commet](https://github.com/commetchat/commet) |
| FluffyChat | Casual-/Mobile-Alternative | freundlich fuer Gaeste/Familie | [krille-chan/fluffychat](https://github.com/krille-chan/fluffychat) |
| Nheko | nativer Power-Client | Debug/Power-User | [Nheko-Reborn/nheko](https://github.com/Nheko-Reborn/nheko) |

**Client-Entscheidung:** Element Web bleibt Pflicht, weil es als Referenzclient fuer Admin, Debugging und Kompatibilitaet funktioniert. Element X ist der Zukunftspfad fuer Matrix 2.0, Rust SDK, Sliding Sync, OIDC und MatrixRTC. Cinny/Sable/Commet sind die bessere Alltags-UX fuer Agentenraeume, Channel-Scanning und Discord-artige Arbeitsweisen.

**Element X Warnung:** iOS sollte fuer mehrere Identitaeten vorsichtig behandelt werden. Logout kann lokale Kryptodaten entfernen; Secure Key Backup muss vor produktiver Nutzung sauber funktionieren.

## 🤖 SDKs, Bots und Appservices

| Repo | Rolle in Credo | Bewertung | GitHub |
|---|---|---|---|
| mautrix/python | Matrix-Bot-Gateway fuer MVP | schneller Python-Pfad fuer Bot und Appservice | [mautrix/python](https://github.com/mautrix/python) |
| matrix-rust-sdk | spaeterer harter Runtime-Pfad | performante Rust-Services fuer Gateway/Worker | [matrix-org/matrix-rust-sdk](https://github.com/matrix-org/matrix-rust-sdk) |
| matrix-appservice-bridge | Appservice-Referenz | spaeter fuer virtuelle Agent-User/Bridges | [matrix-org/matrix-appservice-bridge](https://github.com/matrix-org/matrix-appservice-bridge) |
| maubot | Bot-Framework | optional fuer Matrix-native Bot-Plugins | [maubot/maubot](https://github.com/maubot/maubot) |
| baibot | AI Bot Referenz | Referenz fuer Matrix-AI-Bot-Patterns | [etkecc/baibot](https://github.com/etkecc/baibot) |

## 📬 Bridges

| Repo | Zielnetz | Rolle in Credo | Risiko | GitHub |
|---|---|---|---|---|
| mautrix/telegram | Telegram | gute erste Bridge | niedrig bis mittel | [mautrix/telegram](https://github.com/mautrix/telegram) |
| mautrix/whatsapp | WhatsApp | frueh aktivieren, wenn noetig | mittel: Session-State | [mautrix/whatsapp](https://github.com/mautrix/whatsapp) |
| mautrix/signal | Signal | stark, aber sauber planen | operativ/kryptografisch komplex | [mautrix/signal](https://github.com/mautrix/signal) |
| mautrix/slack | Slack | Team-Interop | Workspace-/Token-Policies | [mautrix/slack](https://github.com/mautrix/slack) |
| mautrix/discord | Discord | nur Bot/Guild sauber nutzen | User-token puppeting riskant | [mautrix/discord](https://github.com/mautrix/discord) |
| mautrix/gmessages | Google Messages | optional | Google-/Android-Session | [mautrix/gmessages](https://github.com/mautrix/gmessages) |
| mautrix/meta | Instagram/Facebook | erst nach Proxy-/VM-Konzept | hoch: Ban, Cookies, Session Locks | [mautrix/meta](https://github.com/mautrix/meta) |
| mautrix/manager | Bridge Login/Management | reduziert Bridge-Login-Reibung | Admin-Tool, kein Zielnetz | [mautrix/manager](https://github.com/mautrix/manager) |
| beeper/platform-imessage | iMessage Relay | Spezialfall mit Apple-Hardware | macOS/Apple-Hardware noetig | [beeper/platform-imessage](https://github.com/beeper/platform-imessage) |

**Bridge-Ops:** Meta/Instagram bleibt eine spaetere Spezialphase. Fuer `mautrix/meta` braucht es Provisioning API, Session-Watchdog, `.well-known/matrix/mautrix`, saubere VM-Isolation, Proxy-Konzept und Kill-Switch.

## 🎙️ MatrixRTC, Voice und Widgets

| Repo | Rolle in Credo | Bewertung | GitHub |
|---|---|---|---|
| Element Call | MatrixRTC Frontend | erst nach Text-MVP, solide Call-Schicht | [element-hq/element-call](https://github.com/element-hq/element-call) |
| lk-jwt-service | LiveKit Auth fuer MatrixRTC | Pflicht fuer Element Call + LiveKit | [element-hq/lk-jwt-service](https://github.com/element-hq/lk-jwt-service) |
| LiveKit | SFU/Media Backend | bester RTC-/Voice-Strang | [livekit/livekit](https://github.com/livekit/livekit) |
| LiveKit Egress | Recording ohne E2EE | nur fuer unverschluesselte Recording-Raeume | [livekit/egress](https://github.com/livekit/egress) |
| LiveKit Agents | Voice Agents | spaeter fuer Matrix Voice/Provider-Mix | [livekit/agents](https://github.com/livekit/agents) |
| Matrix Widget API | Cognitor-/Dashboard-Widgets in Matrix | spaeter nach PNG/Screenshot-MVP | [matrix-org/matrix-widget-api](https://github.com/matrix-org/matrix-widget-api) |

**RTC-Notiz:** MatrixRTC braucht mehr als nur Element Call. Relevant sind `org.matrix.msc4143.rtc_foci`, `lk-jwt-service`, `LIVEKIT_FULL_ACCESS_HOMESERVERS`, TURN/TLS 443, UDP-Portbereiche und MSC3266/MSC4222. Recording bleibt ausserhalb des Text-MVP.

## 📊 Ops, Storage und Admin

| Repo | Rolle in Credo | Bewertung | GitHub |
|---|---|---|---|
| matrix-docker-ansible-deploy | Deployment-Backbone | bevorzugter Ops-Pfad fuer Matrix, Bridges, Clients, TURN | [spantaleev/matrix-docker-ansible-deploy](https://github.com/spantaleev/matrix-docker-ansible-deploy) |
| Synapse Admin | Admin UI | nuetzlich fuer Synapse-Betrieb | [etkecc/synapse-admin](https://github.com/etkecc/synapse-admin) |
| Matrix Authentication Service | OIDC/Auth-Schicht | Ausbauphase fuer saubere Identitaeten | [element-hq/matrix-authentication-service](https://github.com/element-hq/matrix-authentication-service) |
| Draupnir | Moderation/Policy | fuer groessere Raeume/Federation | [the-draupnir-project/Draupnir](https://github.com/the-draupnir-project/Draupnir) |
| synapse-s3-storage-provider | Synapse Media nach S3 | konservativer S3-Pfad fuer Synapse | [matrix-org/synapse-s3-storage-provider](https://github.com/matrix-org/synapse-s3-storage-provider) |

## Credo-eigene Rueckverweise

| Repo | Rolle |
|---|---|
| [Credo](https://github.com/Martin-Hausleitner/Credo) | Architekturdeck, Service-Katalog, Skill-Inventar und Matrix-Repository-Map. |
| [beeper-matrix-proxy](https://github.com/Martin-Hausleitner/beeper-matrix-proxy) | eigene Bridge-Referenz fuer Beeper/BIPA -> Matrix. |
| [discord-voice-obsidian-agent](https://github.com/Martin-Hausleitner/discord-voice-obsidian-agent) | schneller Voice-Agent-Prototyp ausserhalb MatrixRTC. |
| [martins-awesome-skills](https://github.com/Martin-Hausleitner/martins-awesome-skills) | public-safe Skills fuer Hermes/OpenClaw. |
