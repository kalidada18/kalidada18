<div align="center">

<!-- ══════════════════════════════ HERO ══════════════════════════════ -->

<h1>SUJAL LAMICHHANE</h1>

<h3>Cybersecurity Professional &nbsp;·&nbsp; Security Researcher &nbsp;·&nbsp; Certified Ethical Hacker</h3>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=17&duration=2600&pause=1000&color=FF1744&center=true&vCenter=true&repeat=true&width=760&height=42&lines=%24+whoami+%E2%86%92+Security+Operations+Analyst;Hunting+threats.+Engineering+detections.+Shipping+defenses.;%24+./threat_hunt+--scope+SIEM+--mode+proactive;OSINT+%C2%B7+Malware+Analysis+%C2%B7+Detection+Engineering+%C2%B7+SOAR" alt="Terminal-style animated typing introduction of Sujal Lamichhane" />

<br/>

![Threatbase status](https://img.shields.io/website?style=flat-square&up_color=39d353&upMessage=threatbase%20LIVE&down_color=3F3F46&downMessage=threatbase%20DOWN&labelColor=18181B&url=https://threatbase.qzz.io)
![Open to collaboration](https://img.shields.io/badge/open%20to%20collaboration-3F3F46?style=flat-square&labelColor=18181B)
![EC Council CEH](https://img.shields.io/badge/EC_Council-CEH-3F3F46?style=flat-square&labelColor=18181B)

<br/><br/>

</div>

<!-- ═══════════════════════ TERMINAL BRIEFING ═══════════════════════ -->

## 📋 Briefing

```bash
$ ssh sujal@kalidada18.dev -p 2222
┌──(sujal㉿kali)-[~]
└─$ cat ./profile.brief
```

> I design, break, and harden security systems. Certified Ethical Hacker building
> production-grade detection pipelines, open-source SOC infrastructure, and an OSINT
> platform that processes millions of IOCs.

<sub><code>B.Sc Computer Science - Network Technology and Cybersecurity</code></sub>

| Core disciplines | Research interests |
|:-----------------|:-------------------|
| Detection Engineering | Adversary Emulation (ATT&CK) |
| SIEM Telemetry and Correlation | Open-Source SOC Orchestration |
| SOAR Automation | OSINT and Threat Feed Intelligence |
| Threat Hunting | ML-Assisted Network Defense |
| Penetration Testing | Deception Tech and Honeypot Telemetry |

<!-- ════════════════════════════ ARSENAL ══════════════════════════════ -->

## 🛠️ Arsenal

#### 🏆 Capstone · Unified Open-Source SOC Framework

**[Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework](https://github.com/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework)**

![Stars](https://img.shields.io/github/stars/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Forks](https://img.shields.io/github/forks/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=3F3F46&labelColor=18181B)&nbsp;
![Last commit](https://img.shields.io/github/last-commit/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&color=9ca3af&labelColor=18181B)

`Wazuh / Suricata / Shuffle / TheHive / MISP`

> Final-year capstone: an enterprise-grade SOC built entirely from open source,
> wiring Wazuh SIEM, Suricata NIDS, Shuffle SOAR, TheHive, and MISP into one
> detection, correlation, and automated triage pipeline.

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

<br/>

<table width="100%">
<tr>
<td width="62%" valign="top">

#### 🌐 Threatbase · production OSINT platform

**[threatbase](https://github.com/kalidada18/threatbase)**

![Stars](https://img.shields.io/github/stars/kalidada18/threatbase?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Feeds](https://img.shields.io/badge/feeds-54-3F3F46?style=flat-square&labelColor=18181B)&nbsp;
![Pipeline](https://img.shields.io/github/actions/workflow/status/kalidada18/threatbase/update-feed.yml?style=flat-square&label=feeds&labelColor=18181B)&nbsp;
![Uptime](https://img.shields.io/website?style=flat-square&up_color=39d353&upMessage=LIVE&down_color=3F3F46&downMessage=DOWN&labelColor=18181B&url=https://threatbase.qzz.io)

`TypeScript / Python / React / Cloudflare`

> High-throughput OSINT aggregation consolidating **54 threat feeds** into
> deduplicated IP, CIDR, domain, URL, and SHA-256 blocklists with live
> dashboarding and retrospective archives.

```
54 Feeds ──> Fetch and Classify ──> Raw IOC Blocklists (IP / Domain / Hash)
     │                                   ├──> Live Dashboard · threatbase.qzz.io
     └───────────────────────────────────┴──> Retrospective ZIP Archives & Git Mirrors
```

</td>
<td width="38%" valign="top" align="center">

<a href="https://star-history.com/#kalidada18/threatbase&Date">
<img src="https://api.star-history.com/svg?repos=kalidada18/threatbase&type=Date" width="100%" alt="Threatbase star growth chart over time" />
</a>

</td>
</tr>
<tr>
<td colspan="2" height="20"></td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🛡️ KaliWall · ML network defense

**[KaliWall](https://github.com/kalidada18/KaliWall)**

![Stars](https://img.shields.io/github/stars/kalidada18/KaliWall?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Go](https://img.shields.io/badge/Go-1.21%2B-3F3F46?style=flat-square&logo=go&logoColor=FF1744&labelColor=18181B)

`Go / Linux / XGBoost`

> A Linux firewall with real-time deep packet inspection, GeoIP filtering,
> VirusTotal intel lookups, and XGBoost anomaly scoring behind a
> FortiGate-inspired console.

</td>
<td width="50%" valign="top">

#### ⚡ Multi-Layer SIEM · defense in depth

**[Multi-Layer-Security-Integration-Based-on-SIEM-Solutions](https://github.com/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions)**

![Stars](https://img.shields.io/github/stars/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![SIEM](https://img.shields.io/badge/Splunk%20%2F%20Elastic-3F3F46?style=flat-square&labelColor=18181B)

`Splunk / Elastic / Sysmon / Logstash`

```
├── Perimeter    firewall + Snort/Suricata IDS
├── Host         Sysmon telemetry + Logstash pipeline
├── Analytics    SIEM correlation and dashboards
└── Response     automated incident alerting
```

</td>
</tr>
</table>

<!-- ═══════════════════════════ RESEARCH ══════════════════════════════ -->

## 🔬 Research

| Focus | Project | Stack |
|:------|:--------|:------|
| Deception telemetry and attacker profiling | **[honeypot-java](https://github.com/kalidada18/honeypot-java)** | `Java` |
| Volumetric and protocol resilience testing | **[dos-attack](https://github.com/kalidada18/dos-attack)** | `Python` |
| ARP poisoning and rogue DNS simulation | **[dns-spoofing-tool](https://github.com/kalidada18/dns-spoofing-tool)** | `Python` |

<sub>Research builds are published for defensive study, isolated lab environments, and authorized testing only.</sub>

<!-- ═══════════════════════════ TOOLING ═══════════════════════════════ -->

## 🧰 Tooling

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,go,ts,js,bash,powershell,java,sql&theme=dark" alt="Programming languages: Python, Go, TypeScript, JavaScript, Bash, PowerShell, Java, SQL. Hover to animate" />
  </a>
</p>
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=linux,kali,docker,git,github,cloudflare,react,mysql&theme=dark" alt="Platform stack: Linux, Kali, Docker, Git, GitHub, Cloudflare, React, MySQL. Hover to animate" />
  </a>
</p>

<details open>
<summary><b>📡 SOC &amp; Defensive Engineering</b></summary>
<br/>

![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat-square&logo=splunk&logoColor=FF1744&labelColor=18181B)&nbsp;
![Elastic](https://img.shields.io/badge/Elastic_SIEM-005571?style=flat-square&logo=elasticcloud&logoColor=ffffff&labelColor=18181B)&nbsp;
![Wazuh](https://img.shields.io/badge/Wazuh-00f58a?style=flat-square&labelColor=18181B)&nbsp;
![Shuffle SOAR](https://img.shields.io/badge/Shuffle_SOAR-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![TheHive](https://img.shields.io/badge/TheHive-F7A41D?style=flat-square&labelColor=18181B)&nbsp;
![MISP](https://img.shields.io/badge/MISP-e74343?style=flat-square&labelColor=18181B)&nbsp;
![Suricata](https://img.shields.io/badge/Suricata-88c070?style=flat-square&labelColor=18181B)&nbsp;
![Snort](https://img.shields.io/badge/Snort-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![FortiGate](https://img.shields.io/badge/FortiGate-EE3124?style=flat-square&logo=fortinet&logoColor=ffffff&labelColor=18181B)&nbsp;
![Sysmon](https://img.shields.io/badge/Sysmon-0078d4?style=flat-square&logo=windows&logoColor=ffffff&labelColor=18181B)

</details>

<details open>
<summary><b>⚔️ Offensive Security &amp; Testing</b></summary>
<br/>

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=ffffff&labelColor=18181B)&nbsp;
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square&labelColor=18181B)&nbsp;
![Metasploit](https://img.shields.io/badge/Metasploit-7DCB40?style=flat-square&labelColor=18181B)&nbsp;
![Nmap](https://img.shields.io/badge/Nmap-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=ffffff&labelColor=18181B)&nbsp;
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-001D2C?style=flat-square&logo=owasp&logoColor=ffffff&labelColor=18181B)&nbsp;
![VirusTotal](https://img.shields.io/badge/VirusTotal-394EFF?style=flat-square&logo=virustotal&logoColor=ffffff&labelColor=18181B)

</details>

<br/>

```
FIELD PROFICIENCY                                          EST. SCALE
SOC & Detection Engineering     █████████████████░░░  85%
Threat Hunting & SOAR           ████████████████░░░░  80%
Network Defense & DPI           ██████████████████░░  90%
Offensive Security & Pentesting ███████████████░░░░░  75%
OSINT & Intelligence Fusion     ███████████████████░  95%
```

<!-- ══════════════════════════ COMBAT RECORD ══════════════════════════ -->

## 📈 Combat Record

<div align="center">

![Followers](https://img.shields.io/github/followers/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Stars earned](https://img.shields.io/github/stars/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Repositories](https://img.shields.io/github/repos/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![OSINT feeds](https://img.shields.io/badge/OSINT%20feeds-54%20active-3F3F46?style=flat-square&labelColor=18181B)

<br/><br/>

<img src="https://streak-stats.demolab.com/?user=kalidada18&theme=dark&background=0d0d0d&ring=FF1744&fire=FF1744&currStreakLabel=FF1744&sideLabels=9ca3af&dates=6b7280&sideNums=FF1744&currStreakNum=ffffff&hide_border=true" height="158" alt="GitHub contribution streak statistics" />

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

</div>

<!-- ══════════════════════ CONTACT UPLINK ══════════════════════ -->

## 🛰️ Contact Uplink

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-sujallamichhane.com.np-FF1744?style=for-the-badge&logo=firefox&logoColor=ffffff&labelColor=18181B)](https://sujallamichhane.com.np)&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sujal%20Lamichhane-0A66C2?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=18181B)](https://linkedin.com/in/sujal-lamichhane)&nbsp;
[![Email](https://img.shields.io/badge/Email-lamichhanesujal18%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=18181B)](mailto:lamichhanesujal18@gmail.com)&nbsp;
[![Threatbase](https://img.shields.io/badge/Threatbase-threatbase.qzz.io-FF1744?style=for-the-badge&logo=cloudflare&logoColor=ffffff&labelColor=18181B)](https://threatbase.qzz.io)

<br/>

```
┌──────────────────────────────────────────────────────────┐
│  hack ethically. defend relentlessly.   -- sujal, 2026   │
└──────────────────────────────────────────────────────────┘
```

<sub><img src="https://komarev.com/ghpvc/?username=kalidada18&style=flat-square&color=FF1744&label=VISITS" alt="Profile visitor count" /></sub>

</div>
