#!/usr/bin/env python3
"""Reproducible synthetic audio codec/container identification lab.

Requires Python 3.9+, FFmpeg and ffprobe on PATH. No third-party Python modules.
This does not test actual WhatsApp voice notes or device compatibility.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
import shutil
import struct
import subprocess
import wave

BASE = Path(__file__).resolve().parent
OUT = BASE / "generated"
RATE = 16000
SECONDS = 8


def make_wav(path: Path) -> None:
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        buf = bytearray()
        for i in range(RATE * SECONDS):
            t = i / RATE
            phase = t % 1.0
            if phase < 0.15:
                v = 0.0
            else:
                freq = (220, 330, 440, 550)[int(t) % 4]
                env = 0.38 * (1.0 - 0.40 * (phase - 0.15))
                v = env * (math.sin(2 * math.pi * freq * t) + 0.18 * math.sin(4 * math.pi * freq * t))
            val = max(-32768, min(32767, round(v * 32767)))
            buf.extend(struct.pack("<h", val))
        w.writeframes(buf)


def run(args: list[str]) -> str:
    p = subprocess.run(args, text=True, capture_output=True, check=False)
    if p.returncode != 0:
        raise RuntimeError("Command failed: " + " ".join(args) + "\n" + p.stderr[-1500:])
    return p.stdout


def probe(path: Path) -> dict:
    info = json.loads(run(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries",
                           "stream=codec_name,sample_rate,channels,bit_rate:format=format_name,duration,bit_rate", "-of", "json", str(path)]))
    a = info["streams"][0]
    fmt = info["format"]
    return {
        "filename": path.name,
        "container": fmt.get("format_name", ""),
        "codec": a.get("codec_name", ""),
        "sample_rate_hz": int(a.get("sample_rate", 0)),
        "channels": int(a.get("channels", 0)),
        "duration_s": round(float(fmt.get("duration", 0)), 3),
        "size_bytes": path.stat().st_size,
        "bitrate_container_bps": int(fmt.get("bit_rate", 0)),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main() -> None:
    for binary in ("ffmpeg", "ffprobe"):
        if not shutil.which(binary):
            raise SystemExit(f"Missing dependency: {binary}")
    OUT.mkdir(exist_ok=True)
    wav = OUT / "reference.wav"
    make_wav(wav)
    recipes: list[tuple[str, list[str]]] = [
        ("sample.mp3", ["-c:a", "libmp3lame", "-b:a", "64k"]),
        ("sample.opus", ["-c:a", "libopus", "-b:a", "32k", "-vbr", "off", "-ar", "48000"]),
        ("sample.ogg", ["-c:a", "libvorbis", "-q:a", "3"]),
        ("sample.m4a", ["-c:a", "aac", "-b:a", "64k"]),
        ("sample.aac", ["-c:a", "aac", "-b:a", "64k", "-f", "adts"]),
        ("sample.3gp", ["-c:a", "aac", "-b:a", "64k", "-f", "3gp"]),
    ]
    paths = [wav]
    for name, options in recipes:
        dest = OUT / name
        run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(wav), "-vn", *options, str(dest)])
        paths.append(dest)
    rows = [probe(p) for p in paths]
    assert len(rows) == 7 and all(row["duration_s"] >= 7.99 for row in rows)
    assert [r["codec"] for r in rows] == ["pcm_s16le", "mp3", "opus", "vorbis", "aac", "aac", "aac"]
    cols = list(rows[0])
    with (BASE / "measurements.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        writer.writerows(rows)
    (BASE / "measurements.json").write_text(json.dumps({
        "ffmpeg_version": run(["ffmpeg", "-version"]).splitlines()[0],
        "ffprobe_version": run(["ffprobe", "-version"]).splitlines()[0],
        "test_signal": "8 sec generated mono 16 kHz PCM; alternating synthetic tones and pauses; not speech",
        "samples": rows
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for r in rows:
        print(f"{r['filename']:16} {r['codec']:12} {r['size_bytes']:8} bytes  {r['duration_s']:5} s")
    print("Wrote measurements.csv and measurements.json")


if __name__ == "__main__":
    main()
