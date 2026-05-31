# OpenHuman-Integration in Credo

Diese Datei plant, wie das aktuelle [OpenHuman](https://github.com/tinyhumansai/openhuman) (tinyhumansai, GPL-3.0, ~30k Stars, Tauri/Rust + TypeScript) sauber in den Credo-Stack einlaeuft. Sie ist absichtlich handlungsorientiert: Was uebernehmen wir, was bricht mit Credo-Prinzipien, und in welche Phase gehoert es?

## 🧭 Executive Synthesis

OpenHuman und Credo loesen unterschiedliche Schichten desselben Problems:

```text
OpenHuman ist ein reifer, lokaler Personal-Agent:
  Tauri-Desktop, lokale SQLite Memory Tree, Obsidian-Vault,
  118+ OAuth-Integrationen (Composio), 20-Minuten Auto-Fetch,
  Voice (STT + ElevenLabs TTS), Token-Kompression, Model-Routing.

Credo ist der gehostete, governte Mehragenten-Backbone:
  Matrix-Raeume, Policy-vor-Tool, Job-Queue, Artefakt-Ledger,
  Ed25519-signierte Aktionen, m-of-n Quorum, OTel-Audit, OSS-first.
```

Die Integrationsthese: **OpenHuman wird die Personal-/Edge-Schicht und eine zweite Desktop-UX von Credo, nicht ein zweites Backend.** Sein lokaler Kontext, seine Integrationen und seine Voice-Schicht sind wertvoll, muessen aber durch Credos Policy-Gates, Memory-Modi, Audit und Signatur laufen. Die wichtigste Abstraktion bleibt: **jede Aktion hat einen Raum, eine Policy, einen Job, ein Artefakt und eine Spur** — auch wenn sie aus OpenHuman kommt.

## 🔄 Was OpenHuman in Credo ersetzt

Credo uebernimmt OpenHuman als **Edge-Schicht**. Die folgenden bisherigen Bausteine werden dadurch abgeloest (siehe auch das alt -> neu Mapping im [README](../README.md#-openhuman-als-personal-edge-schicht)). Der governte Backbone bleibt unveraendert credo.

| credo-Baustein (alt) | Jetzt: OpenHuman |
|---|---|
| Hermes Desktop · Cognitor Companion | OpenHuman Desktop (Tauri) als zweite Human-Surface |
| mautrix Bridges · Beeper · Mail-Inbox · Chatwoot | 118+ OAuth-Integrationen mit 20-Min-Auto-Fetch |
| Logseq / Obsidian + ActivityWatch | Memory Tree / Vault (komprimierte Markdown-Chunks) |
| Hermes Voice Agent (STT/TTS) | OpenHuman Voice ueber Element Call / LiveKit |
| Eigener Matrix-Client (war "nicht im MVP") | OpenHuman Desktop deckt die Client-Rolle ab |

**Bleibt credo-nativ:** Matrix-Kern (Synapse/Rooms/Admin), Policy-Gate + Valkey-Jobs, Governance (Ed25519/Safe/IPFS), Postgres/pgvector + MinIO als kanonisches Ledger, OTel/Grafana/NetBird.

## 🧩 Was OpenHuman mitbringt

| OpenHuman-Faehigkeit | Kurz | Credo-Relevanz |
|---|---|---|
| Memory Tree | Lokale SQLite, komprimierte Markdown-Chunks (<=3k Token), Obsidian-kompatibler Vault | Hoch: passt fast 1:1 auf Credos Memory-Modi und Obsidian-Review-Layer |
| 118+ Integrationen | OAuth via Composio-Connector, Auto-Fetch alle 20 Minuten (Gmail, Notion, GitHub, Slack, Calendar, Jira) | Hoch, aber Policy-/OSS-Konflikt: Composio ist managed, nicht OSS-first |
| Tauri-Desktop-UX | Rust + TS, Mascot, Hintergrund-Reasoning, Google-Meet-Beitritt | Mittel: zweite Human-Surface neben Element Web / Cinny |
| Voice | STT-Input, ElevenLabs-TTS-Output | Mittel: ElevenLabs ist proprietaer, gehoert in den Voice-Phasen-Pfad |
| Token-Kompression | "TokenJuice", bis zu -80% Kosten | Quer: Kosten-/Observability-Hebel fuer alle Agentenlaeufe |
| Model-Routing | Auswahl des passenden LLM je Workload | Quer: ergaenzt Hermes/OpenClaw/Codex-Routing |
| Core-Tools | Web-Search, Scrape, Filesystem, Git | Mittel: als MCP-/Skill-Tools mit Scope und Audit behandeln |
| agentmemory-Backend | Optionales cross-agent Memory | Mittel: Bruecke zu pgvector-Runtime-Memory pruefen |

## ⚠️ Prinzipien-Konflikte (zuerst klaeren)

Bevor Code fliesst, muessen vier Spannungen bewusst entschieden werden. Sonst importiert Credo stillschweigend fremde Defaults.

| Konflikt | OpenHuman-Default | Credo-Prinzip | Empfehlung |
|---|---|---|---|
| Managed vs OSS-first | Composio proxyt OAuth zentral | "Decentralisation without OSS is just outsourcing" | Composio ist der Edge-Default fuer schnelle Reichweite, laeuft aber nur im MCP-Untrusted-Regime (Scope, Manifest, Allowlist, Audit). Native OSS-Bridge/MCP bleibt das Migrationsziel pro Integration. |
| Proprietaere Voice | ElevenLabs TTS | OSS-/Self-Hosted-first | TTS hinter Adapter; Default OSS (z.B. Piper/Coqui-Nachfolger), ElevenLabs nur als Opt-in-Profil |
| Single-User vs governt | Lokaler Personal-Agent, ein Nutzer, voller Schreibzugriff | m-of-n Quorum, Policy-vor-Tool, read-only Memory-Default | OpenHuman-Node bekommt eine Device-Identitaet und schreibt nur ueber Credos Write-Gates |
| Lizenz | GPL-3.0 (App) | Gemischt (AGPL-3.0, Apache-2.0, MIT, BSD-3) | GPL-Grenzen pruefen: OpenHuman als getrennter Prozess/Client koppeln, nicht als Bibliothek in MIT-Komponenten linken |

## 🧠 Memory-Bruecke (groesster Gewinn)

Hier passen die beiden Projekte am besten. OpenHumans Memory Tree und Credos Drei-Stufen-Memory sind dasselbe Konzept in zwei Reifegraden.

| OpenHuman | Credo-Memory-Modus | Mapping |
|---|---|---|
| Auto-Fetch-Rohdaten (20-Min-Sync) | Ephemeral Run Context | Frischer Import bleibt zunaechst fluechtig und ungeprueft |
| Memory-Tree-Chunks (komprimiertes Markdown) | Reviewed Project Memory | Chunk wird Vorschlag, nicht sofort kanonisch |
| Obsidian-Vault (kuratiert) | Long-term Canonical Memory | Menschlich lesbar in Markdown/Git, mit Audit |

Schritte:

1. OpenHuman-Vault als Obsidian-/Markdown-Quelle an Credos Memory-Pipeline anbinden (read-only Default).
2. Memory-Tree-Chunks auf Credos Memory-Typen abbilden: Decision, Project, Person, Meeting, Task, Source, Runbook.
3. Chunks vor persistentem Write durch Write-Gate schicken: Quellenlink, Review-Status, Loeschpfad, Ed25519-Signatur des schreibenden Node.
4. Embeddings/Retrieval in Postgres + pgvector zentralisieren; OpenHumans lokale SQLite bleibt Edge-Cache, nicht kanonische Quelle.
5. Memory-Poisoning-Risiko adressieren: Auto-Fetch-Daten sind untrusted, kommen also nie ungeprueft in Canonical Memory.

Mehr Details: [research-improvements.md](research-improvements.md) (Abschnitt Memory) und [target-stack.md](target-stack.md).

## 📬 Integrationen und Auto-Fetch (Composio sauber zaehmen)

OpenHumans Integrationen (118+, Auto-Fetch) ersetzen in der Edge-Schicht die bisherige mautrix-Bridge-Inbox. Das bringt schnelle Reichweite, ist aber zugleich der groesste Policy-Bruch: Composio ist ein managed Connector, Credo will OSS-first und keine Consumer-Tokens zentral. Deshalb gilt ein striktes Regime.

Regeln fuer den Credo-Pfad:

- Composio laeuft im selben Untrusted-Regime wie MCP-Tools: Scope, Manifest, Allowlist, Audit.
- Pro Integration minimale OAuth-Scopes, getrennte Credentials, kein zentraler Consumer-Cookie-Speicher.
- Native OSS-Bridge oder MCP-Integration bleibt das **Migrationsziel** je Connector (Telegram, WhatsApp, Signal, Slack, Discord) — Composio ist der schnelle Start, nicht das Endbild.
- Auto-Fetch-Crawler laeuft als eigener Worker mit Run-ID; jeder Pull erzeugt einen Job und ein Artefakt, kein stiller Hintergrund-Write.
- Riskante Integrationen in VM/Proxy mit Kill-Switch.

Mehr Details: [matrix-ops-runbook.md](matrix-ops-runbook.md) (Bridges) und Phase 3 der [Roadmap](implementation-roadmap.md).

## 🖥️ Desktop-UX und Voice

| Thema | Plan |
|---|---|
| Tauri-Desktop | Als zweite Human-Surface neben Element Web / Cinny fuehren. Die App spricht Matrix-Raeume, nicht ein eigenes Backend. Mascot/Background-Reasoning sind UX, keine Autoritaet. |
| Voice STT/TTS | In den bestehenden Voice-Pfad einordnen: erst ausserhalb MatrixRTC testen, dann Element Call + LiveKit. TTS hinter Adapter, OSS-Default. |
| Google-Meet-Beitritt | Als separater RTC-Teilnehmer behandeln, nicht als impliziter Endpunkt. Recording-/E2EE-Regeln aus der Voice-Phase gelten. |

OpenHumans Voice darf den Text-MVP **nicht** blockieren — "Voice is Separate" bleibt gueltig.

## 🔁 Querschnitt: Kosten und Routing

- **Token-Kompression (TokenJuice):** als optionaler Layer vor LLM-Calls evaluieren; Wirkung in OTel-Spans (`llm.request`) messen, nicht blind vertrauen.
- **Model-Routing:** OpenHumans Router gegen Credos Hermes/OpenClaw/Codex-Routing abgleichen — ein Routing-Entscheider, nicht zwei konkurrierende.
- Beide Hebel gehoeren in die Observability-Spans, damit Kosten-Spikes alarmierbar bleiben.

## 🗺️ Einordnung in die bestehende Roadmap

Die Integration erfindet keine neue Phasenstruktur, sondern haengt an bestehende Phasen an.

| Roadmap-Phase | OpenHuman-Beitrag |
|---|---|
| Phase 2: Memory und Wissen | Memory-Tree-/Vault-Bruecke, Chunk-Mapping auf Memory-Typen, pgvector als Runtime |
| Phase 2b: Trace Every Run | Auto-Fetch-Pulls und Memory-Writes als getrennte OTel-Spans mit Run-ID |
| Phase 3: Bridges | OpenHuman/Composio-Integrationen ersetzen die Bridge-Inbox; OSS-Bridge/MCP als Migrationsziel; Token-/VM-Regeln |
| Phase 4: RTC und Voice | STT/TTS-Adapter, ElevenLabs als Opt-in, Meet-Beitritt als RTC-Teilnehmer |
| Phase 5: Observability | Token-Kompression und Routing messbar machen |

## 🚀 Naechste konkrete Schritte

| Prioritaet | Schritt | Ziel-Datei | Status |
|---:|---|---|---|
| 1 | Memory-Bruecke spezifizieren: Vault -> Write-Gate -> pgvector mit Memory-Typen-Mapping | [target-stack.md](target-stack.md#-memory-bruecke-openhuman-vault--write-gate--pgvector) | ✅ umgesetzt |
| 2 | Composio-Untrusted-Regime und OSS-Bridge-Migrationsziel im Bridge-Runbook festschreiben | [matrix-ops-runbook.md](matrix-ops-runbook.md) | ✅ umgesetzt |
| 3 | OpenHuman-Node-Identitaet (Ed25519 Device Key) und Write-Gate-Flow definieren | [architecture-flows.md](architecture-flows.md) | ✅ umgesetzt |
| 4 | OpenHuman-Core-Tools als risikoklassifizierte Skills registrieren | [hermes-skills.md](hermes-skills.md#openhuman-core-tools-als-risikoklassifizierte-skills) | ✅ umgesetzt |
| 5 | GPL-3.0-Kopplungsgrenze und Voice-/TTS-Adapter dokumentieren | [stack-comparison.md](stack-comparison.md#gpl-30-kopplungsgrenze-und-voice-tts-adapter) | ✅ umgesetzt |

**Status (2026-05-31):** Schritte 1–5 sind umgesetzt — Spezifikationen in den jeweiligen Ziel-Dateien, Beweise (statische Checks + Diagramm-Renders) in [proof/](../proof/).

Quellen: [OpenHuman](https://github.com/tinyhumansai/openhuman), [Composio](https://github.com/ComposioHQ/composio), [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices), [OpenTelemetry GenAI SemConv](https://opentelemetry.io/docs/specs/semconv/gen-ai/).
