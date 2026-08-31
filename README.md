<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=C8F542&text=SUJAL%20LAMICHHANE&fontColor=0d0d0d&fontSize=42&fontAlignY=38&animation=twinkle" width="100%" />

<br/>

<img src="https://readme-typing-svg.demolab.com?font=IBM+Plex+Mono&weight=600&size=15&duration=3000&pause=1400&color=C8F542&center=true&vCenter=true&width=750&height=30&lines=Detection+Engineering+%C2%B7+SIEM+Ops+%C2%B7+Threat+Intel+%C2%B7+Ethical+Hacking;54+OSINT+Feeds.+Millions+of+IOCs.+threatbase.qzz.io;Go+Firewall+%E2%80%94+DPI+%2B+GeoIP+%2B+XGBoost+ML.;Unified+SOC+Framework+%C2%B7+Forbes+College+Capstone." />

<br/>

![](https://img.shields.io/badge/CEH%20v13-EC--Council-C8F542?style=flat-square&labelColor=111111&color=C8F542)&nbsp;
![](https://img.shields.io/badge/CryptoGen%20Nepal-Security%20Ops-333333?style=flat-square&labelColor=1a1a1a&color=333333)&nbsp;
![](https://img.shields.io/badge/Forbes%20College-B.Sc%20CS%20Cybersecurity-333333?style=flat-square&labelColor=1a1a1a&color=333333)&nbsp;
![](https://img.shields.io/badge/Location-Chitwan%2C%20Nepal-333333?style=flat-square&labelColor=1a1a1a&color=333333)&nbsp;
![](https://img.shields.io/badge/Status-Active%20Defense-C8F542?style=flat-square&labelColor=111111&color=C8F542)

</div>

---

## `$ cat profile.txt`

| key | value |
|:----|:------|
| `role` | Security Operations — CryptoGen Nepal |
| `cert` | CEH v13 — EC-Council |
| `edu` | B.Sc CS · Network Technology & Cybersecurity · Forbes College |
| `focus` | Detection Engineering · SIEM Ops · Threat Intel · Ethical Hacking |
| `stack` | Python · Bash · PowerShell · Go · TypeScript · SQL |
| `base` | Chitwan, Nepal |

<br/>

## `$ ls -la ./projects/`

### 🎓 Academic Research & Capstones

**[Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework](https://github.com/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework)** &nbsp;·&nbsp; `🏆 Main College Project`
> Enterprise-grade open-source SOC platform integrating Wazuh SIEM, Suricata NIDS, TheHive Incident Response, and MISP Threat Sharing. Features end-to-end event ingestion, automated log correlation, custom detection rulesets, and SOAR response playbooks.

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Endpoint / Net  │───>│ Suricata / Wazuh│───>│ Centralized     │
│ Telemetry       │    │ Agents (DPI/IDS)│    │ SIEM / Indexer  │
└─────────────────┘    └─────────────────┘    └────────┬────────┘
                                                       │
┌─────────────────┐    ┌─────────────────┐             │
│ TheHive + MISP  │<───│ n8n SOAR        │<────────────┘
│ Case & Intel    │    │ Automation Engine│
└─────────────────┘    └─────────────────┘
```

![Status](https://img.shields.io/badge/Project-Main%20College%20Capstone-C8F542?style=flat-square&labelColor=111111&color=C8F542)&nbsp;
![Stack](https://img.shields.io/badge/Stack-Wazuh%20%7C%20Suricata%20%7C%20TheHive%20%7C%20MISP-333333?style=flat-square&labelColor=111111)&nbsp;
![License](https://img.shields.io/badge/License-MIT-333333?style=flat-square&labelColor=111111)

---

**[Multi-Layer-Security-Integration-Based-on-SIEM-Solutions](https://github.com/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions)** &nbsp;·&nbsp; `⚡ Minor College Project`
> Defense-in-depth security architecture implementing multi-layered event monitoring. Integrates SIEM solutions with host-based detection (Sysmon), network logging, and real-time alert dispatch to mitigate perimeter and lateral threats.

```
├── Perimeter Layer   Network Firewall + Snort / Suricata IDS
├── Host Layer        Sysmon process telemetry + Logstash parsing
├── Analytics Layer   SIEM dashboards, threshold alerts & cross-log correlation
└── Dispatch Layer    Automated incident alert notifications
```

![Status](https://img.shields.io/badge/Project-Minor%20College%20Project-C8F542?style=flat-square&labelColor=111111&color=C8F542)&nbsp;
![Stack](https://img.shields.io/badge/Stack-SIEM%20%7C%20Sysmon%20%7C%20Logstash%20%7C%20Snort-333333?style=flat-square&labelColor=111111)

---

### 🛡️ Production & Security Engineering

**[threatbase](https://github.com/kalidada18/threatbase)** &nbsp;·&nbsp; `TypeScript · Python · React · Cloudflare`
> 54 OSINT feeds aggregated, deduplicated, and published as ready-to-use blocklists. Millions of IOCs across IP, IPv6, CIDR, Domain, URL, and SHA-256. Category-split feeds: C2, Botnet, Brute-Force, Tor, Spam, Exploit, Malware. No auth. No rate limits.

```
54 feeds → fetch · dedup · classify → Raw blocklists (IP/IPv6/CIDR/Domain/URL/Hash)
                                     → React dashboard — threatbase.qzz.io
                                     → Daily ZIP archives (retrospective hunting)
                                     → Chunked Git mirrors (~31 MiB chunks)
```

![Pipeline](https://github.com/kalidada18/threatbase/actions/workflows/update-feed.yml/badge.svg)&nbsp;
![IOCs](https://img.shields.io/badge/IOCs-Millions-C8F542?style=flat-square&labelColor=111111&color=C8F542)&nbsp;
![Feeds](https://img.shields.io/badge/Feeds-54-333333?style=flat-square&labelColor=111111)&nbsp;
![Live](https://img.shields.io/badge/Live-threatbase.qzz.io-333333?style=flat-square&labelColor=111111)

---

**[KaliWall](https://github.com/kalidada18/KaliWall)** &nbsp;·&nbsp; `Go · XGBoost · gopacket · VirusTotal`
> Open-source Linux firewall platform — live firewall control, DPI, GeoIP, VirusTotal threat intel, XGBoost ML anomaly detection. FortiGate-inspired dashboard + full CLI.

```
├── Core firewall   iptables / nftables / ufw — hot-swap at runtime
├── DPI module      HTTP · DNS · TLS · L3 telemetry · queue-pressure stats
├── ML anomaly      XGBoost scoring · override rules · CPU-first inference
├── Threat intel    VirusTotal IP reputation · cache + API key management
├── GeoIP           MaxMind .mmdb / IP2Location CSV · SSE stream
└── Dashboard + CLI FortiGate-inspired web UI · full CLI client
```

![Go](https://img.shields.io/badge/Go-1.21+-333333?style=flat-square&logo=go&logoColor=C8F542&labelColor=111111)&nbsp;
![Linux](https://img.shields.io/badge/Linux-only-333333?style=flat-square&logo=linux&logoColor=aaa&labelColor=111111)&nbsp;
![VT](https://img.shields.io/badge/VirusTotal-integrated-C8F542?style=flat-square&labelColor=111111&color=C8F542)

---

### 🔬 Security Research & Tools

| Repository | Tech | Objective |
|:-----------|:-----|:----------|
| **[honeypot-java](https://github.com/kalidada18/honeypot-java)** | Java | High-interaction decoy service logging unauthorized access vectors |
| **[dos-attack](https://github.com/kalidada18/dos-attack)** | Python | Volumetric & protocol stress testing suite for resilience validation |
| **[dns-spoofing-tool](https://github.com/kalidada18/dns-spoofing-tool)** | Python | ARP cache poisoning and DNS resolution redirection testing tool |

<br/>

## `$ git log --snake-grid`

<div align="center">

### 🐍 Contribution Activity Matrix

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake" src="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
</picture>

</div>

<br/>

## `$ ps aux --current-ops`

```
 TASK         SUBJECT                                            STATE
 ──────────────────────────────────────────────────────────────────────
 studying  →  Advanced Exploit Dev & Privilege Escalation       ACTIVE
 learning  →  Malware Analysis · Reverse Engineering            ACTIVE
 building  →  Unified SOC Lab — Wazuh + Splunk + n8n SOAR       ACTIVE
 building  →  Wazuh correlation engine → Splunk bridge           WIP
 training  →  HackTheBox · TryHackMe · PortSwigger Labs         ONGOING
```

<br/>

## `$ ls ./arsenal/`

**Offensive & Recon**

```
nmap / masscan          ██████████████████░░  90%
burp suite              ████████████████░░░░  80%
metasploit / msfvenom   ███████████████░░░░░  75%
wireshark / tcpdump     █████████████████░░░  85%
nikto / sqlmap          ██████████████░░░░░░  70%
```

**Defensive / SOC**

```
splunk / fortisiem      █████████████████░░░  88%
wazuh / logpoint        █████████████████░░░  85%
fortigate / palo alto   ████████████████░░░░  80%
n8n soar / automation   ██████████████░░░░░░  72%
snort / suricata        ███████████████░░░░░  75%
```

**Languages & Platforms**

![Python](https://img.shields.io/badge/Python-111111?style=flat-square&logo=python&logoColor=C8F542)&nbsp;
![Go](https://img.shields.io/badge/Go-111111?style=flat-square&logo=go&logoColor=C8F542)&nbsp;
![TypeScript](https://img.shields.io/badge/TypeScript-111111?style=flat-square&logo=typescript&logoColor=C8F542)&nbsp;
![Bash](https://img.shields.io/badge/Bash-111111?style=flat-square&logo=gnubash&logoColor=C8F542)&nbsp;
![Linux](https://img.shields.io/badge/Linux-111111?style=flat-square&logo=linux&logoColor=C8F542)&nbsp;
![Docker](https://img.shields.io/badge/Docker-111111?style=flat-square&logo=docker&logoColor=C8F542)&nbsp;
![Splunk](https://img.shields.io/badge/Splunk-111111?style=flat-square&logo=splunk&logoColor=C8F542)&nbsp;
![React](https://img.shields.io/badge/React-111111?style=flat-square&logo=react&logoColor=C8F542)

<br/>

## `$ cat cert.txt`

```
 ┌───────────────────────────────────────────────────────────┐
 │  CEH v13 — Certified Ethical Hacker · EC-Council          │
 │                                                           │
 │  penetration-testing  ·  recon  ·  exploitation           │
 │  vulnerability-assessment  ·  offensive-security          │
 └───────────────────────────────────────────────────────────┘
```

<br/>

## `$ uptime --stats`

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=kalidada18&show_icons=true&theme=dark&bg_color=0d0d0d&title_color=C8F542&icon_color=C8F542&text_color=999999&border_color=1a1a1a&count_private=true&include_all_commits=true" height="170" alt="GitHub Stats" />
&nbsp;
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=kalidada18&layout=compact&theme=dark&bg_color=0d0d0d&title_color=C8F542&text_color=999999&border_color=1a1a1a&hide=html,css" height="170" alt="Top Languages" />

<br/><br/>

<img src="https://streak-stats.demolab.com/?user=kalidada18&theme=dark&background=0d0d0d&ring=C8F542&fire=C8F542&currStreakLabel=C8F542&sideLabels=aaaaaa&dates=aaaaaa&stroke=1a1a1a&sideNums=C8F542&currStreakNum=ffffff" height="165" alt="Streak Stats" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=kalidada18&theme=react-dark&bg_color=0d0d0d&color=C8F542&line=C8F542&point=ffffff&area=true&hide_border=false&border_color=1a1a1a&custom_title=SOC+ENGINEERING+CONTRIBUTION+GRAPH" width="100%" alt="Activity Graph" />

</div>

<br/>

## `$ netstat -contact`

```
 portfolio   sujallamichhane.com.np
 github      github.com/kalidada18
 linkedin    linkedin.com/in/sujal-lamichhane
 email       lamichhanesujal18@gmail.com
 threatbase  threatbase.qzz.io
```

<br/>

<div align="center">
<sub><code>hack ethically. defend relentlessly.</code> &nbsp;·&nbsp; sujal lamichhane · 2026</sub>
</div>
