# Rezept: Shader für Körnung, Verlauf und Verzerrung

Hintergrundflächen aus WebGL und GLSL, ab `technik: webgl` (ER07). Regeln: TE10 (im Bild laufen, aufräumen, Telefonfassung, Standbild), S17, S18, BE11. Lizenzen laut Quelle geprüft, Versionen ungeprüft.

## Vor dem Einbau

Passt es ins Budget der Stufe (`regler.md`), gibt es ein Standbild und eine Telefonfassung (TE10)? Das Standbild liegt als CSS-Hintergrund hinter dem Canvas. Es greift ohne WebGL und bei reduzierter Bewegung.

## 1. Körnung von Hand (ohne Abhängigkeit)

Ein Dreieck über die ganze Fläche, Rauschen aus einer Hash-Funktion im Fragment-Shader. Kein Paket, keine Lizenz nötig. Skript als eigene Datei, Stil im CSS, kein Inline-Skript und kein `style=` (S10, TE06). Die Körnung liegt in der Bühne, nicht fixiert über der Seite (S39), und hat einen Pause-Knopf (S18).

```html
<section class="stage">
  <canvas id="grain" aria-hidden="true"></canvas>
  …
  <button class="grain-pause" aria-pressed="false" aria-label="Körnung anhalten">…</button>
</section>
<script type="module" src="/js/grain.js"></script>
```

```css
.stage { position: relative; }
#grain { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
```

```js
// /js/grain.js
const canvas = document.getElementById('grain');
const pauseButton = document.querySelector('button.grain-pause');
const gl = canvas.getContext('webgl');
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
// TE10: at most 1.5, phones 1
const dpr = matchMedia('(pointer: coarse)').matches ? 1 : Math.min(devicePixelRatio, 1.5);

const vertSrc = `
attribute vec2 aPosition;
void main() {
  gl_Position = vec4(aPosition, 0.0, 1.0);
}`;

const fragSrc = `
precision highp float;
uniform vec2 uResolution;
uniform float uTime;
uniform float uIntensity; // 0.0-0.2 is a usable range

float random(vec2 st) {
  return fract(sin(dot(st.xy, vec2(12.9898, 78.233))) * 43758.5453123);
}

void main() {
  vec2 uv = gl_FragCoord.xy / uResolution.xy;
  // re-seed the hash every frame so grain flickers instead of scrolling
  float grain = random(uv * uResolution.xy + floor(uTime * 24.0));
  vec3 base = vec3(0.055, 0.055, 0.075); // background token in linear sRGB
  vec3 color = base + (grain - 0.5) * uIntensity;
  gl_FragColor = vec4(color, 1.0);
}`;

function compile(type, src) {
  const s = gl.createShader(type);
  gl.shaderSource(s, src);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s));
  return s;
}

if (gl) {
  const program = gl.createProgram();
  gl.attachShader(program, compile(gl.VERTEX_SHADER, vertSrc));
  gl.attachShader(program, compile(gl.FRAGMENT_SHADER, fragSrc));
  gl.linkProgram(program);
  gl.useProgram(program);

  // fullscreen triangle, no index buffer needed
  const buf = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, buf);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);
  const aPosition = gl.getAttribLocation(program, 'aPosition');
  gl.enableVertexAttribArray(aPosition);
  gl.vertexAttribPointer(aPosition, 2, gl.FLOAT, false, 0, 0);

  const uResolution = gl.getUniformLocation(program, 'uResolution');
  const uTime = gl.getUniformLocation(program, 'uTime');
  const uIntensity = gl.getUniformLocation(program, 'uIntensity');

  let raf = 0;
  let visible = false;
  let paused = reduceMotion; // reduced motion: one still frame
  pauseButton?.setAttribute('aria-pressed', String(paused));

  function frame(t) {
    gl.uniform2f(uResolution, canvas.width, canvas.height);
    gl.uniform1f(uTime, t * 0.001);
    gl.uniform1f(uIntensity, 0.06);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    if (visible && !paused) raf = requestAnimationFrame(frame);
  }
  function restart() {
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(frame); // draws at least one still frame
  }

  // size from the stage, not the window; resizing clears the canvas
  new ResizeObserver(() => {
    canvas.width = canvas.clientWidth * dpr;
    canvas.height = canvas.clientHeight * dpr;
    gl.viewport(0, 0, canvas.width, canvas.height);
    restart();
  }).observe(canvas);

  // TE10: run only while in view
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; restart(); }).observe(canvas);

  // S18: pause button
  pauseButton?.addEventListener('click', () => {
    paused = !paused;
    pauseButton.setAttribute('aria-pressed', String(paused));
    restart();
  });
}
```

Stellschrauben: `base` ist der Hintergrund-Token in linearem sRGB, nicht der OKLCH-Text. `uIntensity` 0,02 bis 0,04 ergibt feines Filmkorn, ab 0,12 grobes Rauschen. Hinter das Canvas eine ruhige Fläche oder einen Verlauf legen, kein unruhiges Bild.

