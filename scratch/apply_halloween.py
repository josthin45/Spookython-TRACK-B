import re

path = "src/api/static/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Title and Google Fonts
old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Courier+Prime:wght@400;700&family=Saira+Stencil+One&family=Special+Elite&display=swap" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Creepster&family=Chakra+Petch:wght@400;600;700&family=Archivo:wght@400;500;600;700;800&family=Courier+Prime:wght@400;700&family=Saira+Stencil+One&family=Special+Elite&display=swap" rel="stylesheet">'
html = html.replace(old_fonts, new_fonts)

html = html.replace(
    "<title>Comité de Contención Manta — Infección por Cordyceps (The Last of Us)</title>",
    "<title>🎃 SPOOKYTHON 2026 · Comité de Contención Manta — Plaga Cordyceps</title>"
)

# 2. Update :root variables to Halloween colors
old_root = """:root {
      --void: #0b0d09;
      --void-2: #12150e;
      --void-3: #1a1e15;
      --steel: #2a2f23;
      --steel-2: #3e4632;
      --paper: #d8d0b8;
      --paper-2: #c9c0a5;
      --paper-3: #e6dfc9;
      --paper-4: #f0ead8;
      --paper-edge: #a89f86;
      --paper-shadow: #8f876f;
      --ink: #1a1b15;
      --ink-2: #3d3f31;
      --ink-3: #555644;
      --olive: #6f7a54;
      --olive-2: #8b936c;
      --olive-dark: #3e4632;
      --rust: #9b3b2c;
      --rust-2: #b24a37;
      --rust-deep: #6f291e;
      --amber: #b8843b;
      --amber-2: #d2a052;
      --sage: #4f6b52;
      --sage-2: #6f8f70;
      --blue-ink: #4b6472;
      --mustard: #c2a94f;
      --white: #f0ead8;

      --font-display: 'Saira Stencil One', 'Arial Narrow', Impact, sans-serif;
      --font-label: 'Special Elite', 'Courier New', monospace;
      --font-ui: 'Archivo', 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'Courier Prime', 'Courier New', monospace;

      color-scheme: dark;
    }"""

new_root = """:root {
      /* Paleta Halloween Spookython 2026 */
      --void: #07050b;
      --void-2: #0e0916;
      --void-3: #150d21;
      --steel: #241438;
      --steel-2: #3a1f59;
      --paper: #130a1e;
      --paper-2: #1c102b;
      --paper-3: #27163c;
      --paper-4: #331d4e;
      --paper-edge: #572d82;
      --paper-shadow: #050209;
      --ink: #f5f0fb;
      --ink-2: #d4c8e6;
      --ink-3: #a797be;
      
      /* Acentos temáticos */
      --pumpkin: #ff7518;
      --pumpkin-glow: rgba(255, 117, 24, 0.4);
      --toxic-green: #39ff14;
      --toxic-glow: rgba(57, 255, 20, 0.35);
      --witch-purple: #a855f7;
      --purple-glow: rgba(168, 85, 247, 0.35);
      --blood: #ff1e42;
      --blood-glow: rgba(255, 30, 66, 0.45);
      --blood-deep: #99001f;

      --olive: #ff7518;       /* Calabaza */
      --olive-2: #ffa347;
      --olive-dark: #b84900;
      --rust: #ff1e42;        /* Sangre */
      --rust-2: #ff5271;
      --rust-deep: #b30022;
      --amber: #ff7518;       /* Naranja Halloween */
      --amber-2: #fbbf24;     /* Oro bruja */
      --sage: #39ff14;        /* Verde tóxico */
      --sage-2: #10b981;      /* Slime esmeralda */
      --blue-ink: #a855f7;    /* Púrpura hechizo */
      --mustard: #ffa012;
      --white: #ffffff;

      --font-spooky: 'Creepster', cursive, sans-serif;
      --font-display: 'Chakra Petch', 'Saira Stencil One', sans-serif;
      --font-label: 'Special Elite', 'Courier New', monospace;
      --font-ui: 'Archivo', 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'Courier Prime', 'Courier New', monospace;

      color-scheme: dark;
    }"""

html = html.replace(old_root, new_root)

