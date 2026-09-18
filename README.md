<div align="center">

<table width="100%">
<tr>
<td width="58%" valign="middle" align="left">

<img src="https://wsrv.nl/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fkalidada18%2Fkalidada18%2Fmain%2Fassets%2Favatar.jpeg&mask=circle&w=260&h=260&output=png" width="112" alt="Portrait of Sujal Lamichhane" align="left" hspace="18"/>

# SUJAL<br/>LAMICHHANE

<sub><code>Cybersecurity Professional // Security Researcher // CEH</code></sub>

<br/>

[![Portfolio](https://img.shields.io/badge/sujallamichhane.com.np-FF1744?style=for-the-badge&logo=firefox&logoColor=ffffff&labelColor=18181B)](https://sujallamichhane.com.np)&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=18181B)](https://linkedin.com/in/sujal-lamichhane)&nbsp;
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=18181B)](mailto:lamichhanesujal18@gmail.com)

</td>
<td width="42%" valign="middle" align="left">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=15&duration=2600&pause=1000&color=FF1744&repeat=true&width=430&height=34&lines=%24+whoami+%E2%86%92+Security+Operations+Analyst;Hunting+threats.+Engineering+detections.;%24+./threat_hunt+--scope+SIEM+--mode+proactive;OSINT+%2F+SOAR+%2F+Malware+Analysis+%2F+NIDS" alt="Rotating terminal ticker: security operations analyst, threat hunting, detection engineering" />

<br/>

