<!-- ══════════════════════════════ HERO ══════════════════════════════ -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/main/assets/hero-wordmark-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/main/assets/hero-wordmark-light.svg">
  <img alt="sujal lamichhane, cybersecurity practitioner" src="https://raw.githubusercontent.com/kalidada18/kalidada18/main/assets/hero-wordmark-dark.svg" width="100%" />
</picture>

A cybersecurity practitioner working across **SOC operations**, threat triage, and
**detection engineering**, with hands-on time in **FortiSIEM**, **LogPoint**,
**LogRhythm**, and **Wazuh**.

- **currently:** building detection pipelines and open-source SOC infrastructure in an isolated lab
- **also in my wheelhouse:** incident response, threat hunting and adversary emulation (ATT&CK)
- **ask me about:** alert triage, correlation rules, or hardening Linux
- **open to:** SOC roles, security research and open-source collaboration

[![Portfolio](https://img.shields.io/badge/Portfolio-sujallamichhane.com.np-FF1744?style=flat-square&logo=firefox&logoColor=ffffff&labelColor=18181B)](https://sujallamichhane.com.np)&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sujal%20Lamichhane-0A66C2?style=flat-square&logo=linkedin&logoColor=ffffff&labelColor=18181B)](https://linkedin.com/in/sujal-lamichhane)&nbsp;&nbsp;
[![Email](https://img.shields.io/badge/Email-lamichhanesujal18%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=ffffff&labelColor=18181B)](mailto:lamichhanesujal18@gmail.com)

<br/>

<!-- ═══════════════════════════ ./briefing ═══════════════════════════ -->

## ▸ ./briefing

```bash
┌──(sujal㉿kali)-[~]
└─$ cat ./profile.brief
```

```yaml
# ./profile.brief
operator: sujal lamichhane
cert: EC-Council Certified Ethical Hacker
education: B.Sc Computer Science, Network Technology and Cybersecurity
domains:
  - soc operations
  - threat triage
  - detection engineering
kill_chain: ingest → detect → triage → contain → report
siem_hands_on: FortiSIEM, LogPoint, LogRhythm, Wazuh
scope: isolated lab, authorized testing only
```

<br/>

| Discipline | Execution | Primary stack |
|:-----------|:----------|:--------------|
| **SOC operations** | alert triage, enrichment, escalation, shift handoff | `FortiSIEM` `LogPoint` `LogRhythm` |
| **Detection engineering** | correlation rules, dashboards, ATT&CK mapping | `Wazuh` `Splunk` `Elastic` |
| **Incident response** | case ownership, playbook design, SOAR automation | `TheHive` `Shuffle` `MISP` |
| **Threat hunting** | hypothesis-led hunts on endpoint and network telemetry | `Sysmon` `Suricata` `Wireshark` |
| **Offensive testing** | authorized assessments and hardening follow-through | `Kali` `Burp Suite` `Nmap` |

<br/>

<sub>**Research vectors:** adversary emulation (ATT&CK), open-source SOC orchestration, ML-assisted network defense, deception and honeypot telemetry.</sub>

<br/><br/>

<!-- ══════════════════════════ ./operations ══════════════════════════ -->

## ▸ ./operations

**Minor project · Multi-Layer Security Integration Based on a SIEM Solution**

**[Multi-Layer-Security-Integration-Based-on-SIEM-Solutions](https://github.com/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions)**
<sub><code>pfSense · Suricata · Wazuh · OWASP Juice Shop</code></sub>

![Stars](https://img.shields.io/github/stars/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Forks](https://img.shields.io/github/forks/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions?style=flat-square&logo=github&color=3F3F46&labelColor=18181B)&nbsp;
![Last commit](https://img.shields.io/github/last-commit/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions?style=flat-square&color=3F3F46&labelColor=18181B)

> Defense-in-depth lab: attacks simulated with Kali Linux and OWASP Juice Shop,
> detected in real time across pfSense and Suricata layers, correlated and
> analyzed through a SOC-oriented Wazuh SIEM pipeline.

<br/>

**Major project · Unified Open-Source SOC Framework**

**[Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework](https://github.com/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework)**
<sub><code>Wazuh · Suricata · Shuffle · TheHive · MISP</code></sub>

![Stars](https://img.shields.io/github/stars/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Forks](https://img.shields.io/github/forks/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=3F3F46&labelColor=18181B)&nbsp;
![Last commit](https://img.shields.io/github/last-commit/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&color=3F3F46&labelColor=18181B)

> Final-year capstone: an enterprise-grade SOC assembled entirely from open
> source. detection → enrichment → automated blocking → case handling in one
> incident workflow.

<br/><br/>

`adversary emulation`

- **[ghostimplant](https://github.com/kalidada18/ghostimplant)** `C++` · adversary emulation research framework
- **[Ransomware-Simulation](https://github.com/kalidada18/Ransomware-Simulation)** `Python` · safe ransomware behavior simulation for detection validation
- **[dns-spoofing-tool](https://github.com/kalidada18/dns-spoofing-tool)** `Python` · ARP and DNS spoofing for education and authorized testing

`network defense`

- **[DNS-sink-hole](https://github.com/kalidada18/DNS-sink-hole)** `Python` · Flask and dnsmasq sinkhole that blackholes malicious domains
- **[trafficscannerforrats](https://github.com/kalidada18/trafficscannerforrats)** `Python` · passive PCAP analyzer flagging trojan beaconing and DNS tunneling
- **[honeypot-java](https://github.com/kalidada18/honeypot-java)** `Java` · multi-protocol honeypot logging SSH, HTTP, FTP and RDP tradecraft

`infrastructure & monitoring`

- **[WatchTower](https://github.com/kalidada18/WatchTower)** `Python` · async uptime, SSL and content-change monitoring with alerts

<br/><br/>

<!-- ══════════════════════════ ./toolchain ═══════════════════════════ -->

## ▸ ./toolchain

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,go,ts,js,bash,powershell,java,sql&theme=dark" alt="Programming languages: Python, Go, TypeScript, JavaScript, Bash, PowerShell, Java, SQL" />
  </a>
  <br/>
  <sub><code>languages // scripting</code></sub>
</p>

<br/>

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=linux,kali,docker,git,github,cloudflare,react,mysql&theme=dark" alt="Platform stack: Linux, Kali, Docker, Git, GitHub, Cloudflare, React, MySQL" />
  </a>
  <br/>
  <sub><code>platform // infrastructure</code></sub>
</p>

<br/>

<details open>
<summary><b>soc &amp; defensive engineering</b></summary>
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
<summary><b>offensive security &amp; testing</b></summary>
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

<!-- ═══════════════════════ ./combat_record ══════════════════════════ -->

## ▸ ./combat_record

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=kalidada18&show_icons=true&hide_border=true&bg_color=0d1117&title_color=FF1744&icon_color=FF1744&text_color=e4e4e7&include_all_commits=true&count_private=true" height="165" alt="GitHub statistics: stars, commits, pull requests, contributions" />&nbsp;&nbsp;<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=kalidada18&layout=compact&hide_border=true&bg_color=0d1117&title_color=FF1744&text_color=e4e4e7&langs_count=8" height="165" alt="Top languages by usage" />

<br/><br/>

<img src="https://streak-stats.demolab.com/?user=kalidada18&theme=dark&background=0d1117&ring=FF1744&fire=FF1744&currStreakLabel=FF1744&sideLabels=9ca3af&dates=6b7280&sideNums=FF1744&currStreakNum=ffffff&hide_border=true" height="165" alt="GitHub contribution streak statistics" />

<br/><br/>

<img src="https://ghchart.rshah.org/FF1744/kalidada18" width="100%" alt="Yearly contribution heatmap in crimson" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake.svg">
  <img alt="Snake contribution grid animation" src="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
</picture>

<br/><br/>

</div>

---

<div align="center">

```
┌──────────────────────────────────────────────────────────┐
│  hack ethically. defend relentlessly.   -- sujal, 2026   │
└──────────────────────────────────────────────────────────┘
```

<br/>

<sub><img src="https://komarev.com/ghpvc/?username=kalidada18&style=flat-square&color=FF1744&label=VISITS" alt="Profile visitor count" /></sub>

</div>