# 3. Add canvas and spiderweb styles in CSS
extra_css = """
    /* Canvas de partículas de Halloween */
    #spooky-canvas {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 1;
      opacity: 0.65;
    }
    .spiderweb-corner {
      position: fixed;
      width: 130px; height: 130px;
      pointer-events: none;
      z-index: 40;
      opacity: 0.32;
    }
    .web-tl { top: 0; left: 0; }
    .web-tr { top: 0; right: 0; transform: scaleX(-1); }

    .brand-text h1 {
      font-family: var(--font-spooky) !important;
      letter-spacing: 2px !important;
      font-size: clamp(1.2rem, 2.2vw, 1.7rem) !important;
      text-shadow: 0 0 10px var(--pumpkin), 0 0 20px rgba(255, 117, 24, 0.4);
    }
    .biohazard-badge {
      background: radial-gradient(circle, rgba(255, 117, 24, 0.25) 0%, rgba(20, 10, 30, 0.8) 100%) !important;
      border: 1.5px solid var(--pumpkin) !important;
      color: var(--pumpkin) !important;
      box-shadow: 0 0 16px var(--pumpkin-glow) !important;
      font-size: 1.8rem;
    }
    .btn-sound {
      background: rgba(255, 117, 24, 0.12);
      border: 1px solid rgba(255, 117, 24, 0.4);
      color: #ffa347;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      padding: 0.28rem 0.65rem;
      border-radius: 999px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.2s ease;
    }
    .btn-sound:hover {
      background: rgba(255, 117, 24, 0.28);
      box-shadow: 0 0 12px var(--pumpkin-glow);
      transform: scale(1.04);
    }
    .btn-primary {
      background: linear-gradient(135deg, #ff7518, #dc2626) !important;
      border: 1px solid #ffa347 !important;
      color: #fff !important;
      box-shadow: 0 4px 18px var(--pumpkin-glow) !important;
      text-shadow: 0 1px 2px rgba(0,0,0,0.5);
    }
    .btn-primary:hover:not(:disabled) {
      filter: brightness(1.15) !important;
      box-shadow: 0 6px 24px rgba(255, 117, 24, 0.55) !important;
      transform: translateY(-2px);
    }
    .surprise-box {
      border: 1px solid rgba(255, 117, 24, 0.35) !important;
      background: linear-gradient(135deg, rgba(255, 117, 24, 0.08), rgba(168, 85, 247, 0.05)) !important;
    }
    .btn-surprise:hover {
      border-color: var(--pumpkin) !important;
      box-shadow: 0 0 12px var(--pumpkin-glow) !important;
    }
    input[type="range"]::-webkit-slider-thumb {
      background: var(--pumpkin) !important;
      box-shadow: 0 0 10px var(--pumpkin-glow) !important;
      border: 2px solid #fff !important;
    }
    input[type="range"]::-webkit-slider-thumb:hover {
      background: var(--toxic-green) !important;
      box-shadow: 0 0 14px var(--toxic-glow) !important;
    }
"""

html = html.replace("</style>", extra_css + "\n  </style>")

# 4. Insert Canvas and Spiderwebs in body
body_start = "<body>"
spiderwebs_html = """<body>
  <!-- CANVAS ANIMADO DE HALLOWEEN -->
  <canvas id="spooky-canvas"></canvas>

  <!-- TELARAÑAS EN LAS ESQUINAS -->
  <svg class="spiderweb-corner web-tl" viewBox="0 0 100 100" fill="none" stroke="rgba(255,117,24,0.3)" stroke-width="1.2">
    <path d="M0,0 L100,0 M0,0 L0,100 M0,0 L85,85 M0,0 L50,95 M0,0 L95,50" />
    <path d="M20,0 Q20,20 0,20" /><path d="M40,0 Q40,40 0,40" /><path d="M60,0 Q60,60 0,60" /><path d="M80,0 Q80,80 0,80" /><path d="M100,0 Q100,100 0,100" />
  </svg>
  <svg class="spiderweb-corner web-tr" viewBox="0 0 100 100" fill="none" stroke="rgba(168,85,247,0.3)" stroke-width="1.2">
    <path d="M0,0 L100,0 M0,0 L0,100 M0,0 L85,85 M0,0 L50,95 M0,0 L95,50" />
    <path d="M20,0 Q20,20 0,20" /><path d="M40,0 Q40,40 0,40" /><path d="M60,0 Q60,60 0,60" /><path d="M80,0 Q80,80 0,80" /><path d="M100,0 Q100,100 0,100" />
  </svg>"""

html = html.replace(body_start, spiderwebs_html, 1)

# 5. Header adjustments
old_header_text = '<h1>MANTA · COMITÉ DE CONTENCIÓN CORDYCEPS</h1>'
new_header_text = '<h1>SPOOKYTHON 2026 · BROTE CORDYCEPS MANTA</h1>'
html = html.replace(old_header_text, new_header_text)

old_badge = '<div class="biohazard-badge" aria-hidden="true"><svg class="icon"><use href="#i-bio"></use></svg></div>'
new_badge = '<div class="biohazard-badge" id="header-pumpkin" title="Noche de Halloween - Spookython 2026">🎃</div>'
html = html.replace(old_badge, new_badge)

# Add Sound FX toggle in status tags
sound_btn = """<button type="button" class="btn-sound" id="btn-sound-toggle" onclick="toggleAudioFX()">
          <span id="sound-icon">🔈</span> <span id="sound-text">Audio FX</span>
        </button>
        <span class="pill" style="border-color:rgba(255,117,24,0.4);background:rgba(255,117,24,0.12);color:#ffa347;">🎃 31 OCTUBRE</span>"""

