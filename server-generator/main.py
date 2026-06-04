<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jujutsu Shenanigans — Server Manager</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Rajdhani:wght@400;500;600;700&display=swap');

:root{
  --red:#ff1a1a;--blue:#00cfff;--gold:#ffd700;--purple:#cc44ff;
  --dark:#06080f;--darker:#030508;--glass:rgba(0,207,255,.07);
  --glass-b:rgba(0,207,255,.18);--red-glow:rgba(255,26,26,.4);
  --blue-glow:rgba(0,207,255,.4);
}
*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  background:var(--darker);
  color:#fff;
  font-family:'Rajdhani',sans-serif;
  min-height:100vh;
  overflow-x:hidden;
}

/* ── ANIMATED BACKGROUND ── */
body::before{
  content:'';position:fixed;inset:0;z-index:0;
  background:
    radial-gradient(ellipse 80% 50% at 20% 10%,rgba(255,26,26,.08) 0%,transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 80%,rgba(0,207,255,.07) 0%,transparent 60%),
    radial-gradient(ellipse 40% 60% at 50% 50%,rgba(100,0,180,.05) 0%,transparent 70%);
  pointer-events:none;
}

/* grid overlay */
body::after{
  content:'';position:fixed;inset:0;z-index:0;
  background-image:
    linear-gradient(rgba(0,207,255,.03) 1px,transparent 1px),
    linear-gradient(90deg,rgba(0,207,255,.03) 1px,transparent 1px);
  background-size:48px 48px;
  pointer-events:none;
}

/* ── HEADER ── */
header{
  position:relative;z-index:10;
  padding:28px 40px 24px;
  border-bottom:1px solid rgba(0,207,255,.12);
  background:rgba(3,5,8,.8);
  backdrop-filter:blur(16px);
  display:flex;align-items:center;justify-content:space-between;
  flex-wrap:wrap;gap:12px;
}
.logo{
  font-family:'Bebas Neue',sans-serif;
  font-size:clamp(22px,3vw,32px);
  letter-spacing:4px;
  background:linear-gradient(135deg,var(--red),var(--blue));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 14px rgba(255,26,26,.5));
}
.logo span{color:rgba(255,255,255,.3);-webkit-text-fill-color:rgba(255,255,255,.3);}
.header-badge{
  font-size:10px;letter-spacing:3px;text-transform:uppercase;
  color:var(--blue);border:1px solid var(--glass-b);
  padding:5px 12px;border-radius:20px;
  background:var(--glass);
}

