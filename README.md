<!-- ══════════════════════════════════════════════════════════════
     kalidada18 · GitHub Profile README
     Taste-Kill v1 · DV:8 · MI:6 · VD:4
     Grounded in real repos. No slop copy. No AI purple.
     ══════════════════════════════════════════════════════════════ -->

<div align="left">

<table border="0" cellspacing="0" cellpadding="0" width="100%">
<tr>
<td width="60%" valign="bottom">

<br/>

<sub><code>kalidada18</code> &nbsp;·&nbsp; L1 SOC Analyst &nbsp;·&nbsp; CryptoGen Nepal &nbsp;·&nbsp; CEH v13</sub>

<br/>

# SUJAL<br/>LAMICHHANE

<br/>

<img src="https://readme-typing-svg.demolab.com?font=IBM+Plex+Mono&weight=500&size=13&duration=3000&pause=1400&color=C8F542&center=false&vCenter=true&width=540&height=26&lines=54+OSINT+feeds.+Millions+of+IOCs.+threatbase.qzz.io;Go+firewall+with+DPI%2C+GeoIP+%2B+XGBoost+ML.;Threat+detection+from+Nepal+—+built+in+public." />

</td>
<td width="40%" valign="top" align="right">

<br/><br/>

```
┌──────────────────────┐
│ role    L1 SOC       │
│ cert    CEH v13      │
│ mssp    CryptoGen NP │
│ base    Chitwan, NP  │
│ status  [ACTIVE]     │
└──────────────────────┘
```

</td>
</tr>
</table>

</div>

---

**`01 ·`** &nbsp;**PROFILE**

<table border="0" cellpadding="5">
<tr><td><code>role</code></td><td>L1 SOC Analyst — CryptoGen Nepal (MSSP)</td></tr>
<tr><td><code>cert</code></td><td>CEH v13 — EC-Council</td></tr>
<tr><td><code>edu</code></td><td>B.Sc CS · Network Technology & Cybersecurity · Forbes College</td></tr>
<tr><td><code>focus</code></td><td>Detection Engineering · SIEM Ops · Threat Intel · Ethical Hacking</td></tr>
<tr><td><code>languages</code></td><td>Python · Bash · PowerShell · Go · TypeScript</td></tr>
<tr><td><code>base</code></td><td>Chitwan, Nepal</td></tr>
</table>

---

**`02 ·`** &nbsp;**SHIPPED PROJECTS**

<br/>