## 2. paper-shaders (`@paper-design/shaders-react`)

Über 30 fertige GPU-Shader ohne Abhängigkeit als React-Bausteine: Verläufe, Punktraster, Rauschen, Halbton, Polarlicht. Lizenz Apache 2.0 (LICENSE im Repo `paper-design/shaders`). Version laut Quelle 0.0.8x, ungeprüft.

```bash
npm install @paper-design/shaders-react
# vanilla JS/no React: npm install @paper-design/shaders
```

```jsx
import { MeshGradient } from '@paper-design/shaders-react';
import { SceneFrame } from './SceneFrame'; // rezepte/3d.md: in view only, still image, pause button

export default function Hero() {
  return (
    <SceneFrame still="/hero-still.webp">
      {() => (
        <MeshGradient
          colors={['#5100ff', '#00ff80', '#ffcc00', '#ea00ff']} // replace with 3-4 stops from the project palette
          speed={0.1}
          style={{ width: '100%', height: '100%' }}
          // also: distortion, swirl
        />
      )}
    </SceneFrame>
  );
}
```

Stellschrauben: drei bis vier Farben aus der Projektskala; `speed` 0,05 bis 0,15 statt der Vorgabe. Auch als Streifen oder Kartenecke statt vollflächig. Ob `MeshGradient` die Pixeldichte deckeln lässt, ist ungeprüft; vor der Auslieferung nach TE10 messen. `SceneFrame` (`rezepte/3d.md`) baut ihn außerhalb des Bildes ab, zeigt bei reduzierter Bewegung und nach dem Pause-Knopf das Standbild (TE10, S17, S18). In Astro als Insel mit `client:visible`.

## 3. ShaderGradient (`@shadergradient/react`)

Hülle um React Three Fiber mit Szenen `plane`, `sphere`, `waterPlane` und Kamerasteuerung. Lizenz MIT (npm und Repo `ruucm/shadergradient`). Zieht Three.js und R3F mit; nur sinnvoll, wenn die Seite das schon trägt (BE11), sonst Abschnitt 1 oder 2.

```bash
npm i @shadergradient/react @react-three/fiber three three-stdlib camera-controls
npm i -D @types/three
```

```jsx
import { ShaderGradientCanvas, ShaderGradient } from '@shadergradient/react';
import { SceneFrame } from './SceneFrame'; // rezepte/3d.md: in view only, still image, pause button

export default function Hero() {
  return (
    <SceneFrame still="/hero-still.webp">
      {() => (
        <ShaderGradientCanvas style={{ position: 'absolute', inset: 0 }}>
          <ShaderGradient type="sphere" color1="#52ff89" color2="#dbba95" color3="#d0bce1" uSpeed={0.4} />
        </ShaderGradientCanvas>
      )}
    </SceneFrame>
  );
}
```

Stellschrauben: `type` und Kamera (`cAzimuthAngle`, `cPolarAngle`, `cDistance`). Ob `ShaderGradientCanvas` die Pixeldichte deckeln lässt, ist ungeprüft; Pixeldichte nach TE10 prüfen, bevor es ausgeliefert wird. Eigenes R3F: `rezepte/3d.md`.

## 4. Three.js `ShaderMaterial` (Verzerrung)

Eigener Vertex- und Fragment-Shader auf einem Mesh, wenn fertige Bausteine den Effekt nicht haben: Welle unter dem Zeiger über einem Bild, verschobene Fläche. Lizenz MIT (`mrdoob/three.js`).

```bash
npm install three
```