![Threatbase status](https://img.shields.io/website?style=flat-square&up_color=39d353&upMessage=threatbase%20LIVE&down_color=3F3F46&downMessage=threatbase%20DOWN&labelColor=18181B&url=https://threatbase.qzz.io)
![Open to collaboration](https://img.shields.io/badge/open%20to%20collaboration-3F3F46?style=flat-square&labelColor=18181B)

<br/>

<sub><code>Chitwan, Nepal</code></sub>

</td>
</tr>
</table>

</div>

## Briefing

```bash
$ ssh sujal@kalidada18.dev -p 2222
┌──(sujal㉿kali)-[~]
└─$ cat ./profile.brief
```

> I design, break, and harden security systems. Certified Ethical Hacker building
> production-grade detection pipelines, open-source SOC infrastructure, and an OSINT
> platform that processes millions of IOCs. B.Sc Computer Science, specializing in
> Network Technology and Cybersecurity.

| Core disciplines | Research interests |
|:-----------------|:-------------------|
| Detection Engineering | Adversary Emulation (ATT&CK) |
| SIEM Telemetry and Correlation | Open-Source SOC Orchestration |
| SOAR Automation | OSINT and Threat Feed Intelligence |
| Threat Hunting | ML-Assisted Network Defense |
| Penetration Testing | Deception Tech and Honeypot Telemetry |

## Arsenal

**Unified Open-Source SOC Framework** · capstone research, shipped as code
**[Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework](https://github.com/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework)**

![Stars](https://img.shields.io/github/stars/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Forks](https://img.shields.io/github/forks/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=3F3F46&labelColor=18181B)&nbsp;
![Last commit](https://img.shields.io/github/last-commit/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&color=9ca3af&labelColor=18181B)

An enterprise-grade SOC built entirely from open source: Wazuh SIEM, Suricata NIDS,
Shuffle SOAR, TheHive, and MISP wired into one detection, correlation, and automated
triage pipeline.

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

**Threatbase** · production OSINT platform
**[threatbase](https://github.com/kalidada18/threatbase)**

![Stars](https://img.shields.io/github/stars/kalidada18/threatbase?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Feed pipeline](https://github.com/kalidada18/threatbase/actions/workflows/update-feed.yml/badge.svg?label=feeds&labelColor=18181B)&nbsp;
![Uptime](https://img.shields.io/website?style=flat-square&up_color=39d353&upMessage=LIVE&down_color=3F3F46&downMessage=DOWN&labelColor=18181B&url=https://threatbase.qzz.io)

`TypeScript / Python / React / Cloudflare`
54 threat feeds consolidated into deduplicated IP, CIDR, domain, URL, and SHA-256
blocklists with live dashboarding and retrospective archives.

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

**KaliWall** · ML network defense
**[KaliWall](https://github.com/kalidada18/KaliWall)**

![Stars](https://img.shields.io/github/stars/kalidada18/KaliWall?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Go](https://img.shields.io/badge/Go-1.21%2B-3F3F46?style=flat-square&logo=go&logoColor=FF1744&labelColor=18181B)

A Linux firewall with real-time deep packet inspection, GeoIP filtering, VirusTotal
intel lookups, and XGBoost anomaly scoring behind a FortiGate-inspired console.

</td>
<td width="50%" valign="top">

**Multi-Layer SIEM Integration** · defense in depth
**[Multi-Layer-Security-Integration-Based-on-SIEM-Solutions](https://github.com/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions)**

![Stars](https://img.shields.io/github/stars/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![SIEM](https://img.shields.io/badge/Splunk%20%2F%20Elastic-3F3F46?style=flat-square&labelColor=18181B)

```
├── Perimeter    firewall + Snort/Suricata IDS
├── Host         Sysmon telemetry + Logstash pipeline
├── Analytics    SIEM correlation and dashboards
└── Response     automated incident alerting
```

</td>
</tr>
</table>

## Research

| Focus | Project | Stack |
|:------|:--------|:------|
| Deception telemetry and attacker profiling | **[honeypot-java](https://github.com/kalidada18/honeypot-java)** | `Java` |
| Volumetric and protocol resilience testing | **[dos-attack](https://github.com/kalidada18/dos-attack)** | `Python` |
| ARP poisoning and rogue DNS simulation | **[dns-spoofing-tool](https://github.com/kalidada18/dns-spoofing-tool)** | `Python` |

## Tooling

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,go,ts,js,bash,powershell,java,sql&theme=dark" alt="Languages: Python, Go, TypeScript, JavaScript, Bash, PowerShell, Java, SQL. Hover to animate" />
  </a>
</p>
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=linux,kali,docker,git,github,cloudflare,react,mysql&theme=dark" alt="Platforms: Linux, Kali, Docker, Git, GitHub, Cloudflare, React, MySQL. Hover to animate" />
  </a>
</p>

<details open>
<summary><b>SOC and defensive engineering</b></summary>
<br/>

![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat-square&logo=splunk&logoColor=FF1744)&nbsp;
![Elastic](https://img.shields.io/badge/Elastic_SIEM-005571?style=flat-square&logo=elasticcloud&logoColor=ffffff)&nbsp;
![Wazuh](https://img.shields.io/badge/Wazuh-00f58a?style=flat-square&labelColor=18181B)&nbsp;
![Shuffle SOAR](https://img.shields.io/badge/Shuffle_SOAR-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![TheHive](https://img.shields.io/badge/TheHive-F7A41D?style=flat-square&labelColor=18181B)&nbsp;
![MISP](https://img.shields.io/badge/MISP-e74343?style=flat-square&labelColor=18181B)&nbsp;
![Suricata](https://img.shields.io/badge/Suricata-88c070?style=flat-square&labelColor=18181B)&nbsp;
![Snort](https://img.shields.io/badge/Snort-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![FortiGate](https://img.shields.io/badge/FortiGate-EE3124?style=flat-square&logo=fortinet&logoColor=ffffff)&nbsp;
![Sysmon](https://img.shields.io/badge/Sysmon-0078d4?style=flat-square&logo=windows&logoColor=ffffff)

</details>

<details open>
<summary><b>Offensive security and testing</b></summary>
<br/>

![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=ffffff)&nbsp;
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square&labelColor=18181B)&nbsp;
![Metasploit](https://img.shields.io/badge/Metasploit-7DCB40?style=flat-square&labelColor=18181B)&nbsp;
![Nmap](https://img.shields.io/badge/Nmap-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=ffffff)&nbsp;
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-001D2C?style=flat-square&logo=owasp&logoColor=ffffff)&nbsp;
![VirusTotal](https://img.shields.io/badge/VirusTotal-394EFF?style=flat-square&logo=virustotal&logoColor=ffffff)

</details>

<br/>

```
SOC & DEFENSIVE ENGINEERING
Splunk / FortiSIEM        █████████████████░░  88%
Wazuh / Elastic SIEM      █████████████████░░  88%
Shuffle SOAR Automation   █████████████████░░  88%
Suricata / Snort NIDS     ███████████████░░░░  78%
FortiGate / Palo Alto     ████████████████░░░  80%

OFFENSIVE SECURITY & PENETRATION TESTING
Nmap / Masscan            ██████████████████░  90%
Burp Suite Professional   ████████████████░░░  80%
Wireshark / Packet DPI    █████████████████░░  85%
Metasploit Framework      ███████████████░░░░  75%
```

## Record

<div align="center">

![Followers](https://img.shields.io/github/followers/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Stars earned](https://img.shields.io/github/stars/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Repositories](https://img.shields.io/github/repos/kalidada18?style=flat-square&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Contributions](https://img.shields.io/badge/contributions-1%2C390%2B-3F3F46?style=flat-square&labelColor=18181B)

<br/><br/>

<img src="https://streak-stats.demolab.com/?user=kalidada18&theme=dark&background=0d0d0d&ring=FF1744&fire=FF1744&currStreakLabel=FF1744&sideLabels=9ca3af&dates=6b7280&sideNums=FF1744&currStreakNum=ffffff&hide_border=true" height="158" alt="GitHub contribution streak: current and longest streak with total contributions" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake.svg">
  <img alt="Animated snake tracing the GitHub contribution grid" src="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
</picture>

</div>

## Contact

<div align="center">

```
┌──────────────────────────────────────────────────────────┐
│  hack ethically. defend relentlessly.   -- sujal, 2026   │
└──────────────────────────────────────────────────────────┘
```

[![Email](https://img.shields.io/badge/lamichhanesujal18@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=18181B)](mailto:lamichhanesujal18@gmail.com)&nbsp;
[![Threatbase](https://img.shields.io/badge/threatbase.qzz.io-FF1744?style=for-the-badge&logo=cloudflare&logoColor=ffffff&labelColor=18181B)](https://threatbase.qzz.io)

<br/>

<sub><img src="https://komarev.com/ghpvc/?username=kalidada18&style=flat-square&color=FF1744&label=VISITS" alt="Profile visitor count" /></sub>

</div>
