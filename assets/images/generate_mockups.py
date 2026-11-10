import os

images_dir = "/home/mars/Projects/Portfolio/assets/images"
os.makedirs(images_dir, exist_ok=True)

# 1. Veda Voice Assistant SVG Mockup
veda_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#120c1e"/>
      <stop offset="50%" stop-color="#19102b"/>
      <stop offset="100%" stop-color="#0a0612"/>
    </linearGradient>
    <linearGradient id="wave-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7928ca"/>
      <stop offset="50%" stop-color="#ff0080"/>
      <stop offset="100%" stop-color="#00dfd8"/>
    </linearGradient>
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22163b" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#160e26" stop-opacity="0.9"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="800" height="500" rx="16" fill="url(#bg-grad)"/>

  <!-- Window Header -->
  <rect width="800" height="42" rx="16" fill="#1b122f"/>
  <rect y="26" width="800" height="16" fill="#1b122f"/>
  <circle cx="28" cy="21" r="6" fill="#ff5f56"/>
  <circle cx="48" cy="21" r="6" fill="#ffbd2e"/>
  <circle cx="68" cy="21" r="6" fill="#27c93f"/>
  <text x="400" y="26" fill="#9d8bb8" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="13" font-weight="500" text-anchor="middle">veda-voice-assistant — ai companion</text>

  <!-- Top Badges -->
  <g transform="translate(40, 65)">
    <rect width="180" height="28" rx="14" fill="#261742" stroke="#7928ca" stroke-width="1"/>
    <circle cx="16" cy="14" r="4" fill="#00dfd8" filter="url(#glow)"/>
    <text x="28" y="18" fill="#e2d9f3" font-family="sans-serif" font-size="11" font-weight="600">WebRTC VAD: ACTIVE</text>

    <rect x="195" width="130" height="28" rx="14" fill="#261742" stroke="#ff0080" stroke-width="1"/>
    <text x="210" y="18" fill="#ff99cf" font-family="sans-serif" font-size="11" font-weight="600">LATENCY: 128ms</text>

    <rect x="340" width="160" height="28" rx="14" fill="#261742" stroke="#4285f4" stroke-width="1"/>
    <text x="355" y="18" fill="#a8c7fa" font-family="sans-serif" font-size="11" font-weight="600">LLM: GEMINI + GPT-4</text>
  </g>

  <!-- Audio Waveform Visualizer -->
  <g transform="translate(40, 115)">
    <rect width="720" height="110" rx="14" fill="url(#card-grad)" stroke="#39245e" stroke-width="1"/>
    <text x="24" y="32" fill="#d0bdf4" font-family="sans-serif" font-size="12" font-weight="600">SPEECH WAVEFORM STREAM</text>

    <!-- Wave Bars -->
    <g transform="translate(30, 48)">
      <rect x="0" y="20" width="6" height="25" rx="3" fill="url(#wave-grad)"/>
      <rect x="14" y="10" width="6" height="45" rx="3" fill="url(#wave-grad)"/>
      <rect x="28" y="2" width="6" height="60" rx="3" fill="url(#wave-grad)"/>
      <rect x="42" y="15" width="6" height="35" rx="3" fill="url(#wave-grad)"/>
      <rect x="56" y="5" width="6" height="55" rx="3" fill="url(#wave-grad)"/>
      <rect x="70" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)" filter="url(#glow)"/>
      <rect x="84" y="8" width="6" height="50" rx="3" fill="url(#wave-grad)"/>
      <rect x="98" y="18" width="6" height="30" rx="3" fill="url(#wave-grad)"/>
      <rect x="112" y="24" width="6" height="18" rx="3" fill="url(#wave-grad)"/>
      <rect x="126" y="12" width="6" height="42" rx="3" fill="url(#wave-grad)"/>
      <rect x="140" y="4" width="6" height="58" rx="3" fill="url(#wave-grad)"/>
      <rect x="154" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)" filter="url(#glow)"/>
      <rect x="168" y="10" width="6" height="45" rx="3" fill="url(#wave-grad)"/>
      <rect x="182" y="20" width="6" height="25" rx="3" fill="url(#wave-grad)"/>
      <rect x="196" y="5" width="6" height="55" rx="3" fill="url(#wave-grad)"/>
      <rect x="210" y="14" width="6" height="38" rx="3" fill="url(#wave-grad)"/>
      <rect x="224" y="22" width="6" height="20" rx="3" fill="url(#wave-grad)"/>
      <rect x="238" y="8" width="6" height="50" rx="3" fill="url(#wave-grad)"/>
      <rect x="252" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)" filter="url(#glow)"/>
      <rect x="266" y="6" width="6" height="52" rx="3" fill="url(#wave-grad)"/>
      <rect x="280" y="18" width="6" height="28" rx="3" fill="url(#wave-grad)"/>
      <rect x="294" y="25" width="6" height="15" rx="3" fill="url(#wave-grad)"/>
      <rect x="308" y="15" width="6" height="35" rx="3" fill="url(#wave-grad)"/>
      <rect x="322" y="5" width="6" height="55" rx="3" fill="url(#wave-grad)"/>
      <rect x="336" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)"/>
      <rect x="350" y="12" width="6" height="42" rx="3" fill="url(#wave-grad)"/>
      <rect x="364" y="20" width="6" height="25" rx="3" fill="url(#wave-grad)"/>
      <rect x="378" y="8" width="6" height="48" rx="3" fill="url(#wave-grad)"/>
      <rect x="392" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)" filter="url(#glow)"/>
      <rect x="406" y="14" width="6" height="38" rx="3" fill="url(#wave-grad)"/>
      <rect x="420" y="22" width="6" height="22" rx="3" fill="url(#wave-grad)"/>
      <rect x="434" y="6" width="6" height="54" rx="3" fill="url(#wave-grad)"/>
      <rect x="448" y="12" width="6" height="42" rx="3" fill="url(#wave-grad)"/>
      <rect x="462" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)"/>
      <rect x="476" y="16" width="6" height="34" rx="3" fill="url(#wave-grad)"/>
      <rect x="490" y="24" width="6" height="18" rx="3" fill="url(#wave-grad)"/>
      <rect x="504" y="8" width="6" height="50" rx="3" fill="url(#wave-grad)"/>
      <rect x="518" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)" filter="url(#glow)"/>
      <rect x="532" y="10" width="6" height="46" rx="3" fill="url(#wave-grad)"/>
      <rect x="546" y="20" width="6" height="26" rx="3" fill="url(#wave-grad)"/>
      <rect x="560" y="4" width="6" height="58" rx="3" fill="url(#wave-grad)"/>
      <rect x="574" y="15" width="6" height="36" rx="3" fill="url(#wave-grad)"/>
      <rect x="588" y="22" width="6" height="22" rx="3" fill="url(#wave-grad)"/>
      <rect x="602" y="10" width="6" height="45" rx="3" fill="url(#wave-grad)"/>
      <rect x="616" y="0" width="6" height="65" rx="3" fill="url(#wave-grad)"/>
      <rect x="630" y="16" width="6" height="34" rx="3" fill="url(#wave-grad)"/>
      <rect x="644" y="24" width="6" height="18" rx="3" fill="url(#wave-grad)"/>
    </g>
  </g>

  <!-- Live Conversation Dialogue Box -->
  <g transform="translate(40, 245)">
    <rect width="720" height="225" rx="14" fill="#181126" stroke="#31224f" stroke-width="1"/>
    
    <!-- User Bubble -->
    <g transform="translate(24, 20)">
      <rect width="52" height="22" rx="6" fill="#39245e"/>
      <text x="12" y="15" fill="#e2d9f3" font-family="sans-serif" font-size="11" font-weight="700">USER</text>
      <text x="64" y="16" fill="#ffffff" font-family="sans-serif" font-size="13">"Veda, how does our audio pipeline achieve sub-200ms response times?"</text>
    </g>

    <!-- Veda AI Bubble -->
    <g transform="translate(24, 62)">
      <rect width="54" height="22" rx="6" fill="#00dfd8"/>
      <text x="10" y="15" fill="#000000" font-family="sans-serif" font-size="11" font-weight="700">VEDA</text>
      <text x="64" y="16" fill="#00dfd8" font-family="sans-serif" font-size="13" font-weight="600">Deepgram Nova-2 Streaming STT + WebRTC VAD</text>
      <text x="24" y="44" fill="#c4b5e0" font-family="sans-serif" font-size="12.5" line-height="1.5">
        "We capture chunks directly through PipeWire/PulseAudio, apply silence clipping,
      </text>
      <text x="24" y="66" fill="#c4b5e0" font-family="sans-serif" font-size="12.5">
        and stream concurrently to LLM endpoints with automated model failover."
      </text>
    </g>

    <!-- Footer Chips -->
    <g transform="translate(24, 175)">
      <rect width="115" height="26" rx="6" fill="#261742"/>
      <text x="12" y="17" fill="#a48fd1" font-family="monospace" font-size="11">Python 3.12</text>

      <rect x="125" width="135" height="26" rx="6" fill="#261742"/>
      <text x="137" y="17" fill="#a48fd1" font-family="monospace" font-size="11">Deepgram Nova-2</text>

      <rect x="270" width="110" height="26" rx="6" fill="#261742"/>
      <text x="282" y="17" fill="#a48fd1" font-family="monospace" font-size="11">Edge-TTS</text>

      <rect x="390" width="140" height="26" rx="6" fill="#261742"/>
      <text x="402" y="17" fill="#a48fd1" font-family="monospace" font-size="11">PulseAudio/VAD</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(images_dir, "veda.svg"), "w") as f:
    f.write(veda_svg)

