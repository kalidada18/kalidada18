<div align="center">

<!-- ══════════════════════════════ HERO ══════════════════════════════ -->

<p>
  <a href="https://sujallamichhane.com.np">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://wsrv.nl/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fkalidada18%2Fkalidada18%2Fmain%2Fassets%2Favatar.jpeg&mask=circle&w=340&h=340&output=png">
      <source media="(prefers-color-scheme: light)" srcset="https://wsrv.nl/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fkalidada18%2Fkalidada18%2Fmain%2Fassets%2Favatar.jpeg&mask=circle&w=340&h=340&output=png">
      <img src="assets/avatar.jpeg" width="168" alt="Sujal Lamichhane - Cybersecurity Professional and Security Researcher" align="center" />
    </picture>
  </a>
</p>

<h1>SUJAL LAMICHHANE</h1>

<code>SECURITY OPERATIONS</code> &nbsp;·&nbsp; <code>THREAT RESEARCH</code> &nbsp;·&nbsp; <code>CEH</code>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=16&duration=2600&pause=1000&color=FF1744&center=true&vCenter=true&repeat=true&width=720&height=40&lines=%24+whoami+%E2%86%92+Security+Operations+Analyst;Hunting+threats.+Engineering+detections.+Shipping+defenses.;%24+./threat_hunt+--scope+SIEM+--mode+proactive;OSINT+%C2%B7+Detection+Engineering+%C2%B7+SOAR+Automation+%C2%B7+Malware+Analysis" alt="Animated terminal-style rotating introduction: security operations analyst, threat hunting, detection engineering" />

<br/>