```js
import * as THREE from 'three';

const host = document.querySelector('.distortion');
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const dpr = matchMedia('(pointer: coarse)').matches ? 1 : Math.min(devicePixelRatio, 1.5);

const scene = new THREE.Scene();
const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(dpr);
renderer.setSize(host.clientWidth, host.clientHeight);
host.appendChild(renderer.domElement);

const uniforms = {
  uTime: { value: 0 },
  uMouse: { value: new THREE.Vector2(0.5, 0.5) },
};

const material = new THREE.ShaderMaterial({
  uniforms,
  vertexShader: /* glsl */ `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = vec4(position, 1.0);
    }
  `,
  fragmentShader: /* glsl */ `
    precision highp float;
    varying vec2 vUv;
    uniform float uTime;
    uniform vec2 uMouse;

    void main() {
      vec2 uv = vUv;
      // ripple distortion centered on pointer position
      float dist = distance(uv, uMouse);
      float ripple = sin(dist * 40.0 - uTime * 3.0) * 0.02 * smoothstep(0.4, 0.0, dist);
      uv += ripple;
      vec3 color = vec3(uv, 0.5 + 0.5 * sin(uTime * 0.5));
      gl_FragColor = vec4(color, 1.0);
    }
  `,
});

const quad = new THREE.Mesh(new THREE.PlaneGeometry(2, 2), material);
scene.add(quad);

if (matchMedia('(hover: hover)').matches) {
  host.addEventListener('pointermove', (e) => {
    const r = host.getBoundingClientRect();
    uniforms.uMouse.value.set((e.clientX - r.left) / r.width, 1 - (e.clientY - r.top) / r.height);
  });
}

const pauseButton = host.querySelector('button.pause'); // S18: runs longer than 5 s
let raf = 0;
let visible = false;
let paused = reduceMotion; // reduced motion: one still frame
pauseButton?.setAttribute('aria-pressed', String(paused));

function animate(t) {
  uniforms.uTime.value = t * 0.001;
  renderer.render(scene, camera);
  if (visible && !paused) raf = requestAnimationFrame(animate);
}
function restart() {
  cancelAnimationFrame(raf);
  raf = requestAnimationFrame(animate); // draws at least one still frame
}

// TE10: run only while in view
const io = new IntersectionObserver(([e]) => { visible = e.isIntersecting; restart(); });
io.observe(host);
pauseButton?.addEventListener('click', () => {
  paused = !paused;
  pauseButton.setAttribute('aria-pressed', String(paused));
  restart();
});

export function destroy() {
  io.disconnect();
  cancelAnimationFrame(raf);
  quad.geometry.dispose();
  material.dispose();
  renderer.dispose();
  renderer.domElement.remove();
}
```

Die Entscheidung steckt in der Verzerrung (Welle, Domain-Warp, Farbversatz). `uMouse` und `uTime` lassen sich auch aus Scrollstand oder Zeigertempo speisen statt aus der Uhr. Hover nur unter `(hover: hover)` (TE13).

## 5. Verlaufsnetz durch Verschiebung der Eckpunkte

Der „Stripe-Verlauf“: eine fein unterteilte Fläche, Eckpunkte per Rauschen verschoben, Farben zwischen den Rauschbändern gemischt, Kamera gerade von vorn. Fertig verpackt ist das `MeshGradient` aus Abschnitt 2; von Hand nur, wenn mehr Steuerung nötig ist, etwa Verschiebung aus echten Daten. Bekannte Vorlage `jordienr/whatamesh` hat keine LICENSE: nur Technik lesen, nichts kopieren oder installieren.

```glsl
// vertex shader — displaces a subdivided plane using simplex/value noise
uniform float uTime;
varying vec3 vColor;

// value-noise placeholder: swap in a real simplex noise (e.g. Ashima's
// webgl-noise, MIT-licensed: https://github.com/ashima/webgl-noise)
float noise(vec2 p) {
  return fract(sin(dot(p, vec2(41.0, 289.0))) * 45758.5453);
}

void main() {
  vec3 pos = position;
  float n = noise(pos.xy * 0.6 + uTime * 0.05);
  pos.z += n * 0.6; // displacement strength
  vColor = mix(vec3(0.10, 0.05, 0.30), vec3(0.85, 0.65, 0.95), n);
  gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
}
```

Der Fragment-Shader gibt nur `vColor` aus: `gl_FragColor = vec4(vColor, 1.0);`. Dazu `THREE.PlaneGeometry(4, 4, 64, 64)` (viele Segmente, sonst bewegt sich nichts) und ein `ShaderMaterial` mit beiden Shadern; Gerüst mit Pixeldichte, Beobachter, Pause-Knopf und `destroy()` wie in Abschnitt 4. Für weichere Formen echtes Simplex-Rauschen (Ashima webgl-noise, MIT), drei bis vier Farben aus der Projektskala, Frequenz der Verschiebung variieren.

## Quellen

- Shadertoy, https://www.shadertoy.com: größte Sammlung von Fragment-Shadern. Standardlizenz CC BY-NC-SA 3.0 (keine kommerzielle Nutzung), außer der Autor nennt eine andere. Nur Technik nachbauen, nicht einfügen.
- Paper Shaders, https://shaders.paper.design/: Editor für `@paper-design/shaders`, Einstellungen ausprobieren und exportieren. Apache 2.0.
- ShaderGradient, https://www.shadergradient.co/: Export nach Figma, Framer, React. Bedingungen des Editors vorher prüfen; das npm-Paket ist MIT.
- Three.js Beispiele, https://threejs.org/examples/: Filter `webgl_shader*` und `webgl_gpgpu*`. MIT.
- OGL Beispiele, https://oframe.github.io/ogl/examples/: WebGL-Bibliothek um 8 KB ohne Abhängigkeit (Unlicense), leichter als Three.js, wenn nur eine Shaderfläche gebraucht wird.
- Ashima webgl-noise, https://github.com/ashima/webgl-noise: Simplex-Rauschen, MIT.
