import { useEffect, useRef } from "react";

// Visual noise only. This generator is not the simulation seed: it never
// reads FormState and never enters POST /api/simulate or the SHA-256 fingerprint.
function makeVisualRng(seed: number) {
  let state = seed >>> 0;
  return () => {
    state = (Math.imul(1664525, state) + 1013904223) >>> 0;
    return state / 4294967296;
  };
}

type Particle = {
  x: number;
  y: number;
  r: number;
  vx: number;
  vy: number;
  color: string;
  alpha: number;
};

type Bat = {
  x: number;
  y: number;
  size: number;
  speed: number;
  angle: number;
  wingSpeed: number;
};

export function SpookyCanvas() {
  const ref = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = ref.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const rand = makeVisualRng(0x5a110ee1);
    let w = 0;
    let h = 0;

    function resize() {
      w = canvas!.width = window.innerWidth;
      h = canvas!.height = window.innerHeight;
    }
    resize();
    window.addEventListener("resize", resize);

    const particles: Particle[] = [];
    for (let i = 0; i < 40; i++) {
      particles.push({
        x: rand() * w,
        y: rand() * h,
        r: rand() * 2.2 + 1,
        vx: (rand() - 0.5) * 0.4,
        vy: -rand() * 0.5 - 0.2,
        color: rand() > 0.5 ? "rgba(255, 117, 24, " : "rgba(57, 255, 20, ",
        alpha: rand() * 0.5 + 0.2,
      });
    }

    const bats: Bat[] = [];
    for (let i = 0; i < 5; i++) {
      bats.push({
        x: rand() * w,
        y: rand() * (h * 0.5),
        size: rand() * 7 + 7,
        speed: rand() * 1.4 + 0.7,
        angle: 0,
        wingSpeed: rand() * 0.15 + 0.15,
      });
    }

    function drawBat(b: Bat) {
      ctx!.save();
      ctx!.translate(b.x, b.y);
      ctx!.strokeStyle = "rgba(216, 180, 255, 0.95)";
      ctx!.lineWidth = 1.2;
      ctx!.fillStyle = "rgba(74, 32, 112, 0.95)";
      ctx!.beginPath();
      const wing = Math.sin(b.angle) * (b.size * 0.5);
      ctx!.moveTo(0, 0);
      ctx!.quadraticCurveTo(-b.size, -wing, -b.size * 1.5, 0);
      ctx!.quadraticCurveTo(-b.size * 0.5, b.size * 0.3, 0, b.size * 0.5);
      ctx!.quadraticCurveTo(b.size * 0.5, b.size * 0.3, b.size * 1.5, 0);
      ctx!.quadraticCurveTo(b.size, -wing, 0, 0);
      ctx!.fill();
      ctx!.stroke();
      ctx!.restore();
    }

    const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let frame = 0;

    function animate() {
      ctx!.clearRect(0, 0, w, h);
      particles.forEach((p) => {
        if (!reduced) {
          p.x += p.vx;
          p.y += p.vy;
          if (p.y < 0) {
            p.y = h;
            p.x = rand() * w;
          }
          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;
        }
        ctx!.beginPath();
        ctx!.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx!.fillStyle = p.color + p.alpha + ")";
        ctx!.shadowBlur = 6;
        ctx!.shadowColor = p.color + "0.7)";
        ctx!.fill();
        ctx!.shadowBlur = 0;
      });

      bats.forEach((b) => {
        if (!reduced) {
          b.x -= b.speed;
          b.y += Math.sin(b.angle * 0.5) * 0.4;
          b.angle += b.wingSpeed;
          if (b.x < -30) {
            b.x = w + 30;
            b.y = rand() * (h * 0.5);
          }
        }
        drawBat(b);
      });
      if (!reduced) frame = requestAnimationFrame(animate);
    }
    animate();

    return () => {
      cancelAnimationFrame(frame);
      window.removeEventListener("resize", resize);
    };
  }, []);

  return <canvas ref={ref} id="spooky-canvas" className="spooky-canvas" aria-hidden="true" />;
}

export function Cobwebs() {
  return (
    <>
      <svg
        className="spiderweb-corner web-tl"
        viewBox="0 0 100 100"
        fill="none"
        stroke="rgba(255,117,24,0.9)"
        strokeWidth="1.2"
        aria-hidden="true"
      >
        <path d="M0,0 L100,0 M0,0 L0,100 M0,0 L85,85 M0,0 L50,95 M0,0 L95,50" />
        <path d="M20,0 Q20,20 0,20" />
        <path d="M40,0 Q40,40 0,40" />
        <path d="M60,0 Q60,60 0,60" />
        <path d="M80,0 Q80,80 0,80" />
        <path d="M100,0 Q100,100 0,100" />
      </svg>
      <svg
        className="spiderweb-corner web-tr"
        viewBox="0 0 100 100"
        fill="none"
        stroke="rgba(168,85,247,0.85)"
        strokeWidth="1.2"
        aria-hidden="true"
      >
        <path d="M0,0 L100,0 M0,0 L0,100 M0,0 L85,85 M0,0 L50,95 M0,0 L95,50" />
        <path d="M20,0 Q20,20 0,20" />
        <path d="M40,0 Q40,40 0,40" />
        <path d="M60,0 Q60,60 0,60" />
        <path d="M80,0 Q80,80 0,80" />
        <path d="M100,0 Q100,100 0,100" />
      </svg>
    </>
  );
}
