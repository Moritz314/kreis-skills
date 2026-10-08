# Shaders: noise, grain, gradients, distortion

WebGL/GLSL techniques for decorative background layers — animated grain, mesh
gradients, liquid distortion, noise fields. Use for hero sections, section
dividers, empty states, and ambient product-UI backgrounds where a brand wants
to read as technically confident.

**When NOT to use this:** content-heavy pages (docs, dashboards with dense
tables, long-form reading) where a moving background competes with
comprehension; low-power/mobile-first audiences — a full-screen WebGL canvas
easily costs 10-20% battery drain per hour and will visibly heat a phone;
anywhere impeccable's brand-vs-product split says "product" — utilitarian
screens (settings, forms, data tools) should stay static so the shader doesn't
read as decoration fighting the task. Also skip it, or strip it down hard, when
`prefers-reduced-motion` is set — always provide a static fallback (see budget
notes in SKILL.md).

The single most templated look in this space is a slowly-morphing
purple-to-blue perlin blob on black — it is originkit.dev's own opening move
and it has been copied enough to read as a theme, not a decision. If you reach
for a mesh gradient, the way out is described per-technique below (tie to the
project's actual palette, break the "one soft blob" silhouette, pair with an
unusual layout).

---

## 1. Hand-rolled grain/noise shader (zero dependencies)

What: a single fullscreen-triangle draw call with a hash-based noise function
in the fragment shader. No library, no bundle cost, full control over the
noise function. This is the right choice when you want fine-grained control
over exactly how the grain looks and moves rather than a general-purpose
gradient tool.

License: none needed — you own the code.

No install. Drop this into any page:

```html
<canvas id="grain" style="position:fixed;inset:0;width:100%;height:100%"></canvas>
<script>
const canvas = document.getElementById('grain');
const gl = canvas.getContext('webgl');

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
  vec3 base = vec3(0.055, 0.055, 0.075); // swap for your OKLCH background
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

function resize() {
  canvas.width = innerWidth * devicePixelRatio;
  canvas.height = innerHeight * devicePixelRatio;
  gl.viewport(0, 0, canvas.width, canvas.height);
}
addEventListener('resize', resize);
resize();
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

function frame(t) {
  gl.uniform2f(uResolution, canvas.width, canvas.height);
  gl.uniform1f(uTime, reduceMotion ? 0 : t * 0.001);
  gl.uniform1f(uIntensity, 0.06);
  gl.drawArrays(gl.TRIANGLES, 0, 3);
  if (!reduceMotion) requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
</script>
```

Bespoke: replace `base` with the project's actual background token (in linear
sRGB, not the raw OKLCH string), and tune `uIntensity` — film-grain-subtle
(0.02-0.04) reads premium/editorial, heavy static (0.12+) reads glitchy/tech.
Combine with a solid or gradient `background` behind the canvas rather than
alpha-blending noise over a busy image.

---

## 2. paper-shaders (`@paper-design/shaders-react`)

What: a curated set of 30+ zero-dependency GPU shaders (mesh gradients, dot
grids, noise textures, halftone, aurora) shipped as drop-in React components —
no GLSL to write, no Three.js. Distinctive because it's not just "one perlin
blob preset" — it includes non-gradient effects (halftone, dot-grid,
static/noise) that read less like the default hero.

License: Apache 2.0, free for commercial use. Verified against the LICENSE
file in the `paper-design/shaders` GitHub repo (Apache License, Version 2.0).
npm shows active releases (0.0.8x range as of writing).

```bash
npm install @paper-design/shaders-react
# vanilla JS/no React: npm install @paper-design/shaders
```

```jsx
import { MeshGradient } from '@paper-design/shaders-react';

export default function Hero() {
  return (
    <MeshGradient
      colors={['#5100ff', '#00ff80', '#ffcc00', '#ea00ff']}
      speed={0.2}
      style={{ width: '100%', height: 400 }}
      // also: distortion, swirl — tune for how liquid vs. flat it reads
    />
  );
}
```

Bespoke: pass the project's real palette (3-4 stops pulled from its OKLCH
scale, not the demo purple/green/yellow/magenta) and drop `speed` well below
the default — 0.05-0.15 reads intentional, the default speed reads like a
screensaver. Crop it into an unexpected shape (a sidebar strip, a card corner)
instead of a full-bleed hero to avoid the templated read.

---

## 3. ShaderGradient (`@shadergradient/react`)

What: React Three Fiber wrapper around a curated set of animated gradient
"scenes" (plane, sphere, waterPlane) with camera controls — closer to a 3D
gradient sculpture than a flat shader. Distinctive when combined with
`type='sphere'` or `'waterPlane'` and an off-center camera rather than the
default flat plane.

License: MIT. Confirmed via search of the npm package metadata and the
`ruucm/shadergradient` GitHub repo — both `shadergradient` and
`@shadergradient/react` list MIT.

```bash
npm i @shadergradient/react @react-three/fiber three three-stdlib camera-controls
npm i -D @types/three
```