# 2. Multi-User Chat System Terminal Mockup
chat_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="term-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1613"/>
      <stop offset="100%" stop-color="#050a08"/>
    </linearGradient>
  </defs>

  <!-- Window Frame -->
  <rect width="800" height="500" rx="16" fill="url(#term-bg)" stroke="#1d382d" stroke-width="1.5"/>

  <!-- Window Header -->
  <rect width="800" height="42" rx="16" fill="#14261f"/>
  <rect y="26" width="800" height="16" fill="#14261f"/>
  <circle cx="28" cy="21" r="6" fill="#ff5f56"/>
  <circle cx="48" cy="21" r="6" fill="#ffbd2e"/>
  <circle cx="68" cy="21" r="6" fill="#27c93f"/>
  <text x="400" y="26" fill="#75a894" font-family="monospace" font-size="13" font-weight="600" text-anchor="middle">mars@systems-lab: ~/chat_project (c / posix sockets)</text>

  <!-- Terminal Content -->
  <g transform="translate(35, 75)" font-family="'JetBrains Mono', 'Fira Code', 'Courier New', monospace" font-size="13">
    <!-- Command -->
    <text x="0" y="0" fill="#00ffaa" font-weight="700">mars@lab:~$</text>
    <text x="110" y="0" fill="#ffffff">./server --port 8080 --threads 16 --nonblock</text>

    <!-- Server Output -->
    <text x="0" y="32" fill="#69857b">[INIT]</text>
    <text x="60" y="32" fill="#9cd6c3">Socket descriptor created (AF_INET, SOCK_STREAM)</text>

    <text x="0" y="60" fill="#69857b">[BIND]</text>
    <text x="60" y="60" fill="#9cd6c3">Bound successfully to 0.0.0.0:8080 (SO_REUSEADDR enabled)</text>

    <text x="0" y="88" fill="#69857b">[LISTEN]</text>
    <text x="60" y="88" fill="#00ffaa">Master accept loop listening for concurrent connections...</text>

    <!-- Client Events -->
    <text x="0" y="125" fill="#facc15">[CONNECT]</text>
    <text x="85" y="125" fill="#ffffff">Client #1 connected from 127.0.0.1:54210 -> pthread_create(worker_1)</text>

    <text x="0" y="153" fill="#facc15">[AUTH]</text>
    <text x="85" y="153" fill="#ffffff">Handshake verified: user &apos;adios-mars&apos; registered to #systems</text>

    <text x="0" y="181" fill="#facc15">[CONNECT]</text>
    <text x="85" y="181" fill="#ffffff">Client #2 connected from 127.0.0.1:54218 -> pthread_create(worker_2)</text>

    <text x="0" y="218" fill="#38bdf8">[FILE_TRANSFER]</text>
    <text x="135" y="218" fill="#e0f2fe">Chunked stream started: kernel_image.iso (42.8 MB)</text>

    <text x="0" y="246" fill="#38bdf8">[FRAMING]</text>
    <text x="135" y="246" fill="#93c5fd">8192-byte frames | SHA-256 handshake: VERIFIED | zero packet loss</text>

    <text x="0" y="280" fill="#4ade80">[MUTEX]</text>
    <text x="85" y="280" fill="#86efac">pthread_mutex_lock(&amp;room_registry_lock) -> 0 contention deadlocks</text>

    <!-- Prompt with blinking cursor -->
    <text x="0" y="335" fill="#00ffaa" font-weight="700">mars@lab:~$</text>
    <text x="110" y="335" fill="#ffffff">netstat -tulpn | grep 8080</text>
    <rect x="365" y="322" width="9" height="17" fill="#00ffaa"/>

    <!-- Bottom specs bar -->
    <g transform="translate(0, 370)">
      <rect width="730" height="30" rx="6" fill="#14261f" stroke="#1d382d" stroke-width="1"/>
      <text x="15" y="20" fill="#75a894" font-size="11">POLL / EPOLL</text>
      <text x="120" y="20" fill="#75a894" font-size="11">POSIX THREADS</text>
      <text x="240" y="20" fill="#75a894" font-size="11">RAW BERKELEY SOCKETS</text>
      <text x="430" y="20" fill="#00ffaa" font-size="11" font-weight="700">STATUS: ACTIVE 0% PACKET DROP</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(images_dir, "chat.svg"), "w") as f:
    f.write(chat_svg)