![CEH Certified](https://img.shields.io/badge/CEH-EC--Council-FF1744?style=for-the-badge&logo=edx&logoColor=ffffff&labelColor=18181B)&nbsp;
![Threatbase Live](https://img.shields.io/website?style=for-the-badge&up_color=FF1744&upMessage=threatbase%20LIVE&downMessage=threatbase%20DOWN&down_color=3F3F46&label=OSINT%20Platform&labelColor=18181B&url=https://threatbase.qzz.io)&nbsp;
![Open to Collaboration](https://img.shields.io/badge/Status-Open%20to%20Collaboration-39d353?style=for-the-badge&labelColor=18181B)

<br/><br/>

</div>

<!-- ═══════════════════ 01 // OPERATOR BRIEFING ═══════════════════ -->

## <code>01&nbsp;//</code> OPERATOR BRIEFING

```bash
$ ssh sujal@kalidada18.dev -p 2222
┌──(sujal㉿kali)-[~]
└─$ cat ./profile.brief
```

> **Independent Cybersecurity Professional & Security Researcher** based in Chitwan, Nepal.
> I design, break, and harden security systems — building production-grade detection pipelines,
> open-source SOC infrastructure, and OSINT platforms that process **millions of IOCs**.
> Certified Ethical Hacker (CEH) with a B.Sc in Computer Science specializing in
> Network Technology & Cybersecurity.

| CORE DISCIPLINES | RESEARCH INTERESTS |
|:-----------------|:-------------------|
| ▸ Detection Engineering | ▸ Adversary Emulation (ATT&CK) |
| ▸ SIEM Telemetry & Correlation | ▸ Open-Source SOC Orchestration |
| ▸ SOAR Automation | ▸ OSINT & Threat Feed Intelligence |
| ▸ Threat Hunting & Intelligence | ▸ ML-Assisted Network Defense |
| ▸ Penetration Testing | ▸ Deception Tech & Honeypot Telemetry |

---

<!-- ═══════════════════ 02 // FIELD ARSENAL ═══════════════════ -->

## <code>02&nbsp;//</code> FIELD ARSENAL <sub>live repo telemetry · auto-synced</sub>

<table width="100%">
<tr>
<td width="50%" valign="top">

#### Unified Open-Source SOC Framework &nbsp;<sup>`CAP-2025`</sup>
**[Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework](https://github.com/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework)**

![Stars](https://img.shields.io/github/stars/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Forks](https://img.shields.io/github/forks/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&logo=github&color=3F3F46&labelColor=18181B)&nbsp;
![Last Commit](https://img.shields.io/github/last-commit/kalidada18/Integration-of-Open-Source-Security-Tools-for-a-Unified-SOC-Framework?style=flat-square&color=39d353&labelColor=18181B)

> Final-year capstone: enterprise-grade SOC integrating **Wazuh SIEM**, **Suricata NIDS**, **Shuffle SOAR**, **TheHive**, and **MISP** for real-time detection, correlation, and automated triage.

<details>
<summary><sub>▶ architecture — SOC kill chain</sub></summary>

<br/>

```
┌─────────────────────────┐      ┌─────────────────────────┐      ┌─────────────────────────┐
│ Endpoint / Network      │────> │ Suricata NIDS &         │────> │ Wazuh Centralized       │
│ Telemetry Collectors    │      │ Wazuh Endpoint Agents   │      │ SIEM & Indexer Engine   │
└─────────────────────────┘      └─────────────────────────┘      └────────────┬────────────┘
                                                                               │ triggered
┌─────────────────────────┐      ┌─────────────────────────┐                   │ alerts
│ TheHive Incident Cases  │ <─── │ Shuffle SOAR            │ <─────────────────┘
│ & MISP Threat Intel     │      │ Automation Engine       │
└─────────────────────────┘      └─────────────────────────┘
```

</details>

</td>
<td width="50%" valign="top">

#### Threatbase — OSINT Platform &nbsp;<sup>`OPS-LIVE`</sup>
**[threatbase](https://github.com/kalidada18/threatbase)**

![Stars](https://img.shields.io/github/stars/kalidada18/threatbase?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Pipeline](https://github.com/kalidada18/threatbase/actions/workflows/update-feed.yml/badge.svg?label=feeds&labelColor=18181B)&nbsp;
![Uptime](https://img.shields.io/website?style=flat-square&up_color=39d353&upMessage=LIVE&down_color=3F3F46&downMessage=DOWN&labelColor=18181B&url=https://threatbase.qzz.io)

> `TypeScript · Python · React · Cloudflare` — high-throughput OSINT aggregation consolidating **54 threat feeds** into deduplicated IP/CIDR/Domain/URL/SHA-256 blocklists.

<details>
<summary><sub>▶ architecture — intake pipeline</sub></summary>

<br/>

```
54 Feeds ──> Fetch & Classify ──> Raw IOC Blocklists (IP / Domain / Hash)
     │                                ├──> Live Dashboard · threatbase.qzz.io
     └────────────────────────────────┴──> Retrospective ZIP Archives & Git Mirrors
```

</details>

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### KaliWall — ML Network Defense &nbsp;<sup>`ML-NDR`</sup>
**[KaliWall](https://github.com/kalidada18/KaliWall)**

![Stars](https://img.shields.io/github/stars/kalidada18/KaliWall?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![Go](https://img.shields.io/badge/Go-1.21%2B-3F3F46?style=flat-square&logo=go&logoColor=FF1744&labelColor=18181B)

> `Go · XGBoost · gopacket · VirusTotal` — Linux firewall with real-time DPI, GeoIP filtering, VT threat intel, and XGBoost anomaly scoring behind a FortiGate-inspired UI.

</td>
<td width="50%" valign="top">

#### Multi-Layer SIEM Integration &nbsp;<sup>`DEF-DI`</sup>
**[Multi-Layer-Security-Integration-Based-on-SIEM-Solutions](https://github.com/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions)**

![Stars](https://img.shields.io/github/stars/kalidada18/Multi-Layer-Security-Integration-Based-on-SIEM-Solutions?style=flat-square&logo=github&color=FF1744&labelColor=18181B)&nbsp;
![SIEM](https://img.shields.io/badge/SIEM-Splunk%20%2F%20Elastic-3F3F46?style=flat-square&labelColor=18181B)

> Defense-in-depth architecture: centralized SIEM monitoring, Sysmon process tracing, Snort/Suricata perimeter defense, and threshold alerting pipelines.

```
├── 1. Perimeter   Network Firewall + Snort/Suricata IDS
├── 2. Host        Sysmon telemetry + Logstash pipeline
├── 3. Analytics   SIEM dashboards & cross-log correlation
└── 4. Response    Automated incident alert dispatch
```

</td>
</tr>
</table>

### Growth Signal — threatbase

<p align="center">
  <a href="https://star-history.com/#kalidada18/threatbase&Date">
    <img src="https://api.star-history.com/svg?repos=kalidada18/threatbase&type=Date" width="600" alt="Threatbase star history growth chart" />
  </a>
</p>

---

<!-- ═══════════════════ 03 // RESEARCH VAULT ═══════════════════ -->

## <code>03&nbsp;//</code> RESEARCH VAULT

| Signature | Project | Stack | Domain |
|:----------|:--------|:------|:-------|
| `DECEP` | **[honeypot-java](https://github.com/kalidada18/honeypot-java)** | `Java` | Deception telemetry & attacker profiling |
| `AVAIL` | **[dos-attack](https://github.com/kalidada18/dos-attack)** | `Python` | Volumetric & protocol resilience testing |
| `MiTM` | **[dns-spoofing-tool](https://github.com/kalidada18/dns-spoofing-tool)** | `Python` | ARP poisoning & rogue DNS simulation |

---

<!-- ═══════════════════ 04 // THE ARMORY ═══════════════════ -->

## <code>04&nbsp;//</code> THE ARMORY

<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,go,ts,js,bash,powershell,java,sql&theme=dark" alt="Programming stack: Python, Go, TypeScript, JavaScript, Bash, PowerShell, Java, SQL — hover to animate" />
  </a>
</p>
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=linux,kali,docker,git,github,cloudflare,react,mysql&theme=dark" alt="Platform stack: Linux, Kali, Docker, Git, GitHub, Cloudflare, React, MySQL — hover to animate" />
  </a>
</p>

<details open>
<summary><b>SOC &amp; Defensive Engineering</b></summary>
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
<summary><b>Offensive Security &amp; Testing</b></summary>
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

**Field Proficiency Matrix**

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

---

<!-- ═══════════════════ 05 // COMBAT RECORD ═══════════════════ -->

## <code>05&nbsp;//</code> COMBAT RECORD <sub>live telemetry</sub>

<div align="center">

![Followers](https://img.shields.io/github/followers/kalidada18?style=for-the-badge&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Stars Earned](https://img.shields.io/github/stars/kalidada18?style=for-the-badge&logo=github&labelColor=18181B&color=FF1744)&nbsp;
![Repositories](https://img.shields.io/github/repos/kalidada18?style=for-the-badge&logo=github&labelColor=18181B&color=FF1744)

<br/><br/>

<img src="https://streak-stats.demolab.com/?user=kalidada18&theme=dark&background=0d0d0d&ring=FF1744&fire=FF1744&currStreakLabel=FF1744&sideLabels=9ca3af&dates=6b7280&sideNums=FF1744&currStreakNum=ffffff&hide_border=true" height="180" alt="GitHub contribution streak statistics: current and longest streaks" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake.svg">
  <img alt="Animated snake tracing the GitHub contribution grid" src="https://raw.githubusercontent.com/kalidada18/kalidada18/output/github-contribution-grid-snake-dark.svg">
</picture>

<br/>

![](https://img.shields.io/badge/Total%20Contributions-1%2C390%2B-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![](https://img.shields.io/badge/Public%20Repos-20%2B-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![](https://img.shields.io/badge/IOCs%20Processed-Millions-FF1744?style=flat-square&labelColor=18181B)&nbsp;
![](https://img.shields.io/badge/OSINT%20Feeds-54%20Active-FF1744?style=flat-square&labelColor=18181B)

</div>

---

<!-- ═══════════════════ 06 // CONTACT UPLINK ═══════════════════ -->

## <code>06&nbsp;//</code> CONTACT UPLINK

<div align="center">

[![Portfolio](https://img.shields.io/badge/Portfolio-sujallamichhane.com.np-FF1744?style=for-the-badge&logo=firefox&logoColor=ffffff&labelColor=18181B)](https://sujallamichhane.com.np)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sujal%20Lamichhane-0A66C2?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=18181B)](https://linkedin.com/in/sujal-lamichhane)
&nbsp;
[![Email](https://img.shields.io/badge/Email-lamichhanesujal18%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=18181B)](mailto:lamichhanesujal18@gmail.com)
&nbsp;
[![Threatbase](https://img.shields.io/badge/Threatbase-threatbase.qzz.io-FF1744?style=for-the-badge&logo=cloudflare&logoColor=ffffff&labelColor=18181B)](https://threatbase.qzz.io)

<br/>

```
┌──────────────────────────────────────────────────────────┐
│  hack ethically. defend relentlessly.   -- sujal, 2026   │
└──────────────────────────────────────────────────────────┘
```

<sub><img src="https://komarev.com/ghpvc/?username=kalidada18&style=flat-square&color=FF1744&label=VISITS" alt="Profile visitor counter" /> &nbsp;·&nbsp; last sync: live</sub>

</div>
