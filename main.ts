// The picture that tastes of one ingredient — HONEY.
//
// A wooden honey dipper dripping golden honey into a pool, warm light on a
// dark warm-brown background. The picture was rendered in this session from
// scene.html (SVG) with Playwright and committed as entry.png; this program
// copies that exact image to /output/entry.png so every run is byte-identical.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = "/output";

mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
console.log("wrote /output/entry.png");