```jsx
import { ShaderGradientCanvas, ShaderGradient } from '@shadergradient/react';

export default function Hero() {
  return (
    <ShaderGradientCanvas style={{ position: 'absolute', inset: 0 }}>
      <ShaderGradient
        type="plane"
        color1="#52ff89"
        color2="#dbba95"
        color3="#d0bce1"
        uSpeed={0.4}
      />
    </ShaderGradientCanvas>
  );
}
```

Bespoke: this pulls in Three.js + R3F as peer deps — only reach for it if the
page already carries that weight (e.g. a 3D scene elsewhere), otherwise
paper-shaders or the hand-rolled canvas is far lighter. Vary `type` and camera
props (`cAzimuthAngle`, `cPolarAngle`, `cDistance`) rather than shipping the
docs' default plane framing.

---

## 4. Three.js custom `ShaderMaterial` (liquid/distortion effects)

What: write your own vertex + fragment shader and attach it to a Three.js
mesh via `THREE.ShaderMaterial`. This is the right layer when paper-shaders'
presets don't cover the effect — e.g. a UV-distortion "liquid" hover effect
over an image, or a displaced plane.

License: MIT (three.js, confirmed on `mrdoob/three.js` LICENSE file; current
npm `three` package is actively published).

```bash
npm install three
```

```js
import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0, 1);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

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
      // ripple distortion centered on mouse position
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

addEventListener('mousemove', (e) => {
  uniforms.uMouse.value.set(e.clientX / innerWidth, 1 - e.clientY / innerHeight);
});

function animate(t) {
  uniforms.uTime.value = t * 0.001;
  renderer.render(scene, camera);
  requestAnimationFrame(animate);
}
requestAnimationFrame(animate);
```

Bespoke: this scaffold is deliberately generic — the distortion math (ripple,
domain-warp, RGB-shift-on-scroll) is where the actual design decision lives.
Drive `uMouse`/`uTime` from scroll position or cursor velocity instead of a
flat clock so the effect feels responsive to the visitor, not just looping.

---

## 5. Mesh gradient via vertex displacement (hand-rolled technique)

What: the "Stripe gradient" look (soft, colorful, plane-warping gradient) is
not a single library so much as a known technique — a plane mesh with
per-vertex noise-driven displacement, vertex colors interpolated across noise
bands, rendered from a straight-on orthographic camera. `jordienr/whatamesh`
is the commonly cited reference implementation of this technique — **note:
that repo has no LICENSE file**, so treat it as read-for-technique only, not a
dependency to install or copy verbatim. paper-shaders' `MeshGradient` (#2
above) is the maintained, license-clear packaged version of the same idea; use
this hand-rolled route only when you need control the packaged version
doesn't expose (e.g. driving displacement from real data instead of noise).

License: n/a — implement from the technique description; do not vendor
whatamesh's source without checking with the author first.

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
  pos.z += n * 0.6; // displacement strength — the "liquid-ness" of the mesh
  vColor = mix(vec3(0.10, 0.05, 0.30), vec3(0.85, 0.65, 0.95), n);
  gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
}
```

```glsl
// fragment shader — just outputs the interpolated vertex color
varying vec3 vColor;
void main() {
  gl_FragColor = vec4(vColor, 1.0);
}
```

Use a `THREE.PlaneGeometry(4, 4, 64, 64)` (high segment count — the
displacement needs vertices to move) with a `ShaderMaterial` wrapping these
two shaders, camera looking straight at the plane.

Bespoke: swap the placeholder hash noise for real simplex noise (Ashima's
webgl-noise, MIT) for smoother blobs; the templated failure mode here is
exactly two colors blending into a single soft blob — use 3-4 color stops
tied to the brand's actual OKLCH scale and vary displacement frequency so the
mesh reads as folded fabric, not a lava lamp.

---

## Live lookup

- **Shadertoy** — https://www.shadertoy.com — the largest inspiration
  corpus for GLSL fragment-shader effects (noise fields, raymarching,
  distortion). **Not license-clear for direct copy**: shaders default to
  CC BY-NC-SA 3.0 (no commercial use) unless the author states otherwise —
  check each shader's own header/license note before adapting it, and treat
  it as a technique reference to reimplement, not a source to paste into a
  commercial product.
- **Paper Shaders site** — https://shaders.paper.design/ — the visual
  editor for `@paper-design/shaders`; browse presets, tune params live, export
  the config. Apache 2.0 per the package license above.
- **ShaderGradient editor** — https://www.shadergradient.co/ (Figma/Framer/
  React export tool for the shadergradient package above) — check current
  export/pricing terms before relying on the hosted editor itself; the
  `@shadergradient/react` npm package is MIT regardless of the editor's terms.
- **Three.js examples** — https://threejs.org/examples/ — official
  example gallery, filter by `webgl_shader*` and `webgl_gpgpu*` for
  distortion/particle patterns; all MIT-licensed like the core library.
- **oframe/ogl examples** — https://oframe.github.io/ogl/examples/ — a
  ~8kb, dependency-free WebGL library (Unlicense/public domain) that's a
  lighter alternative to Three.js when the page only needs a single shader
  plane and not a scene graph; the examples directory doubles as a pattern
  library for minimal shader setups.