html = html.replace('<div class="status-tags">', '<div class="status-tags">\n        ' + sound_btn)

# 6. Brote Sorpresa Buttons text
html = html.replace("⚡ Brote Sorpresa (Prueba del Jurado)", "⚡ Maldiciones del Jurado (Brote Sorpresa)")
html = html.replace("<strong>Doble Contagio</strong>", "<strong>🍄 Niebla de Esporas</strong>")
html = html.replace("<strong>Mitad de Dosis</strong>", "<strong>🪦 Saqueo de Dosis</strong>")
html = html.replace("<strong>Brote en Mercado</strong>", "<strong>🏬 Pánico en Tarqui</strong>")
html = html.replace("<strong>Mutación Fúngica</strong>", "<strong>🧪 Mutación Fúngica</strong>")
html = html.replace("Simular Contención Cordyceps", "🎃 CONJURAR SIMULACIÓN DE CONTENCIÓN")

# 7. Update riskPalette for 3D map
old_pal = """function riskPalette(riesgo) {
      if (riesgo === 'Crítico') return { top: '#7e2f24', side: '#4a1a13', edge: '#b24a37' };
      if (riesgo === 'Alerta') return { top: '#8a5a1e', side: '#553811', edge: '#d2a052' };
      return { top: '#4f5c3d', side: '#2f3825', edge: '#8b936c' };
    }"""

new_pal = """function riskPalette(riesgo) {
      // Paleta Halloween neón para bloques 3D
      if (riesgo === 'Crítico') return { top: '#e11d48', side: '#881337', edge: '#ff4d6d' };
      if (riesgo === 'Alerta') return { top: '#ea580c', side: '#7c2d12', edge: '#ff7518' };
      return { top: '#15803d', side: '#14532d', edge: '#39ff14' };
    }"""

html = html.replace(old_pal, new_pal)

# 8. Update chart curves in JS
old_chart_curves = """        <!-- Curves -->
        <path d="${pathNone}" fill="none" stroke="#9b3b2c" stroke-width="2.5" />
        <path d="${pathRand}" fill="none" stroke="#b8843b" stroke-width="2" stroke-dasharray="4,3" />
        <path d="${pathStrat}" fill="none" stroke="#4f6b52" stroke-width="3" />"""

new_chart_curves = """        <!-- Curves con estética neón Halloween -->
        <path d="${pathNone}" fill="none" stroke="#ff1e42" stroke-width="2.5" />
        <path d="${pathRand}" fill="none" stroke="#ff7518" stroke-width="2" stroke-dasharray="4,3" />
        <path d="${pathStrat}" fill="none" stroke="#39ff14" stroke-width="3" style="filter: drop-shadow(0 0 6px rgba(57,255,20,0.6));" />"""

html = html.replace(old_chart_curves, new_chart_curves)

old_seir_curves = """        <path d="${pS}" fill="none" stroke="#4f6b52" stroke-width="2.5" />
        <path d="${pE}" fill="none" stroke="#b8843b" stroke-width="2.5" />
        <path d="${pI}" fill="none" stroke="#9b3b2c" stroke-width="2.5" />
        <path d="${pR}" fill="none" stroke="#4b6472" stroke-width="2.5" />"""

new_seir_curves = """        <path d="${pS}" fill="none" stroke="#39ff14" stroke-width="2.5" />
        <path d="${pE}" fill="none" stroke="#ff7518" stroke-width="2.5" />
        <path d="${pI}" fill="none" stroke="#ff1e42" stroke-width="2.5" />
        <path d="${pR}" fill="none" stroke="#a855f7" stroke-width="2.5" />"""

html = html.replace(old_seir_curves, new_seir_curves)

