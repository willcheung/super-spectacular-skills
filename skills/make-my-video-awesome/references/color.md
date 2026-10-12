# Color: iPhone HDR footage

## What happens

iPhones record HDR by default (HLG, BT.2020, 10-bit; actually Dolby Vision 8.4 with an HLG base). On an HDR screen it looks punchy. Everywhere this pipeline touches it, it can go wrong:

- **Labelled HDR but 8-bit** → players and the renderer tone-map it again → flat, grey, "washed out".
- **Raw HLG shown as SDR** → acceptable but flat: blacks ~44, whites ~206 (of 16–235).
- **Hand grade that brightens whites** → looks "white", the opposite of the fix.
- **HyperFrames HDR render mode** needs ~24 GB of temp space for a one-minute Short.

Editors like Final Cut, CapCut, Descript, and Premiere hide this with built-in color management. FFmpeg on macOS (Homebrew build) lacks `zscale`/`libplacebo`, so there is no automatic path here; we do it explicitly.

## What `cut.py` does

For any clip whose `color_transfer` is `arib-std-b67`:

1. Decode with the BT.2020 matrix to full-range RGB.
2. Apply `assets/iphone_hlg_to_sdr.cube`, a 3D LUT **fitted to HyperFrames' own preview of HLG footage** (mean error ~2/255). The user liked how the Studio preview looked; this reproduces it.
3. Convert to BT.709 YUV and label the stream BT.709 (`setparams`, because output flags alone don't override frame metadata).
4. Optional taste grade (`warmth` in edit.json): `light` = slightly warmer skin, +15% saturation, +5% contrast, highlights kept neutral so a grey wall stays grey. `none` and `medium` exist; stronger warmth turns white walls cream.

SDR clips skip the LUT and only get labelled.

## When the look is off

Measure before touching anything — `verify.py` prints luma low/avg/high and saturation. Compare against what the user says looks right (a screenshot of the version they liked is gold: sample the same spots — skin, wall, dark clothing — in both).

- Washed/grey → check the tags first (`ffprobe … color_transfer`). An HDR tag on the output is the usual culprit.
- Too cool / pale skin → warmth `light` → `medium`.
- New lighting or location looks wrong → refit the LUT:
  1. Make a 6 s 10-bit HLG test clip from a raw file (`libx265`, `-pix_fmt yuv420p10le`, HLG/BT.2020 tags).
  2. Make a one-`<video>` HyperFrames composition playing it; `npx hyperframes snapshot --at 1,3`.
  3. Extract the same frames from the clip as RGB (`in_<n>.png`, recipe in `fit_lut.py`), name the snapshots `ref_<n>.png`.
  4. `python3 scripts/fit_lut.py WORK_DIR assets/iphone_hlg_to_sdr.cube` and re-cut.

The fitted LUT reflects the footage it was fitted on (grey wall, black shirt, skin). Strong colors far outside that range are extrapolated; check them.

## The real fix

Ask the user to turn off **Settings → Camera → Record Video → HDR Video** for footage meant for this pipeline. SDR footage needs none of the above, and Shorts are watched in SDR almost everywhere.