/* ── HERO ── */
.hero{
  position:relative;z-index:10;
  text-align:center;
  padding:70px 20px 50px;
}
.hero-eyebrow{
  font-size:11px;letter-spacing:6px;text-transform:uppercase;
  color:var(--blue);margin-bottom:18px;opacity:.8;
}
.hero h1{
  font-family:'Bebas Neue',sans-serif;
  font-size:clamp(52px,9vw,110px);
  letter-spacing:6px;line-height:.95;
  margin-bottom:10px;
}
.hero h1 .line1{
  display:block;
  background:linear-gradient(135deg,#fff 0%,rgba(255,255,255,.7) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.hero h1 .line2{
  display:block;
  background:linear-gradient(135deg,var(--red),#ff6600);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  filter:drop-shadow(0 0 30px rgba(255,26,26,.6));
}
.hero-sub{
  font-size:16px;color:rgba(255,255,255,.4);
  letter-spacing:2px;margin-top:16px;
}

/* ── MAIN CONTENT ── */
.content{
  position:relative;z-index:10;
  max-width:960px;margin:0 auto;
  padding:0 24px 80px;
}

/* ── SECTION LABEL ── */
.sec-label{
  font-size:10px;letter-spacing:5px;text-transform:uppercase;
  color:var(--blue);margin-bottom:10px;
  display:flex;align-items:center;gap:10px;
}
.sec-label::after{content:'';flex:1;height:1px;background:var(--glass-b);}

/* ── STEP CARDS ── */
.steps{display:flex;flex-direction:column;gap:16px;margin-bottom:48px;}
.step{
  background:var(--glass);
  border:1px solid var(--glass-b);
  border-radius:14px;
  padding:24px 28px;
  display:grid;grid-template-columns:48px 1fr;gap:16px;
  align-items:start;
  transition:border-color .2s,transform .2s;
}
.step:hover{border-color:rgba(0,207,255,.4);transform:translateX(4px);}
.step-num{
  font-family:'Bebas Neue',sans-serif;font-size:36px;
  background:linear-gradient(135deg,var(--blue),var(--purple));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  line-height:1;
}
.step h3{
  font-family:'Orbitron',sans-serif;font-size:13px;letter-spacing:2px;
  text-transform:uppercase;color:#fff;margin-bottom:6px;
}
.step p{font-size:14px;color:rgba(255,255,255,.5);line-height:1.7;}
.step code,.step .cmd{
  display:inline-block;
  font-family:'Share Tech Mono',monospace;font-size:13px;
  background:rgba(0,0,0,.5);border:1px solid rgba(0,207,255,.2);
  border-radius:5px;padding:2px 8px;color:var(--blue);
}
.step .cmd-block{
  margin-top:10px;
  font-family:'Share Tech Mono',monospace;font-size:13px;
  background:rgba(0,0,0,.6);border:1px solid rgba(0,207,255,.15);
  border-radius:8px;padding:12px 16px;color:#a0e0ff;
  white-space:pre;overflow-x:auto;line-height:1.6;
}
.step .cmd-block .comment{color:rgba(255,255,255,.3);}
.step .tag{
  display:inline-block;font-size:9px;letter-spacing:2px;
  text-transform:uppercase;padding:2px 8px;border-radius:10px;
  margin-left:8px;vertical-align:middle;
}
.tag.free{background:rgba(0,255,100,.12);border:1px solid rgba(0,255,100,.3);color:#0f8;}
.tag.required{background:rgba(255,200,0,.1);border:1px solid rgba(255,200,0,.3);color:#ffd700;}

/* ── SERVER CODE BOX ── */
.code-section{margin-bottom:48px;}
.code-header{
  display:flex;align-items:center;justify-content:space-between;
  margin-bottom:10px;flex-wrap:wrap;gap:8px;
}
.code-header h3{
  font-family:'Orbitron',sans-serif;font-size:12px;
  letter-spacing:2px;text-transform:uppercase;color:#fff;
}
.copy-btn{
  font-family:'Orbitron',sans-serif;font-size:10px;letter-spacing:2px;
  text-transform:uppercase;padding:7px 16px;border:1px solid var(--glass-b);
  border-radius:6px;background:var(--glass);color:var(--blue);
  cursor:pointer;transition:all .18s;
}
.copy-btn:hover{background:rgba(0,207,255,.15);border-color:var(--blue);}
.copy-btn.copied{color:#0f8;border-color:#0f8;}
.code-box{
  background:rgba(0,0,0,.7);border:1px solid rgba(0,207,255,.15);
  border-radius:12px;padding:24px;
  font-family:'Share Tech Mono',monospace;font-size:12.5px;
  color:#c8e8ff;line-height:1.65;
  max-height:520px;overflow-y:auto;
  white-space:pre;
}
.code-box::-webkit-scrollbar{width:6px;}
.code-box::-webkit-scrollbar-track{background:transparent;}
.code-box::-webkit-scrollbar-thumb{background:rgba(0,207,255,.3);border-radius:3px;}
.kw{color:#cc44ff;}
.str{color:#7ec8a0;}
.num{color:#ffd700;}
.cm{color:rgba(255,255,255,.28);}
.fn{color:#00cfff;}
.key{color:#ff8c44;}

/* ── PLATFORM CARDS ── */
.platforms{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin-bottom:48px;}
.plat{
  background:var(--glass);border:1px solid var(--glass-b);
  border-radius:14px;padding:22px 24px;
  transition:all .2s;
}
.plat:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(0,207,255,.1);}
.plat-name{
  font-family:'Orbitron',sans-serif;font-size:15px;font-weight:700;
  margin-bottom:4px;
}
.plat-free{font-size:11px;color:#0f8;letter-spacing:2px;margin-bottom:10px;}
.plat p{font-size:13px;color:rgba(255,255,255,.45);line-height:1.7;}
.plat a{color:var(--blue);text-decoration:none;}
.plat a:hover{text-decoration:underline;}
.plat .plat-steps{
  margin-top:12px;padding-top:12px;
  border-top:1px solid rgba(255,255,255,.07);
}
.plat .plat-steps li{
  font-size:12px;color:rgba(255,255,255,.4);
  margin-bottom:4px;list-style:none;
  padding-left:16px;position:relative;line-height:1.6;
}
.plat .plat-steps li::before{
  content:'→';position:absolute;left:0;color:var(--blue);font-size:10px;top:2px;
}

/* ── INFO BOX ── */
.infobox{
  background:rgba(255,215,0,.05);
  border:1px solid rgba(255,215,0,.2);
  border-radius:12px;padding:18px 22px;
  margin-bottom:48px;
  display:grid;grid-template-columns:32px 1fr;gap:12px;align-items:start;
}
.infobox-icon{font-size:22px;}
.infobox h4{font-family:'Orbitron',sans-serif;font-size:11px;letter-spacing:2px;color:var(--gold);margin-bottom:5px;}
.infobox p{font-size:13px;color:rgba(255,255,255,.45);line-height:1.7;}
.infobox a{color:var(--blue);}

/* ── PACKAGE JSON ── */
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:48px;}
@media(max-width:640px){.two-col{grid-template-columns:1fr;}}

/* ── FOOTER ── */
footer{
  position:relative;z-index:10;
  text-align:center;padding:28px;
  border-top:1px solid rgba(255,255,255,.06);
  font-size:12px;color:rgba(255,255,255,.2);letter-spacing:2px;
}
footer span{color:var(--blue);}

/* ── FLOATING PARTICLES ── */
.particle{
  position:fixed;border-radius:50%;pointer-events:none;z-index:1;
  animation:float linear infinite;opacity:0;
}
@keyframes float{
  0%{transform:translateY(100vh) scale(0);opacity:0;}
  10%{opacity:.6;}
  90%{opacity:.3;}
  100%{transform:translateY(-10vh) scale(1.5);opacity:0;}
}
</style>
</head>
<body>

<!-- Particles -->
<script>
for(let i=0;i<18;i++){
  const p=document.createElement('div');
  p.className='particle';
  const s=2+Math.random()*4;
  p.style.cssText=`width:${s}px;height:${s}px;left:${Math.random()*100}%;
    background:${Math.random()>.5?'rgba(0,207,255,.5)':'rgba(255,26,26,.4)'};
    animation-duration:${8+Math.random()*14}s;
    animation-delay:${Math.random()*10}s;`;
  document.body.appendChild(p);
}
</script>

<header>
  <div class="logo">Jujutsu <span>■</span> Shenanigans</div>
  <div class="header-badge">⚡ Server Manager</div>
</header>

<div class="hero">
  <div class="hero-eyebrow">Multiplayer Infrastructure</div>
  <h1>
    <span class="line1">SERVER</span>
    <span class="line2">SETUP</span>
  </h1>
  <div class="hero-sub">Get your battle server running in under 5 minutes</div>
</div>

<div class="content">

  <!-- WHAT IS THIS -->
  <div class="sec-label">What is this?</div>
  <div class="infobox" style="margin-bottom:32px;">
    <div class="infobox-icon">⚡</div>
    <div>
      <h4>How Multiplayer Works</h4>
      <p>The game client (Website 1) connects to this server via a secure WebSocket (<code>wss://</code>). 
      You deploy this server once to a free cloud host, get a URL, and share it with your friend. 
      Both of you paste that same URL into the game's connect screen. Done — you're in the same match.</p>
    </div>
  </div>

  <!-- STEP BY STEP -->
  <div class="sec-label">Step-by-step setup</div>
  <div class="steps">
    <div class="step">
      <div class="step-num">1</div>
      <div>
        <h3>Copy the server files <span class="tag required">Required</span></h3>
        <p>You need two files: <code>server.js</code> and <code>package.json</code>. 
        Both are shown below — copy each one exactly.</p>
      </div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div>
        <h3>Create a GitHub repo <span class="tag free">Free</span></h3>
        <p>Go to <a href="https://github.com" target="_blank" style="color:var(--blue)">github.com</a> → New Repository → name it <code>jjs-server</code> → set to Public → Create.
        Upload both files to it (drag and drop them into the repo page).</p>
      </div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div>
        <h3>Deploy on Railway <span class="tag free">Free</span></h3>
        <p>Go to <a href="https://railway.app" target="_blank" style="color:var(--blue)">railway.app</a> → Login with GitHub → 
        <strong style="color:#fff">New Project</strong> → <strong style="color:#fff">Deploy from GitHub Repo</strong> → 
        select <code>jjs-server</code>. Railway auto-detects Node.js and deploys it.</p>
        <div class="cmd-block"><span class="comment"># Railway does this automatically — no commands needed</span>
<span class="comment"># It reads package.json and runs: node server.js</span></div>
      </div>
    </div>
    <div class="step">
      <div class="step-num">4</div>
      <div>
        <h3>Get your wss:// URL</h3>
        <p>In Railway: click your project → <strong style="color:#fff">Settings</strong> → 
        scroll to <strong style="color:#fff">Networking</strong> → click <strong style="color:#fff">Generate Domain</strong>. 
        You'll get a URL like:</p>
        <div class="cmd-block">wss://jjs-server-production.up.railway.app</div>
        <p style="margin-top:8px;">Copy that full URL (with <code>wss://</code> at the start).</p>
      </div>
    </div>
    <div class="step">
      <div class="step-num">5</div>
      <div>
        <h3>Share with your friend</h3>
        <p>Send your friend the <strong style="color:#fff">game website URL</strong> (Website 2 on Netlify) 
        AND the <strong style="color:#fff">wss:// server URL</strong>. Both of you open the game, 
        paste the same wss:// URL in the connect box, enter your names, pick your characters, and hit <strong style="color:#fff">JOIN BATTLE</strong>.</p>
      </div>
    </div>
  </div>

  <!-- SERVER CODE -->
  <div class="sec-label">Server files</div>

  <div class="two-col">
    <div>
      <div class="code-header">
        <h3>package.json</h3>
        <button class="copy-btn" onclick="copyCode('pkgjson',this)">Copy</button>
      </div>
      <div class="code-box" id="pkgjson">{
  <span class="key">"name"</span>: <span class="str">"jjs-server"</span>,
  <span class="key">"version"</span>: <span class="str">"1.0.0"</span>,
  <span class="key">"description"</span>: <span class="str">"Jujutsu Shenanigans server"</span>,
  <span class="key">"main"</span>: <span class="str">"server.js"</span>,
  <span class="key">"scripts"</span>: {
    <span class="key">"start"</span>: <span class="str">"node server.js"</span>
  },
  <span class="key">"dependencies"</span>: {
    <span class="key">"ws"</span>: <span class="str">"^8.16.0"</span>
  },
  <span class="key">"engines"</span>: {
    <span class="key">"node"</span>: <span class="str">"&gt;=18.0.0"</span>
  }
}</div>
    </div>
    <div>
      <div class="code-header">
        <h3>README tip</h3>
      </div>
      <div style="background:rgba(255,215,0,.04);border:1px solid rgba(255,215,0,.15);border-radius:12px;padding:20px;">
        <p style="font-size:13px;color:rgba(255,255,255,.5);line-height:1.8;">
          ⚡ Railway's <strong style="color:#fff">free tier</strong> gives you enough compute for several friends in the same match.<br><br>
          🔄 The server <strong style="color:#fff">auto-restarts</strong> if it crashes.<br><br>
          🌐 The <strong style="color:#fff">wss://</strong> URL works from anywhere in the world — no port forwarding needed.<br><br>
          ♻️ To reset the server, just click <strong style="color:#fff">Redeploy</strong> in Railway.
        </p>
      </div>
    </div>
  </div>

  <div class="code-header">
    <h3>server.js — Full server code</h3>
    <button class="copy-btn" onclick="copyCode('serverjs',this)">Copy All</button>
  </div>
  <div class="code-box" id="serverjs" style="max-height:700px;">
<span class="cm">/**
 * Jujutsu Shenanigans — WebSocket Game Server
 * Deploy on Railway / Render / any Node.js host
 * Run locally: npm install && node server.js
 */</span>

<span class="kw">const</span> WebSocket = <span class="fn">require</span>(<span class="str">'ws'</span>);
<span class="kw">const</span> PORT = process.env.PORT || <span class="num">8080</span>;
<span class="kw">const</span> server = <span class="kw">new</span> WebSocket.<span class="fn">Server</span>({ port: PORT });

<span class="cm">// ── Character definitions (must match client) ──</span>
<span class="kw">const</span> CHARS = {
  honored_one:     { maxHp:<span class="num">120</span>, speed:<span class="num">5.5</span>, moves:{ Q:{dmg:<span class="num">0</span>,cd:<span class="num">3</span>,range:<span class="num">3</span>,type:<span class="str">'defense'</span>,name:<span class="str">'Infinity Veil'</span>},    E:{dmg:<span class="num">45</span>,cd:<span class="num">4</span>,range:<span class="num">15</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Blue Pull'</span>},     R:{dmg:<span class="num">60</span>,cd:<span class="num">6</span>,range:<span class="num">15</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Red Crush'</span>},    F:{dmg:<span class="num">150</span>,cd:<span class="num">20</span>,range:<span class="num">20</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Hollow Purple'</span>} }},
  soul_striker:    { maxHp:<span class="num">180</span>, speed:<span class="num">6.2</span>, moves:{ Q:{dmg:<span class="num">55</span>,cd:<span class="num">2</span>,range:<span class="num">3.5</span>,type:<span class="str">'melee'</span>,name:<span class="str">'Divergent Fist'</span>},  E:{dmg:<span class="num">90</span>,cd:<span class="num">8</span>,range:<span class="num">3.5</span>,type:<span class="str">'melee'</span>,name:<span class="str">'Black Flash'</span>},    R:{dmg:<span class="num">30</span>,cd:<span class="num">3</span>,range:<span class="num">8</span>,type:<span class="str">'dash'</span>,name:<span class="str">'Boost Dash'</span>},      F:{dmg:<span class="num">200</span>,cd:<span class="num">25</span>,range:<span class="num">4</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Pummel Storm'</span>} }},
  shadow_summoner: { maxHp:<span class="num">150</span>, speed:<span class="num">5.0</span>, moves:{ Q:{dmg:<span class="num">40</span>,cd:<span class="num">5</span>,range:<span class="num">12</span>,type:<span class="str">'summon'</span>,name:<span class="str">'Divine Dogs'</span>},    E:{dmg:<span class="num">20</span>,cd:<span class="num">6</span>,range:<span class="num">10</span>,type:<span class="str">'cc'</span>,name:<span class="str">'Shadow Bind'</span>},      R:{dmg:<span class="num">35</span>,cd:<span class="num">10</span>,range:<span class="num">8</span>,type:<span class="str">'aoe'</span>,name:<span class="str">'Shadow Garden'</span>},   F:{dmg:<span class="num">180</span>,cd:<span class="num">30</span>,range:<span class="num">15</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Mahoraga'</span>} }},
  king_of_curses:  { maxHp:<span class="num">200</span>, speed:<span class="num">5.0</span>, moves:{ Q:{dmg:<span class="num">70</span>,cd:<span class="num">2</span>,range:<span class="num">12</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Dismantle'</span>},      E:{dmg:<span class="num">100</span>,cd:<span class="num">5</span>,range:<span class="num">5</span>,type:<span class="str">'melee'</span>,name:<span class="str">'Cleave'</span>},          R:{dmg:<span class="num">65</span>,cd:<span class="num">4</span>,range:<span class="num">14</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Flame Arrow'</span>},  F:{dmg:<span class="num">220</span>,cd:<span class="num">35</span>,range:<span class="num">18</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Malevolent Shrine'</span>} }},
  iron_maiden:     { maxHp:<span class="num">130</span>, speed:<span class="num">5.5</span>, moves:{ Q:{dmg:<span class="num">50</span>,cd:<span class="num">3</span>,range:<span class="num">14</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Hairpin Throw'</span>},  E:{dmg:<span class="num">60</span>,cd:<span class="num">5</span>,range:<span class="num">14</span>,type:<span class="str">'curse'</span>,name:<span class="str">'Straw Doll'</span>},     R:{dmg:<span class="num">80</span>,cd:<span class="num">8</span>,range:<span class="num">12</span>,type:<span class="str">'curse'</span>,name:<span class="str">'Resonance'</span>},      F:{dmg:<span class="num">190</span>,cd:<span class="num">28</span>,range:<span class="num">16</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Hairpin Rain'</span>} }},
  jackpot_man:     { maxHp:<span class="num">160</span>, speed:<span class="num">5.8</span>, moves:{ Q:{dmg:<span class="num">60</span>,cd:<span class="num">3</span>,range:<span class="num">10</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Pachinko Blast'</span>},  E:{dmg:<span class="num">0</span>,cd:<span class="num">8</span>,range:<span class="num">0</span>,type:<span class="str">'defense'</span>,name:<span class="str">'Idle Death Gamble'</span>}, R:{dmg:<span class="num">75</span>,cd:<span class="num">5</span>,range:<span class="num">12</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Card Slash'</span>},   F:{dmg:<span class="num">210</span>,cd:<span class="num">30</span>,range:<span class="num">16</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Elimination Chamber'</span>} }},
  dragon_fist:     { maxHp:<span class="num">170</span>, speed:<span class="num">6.0</span>, moves:{ Q:{dmg:<span class="num">65</span>,cd:<span class="num">2</span>,range:<span class="num">4</span>,type:<span class="str">'melee'</span>,name:<span class="str">'Dragon Strike'</span>},    E:{dmg:<span class="num">85</span>,cd:<span class="num">6</span>,range:<span class="num">4</span>,type:<span class="str">'melee'</span>,name:<span class="str">'Flame Rush'</span>},        R:{dmg:<span class="num">40</span>,cd:<span class="num">4</span>,range:<span class="num">6</span>,type:<span class="str">'dash'</span>,name:<span class="str">'Dragon Dash'</span>},        F:{dmg:<span class="num">195</span>,cd:<span class="num">28</span>,range:<span class="num">5</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Dragon Fury'</span>} }},
  blood_painter:   { maxHp:<span class="num">110</span>, speed:<span class="num">5.2</span>, moves:{ Q:{dmg:<span class="num">55</span>,cd:<span class="num">3</span>,range:<span class="num">13</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Paint Slash'</span>},    E:{dmg:<span class="num">70</span>,cd:<span class="num">5</span>,range:<span class="num">12</span>,type:<span class="str">'curse'</span>,name:<span class="str">'Red Scale'</span>},       R:{dmg:<span class="num">45</span>,cd:<span class="num">4</span>,range:<span class="num">11</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Slashing Red'</span>},  F:{dmg:<span class="num">175</span>,cd:<span class="num">25</span>,range:<span class="num">14</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Maximum: Uzumaki'</span>} }},
  steel_fist:      { maxHp:<span class="num">190</span>, speed:<span class="num">4.8</span>, moves:{ Q:{dmg:<span class="num">80</span>,cd:<span class="num">3</span>,range:<span class="num">4</span>,type:<span class="str">'melee'</span>,name:<span class="str">'Iron Fist'</span>},        E:{dmg:<span class="num">0</span>,cd:<span class="num">5</span>,range:<span class="num">0</span>,type:<span class="str">'defense'</span>,name:<span class="str">'Hardened Body'</span>},    R:{dmg:<span class="num">55</span>,cd:<span class="num">4</span>,range:<span class="num">5</span>,type:<span class="str">'melee'</span>,name:<span class="str">'Seismic Slam'</span>},      F:{dmg:<span class="num">205</span>,cd:<span class="num">32</span>,range:<span class="num">6</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Earthbreaker'</span>} }},
  wind_walker:     { maxHp:<span class="num">125</span>, speed:<span class="num">7.0</span>, moves:{ Q:{dmg:<span class="num">35</span>,cd:<span class="num">2</span>,range:<span class="num">12</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Wind Blade'</span>},     E:{dmg:<span class="num">0</span>,cd:<span class="num">4</span>,range:<span class="num">12</span>,type:<span class="str">'dash'</span>,name:<span class="str">'Gale Step'</span>},          R:{dmg:<span class="num">50</span>,cd:<span class="num">5</span>,range:<span class="num">10</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Tornado Cut'</span>},   F:{dmg:<span class="num">160</span>,cd:<span class="num">22</span>,range:<span class="num">14</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Eye of the Storm'</span>} }},
  void_curse:      { maxHp:<span class="num">140</span>, speed:<span class="num">5.3</span>, moves:{ Q:{dmg:<span class="num">60</span>,cd:<span class="num">3</span>,range:<span class="num">11</span>,type:<span class="str">'curse'</span>,name:<span class="str">'Void Touch'</span>},       E:{dmg:<span class="num">80</span>,cd:<span class="num">7</span>,range:<span class="num">9</span>,type:<span class="str">'cc'</span>,name:<span class="str">'Gravity Crush'</span>},       R:{dmg:<span class="num">45</span>,cd:<span class="num">4</span>,range:<span class="num">10</span>,type:<span class="str">'aoe'</span>,name:<span class="str">'Void Field'</span>},         F:{dmg:<span class="num">200</span>,cd:<span class="num">30</span>,range:<span class="num">17</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Cursed Domain'</span>} }},
  thunder_god:     { maxHp:<span class="num">145</span>, speed:<span class="num">6.0</span>, moves:{ Q:{dmg:<span class="num">55</span>,cd:<span class="num">2</span>,range:<span class="num">13</span>,type:<span class="str">'projectile'</span>,name:<span class="str">'Lightning Bolt'</span>},  E:{dmg:<span class="num">75</span>,cd:<span class="num">6</span>,range:<span class="num">8</span>,type:<span class="str">'aoe'</span>,name:<span class="str">'Thunder Clap'</span>},       R:{dmg:<span class="num">0</span>,cd:<span class="num">4</span>,range:<span class="num">10</span>,type:<span class="str">'dash'</span>,name:<span class="str">'Static Dash'</span>},        F:{dmg:<span class="num">185</span>,cd:<span class="num">26</span>,range:<span class="num">15</span>,type:<span class="str">'ultimate'</span>,name:<span class="str">'Mjolnir Storm'</span>} }},
};

<span class="kw">const</span> SPAWNS = [
  [<span class="num">2.5</span>,<span class="num">2.5</span>],[<span class="num">29.5</span>,<span class="num">2.5</span>],[<span class="num">2.5</span>,<span class="num">29.5</span>],[<span class="num">29.5</span>,<span class="num">29.5</span>],
  [<span class="num">8</span>,<span class="num">8</span>],[<span class="num">24</span>,<span class="num">8</span>],[<span class="num">8</span>,<span class="num">24</span>],[<span class="num">24</span>,<span class="num">24</span>],[<span class="num">16</span>,<span class="num">2.5</span>],[<span class="num">16</span>,<span class="num">29.5</span>],
];

<span class="kw">let</span> players = {}, killLog = [], pidCounter = <span class="num">0</span>;

<span class="fn">function</span> <span class="fn">getSpawn</span>(){ <span class="kw">return</span> [...SPAWNS[Math.<span class="fn">floor</span>(Math.<span class="fn">random</span>()*SPAWNS.length)]]; }
<span class="fn">function</span> <span class="fn">dist</span>(a,b){ <span class="kw">return</span> Math.<span class="fn">sqrt</span>((a.x-b.x)**<span class="num">2</span>+(a.z-b.z)**<span class="num">2</span>); }
<span class="fn">function</span> <span class="fn">nowSec</span>(){ <span class="kw">return</span> Date.<span class="fn">now</span>()/<span class="num">1000</span>; }

<span class="fn">function</span> <span class="fn">broadcast</span>(data, exclude=<span class="kw">null</span>){
  <span class="kw">const</span> msg = JSON.<span class="fn">stringify</span>(data);
  server.clients.<span class="fn">forEach</span>(c=>{ <span class="kw">if</span>(c!==exclude&&c.readyState===<span class="num">1</span>) c.<span class="fn">send</span>(msg); });
}

<span class="fn">function</span> <span class="fn">newPlayer</span>(pid,name,char){
  <span class="kw">const</span> c = CHARS[char]||CHARS.soul_striker;
  <span class="kw">const</span> [sx,sz] = <span class="fn">getSpawn</span>();
  <span class="kw">return</span> { id:pid, name, character:char, x:sx, y:<span class="num">0</span>, z:sz, yaw:<span class="num">0</span>,
    hp:c.maxHp, maxHp:c.maxHp, kills:<span class="num">0</span>, deaths:<span class="num">0</span>,
    alive:<span class="kw">true</span>, invincible:<span class="kw">false</span>, rooted:<span class="kw">false</span>, dashing:<span class="kw">false</span>,
    cooldowns:{}, respawnAt:<span class="num">0</span> };
}

<span class="fn">function</span> <span class="fn">applyDamage</span>(atk,tgt,dmg,moveName){
  <span class="kw">const</span> t=players[tgt], a=players[atk];
  <span class="kw">if</span>(!t||!a||!t.alive||t.invincible) <span class="kw">return</span>;
  t.hp = Math.<span class="fn">max</span>(<span class="num">0</span>, t.hp-dmg);
  <span class="kw">if</span>(t.hp<=<span class="num">0</span>){
    t.alive=<span class="kw">false</span>; t.respawnAt=<span class="fn">nowSec</span>()+<span class="num">5</span>; a.kills++; t.deaths++;
    <span class="kw">const</span> entry=`${a.name} eliminated ${t.name} with ${moveName}!`;
    killLog.<span class="fn">push</span>(entry); <span class="kw">if</span>(killLog.length><span class="num">10</span>) killLog.<span class="fn">shift</span>();
    <span class="fn">broadcast</span>({type:<span class="str">'kill_feed'</span>,attacker:a.name,victim:t.name,move:moveName,killLog});
  }
}

server.<span class="fn">on</span>(<span class="str">'connection'</span>, ws2 => {
  <span class="kw">let</span> pid = <span class="kw">null</span>;
  ws2.<span class="fn">on</span>(<span class="str">'message'</span>, raw => {
    <span class="kw">try</span>{
      <span class="kw">const</span> msg = JSON.<span class="fn">parse</span>(raw);

      <span class="kw">if</span>(msg.type===<span class="str">'join'</span>&&!pid){
        pidCounter++;  pid=pidCounter;
        <span class="kw">const</span> char=CHARS[msg.character]?msg.character:<span class="str">'soul_striker'</span>;
        players[pid]=<span class="fn">newPlayer</span>(pid,(msg.name||<span class="str">'Player'</span>).<span class="fn">substring</span>(<span class="num">0</span>,<span class="num">16</span>),char);
        ws2.<span class="fn">send</span>(JSON.<span class="fn">stringify</span>({type:<span class="str">'welcome'</span>,yourId:pid}));
        console.<span class="fn">log</span>(`[+] ${players[pid].name} joined as ${char}`);
        <span class="kw">return</span>;
      }

      <span class="kw">if</span>(!pid||!players[pid]) <span class="kw">return</span>;
      <span class="kw">const</span> p=players[pid];

      <span class="kw">if</span>(msg.type===<span class="str">'move'</span>&&p.alive&&!p.rooted){
        p.x=isFinite(msg.x)?Math.<span class="fn">max</span>(<span class="num">0.5</span>,Math.<span class="fn">min</span>(<span class="num">31.5</span>,msg.x)):p.x;
        p.z=isFinite(msg.z)?Math.<span class="fn">max</span>(<span class="num">0.5</span>,Math.<span class="fn">min</span>(<span class="num">31.5</span>,msg.z)):p.z;
        p.yaw=isFinite(msg.yaw)?msg.yaw:p.yaw;
      }
      <span class="kw">else if</span>(msg.type===<span class="str">'use_move'</span>){
        <span class="kw">const</span> k=msg.key, char=CHARS[p.character]||CHARS.soul_striker;
        <span class="kw">const</span> mv=char.moves[k];
        <span class="kw">if</span>(!mv||!p.alive) <span class="kw">return</span>;
        <span class="kw">if</span>(<span class="fn">nowSec</span>()-(p.cooldowns[k]||<span class="num">0</span>)<mv.cd) <span class="kw">return</span>;
        p.cooldowns[k]=<span class="fn">nowSec</span>();

        <span class="kw">if</span>(mv.type===<span class="str">'defense'</span>){
          p.invincible=<span class="kw">true</span>;
          <span class="fn">setTimeout</span>(()=>{ <span class="kw">if</span>(players[pid]) players[pid].invincible=<span class="kw">false</span>; },<span class="num">2000</span>);
          <span class="fn">broadcast</span>({type:<span class="str">'move_effect'</span>,pid,move:mv.name,effect:<span class="str">'shield'</span>,x:p.x,z:p.z,range:<span class="num">3</span>});
          <span class="kw">return</span>;
        }
        <span class="kw">if</span>(mv.type===<span class="str">'dash'</span>&&mv.dmg===<span class="num">0</span>){
          <span class="cm">// Pure movement dash — handled client side, just broadcast</span>
          <span class="fn">broadcast</span>({type:<span class="str">'move_effect'</span>,pid,move:mv.name,effect:<span class="str">'dash'</span>,x:p.x,z:p.z,range:mv.range});
          <span class="kw">return</span>;
        }

        Object.<span class="fn">entries</span>(players).<span class="fn">forEach</span>(([tid,tp])=>{
          <span class="kw">if</span>(tid==pid||!tp.alive) <span class="kw">return</span>;
          <span class="kw">if</span>(<span class="fn">dist</span>(p,tp)<=mv.range){
            <span class="fn">applyDamage</span>(pid,<span class="fn">parseInt</span>(tid),mv.dmg,mv.name);
            <span class="kw">if</span>(mv.type===<span class="str">'cc'</span>&&!tp.invincible){
              tp.rooted=<span class="kw">true</span>;
              <span class="fn">setTimeout</span>(()=>{ <span class="kw">if</span>(players[tid]) players[tid].rooted=<span class="kw">false</span>; },<span class="num">2000</span>);
            }
          }
        });
        <span class="fn">broadcast</span>({type:<span class="str">'move_effect'</span>,pid,move:mv.name,effect:mv.type,x:p.x,z:p.z,range:mv.range});
      }
      <span class="kw">else if</span>(msg.type===<span class="str">'switch_character'</span>){
        <span class="kw">const</span> char=CHARS[msg.character]?msg.character:<span class="str">'soul_striker'</span>;
        <span class="kw">const</span> c=CHARS[char], [sx,sz]=<span class="fn">getSpawn</span>();
        p.character=char; p.hp=c.maxHp; p.maxHp=c.maxHp;
        p.x=sx; p.z=sz; p.alive=<span class="kw">true</span>; p.invincible=<span class="kw">false</span>; p.rooted=<span class="kw">false</span>; p.cooldowns={};
        console.<span class="fn">log</span>(`  ${p.name} switched to ${char}`);
      }
    }<span class="kw">catch</span>(e){}
  });
  ws2.<span class="fn">on</span>(<span class="str">'close'</span>,()=>{ <span class="kw">if</span>(pid&&players[pid]){ console.<span class="fn">log</span>(`[-] ${players[pid].name} left`); <span class="kw">delete</span> players[pid]; }});
});

<span class="cm">// State broadcast 20Hz</span>
<span class="fn">setInterval</span>(()=>{
  <span class="kw">const</span> t=<span class="fn">nowSec</span>();
  Object.<span class="fn">values</span>(players).<span class="fn">forEach</span>(p=>{
    <span class="kw">if</span>(!p.alive&&p.respawnAt<=t){
      <span class="kw">const</span> c=CHARS[p.character]; <span class="kw">const</span> [sx,sz]=<span class="fn">getSpawn</span>();
      p.x=sx;p.z=sz;p.hp=c.maxHp;p.alive=<span class="kw">true</span>;p.invincible=<span class="kw">false</span>;p.rooted=<span class="kw">false</span>;
    }
  });
  <span class="kw">const</span> lb=Object.<span class="fn">values</span>(players).<span class="fn">sort</span>((a,b)=>b.kills-a.kills).<span class="fn">slice</span>(<span class="num">0</span>,<span class="num">10</span>)
    .<span class="fn">map</span>(p=>({name:p.name,char:p.character,kills:p.kills,deaths:p.deaths}));
  <span class="kw">const</span> pkt={type:<span class="str">'state'</span>,players:{},leaderboard:lb,killLog:killLog.<span class="fn">slice</span>(-<span class="num">5</span>)};
  Object.<span class="fn">entries</span>(players).<span class="fn">forEach</span>(([id,p])=>{
    <span class="kw">const</span> char=CHARS[p.character]||CHARS.soul_striker, cds={};
    Object.<span class="fn">entries</span>(p.cooldowns).<span class="fn">forEach</span>(([k,v])=>{ cds[k]=Math.<span class="fn">max</span>(<span class="num">0</span>,char.moves[k].cd-(t-v)); });
    pkt.players[id]={id:p.id,name:p.name,character:p.character,x:p.x,y:p.y,z:p.z,yaw:p.yaw,
      hp:p.hp,maxHp:p.maxHp,kills:p.kills,deaths:p.deaths,alive:p.alive,
      invincible:p.invincible,rooted:p.rooted,cooldowns:cds};
  });
  <span class="kw">const</span> msg=JSON.<span class="fn">stringify</span>(pkt);
  server.clients.<span class="fn">forEach</span>(c=>{ <span class="kw">if</span>(c.readyState===<span class="num">1</span>) c.<span class="fn">send</span>(msg); });
}, <span class="num">50</span>);

console.<span class="fn">log</span>(<span class="str">`⚡ Jujutsu Shenanigans server on port ${PORT}`</span>);</div>

  <!-- PLATFORMS -->
  <div class="sec-label" style="margin-top:40px;">Where to deploy</div>
  <div class="platforms">
    <div class="plat">
      <div class="plat-name">Railway <span style="color:var(--gold)">★ Recommended</span></div>
      <div class="plat-free">Free tier available</div>
      <p>Easiest option. Auto-detects Node.js, gives you a <code>wss://</code> URL, handles SSL automatically.</p>
      <div class="plat-steps">
        <li>Go to <a href="https://railway.app" target="_blank">railway.app</a></li>
        <li>Login with GitHub</li>
        <li>New Project → Deploy from GitHub</li>
        <li>Select your <code>jjs-server</code> repo</li>
        <li>Settings → Networking → Generate Domain</li>
        <li>Copy the <code>wss://</code> URL</li>
      </div>
    </div>
    <div class="plat">
      <div class="plat-name">Render</div>
      <div class="plat-free">Free tier available</div>
      <p>Also excellent. Use "Web Service" type. May spin down after 15 min inactivity on free tier.</p>
      <div class="plat-steps">
        <li>Go to <a href="https://render.com" target="_blank">render.com</a></li>
        <li>New → Web Service</li>
        <li>Connect GitHub repo</li>
        <li>Build: <code>npm install</code></li>
        <li>Start: <code>node server.js</code></li>
        <li>Copy the <code>wss://</code> URL from dashboard</li>
      </div>
    </div>
    <div class="plat">
      <div class="plat-name">Fly.io</div>
      <div class="plat-free">Free allowance</div>
      <p>More advanced, persistent, global edge deployment. Use if you want lowest latency.</p>
      <div class="plat-steps">
        <li>Install flyctl CLI</li>
        <li><code>fly launch</code> in your repo folder</li>
        <li><code>fly deploy</code></li>
        <li>URL format: <code>wss://app-name.fly.dev</code></li>
      </div>
    </div>
  </div>

  <div class="infobox">
    <div class="infobox-icon">💡</div>
    <div>
      <h4>After deploying</h4>
      <p>Your server URL will look like: <code>wss://jjs-server-production.up.railway.app</code><br>
      Paste that exact URL (with <code>wss://</code>) into the game's connect screen. 
      Share it with friends — everyone who pastes the same URL joins the same server. 
      The server handles up to ~50 players. For more, upgrade Railway's plan.</p>
    </div>
  </div>

</div>

<footer>
  ⚡ <span>Jujutsu Shenanigans</span> — Server Manager &nbsp;·&nbsp; Deploy once, fight forever
</footer>

<script>
function copyCode(id, btn){
  const el = document.getElementById(id);
  const text = el.innerText;
  navigator.clipboard.writeText(text).then(()=>{
    btn.textContent='Copied!';
    btn.classList.add('copied');
    setTimeout(()=>{ btn.textContent='Copy'; btn.classList.remove('copied'); },2000);
  });
}
</script>
</body>
</html>
