# Repo-Landkarte

Diese Datei gruppiert die eigenen und externen Repos nach Rolle im Credo-Stack. Die grosse Roh-Liste aus dem README ist hier abstrahiert.

## 📚 Vollstaendige lokale Inventur

Die komplette lokale Git-Inventur liegt in [local-repositories.md](local-repositories.md). Sie umfasst aktuell **76 lokale Repositories** aus `~/Documents/Playground`, `~/Documents/GitHub` und `~/.openclaw/workspace`, inklusive Worktrees, lokalen Repos ohne Remote und installierten Skill-/Vendor-Checkouts.

| Kategorie | Anzahl | Warum relevant |
|---|---:|---|
| 💬 Matrix / Messaging | 3 | Credo, Beeper/Matrix Proxy und Bridge-Manager bilden den Messaging-Kern. |
| 🤖 Agents / Skills | 20 | OpenClaw, Hermes-nahe Skills, Fintaro-Agenten, Sonar-Worktrees und lokale Agent-Workspaces. |
| 🧑‍💻 Coding Agents | 1 | Codex Computer Use Aktivierung fuer native UI-Automation. |
| 📈 ActivityWatch / Lifelog | 9 | ActivityWatch-Stack, WHOOP, Apple Health, Screen Time, YouTube und Presence-Importer. |
| 💓 Health / Presence | 3 | Lokale WHOOP- und Apple-Health-Menubar-/Live-Sync-Prototypen. |
| 🍎 Apple / Device | 3 | iPhone Mirroring EU Guides und Aktivierungsreferenzen. |
| 🎙️ Voice / Audio | 4 | Sonar, Discord Voice und Craig-Recording-Referenzen. |
| 💼 Business / Finance | 5 | OnlyAPI, CreatorHero, Fintaro und Finance-/Gateway-Arbeit. |
| 🧪 Web / Product Experiments | 8 | Angebotsgeneratoren, Roadmap Builder, Timeline und Website-Experimente. |
| 🌐 Proxy / Browser / Network | 3 | Proxy-, Browser- und Netzwerktooling. |
| 🔬 Other / Research | 10 | Cognitor, Obsidian, Mac-Setup, APOLLO, Sense und Forschungsrepos. |
| 📦 Vendor / Installed Checkouts | 7 | Installierte Skill-Repos und abgeleitete Swift-Package-Checkouts. |

## 🧭 Zentrale Steuerung

| Logo | Repo / Workspace | Rolle |
|---|---|---|
| <img src="https://cdn.simpleicons.org/github/181717" width="22"> | [Credo](https://github.com/Martin-Hausleitner/Credo) | Architekturdeck, Stack-Entscheidungen, Runbook |
| <img src="https://cdn.simpleicons.org/github/181717" width="22"> | [martins-awesome-skills](https://github.com/Martin-Hausleitner/martins-awesome-skills) | Public-safe Hermes/OpenClaw Skill-Sammlung |
| <img src="https://cdn.simpleicons.org/github/181717" width="22"> | [hermes-agent](https://github.com/Martin-Hausleitner/hermes-agent) | Hermes-Fork und Workspace-Customizations |
| <img src="https://cdn.simpleicons.org/github/181717" width="22"> | [openclaw-workspace](https://github.com/Martin-Hausleitner/openclaw-workspace) | Skills, Prompts, Studio-Konfigurationen |

## 💬 Matrix, Bridges und Messaging

| Logo | Repo / Workspace | Rolle |
|---|---|---|
| <img src="https://cdn.simpleicons.org/matrix/000000" width="22"> | [beeper-matrix-proxy](https://github.com/Martin-Hausleitner/beeper-matrix-proxy) | Beeper/BIPA als Matrix-Portale |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="22"> | [bridge-manager](https://github.com/beeper/bridge-manager) | Bridge-Administration und Referenz |
| <img src="https://www.google.com/s2/favicons?domain=github.com&sz=64" width="22"> | `openclaw-hermes-email-control` | Chatwoot, E-Mail, Beeper und Hermes-Control |
| <img src="https://cdn.simpleicons.org/discord/5865F2" width="22"> | [discord-voice-obsidian-agent](https://github.com/Martin-Hausleitner/discord-voice-obsidian-agent) | schneller Voice-Agent-Prototyp |

## 🧩 Cognitor, Dashboards und Kontext

| Logo | Repo / Workspace | Rolle |
|---|---|---|
| <img src="https://cdn.simpleicons.org/react/61DAFB" width="22"> | [cognitor-launcher](https://github.com/Martin-Hausleitner/cognitor-launcher) | Web-, Tray-, Mobile-Agent-Oberflaechen |
| <img src="https://www.google.com/s2/favicons?domain=activitywatch.net&sz=64" width="22"> | [aw-john-harris-wifi](https://github.com/Martin-Hausleitner/aw-john-harris-wifi) | Presence, Wi-Fi, Door Context |
| <img src="https://www.google.com/s2/favicons?domain=whoop.com&sz=64" width="22"> | [aw-importer-whoop](https://github.com/Martin-Hausleitner/aw-importer-whoop) | WHOOP nach ActivityWatch |
| <img src="https://cdn.simpleicons.org/apple/000000" width="22"> | [aw-importer-apple-screentime](https://github.com/Martin-Hausleitner/aw-importer-apple-screentime) | Apple Screen Time nach ActivityWatch |
| <img src="https://cdn.simpleicons.org/youtube/FF0000" width="22"> | [aw-importer-youtube](https://github.com/Martin-Hausleitner/aw-importer-youtube) | YouTube Watch Sessions |

## 🧠 Knowledge und lokale Skills

| Logo | Repo / Workspace | Rolle |
|---|---|---|
| <img src="https://cdn.simpleicons.org/obsidian/7C3AED" width="22"> | [obsidian-notion-ui-customization](https://github.com/Martin-Hausleitner/obsidian-notion-ui-customization) | Knowledge- und Personal-OS-Layer |
| <img src="https://cdn.simpleicons.org/apple/000000" width="22"> | [openclaw-apple-findmy-skill](https://github.com/Martin-Hausleitner/openclaw-apple-findmy-skill) | Find My / Standort-Kontext |
| <img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="22"> | [codex-computer-use-eu-activate](https://github.com/Martin-Hausleitner/codex-computer-use-eu-activate) | Codex Computer Use Aktivierung |
| <img src="https://www.google.com/s2/favicons?domain=openai.com&sz=64" width="22"> | `codex-computer-use-control` | Hermes Skill fuer Computer-Use-MCP |

## 🛠️ Host, Ops und Experimente

| Logo | Repo / Workspace | Rolle |
|---|---|---|
| <img src="https://cdn.simpleicons.org/apple/000000" width="22"> | [mac-ai-dev-setup](https://github.com/Martin-Hausleitner/mac-ai-dev-setup) | Mac AI Dev Setup und Toolchain |
| <img src="https://cdn.simpleicons.org/apple/000000" width="22"> | [mac-ram-rescue](https://github.com/Martin-Hausleitner/mac-ram-rescue) | Host-Stabilitaet und Ressourcenpflege |
| <img src="https://www.google.com/s2/favicons?domain=playwright.dev&sz=64" width="22"> | [browser-use-mcp-plus](https://github.com/Martin-Hausleitner/browser-use-mcp-plus) | Browser-/MCP-Erweiterungen |
| <img src="https://cdn.simpleicons.org/github/181717" width="22"> | [excalidraw-mcp-app](https://github.com/Martin-Hausleitner/excalidraw-mcp-app) | Diagramm- und Visual-MCP |