**[threatbase](https://github.com/kalidada18/threatbase)** &nbsp;·&nbsp; `TypeScript · Python · React · Cloudflare`

```
 54 upstream OSINT feeds  →  Python aggregator  →  GitHub Actions
 (fetch · dedup · classify)    ├── Raw blocklists (IP / IPv6 / CIDR / Domain / URL / Hash)
                                ├── React dashboard — threatbase.qzz.io
                                ├── Daily ZIP archives (retrospective hunting)
                                └── Chunked Git mirrors (~31 MiB chunks)
```

> Millions of deduplicated IOCs. Category-split feeds: C2, Botnet, Brute-Force, Tor, Spam, Exploit, Malware.
> No auth. No rate limits. Drop any feed URL straight into Splunk, Pi-hole, or iptables.

![Feed Pipeline](https://github.com/kalidada18/threatbase/actions/workflows/update-feed.yml/badge.svg)
![IOCs](https://img.shields.io/badge/IOCs-Millions-0f0f0f?style=flat-square&labelColor=0f0f0f&color=C8F542)
![Feeds](https://img.shields.io/badge/Feeds-54-0f0f0f?style=flat-square&labelColor=0f0f0f&color=C8F542)
![License](https://img.shields.io/badge/License-MIT-0f0f0f?style=flat-square&labelColor=0f0f0f&color=333)

<br/>

**[KaliWall](https://github.com/kalidada18/KaliWall)** &nbsp;·&nbsp; `Go · XGBoost · gopacket · VirusTotal`

```
 Layer stack:
 ├── Core firewall      iptables / nftables / ufw — hot-swap backend at runtime
 ├── DPI module         HTTP · DNS · TLS metadata · L3 telemetry · queue-pressure stats
 ├── ML anomaly         XGBoost scoring · override rules · CPU-first inference
 ├── Threat intel       VirusTotal IP reputation · cache + API key management
 ├── GeoIP telemetry    MaxMind .mmdb / IP2Location CSV · SSE stream
 └── Dashboard + CLI    FortiGate-inspired web UI · full CLI client
```

> Linux-only. Requires root. ipsum.txt auto-refreshes via cron or systemd timer.

![Go](https://img.shields.io/badge/Go-1.21+-0f0f0f?style=flat-square&logo=go&logoColor=C8F542&labelColor=0f0f0f)
![Platform](https://img.shields.io/badge/Linux-only-0f0f0f?style=flat-square&logo=linux&logoColor=C8F542&labelColor=0f0f0f)
![VirusTotal](https://img.shields.io/badge/VirusTotal-integrated-0f0f0f?style=flat-square&labelColor=0f0f0f&color=C8F542)

<br/>

**Other repos**

| repo | lang | what |
|------|------|------|
| [honeypot-java](https://github.com/kalidada18/honeypot-java) | Java | Honeypot implementation |
| [dos-attack](https://github.com/kalidada18/dos-attack) | Python | DoS research tooling |
| [dns-spoofing-tool](https://github.com/kalidada18/dns-spoofing-tool) | Python | DNS spoofing lab tool |

---

**`03 ·`** &nbsp;**CURRENT OPS**

```
 studying   →  Advanced Exploit Dev & Privilege Escalation       ACTIVE
 learning   →  Malware Analysis · Reverse Engineering            ACTIVE
 building   →  Home SOC Lab — Wazuh + Splunk + n8n SOAR          WIP
 building   →  Wazuh correlation engine → Splunk bridge           WIP
 training   →  HackTheBox · TryHackMe · PortSwigger Labs         ONGOING
```

---

**`04 ·`** &nbsp;**ARSENAL**

<table border="0" width="100%" cellpadding="0" cellspacing="0">
<tr>
<td width="50%" valign="top">

**Offensive**
```
nmap / masscan          ██████████████████░░  90
burp suite              ████████████████░░░░  80
metasploit / msfvenom   ███████████████░░░░░  75
wireshark / tcpdump     █████████████████░░░  85
nikto / sqlmap          ██████████████░░░░░░  70
```

</td>
<td width="50%" valign="top">

**Defensive / SOC**
```
splunk / fortisiem      █████████████████░░░  88
wazuh / logpoint        █████████████████░░░  85
fortigate / palo alto   ████████████████░░░░  80
n8n soar / automation   ██████████████░░░░░░  72
snort / suricata        ███████████████░░░░░  75
```

</td>
</tr>
</table>

<br/>

![Python](https://img.shields.io/badge/Python-0f0f0f?style=flat-square&logo=python&logoColor=C8F542)&nbsp;
![Go](https://img.shields.io/badge/Go-0f0f0f?style=flat-square&logo=go&logoColor=C8F542)&nbsp;
![TypeScript](https://img.shields.io/badge/TypeScript-0f0f0f?style=flat-square&logo=typescript&logoColor=C8F542)&nbsp;
![Bash](https://img.shields.io/badge/Bash-0f0f0f?style=flat-square&logo=gnubash&logoColor=C8F542)&nbsp;
![Linux](https://img.shields.io/badge/Linux-0f0f0f?style=flat-square&logo=linux&logoColor=C8F542)&nbsp;
![Docker](https://img.shields.io/badge/Docker-0f0f0f?style=flat-square&logo=docker&logoColor=C8F542)&nbsp;
![Splunk](https://img.shields.io/badge/Splunk-0f0f0f?style=flat-square&logo=splunk&logoColor=C8F542)&nbsp;
![React](https://img.shields.io/badge/React-0f0f0f?style=flat-square&logo=react&logoColor=C8F542)

---

**`05 ·`** &nbsp;**CERTIFICATION**

```
 ┌───────────────────────────────────────────────────────────┐
 │  CEH v13 — Certified Ethical Hacker · EC-Council          │
 │                                                           │
 │  penetration-testing · recon · exploitation               │
 │  vulnerability-assessment · offensive-security            │
 └───────────────────────────────────────────────────────────┘
```

---

**`06 ·`** &nbsp;**TELEMETRY**

<table border="0" cellspacing="8" cellpadding="0">
<tr>
<td>
<img src="https://github-readme-stats.vercel.app/api?username=kalidada18&show_icons=true&hide_border=true&bg_color=0d0d0d&title_color=C8F542&icon_color=C8F542&text_color=555555&count_private=true&include_all_commits=true&rank_icon=github" height="150" />
</td>
<td>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=kalidada18&layout=compact&hide_border=true&bg_color=0d0d0d&title_color=C8F542&text_color=555555&langs_count=6" height="150" />
</td>
</tr>
</table>

<img src="https://streak-stats.demolab.com/?user=kalidada18&hide_border=true&background=0d0d0d&ring=C8F542&fire=C8F542&currStreakLabel=C8F542&sideLabels=444444&dates=444444&stroke=0d0d0d&sideNums=C8F542&currStreakNum=ffffff" width="58%" />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=kalidada18&bg_color=0d0d0d&color=C8F542&line=1e1e1e&point=C8F542&area=false&hide_border=true&custom_title=contribution+graph" width="100%" />

---

**`07 ·`** &nbsp;**CONTACT**

```
 portfolio   sujallamichhane.com.np
 github      github.com/kalidada18
 linkedin    linkedin.com/in/sujal-lamichhane
 email       lamichhanesujal18@gmail.com
 threatbase  threatbase.qzz.io
```

---

<sub><code>hack ethically. defend relentlessly.</code> &nbsp;·&nbsp; sujal lamichhane · 2026</sub>
