<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Sujal Lamichhane — Profile</title>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;700&family=Space+Grotesk:wght@300;400;500;700&display=swap" rel="stylesheet" />
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:        #080808;
    --surface:   #0f0f0f;
    --border:    #1e1e1e;
    --border-hi: #2e2e2e;
    --text:      #d0d0d0;
    --text-dim:  #555;
    --text-mute: #333;
    --accent:    #c8f542;        /* acid yellow-green — not teal, not cyan */
    --accent-dim:#7a9a1a;
    --red:       #ff3b3b;
    --mono:      'IBM Plex Mono', monospace;
    --sans:      'Space Grotesk', sans-serif;
  }

  html { background: var(--bg); color: var(--text); font-family: var(--sans); font-size: 16px; line-height: 1.6; }

  body {
    max-width: 960px;
    margin: 0 auto;
    padding: 0;
    border-left: 1px solid var(--border);
    border-right: 1px solid var(--border);
    min-height: 100vh;
  }

  /* ── HEADER ── */
  .hdr {
    border-bottom: 2px solid var(--accent);
    padding: 48px 40px 36px;
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: end;
    gap: 24px;
  }
  .hdr-left {}
  .hdr-eyebrow {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: .12em;
    color: var(--text-dim);
    margin-bottom: 12px;
  }
  .hdr-eyebrow span { color: var(--accent); }
  h1 {
    font-family: var(--mono);
    font-size: clamp(28px, 5vw, 52px);
    font-weight: 700;
    color: #fff;
    line-height: 1.05;
    letter-spacing: -.02em;
  }
  h1 em {
    font-style: normal;
    color: var(--accent);
  }
  .hdr-sub {
    margin-top: 14px;
    font-family: var(--sans);
    font-size: 13px;
    color: var(--text-dim);
    max-width: 420px;
    line-height: 1.5;
  }
  .hdr-meta {
    text-align: right;
  }
  .status-pill {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent);
    border: 1px solid var(--accent);
    padding: 5px 12px;
    letter-spacing: .08em;
    margin-bottom: 14px;
  }
  .status-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent);
    animation: blink 1.4s step-end infinite;
  }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
  .hdr-loc {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--text-dim);
  }

  /* ── NAV STRIP ── */
  .nav {
    display: flex;
    border-bottom: 1px solid var(--border);
    overflow-x: auto;
  }
  .nav a {
    font-family: var(--mono);
    font-size: 11px;
    letter-spacing: .1em;
    color: var(--text-dim);
    text-decoration: none;
    padding: 12px 20px;
    border-right: 1px solid var(--border);
    white-space: nowrap;
    transition: color .15s, background .15s;
  }
  .nav a:hover { color: var(--accent); background: #111; }

  /* ── SECTION LAYOUT ── */
  section {
    border-bottom: 1px solid var(--border);
  }
  .sec-hdr {
    display: flex;
    align-items: baseline;
    gap: 16px;
    padding: 20px 40px 0;
  }
  .sec-label {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: .15em;
    color: var(--text-mute);
    text-transform: uppercase;
  }
  .sec-rule { flex: 1; height: 1px; background: var(--border-hi); }
  .sec-body { padding: 24px 40px 32px; }

  /* ── WHOAMI GRID ── */
  .whoami-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
    border: 1px solid var(--border-hi);
  }
  .wg-row {
    display: contents;
  }
  .wg-row > * {
    border-bottom: 1px solid var(--border);
    border-right: 1px solid var(--border);
    padding: 11px 16px;
    font-family: var(--mono);
    font-size: 12px;
  }
  .wg-row:last-child > * { border-bottom: none; }
  .wg-k {
    color: var(--text-dim);
    letter-spacing: .06em;
  }
  .wg-v {
    color: var(--text);
    border-right: none !important;
  }
  .wg-v .hl { color: var(--accent); }

  /* ── CURRENT OPS ── */
  .ops-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 0;
    border: 1px solid var(--border-hi);
  }
  .ops-item {
    display: grid;
    grid-template-columns: 120px 1fr;
    border-bottom: 1px solid var(--border);
    font-family: var(--mono);
    font-size: 12px;
  }
  .ops-item:last-child { border-bottom: none; }
  .ops-tag {
    padding: 12px 16px;
    color: var(--text-mute);
    border-right: 1px solid var(--border);
    letter-spacing: .06em;
    font-size: 10px;
  }
  .ops-desc {
    padding: 12px 16px;
    color: var(--text);
    line-height: 1.4;
  }
  .ops-desc .tag {
    display: inline-block;
    background: #141414;
    border: 1px solid var(--border-hi);
    color: var(--accent-dim);
    font-size: 10px;
    padding: 1px 6px;
    margin-left: 8px;
    vertical-align: middle;
  }

  /* ── ARSENAL ── */
  .arsenal-cols {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }
  .arsenal-block {}
  .arsenal-title {
    font-family: var(--mono);
    font-size: 10px;
    letter-spacing: .15em;
    color: var(--accent-dim);
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border-hi);
  }
  .tool-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 7px 0;
    border-bottom: 1px solid var(--border);
    font-family: var(--mono);
    font-size: 12px;
    color: var(--text);
  }
  .tool-row:last-child { border-bottom: none; }
  .tool-bar {
    height: 2px;
    background: var(--accent);
    opacity: .25;
    flex: 1;
    position: relative;
  }
  .tool-bar-fill {
    position: absolute;
    left: 0; top: 0; height: 100%;
    background: var(--accent);
    opacity: 1;
  }
  .tool-pct {
    font-size: 10px;
    color: var(--text-mute);
    min-width: 28px;
    text-align: right;
  }

  /* ── CERT ── */
  .cert-block {
    border: 1px solid var(--border-hi);
    display: grid;
    grid-template-columns: auto 1fr;
  }
  .cert-badge {
    background: var(--surface);
    border-right: 1px solid var(--border-hi);
    padding: 24px 28px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
  }
  .cert-icon {
    font-size: 32px;
    line-height: 1;
  }
  .cert-abbr {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--accent);
    letter-spacing: .1em;
  }
  .cert-body {
    padding: 24px 28px;
  }
  .cert-title {
    font-family: var(--sans);
    font-size: 18px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 4px;
  }
  .cert-issuer {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--text-dim);
    margin-bottom: 16px;
  }
  .cert-tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }
  .ctag {
    font-family: var(--mono);
    font-size: 10px;
    border: 1px solid var(--border-hi);
    color: var(--text-dim);
    padding: 3px 8px;
    letter-spacing: .06em;
  }

  /* ── CONTACT ── */
  .contact-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    border: 1px solid var(--border-hi);
  }
  .contact-item {
    display: flex;
    flex-direction: column;
    gap: 4px;
    padding: 16px 20px;
    border-right: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    text-decoration: none;
    transition: background .15s;
  }
  .contact-item:nth-child(2n) { border-right: none; }
  .contact-item:nth-last-child(-n+2) { border-bottom: none; }
  .contact-item:hover { background: #111; }
  .c-platform {
    font-family: var(--mono);
    font-size: 10px;
    color: var(--text-mute);
    letter-spacing: .1em;
  }
  .c-handle {
    font-family: var(--mono);
    font-size: 13px;
    color: var(--accent);
  }

  /* ── MOTTO ── */
  .motto {
    padding: 32px 40px;
    border-top: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .motto-text {
    font-family: var(--mono);
    font-size: 14px;
    color: var(--text-dim);
    letter-spacing: .04em;
  }
  .motto-text strong { color: var(--accent); font-weight: 500; }
  .motto-year {
    font-family: var(--mono);
    font-size: 11px;
    color: var(--text-mute);
  }

  @media (max-width: 640px) {
    .hdr { grid-template-columns: 1fr; padding: 32px 20px 24px; }
    .hdr-meta { text-align: left; }
    .sec-hdr { padding: 16px 20px 0; }
    .sec-body { padding: 20px 20px 24px; }
    .whoami-grid { grid-template-columns: 1fr; }
    .wg-row > * { border-right: none !important; }
    .arsenal-cols { grid-template-columns: 1fr; }
    .contact-grid { grid-template-columns: 1fr; }
    .contact-item { border-right: none !important; }
    .motto { flex-direction: column; gap: 8px; align-items: flex-start; padding: 24px 20px; }
    .cert-block { grid-template-columns: 1fr; }
    .cert-badge { border-right: none; border-bottom: 1px solid var(--border-hi); padding: 20px; }
    .ops-item { grid-template-columns: 80px 1fr; }
  }
</style>
</head>
<body>

<!-- HEADER -->
<header class="hdr">
  <div class="hdr-left">
    <div class="hdr-eyebrow">
      <span>[ L1 SOC Analyst ]</span> — CryptoGen Nepal · MSSP
    </div>
    <h1>SUJAL<br><em>LAMICHHANE</em></h1>
    <p class="hdr-sub">
      Threat detection, SIEM ops, and open-source security tooling.
      CEH v13. Defending infrastructure so others don't have to.
    </p>
  </div>
  <div class="hdr-meta">
    <div class="status-pill">
      <span class="status-dot"></span>ACTIVE
    </div>
    <div class="hdr-loc">Chitwan, Nepal 🇳🇵</div>
  </div>
</header>

<!-- NAV -->
<nav class="nav">
  <a href="#whoami">whoami</a>
  <a href="#ops">current_ops</a>
  <a href="#arsenal">arsenal</a>
  <a href="#cert">certifications</a>
  <a href="#contact">contact</a>
</nav>

<!-- WHOAMI -->
<section id="whoami">
  <div class="sec-hdr">
    <span class="sec-label">01 / profile</span>
    <span class="sec-rule"></span>
  </div>
  <div class="sec-body">
    <div class="whoami-grid">
      <div class="wg-row">
        <div class="wg-k">ROLE</div>
        <div class="wg-v"><span class="hl">L1 SOC Analyst</span> — threat triage, SIEM, incident response</div>
      </div>
      <div class="wg-row">
        <div class="wg-k">EMPLOYER</div>
        <div class="wg-v">CryptoGen Nepal (MSSP)</div>
      </div>
      <div class="wg-row">
        <div class="wg-k">EDUCATION</div>
        <div class="wg-v">B.Sc CS — Network Technology & Cybersecurity · Forbes College</div>
      </div>
      <div class="wg-row">
        <div class="wg-k">CERT</div>
        <div class="wg-v"><span class="hl">CEH v13</span> — EC-Council</div>
      </div>
      <div class="wg-row">
        <div class="wg-k">STACK</div>
        <div class="wg-v">Python · Bash · PowerShell · Linux</div>
      </div>
      <div class="wg-row">
        <div class="wg-k">FOCUS</div>
        <div class="wg-v">SIEM · Threat Intel · Detection Engineering · SOAR · Ethical Hacking</div>
      </div>
      <div class="wg-row">
        <div class="wg-k">BASE</div>
        <div class="wg-v">Chitwan, Nepal 🇳🇵</div>
      </div>
    </div>
  </div>
</section>

<!-- CURRENT OPS -->
<section id="ops">
  <div class="sec-hdr">
    <span class="sec-label">02 / current_ops</span>
    <span class="sec-rule"></span>
  </div>
  <div class="sec-body">
    <ul class="ops-list">
      <li class="ops-item">
        <span class="ops-tag">STUDYING</span>
        <span class="ops-desc">Advanced Exploit Development & Privilege Escalation<span class="tag">ACTIVE</span></span>
      </li>
      <li class="ops-item">
        <span class="ops-tag">LEARNING</span>
        <span class="ops-desc">Malware Analysis · Reverse Engineering</span>
      </li>
      <li class="ops-item">
        <span class="ops-tag">BUILDING</span>
        <span class="ops-desc">Home SOC Lab — Wazuh, Splunk, n8n AI triage agent, Threatbase platform<span class="tag">WIP</span></span>
      </li>
      <li class="ops-item">
        <span class="ops-tag">TRAINING</span>
        <span class="ops-desc">HackTheBox · TryHackMe · PortSwigger Web Security Academy</span>
      </li>
      <li class="ops-item">
        <span class="ops-tag">TOOLS</span>
        <span class="ops-desc">backdoor_detector.py · log_parser.py · Wazuh Correlation Engine</span>
      </li>
    </ul>
  </div>
</section>

<!-- ARSENAL -->
<section id="arsenal">
  <div class="sec-hdr">
    <span class="sec-label">03 / arsenal</span>
    <span class="sec-rule"></span>
  </div>
  <div class="sec-body">
    <div class="arsenal-cols">
      <div class="arsenal-block">
        <div class="arsenal-title">OFFENSIVE / RECON</div>
        <div class="tool-row">
          Nmap / Masscan
          <div class="tool-bar"><div class="tool-bar-fill" style="width:90%"></div></div>
          <span class="tool-pct">90%</span>
        </div>
        <div class="tool-row">
          Metasploit / MSFvenom
          <div class="tool-bar"><div class="tool-bar-fill" style="width:75%"></div></div>
          <span class="tool-pct">75%</span>
        </div>
        <div class="tool-row">
          Burp Suite
          <div class="tool-bar"><div class="tool-bar-fill" style="width:80%"></div></div>
          <span class="tool-pct">80%</span>
        </div>
        <div class="tool-row">
          Nikto / SQLMap
          <div class="tool-bar"><div class="tool-bar-fill" style="width:70%"></div></div>
          <span class="tool-pct">70%</span>
        </div>
        <div class="tool-row">
          Subfinder / TheHarvester
          <div class="tool-bar"><div class="tool-bar-fill" style="width:78%"></div></div>
          <span class="tool-pct">78%</span>
        </div>
        <div class="tool-row">
          Wireshark / tcpdump
          <div class="tool-bar"><div class="tool-bar-fill" style="width:85%"></div></div>
          <span class="tool-pct">85%</span>
        </div>
      </div>
      <div class="arsenal-block">
        <div class="arsenal-title">DEFENSIVE / SOC OPS</div>
        <div class="tool-row">
          Splunk / FortiSIEM
          <div class="tool-bar"><div class="tool-bar-fill" style="width:88%"></div></div>
          <span class="tool-pct">88%</span>
        </div>
        <div class="tool-row">
          Wazuh / LogPoint
          <div class="tool-bar"><div class="tool-bar-fill" style="width:85%"></div></div>
          <span class="tool-pct">85%</span>
        </div>
        <div class="tool-row">
          FortiGate / Palo Alto
          <div class="tool-bar"><div class="tool-bar-fill" style="width:80%"></div></div>
          <span class="tool-pct">80%</span>
        </div>
        <div class="tool-row">
          pfSense / OPNsense
          <div class="tool-bar"><div class="tool-bar-fill" style="width:78%"></div></div>
          <span class="tool-pct">78%</span>
        </div>
        <div class="tool-row">
          n8n SOAR / Automation
          <div class="tool-bar"><div class="tool-bar-fill" style="width:72%"></div></div>
          <span class="tool-pct">72%</span>
        </div>
        <div class="tool-row">
          Snort / Suricata IDS
          <div class="tool-bar"><div class="tool-bar-fill" style="width:75%"></div></div>
          <span class="tool-pct">75%</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CERT -->
<section id="cert">
  <div class="sec-hdr">
    <span class="sec-label">04 / certifications</span>
    <span class="sec-rule"></span>
  </div>
  <div class="sec-body">
    <div class="cert-block">
      <div class="cert-badge">
        <div class="cert-icon">⬡</div>
        <div class="cert-abbr">CEH v13</div>
      </div>
      <div class="cert-body">
        <div class="cert-title">Certified Ethical Hacker</div>
        <div class="cert-issuer">EC-Council — International</div>
        <div class="cert-tags">
          <span class="ctag">PENETRATION TESTING</span>
          <span class="ctag">RECON</span>
          <span class="ctag">VULNERABILITY ASSESSMENT</span>
          <span class="ctag">EXPLOITATION</span>
          <span class="ctag">OFFENSIVE SECURITY</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CONTACT -->
<section id="contact">
  <div class="sec-hdr">
    <span class="sec-label">05 / establish_contact</span>
    <span class="sec-rule"></span>
  </div>
  <div class="sec-body">
    <div class="contact-grid">
      <a class="contact-item" href="https://sujallamichhane.com.np" target="_blank" rel="noopener">
        <span class="c-platform">PORTFOLIO</span>
        <span class="c-handle">sujallamichhane.com.np</span>
      </a>
      <a class="contact-item" href="https://github.com/sujallamichhane18" target="_blank" rel="noopener">
        <span class="c-platform">GITHUB</span>
        <span class="c-handle">@sujallamichhane18</span>
      </a>
      <a class="contact-item" href="https://linkedin.com/in/sujal-lamichhane" target="_blank" rel="noopener">
        <span class="c-platform">LINKEDIN</span>
        <span class="c-handle">sujal-lamichhane</span>
      </a>
      <a class="contact-item" href="mailto:lamichhanesujal18@gmail.com">
        <span class="c-platform">EMAIL</span>
        <span class="c-handle">lamichhanesujal18@gmail.com</span>
      </a>
    </div>
  </div>
</section>

<!-- MOTTO -->
<div class="motto">
  <div class="motto-text">
    <strong>Hack ethically.</strong> Defend relentlessly.
  </div>
  <div class="motto-year">© 2026 Sujal Lamichhane</div>
</div>

</body>
</html>