# 9. Add Spooky audio and canvas scripts
spooky_scripts = """
    // --- SINTETIZADOR DE AUDIO HALLOWEEN (WEB AUDIO API NATIVO) ---
    let audioFXEnabled = false;
    let audioCtx = null;

    function initAudio() {
      if (!audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        audioCtx = new AudioContext();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }
    }

    function toggleAudioFX() {
      audioFXEnabled = !audioFXEnabled;
      const icon = document.getElementById('sound-icon');
      const text = document.getElementById('sound-text');
      if (audioFXEnabled) {
        initAudio();
        icon.textContent = '🔊';
        text.textContent = 'Audio FX: Activado';
        playSpookySound('howl');
        showToast('🎃 Audio de Noche de Brujas Activado');
      } else {
        icon.textContent = '🔈';
        text.textContent = 'Audio FX: Desactivado';
        showToast('🔇 Audio silenciado');
      }
    }

    function playSpookySound(type) {
      if (!audioFXEnabled || !audioCtx) return;
      try {
        const t = audioCtx.currentTime;
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain);
        gain.connect(audioCtx.destination);

        if (type === 'conjure') {
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(440, t);
          osc.frequency.exponentialRampToValueAtTime(110, t + 0.5);
          gain.gain.setValueAtTime(0.12, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.5);
          osc.start(t);
          osc.stop(t + 0.5);
        } else if (type === 'curse') {
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(180, t);
          osc.frequency.linearRampToValueAtTime(45, t + 0.35);
          gain.gain.setValueAtTime(0.18, t);
          gain.gain.linearRampToValueAtTime(0.001, t + 0.4);
          osc.start(t);
          osc.stop(t + 0.4);
        } else if (type === 'howl') {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(260, t);
          osc.frequency.exponentialRampToValueAtTime(520, t + 0.3);
          osc.frequency.exponentialRampToValueAtTime(220, t + 0.7);
          gain.gain.setValueAtTime(0.08, t);
          gain.gain.linearRampToValueAtTime(0.001, t + 0.7);
          osc.start(t);
          osc.stop(t + 0.7);
        } else if (type === 'success') {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(587.33, t);
          osc.frequency.setValueAtTime(880, t + 0.1);
          gain.gain.setValueAtTime(0.1, t);
          gain.gain.exponentialRampToValueAtTime(0.001, t + 0.6);
          osc.start(t);
          osc.stop(t + 0.6);
        }
      } catch (e) {
        console.warn('Audio error:', e);
      }
    }

    // --- CANVAS ANIMADO (ESPORAS Y MURCIÉLAGOS) ---
    function initSpookyCanvas() {
      const canvas = document.getElementById('spooky-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let w, h;

      function resize() {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      }
      window.addEventListener('resize', resize);
      resize();

      const particles = [];
      for (let i = 0; i < 40; i++) {
        particles.push({
          x: Math.random() * w,
          y: Math.random() * h,
          r: Math.random() * 2.2 + 1,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -Math.random() * 0.5 - 0.2,
          color: Math.random() > 0.5 ? 'rgba(255, 117, 24, ' : 'rgba(57, 255, 20, ',
          alpha: Math.random() * 0.5 + 0.2
        });
      }

      const bats = [];
      for (let i = 0; i < 5; i++) {
        bats.push({
          x: Math.random() * w,
          y: Math.random() * (h * 0.5),
          size: Math.random() * 7 + 7,
          speed: Math.random() * 1.4 + 0.7,
          angle: 0,
          wingSpeed: Math.random() * 0.15 + 0.15
        });
      }

      function drawBat(b) {
        ctx.save();
        ctx.translate(b.x, b.y);
        ctx.fillStyle = 'rgba(25, 12, 38, 0.65)';
        ctx.beginPath();
        const wing = Math.sin(b.angle) * (b.size * 0.5);
        ctx.moveTo(0, 0);
        ctx.quadraticCurveTo(-b.size, -wing, -b.size * 1.5, 0);
        ctx.quadraticCurveTo(-b.size * 0.5, b.size * 0.3, 0, b.size * 0.5);
        ctx.quadraticCurveTo(b.size * 0.5, b.size * 0.3, b.size * 1.5, 0);
        ctx.quadraticCurveTo(b.size, -wing, 0, 0);
        ctx.fill();
        ctx.restore();
      }

      function animate() {
        ctx.clearRect(0, 0, w, h);
        particles.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          if (p.y < 0) { p.y = h; p.x = Math.random() * w; }
          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;

          ctx.beginPath();
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fillStyle = p.color + p.alpha + ')';
          ctx.shadowBlur = 6;
          ctx.shadowColor = p.color + '0.7)';
          ctx.fill();
          ctx.shadowBlur = 0;
        });

        bats.forEach(b => {
          b.x -= b.speed;
          b.y += Math.sin(b.angle * 0.5) * 0.4;
          b.angle += b.wingSpeed;
          if (b.x < -30) {
            b.x = w + 30;
            b.y = Math.random() * (h * 0.5);
          }
          drawBat(b);
        });

        requestAnimationFrame(animate);
      }
      animate();
    }
"""

html = html.replace("window.addEventListener('DOMContentLoaded', () => {", spooky_scripts + "\n    window.addEventListener('DOMContentLoaded', () => {\n      initSpookyCanvas();")

# Add sound triggers
html = html.replace("loading = true;", "playSpookySound('conjure');\n      loading = true;")
html = html.replace("showToast('✔ Simulación completada con éxito');", "playSpookySound('success');\n        showToast('🎃 ¡Simulación completada con éxito!');")
html = html.replace("function applySurprise(kind) {", "function applySurprise(kind) {\n      playSpookySound('curse');")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Halloween transformation applied successfully!")
