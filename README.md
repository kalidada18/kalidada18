<div align="center">

<!-- ══════════════════════════════ HERO ══════════════════════════════ -->

<h1>SUJAL LAMICHHANE</h1>

<h3>Cybersecurity Practitioner &nbsp;·&nbsp; Security Researcher &nbsp;·&nbsp; Certified Ethical Hacker</h3>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&duration=2600&pause=1000&color=FF1744&center=true&vCenter=true&repeat=true&width=760&height=42&lines=%24+whoami+%E2%86%92+Cybersecurity+Practitioner;Hunting+threats.+Engineering+detections.+Shipping+defenses.;%24+./threat_hunt+--scope+SIEM+--mode+proactive;FortiSIEM+%C2%B7+LogPoint+%C2%B7+LogRhythm+%C2%B7+Wazuh" alt="Terminal-style animated typing introduction of Sujal Lamichhane" />

<br/><br/>

[![EC Council CEH](https://img.shields.io/badge/EC_Council-CEH-3F3F46?style=flat-square&labelColor=18181B)](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)&nbsp;&nbsp;
![Open to collaboration](https://img.shields.io/badge/open%20to%20collaboration-FF1744?style=flat-square&labelColor=18181B)&nbsp;&nbsp;
[![Threatbase](https://img.shields.io/badge/threatbase-OSINT%20platform-3F3F46?style=flat-square&logo=cloudflare&logoColor=ffffff&labelColor=18181B)](https://threatbase.qzz.io)

<br/><br/>

</div>

<!-- ═══════════════════════ TERMINAL BRIEFING ═══════════════════════ -->

## 📋 Briefing

```bash
$ ssh sujal@kalidada18.dev -p 2222
┌──(sujal㉿kali)-[~]
└─$ cat ./profile.brief
```

<br/>

<table width="100%">
<tr>
<td width="55%" valign="top">

> Cybersecurity practitioner working across **SOC operations, threat triage, and
> detection engineering**, with hands-on time in FortiSIEM, LogPoint, LogRhythm,
> and Wazuh. I design, break, and harden security systems: production-grade
> detection pipelines, open-source SOC infrastructure, and an OSINT platform
> that processes millions of IOCs.

<sub><code>B.Sc Computer Science · Network Technology and Cybersecurity</code></sub>

</td>
<td width="3%"></td>
<td width="42%" valign="top">

```yaml
# ./profile.brief
operator: sujal lamichhane
cert: EC-Council Certified Ethical Hacker
domains:
  - soc operations
  - threat triage
  - detection engineering
kill_chain: ingest > detect > triage > contain > report
siem_hands_on: FortiSIEM, LogPoint, LogRhythm, Wazuh
osint_pipeline: 54 feeds, deduplicated
scope: isolated lab, authorized testing only
```

</td>
</tr>
</table>

<br/>

| Discipline | Execution | Primary stack |
|:-----------|:----------|:--------------|
| SOC operations | alert triage, enrichment, escalation, shift handoff | FortiSIEM / LogPoint / LogRhythm |
| Detection engineering | correlation rules, dashboards, ATT&CK mapping | Wazuh / Splunk / Elastic |
| Incident response | case ownership, playbook design, SOAR automation | TheHive / Shuffle / MISP |
| Threat hunting | hypothesis-led hunts on endpoint and network telemetry | Sysmon / Suricata / Wireshark |
| Offensive testing | authorized assessments and hardening follow-through | Kali / Burp Suite / Nmap |
| OSINT fusion | feed ingestion, IOC dedupe, blocklist publishing | threatbase / MISP |

<br/>

<sub>**Research vectors:** adversary emulation (ATT&CK), open-source SOC orchestration, OSINT and threat feed intelligence, ML-assisted network defense, deception and honeypot telemetry.</sub>

<br/><br/>

<!-- ════════════════════════════ ARSENAL ══════════════════════════════ -->

## 🛠️ Arsenal

#### 🏆 Capstone · Unified Open-Source SOC Framework

**[Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework](https://github.com/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework)**  
<sub><code>detection → correlation → automated triage, one pipeline</code></sub>

![Stars](https://img.shields.io/github/stars/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Forks](https://img.shields.io/github/forks/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=3F3F46&labelColor=18181B)&nbsp;
![Last commit](https://img.shields.io/github/last-commit/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&color=3F3F46&labelColor=18181B)

`Wazuh / Suricata / Shuffle / TheHive / MISP`

> Final-year capstone: an enterprise-grade SOC assembled entirely from open
> source, with endpoint and network telemetry, centralized correlation, and
> automated triage feeding one incident workflow.

<details>
<summary><sub>architecture</sub></summary>

<br/>

```
┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│ Endpoint / Network      │────> │ Suricata NIDS &         │────> │ Wazuh Centralized       │
│ Telemetry Collectors    │      │ Wazuh Endpoint Agents   │      │ SIEM & Indexer Engine   │
└─────────────────────────┘      └─────────────────────────┘      └────────────┬────────────┘
                                                                               │ alerts
┌─────────────────────────┐      ┌─────────────────────────┐                   │
│ TheHive Incident Cases  │ <─── │ Shuffle SOAR            │ <─────────────────┘
│ & MISP Threat Intel     │      │ Automation Engine       │
└─────────────────────────┘      └─────────────────────────┘
```

</details>

<br/><br/>

<table width="100%">
<tr>
<td width="60%" valign="top">

#### 🌐 Threatbase · production OSINT platform

**[threatbase](https://github.com/kalidada18/threatbase)**  
<sub><code>TypeScript / Python / React / Cloudflare</code></sub>

![Stars](https://img.shields.io/github/stars/kalidada18/threatbase?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Feed pipeline](https://img.shields.io/github/actions/workflow/status/kalidada18/threatbase/update-feed.yml?style=flat-square&label=feed%20pipeline&labelColor=18181B)

> CI-scheduled ingestion polls **54 threat feeds**, deduplicates across
> sources, and publishes versioned IP, CIDR, domain, URL, and SHA-256
> blocklists to a live dashboard with retrospective archives.

```
54 feeds ──> fetch ──> classify ──> dedupe
  ├──> IP / CIDR / domain / URL lists
  ├──> SHA-256 hash blocklists
  ├──> live dashboard · threatbase.qzz.io
  └──> ZIP archives · git mirrors
```

</td>
<td width="3%"></td>
<td width="37%" valign="top" align="center">

<a href="https://star-history.com/#kalidada18/threatbase&Date">
<img src="https://api.star-history.com/svg?repos=kalidada18/threatbase&type=Date" width="100%" alt="Threatbase star growth chart over time" />
</a>

</td>
</tr>
<tr>
<td colspan="3" height="24"></td>
</tr>
<tr>
<td width="60%" valign="top">

#### 🛡️ KaliWall · ML network defense

**[KaliWall](https://github.com/kalidada18/KaliWall)**  
<sub><code>Go / Linux / XGBoost</code></sub>

![Stars](https://img.shields.io/github/stars/kalidada18/KaliWall?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Go](https://img.shields.io/badge/Go-1.21%2B-3F3F46?style=flat-square&logo=go&logoColor=FF1744&labelColor=18181B)

> A Linux firewall with real-time deep packet inspection, GeoIP filtering,
> VirusTotal intel lookups, and XGBoost anomaly scoring behind a
> FortiGate-inspired console.

```
ingress ──> DPI ──> GeoIP ──> VT lookup
        └──> XGBoost score ──> verdict
```

</td>
<td width="3%"></td>
<td width="37%" valign="top">

#### ⚡ Multi-Layer SIEM · defense in depth

**[Multi-Layer-Security-Integration](https://github.com/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions)**  
<sub><code>Splunk / Elastic / Sysmon / Logstash</code></sub>

![Stars](https://img.shields.io/github/stars/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions?style=flat-square&logo=github&color=FF1744&labelColor=18181B)

```
├── Perimeter   fw + Suricata IDS
├── Host        Sysmon + Logstash
├── Analytics   SIEM correlation
└── Response    auto alerting
```

</td>
</tr>
</table>

<br/><br/>

<!-- ═══════════════════════════ RESEARCH ══════════════════════════════ -->

## 🔬 Research

| Focus | Project | Stack |
|:------|:--------|:------|
| Deception telemetry and attacker profiling | **[honeypot-java](https://github.com/kalidada18/honeypot-java)** | `Java` |
| Volumetric and protocol resilience testing | **[dos-attack](https://github.com/kalidada18/dos-attack)** | `Python` |
| ARP poisoning and rogue DNS simulation | **[dns-spoofing-tool](https://github.com/kalidada18/dns-spoofing-tool)** | `Python` |

<br/>

<sub>Research builds are published for defensive study, isolated lab environments, and authorized testing only.</sub>

<br/><br/>

<!-- ═══════════════════════════ TOOLING ═══════════════════════════════ -->

## 🧰 Tooling

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,go,ts,js,bash,powershell,java,sql&theme=dark" alt="Programming languages: Python, Go, TypeScript, JavaScript, Bash, PowerShell, Java, SQL. Hover to animate" />
  </a>
  <br/>
  <sub><code>languages // scripting</code></sub>
</p>

<br/>

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=linux,kali,docker,git,github,cloudflare,react,mysql&theme=dark" alt="Platform stack: Linux, Kali, Docker, Git, GitHub, Cloudflare, React, MySQL. Hover to animate" />
  </a>
  <br/>
  <sub><code>platform // infrastructure</code></sub>
</p>

<br/>

<details open>
<summary><b>📡 SOC &amp; Defensive Engineering</b></summary>
<br/>

![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat-square&logo=splunk&logoColor=FF1744&labelColor=18181B)&nbsp;
![Elastic](https://img.shields.io/badge/Elastic_SIEM-005571?style=flat-square&logo=elasticcloud&logoColor=ffffff&labelColor=18181B)&nbsp;
![Wazuh](https://img.shields.io/badge/Wazuh-3F3F46?style=flat-square&labelColor=18181B)&nbsp;
![FortiSIEM](https://img.shields.io/badge/FortiSIEM-3F3F46?style=flat-square&logo=fortinet&logoColor=EE3124&labelColor=18181B)&nbsp;
![LogPoint](https://img.shields.io/badge/LogPoint-3F3F46?style=flat-square&labelColor=18181B)&nbsp;
![LogRhythm](https://img.shields.io/badge/LogRhythm-3F3F46?style=flat-square&labelColor=18181B)

![Shuffle SOAR](https://img.shields.io/badge/Shuffle_SOAR-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![TheHive](https://img.shields.io/badge/TheHive-F7A41D?style=flat-square&labelColor=18181B)&nbsp;
![MISP](https://img.shields.io/badge/MISP-e74343?style=flat-square&labelColor=18181B)

![Suricata](https://img.shields.io/badge/Suricata-88c070?style=flat-square&labelColor=18181B)&nbsp;
![Snort](https://img.shields.io/badge/Snort-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![FortiGate](https://img.shields.io/badge/FortiGate-EE3124?style=flat-square&logo=fortinet&logoColor=ffffff&labelColor=18181B)&nbsp;
![Sysmon](https://img.shields.io/badge/Sysmon-0078d4?style=flat-square&logo=windows&logoColor=ffffff&labelColor=18181B)

</details>

<br/>

<details open>
<summary><b>⚔️ Offensive Security &amp; Testing</b></summary>
<br/>

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=ffffff&labelColor=18181B)&nbsp;
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square&labelColor=18181B)&nbsp;
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-001D2C?style=flat-square&logo=owasp&logoColor=ffffff&labelColor=18181B)&nbsp;
![Metasploit](https://img.shields.io/badge/Metasploit-7DCB40?style=flat-square&labelColor=18181B)

![Nmap](https://img.shields.io/badge/Nmap-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=ffffff&labelColor=18181B)&nbsp;
![VirusTotal](https://img.shields.io/badge/VirusTotal-394EFF?style=flat-square&logo=virustotal&logoColor=ffffff&labelColor=18181B)

</details>

<br/><br/>

```
FIELD PROFICIENCY                                          EST. SCALE
SOC & Detection Engineering     █████████████████░░░  85%
Threat Hunting & SOAR           ████████████████░░░░  80%
Network Defense & DPI           ██████████████████░░  90%
Offensive Security & Pentesting ███████████████░░░░░  75%
OSINT & Intelligence Fusion     ███████████████████░  95%
```

<br/><br/>

<!-- ══════════════════════════ COMBAT RECORD ══════════════════════════ -->

## 📈 Combat Record

<div align="center">

![Followers](https://img.shields.io/github/followers/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Stars earned](https://img.shields.io/github/stars/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Repositories](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Fusers%2Fkalidada18&query=%24.public_repos&label=repositories&style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![OSINT feeds](https://img.shields.io/badge/OSINT%20feeds-54%20active-3F3F46?style=flat-square&labelColor=18181B)

<br/><br/>

<img src="https://streak-stats.demolab.com/?user=kalidada18&theme=dark&background=0d0d0d&ring=FF1744&fire=FF1744&currStreakLabel=FF1744&sideLabels=9ca3af&dates=6b7280&sideNums=FF1744&currStreakNum=ffffff&hide_border=true" height="158" alt="GitHub contribution streak statistics" />

<br/><br/>

<img src="https://github-readme-stats.vercel.app/api?username=kalidada18&show_icons=true&hide_border=true&layout=compact&include_all_commits=true&bg_color=0d0d0d&title_color=FF1744&icon_color=FF1744&text_color=9ca3af&rank_icon=github" height="158" alt="GitHub profile activity statistics" />&nbsp;&nbsp;<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=kalidada18&show_icons=true&hide_border=true&layout=compact&langs_count=8&bg_color=0d0d0d&title_color=FF1744&text_color=9ca3af" height="158" alt="Most used programming languages" />

<br/><br/>

<img src="https://github-profile-trophy.vercel.app/?username=kalidada18&theme=onedark&no-frame=true&no-bg=true&column=7&margin-w=4&margin-h=4" width="100%" alt="GitHub profile achievement trophies" />

<br/><br/>

<img src="https://ghchart.rshah.org/FF1744/kalidada18" width="100%" alt="Yearly contribution heatmap in crimson" />

<br/>

<sub>full-year contribution heatmap</sub>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake.svg">
  <img alt="Snake contribution grid animation" src="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
</picture>

<br/><br/>

</div>

<!-- ══════════════════════ CONTACT UPLINK ══════════════════════ -->

## 🛰️ Contact Uplink

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-sujallamichhane.com.np-FF1744?style=for-the-badge&logo=firefox&logoColor=ffffff&labelColor=18181B)](https://sujallamichhane.com.np)&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sujal%20Lamichhane-0A66C2?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=18181B)](https://linkedin.com/in/sujal-lamichhane)

[![Email](https://img.shields.io/badge/Email-lamichhanesujal18%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=18181B)](mailto:lamichhanesujal18@gmail.com)&nbsp;&nbsp;
[![Threatbase](https://img.shields.io/badge/Threatbase-threatbase.qzz.io-FF1744?style=for-the-badge&logo=cloudflare&logoColor=ffffff&labelColor=18181B)](https://threatbase.qzz.io)

<br/><br/>

```
┌──────────────────────────────────────────────────────────┐
│  hack ethically. defend relentlessly.   -- sujal, 2026   │
└──────────────────────────────────────────────────────────┘
```

<br/>

<sub><img src="https://komarev.com/ghpvc/?username=kalidada18&style=flat-square&color=FF1744&label=VISITS" alt="Profile visitor count" /></sub>

</div>