# 3. Campus Attendance Bot Telegram UI Mockup
bot_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="tg-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#182330"/>
      <stop offset="100%" stop-color="#0f1620"/>
    </linearGradient>
    <linearGradient id="tg-bubble" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2b5278"/>
      <stop offset="100%" stop-color="#1e3a55"/>
    </linearGradient>
  </defs>

  <!-- Window Frame -->
  <rect width="800" height="500" rx="16" fill="url(#tg-bg)" stroke="#22364a" stroke-width="1.5"/>

  <!-- Window Header -->
  <rect width="800" height="50" rx="16" fill="#202d3d"/>
  <rect y="32" width="800" height="18" fill="#202d3d"/>
  <circle cx="28" cy="25" r="6" fill="#ff5f56"/>
  <circle cx="48" cy="25" r="6" fill="#ffbd2e"/>
  <circle cx="68" cy="25" r="6" fill="#27c93f"/>

  <!-- Telegram Bot Avatar & Header -->
  <circle cx="120" cy="25" r="16" fill="#2aabee"/>
  <text x="120" y="30" fill="#ffffff" font-family="sans-serif" font-size="15" font-weight="700" text-anchor="middle">🤖</text>
  <text x="145" y="24" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="600">Campus Attendance Bot</text>
  <text x="145" y="39" fill="#6c88a3" font-family="sans-serif" font-size="11">bot &middot; Python Aiogram 3 &middot; SQLite</text>

  <!-- Chat Messages -->
  <g transform="translate(40, 75)">
    <!-- Bot Message 1 -->
    <rect width="480" height="110" rx="12" fill="url(#tg-bubble)"/>
    <text x="20" y="28" fill="#54c4ff" font-family="sans-serif" font-size="13" font-weight="700">Attendance Manager v2.4 (Active Session)</text>
    <text x="20" y="52" fill="#ffffff" font-family="sans-serif" font-size="12.5">Course: Software Architecture (SE-402)</text>
    <text x="20" y="74" fill="#ffffff" font-family="sans-serif" font-size="12.5">Hall: Tech Lab 3 &middot; Time: 10:00 AM &ndash; 12:00 PM</text>
    <text x="20" y="96" fill="#9ec5e8" font-family="sans-serif" font-size="11.5">Tap below to log present status or request automated PDF.</text>

    <!-- Inline Keyboard Buttons -->
    <g transform="translate(0, 120)">
      <rect width="235" height="36" rx="8" fill="#203a54" stroke="#375d85" stroke-width="1"/>
      <text x="117" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="600" text-anchor="middle">✅ Mark Present (One-Tap)</text>

      <rect x="245" width="235" height="36" rx="8" fill="#203a54" stroke="#375d85" stroke-width="1"/>
      <text x="362" y="23" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="600" text-anchor="middle">📊 Real-Time Stats</text>
    </g>

    <!-- Stats Card Response -->
    <g transform="translate(0, 175)">
      <rect width="720" height="180" rx="12" fill="#1b2838" stroke="#2c4460" stroke-width="1"/>
      <text x="24" y="32" fill="#54c4ff" font-family="sans-serif" font-size="14" font-weight="700">SESSION ATTENDANCE SUMMARY</text>
      
      <!-- Progress Bar -->
      <g transform="translate(24, 50)">
        <rect width="670" height="10" rx="5" fill="#0f1722"/>
        <rect width="615" height="10" rx="5" fill="#22c55e"/>
      </g>
      <text x="24" y="80" fill="#ffffff" font-family="sans-serif" font-size="13">Present: 48 Students (91.8%) &middot; Absent: 4</text>
      <text x="24" y="104" fill="#8ca4bc" font-family="sans-serif" font-size="12">Database: SQLite with atomic write lock transactions</text>

      <!-- Action Chips -->
      <g transform="translate(24, 125)">
        <rect width="180" height="32" rx="6" fill="#173522" stroke="#22c55e" stroke-width="1"/>
        <text x="90" y="21" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="600" text-anchor="middle">📄 PDF Export Ready</text>

        <rect x="195" width="180" height="32" rx="6" fill="#203a54" stroke="#375d85" stroke-width="1"/>
        <text x="285" y="21" fill="#9ec5e8" font-family="sans-serif" font-size="12" font-weight="600" text-anchor="middle">🔒 Admin Verified</text>
      </g>
    </g>
  </g>
