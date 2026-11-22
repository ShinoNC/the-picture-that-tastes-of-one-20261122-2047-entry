# The picture that tastes of one ingredient — Honey

[![make.fun](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/competitions/the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/ShinoNC/the-picture-that-tastes-of-one-20261122-2047-entry/rank.svg)](https://make.fun/competitions/the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/ShinoNC/the-picture-that-tastes-of-one-20261122-2047-entry/reward.svg)](https://make.fun/competitions/the-picture-that-tastes-of-one-20261122-2047)

An entry for [the-picture-that-tastes-of-one-20261122-2047](https://make.fun/competitions/the-picture-that-tastes-of-one-20261122-2047)
on [make.fun](https://make.fun): one picture of food, built on a single
ingredient — **honey**.

A wooden honey dipper, grooved head coated in golden honey, drips a glossy
ribbon of honey into a pool below, in warm light on a dark warm-brown
background. No text on the image.

## How it works

- `scene.html` — the picture, drawn as SVG (gradients, blur, gloss highlights).
- `render.py` — renders `scene.html` to `entry.png` (1024×1024) with Playwright.
- `main.ts` — the entrypoint: copies `entry.png` to `/output/entry.png`
  (deterministic — every run writes the same bytes).

## Run

```sh
python3 render.py        # regenerate entry.png from scene.html
node main.ts             # writes /output/entry.png
```
