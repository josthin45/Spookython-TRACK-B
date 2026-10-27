// Oscillator FX only. Stays muted until the listener opts in.
// currentTime schedules tones; it is never copied into the seed or the POST body.

export type SpookySound = "conjure" | "curse" | "howl" | "success";

let audioFXEnabled = false;
let audioCtx: AudioContext | null = null;

type AudioContextCtor = typeof AudioContext;

function audioContextCtor(): AudioContextCtor | null {
  if (typeof window.AudioContext === "function") return window.AudioContext;
  const legacy = (window as Window & { webkitAudioContext?: AudioContextCtor }).webkitAudioContext;
  return typeof legacy === "function" ? legacy : null;
}

function initAudio() {
  if (!audioCtx) {
    const Ctor = audioContextCtor();
    if (!Ctor) return;
    audioCtx = new Ctor();
  }
  if (audioCtx.state === "suspended") {
    void audioCtx.resume();
  }
}

export function toggleAudioFX() {
  audioFXEnabled = !audioFXEnabled;
  if (audioFXEnabled) {
    initAudio();
    playSpookySound("howl");
  }
  return audioFXEnabled;
}

export function playSpookySound(type: SpookySound) {
  if (!audioFXEnabled || !audioCtx) return;
  try {
    const t = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.connect(gain);
    gain.connect(audioCtx.destination);

    if (type === "conjure") {
      osc.type = "sawtooth";
      osc.frequency.setValueAtTime(440, t);
      osc.frequency.exponentialRampToValueAtTime(110, t + 0.5);
      gain.gain.setValueAtTime(0.12, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.5);
      osc.start(t);
      osc.stop(t + 0.5);
    } else if (type === "curse") {
      osc.type = "triangle";
      osc.frequency.setValueAtTime(180, t);
      osc.frequency.linearRampToValueAtTime(45, t + 0.35);
      gain.gain.setValueAtTime(0.18, t);
      gain.gain.linearRampToValueAtTime(0.001, t + 0.4);
      osc.start(t);
      osc.stop(t + 0.4);
    } else if (type === "howl") {
      osc.type = "sine";
      osc.frequency.setValueAtTime(260, t);
      osc.frequency.exponentialRampToValueAtTime(520, t + 0.3);
      osc.frequency.exponentialRampToValueAtTime(220, t + 0.7);
      gain.gain.setValueAtTime(0.08, t);
      gain.gain.linearRampToValueAtTime(0.001, t + 0.7);
      osc.start(t);
      osc.stop(t + 0.7);
    } else {
      osc.type = "sine";
      osc.frequency.setValueAtTime(587.33, t);
      osc.frequency.setValueAtTime(880, t + 0.1);
      gain.gain.setValueAtTime(0.1, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.6);
      osc.start(t);
      osc.stop(t + 0.6);
    }
  } catch (err) {
    console.warn("Audio error:", err);
  }
}
