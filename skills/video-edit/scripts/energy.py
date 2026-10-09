#!/usr/bin/env python3
"""Print audio energy around a cut point so boundaries can be placed in real silence.

Usage: python3 energy.py CLIP START END
Prints one line per 50ms: time and a bar. Whisper word timestamps can drift
0.4-0.6s; trust the bars over the transcript when choosing a cut.
"""
import array, subprocess, sys

clip, a, b = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
pcm = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(a), "-to", str(b), "-i", clip,
                      "-vn", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                     capture_output=True, check=True).stdout
s, H = array.array("h", pcm), 800
for i in range(0, len(s) - H, H):
    r = (sum(x * x for x in s[i:i + H]) / H) ** 0.5
    print(f"{a + i / 16000:7.2f} " + "#" * int(r / 150))