</svg>'''

with open(os.path.join(images_dir, "bot.svg"), "w") as f:
    f.write(bot_svg)

# 4. Taxi Ale Navigation App Mockup
taxi_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="map-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#13242e"/>
      <stop offset="100%" stop-color="#0b161c"/>
    </linearGradient>
  </defs>

  <!-- Window Frame -->
  <rect width="800" height="500" rx="16" fill="url(#map-bg)" stroke="#1f4052" stroke-width="1.5"/>

  <!-- Window Header -->
  <rect width="800" height="42" rx="16" fill="#162e3b"/>
  <rect y="26" width="800" height="16" fill="#162e3b"/>
  <circle cx="28" cy="21" r="6" fill="#ff5f56"/>
  <circle cx="48" cy="21" r="6" fill="#ffbd2e"/>
  <circle cx="68" cy="21" r="6" fill="#27c93f"/>
  <text x="400" y="26" fill="#75b2cc" font-family="sans-serif" font-size="13" font-weight="600" text-anchor="middle">Taxi Ale (ታክሲ አለ) — Real-Time Minibus Transit Navigator</text>

  <!-- Simulated Dark Map Lines & Roads -->
  <g stroke="#1d4254" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" opacity="0.6">
    <path d="M-20 180 L220 160 L450 280 L750 210 L820 220"/>
    <path d="M120 40 L220 160 L310 480"/>
    <path d="M450 280 L490 520"/>
    <path d="M400 40 L450 280 L620 120"/>
    <path d="M220 160 L500 130 L720 380"/>
  </g>

  <!-- Active Transit Route (Glowing Cyan Line) -->
  <path d="M80 340 L220 270 L380 230 L550 160 L700 140" stroke="#00dfd8" stroke-width="6" stroke-linecap="round" fill="none" opacity="0.9"/>
  <circle cx="80" cy="340" r="8" fill="#ff0080"/>
  <text x="70" y="375" fill="#ff99cf" font-family="sans-serif" font-size="12" font-weight="700">Megenagna</text>

  <circle cx="700" cy="140" r="8" fill="#22c55e"/>
  <text x="680" y="120" fill="#4ade80" font-family="sans-serif" font-size="12" font-weight="700">Piazza</text>

  <!-- Floating Minibus Position -->
  <g transform="translate(380, 230)">
    <circle r="22" fill="#00dfd8" fill-opacity="0.25"/>
    <circle r="14" fill="#00dfd8"/>
    <text y="5" fill="#000000" font-family="sans-serif" font-size="13" font-weight="900" text-anchor="middle">🚐</text>
  </g>

  <!-- Overlay UI Card (Top Left) -->
  <g transform="translate(40, 65)">
    <rect width="320" height="95" rx="12" fill="#0f2029" stroke="#1f4a5e" stroke-width="1.5"/>
    <text x="18" y="28" fill="#00dfd8" font-family="sans-serif" font-size="13" font-weight="700">ROUTE: MEGENAGNA → PIAZZA</text>
    <text x="18" y="52" fill="#ffffff" font-family="sans-serif" font-size="12">Next Arrival: 4 mins &middot; Fare: 15 ETB</text>
    <text x="18" y="75" fill="#75b2cc" font-family="sans-serif" font-size="11.5">🟢 3 Seats Available &middot; Driver Verified</text>
  </g>

  <!-- Bottom Floating Stats Bar -->
  <g transform="translate(40, 410)">
    <rect width="720" height="55" rx="12" fill="#0d1b22" stroke="#1f4a5e" stroke-width="1"/>
    <text x="24" y="32" fill="#ffffff" font-family="sans-serif" font-size="12.5" font-weight="600">Built with Flutter &amp; Dart</text>
    <text x="220" y="32" fill="#75b2cc" font-family="sans-serif" font-size="12">OpenStreetMap Tiles &middot; OSRM Routing Engine &middot; Two-Phase GPS</text>
  </g>
</svg>'''

with open(os.path.join(images_dir, "taxi.svg"), "w") as f:
    f.write(taxi_svg)

print("Mockup generation complete!")
