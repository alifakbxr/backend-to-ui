#!/usr/bin/env python3
"""Basic, dependency-free checks for the promotional MP4/GIF.

Browser playback smoothness is subjective and must still be visually inspected.
"""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import struct
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "media" / "intro.mp4"
GIF = ROOT / "media" / "intro.gif"


def probe(path: Path) -> dict:
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries",
        "stream=codec_name,width,height,nb_frames,avg_frame_rate:"
        "format=duration", "-of", "json", str(path),
    ], text=True))


class IntroMediaTests(unittest.TestCase):
    def test_media_exists_and_stays_small(self):
        self.assertTrue(VIDEO.is_file())
        self.assertTrue(GIF.is_file())
        self.assertLess(VIDEO.stat().st_size, 5_000_000)
        self.assertLess(GIF.stat().st_size, 3_000_000)

    def test_gif_dimensions_and_signature(self):
        payload = GIF.read_bytes()[:10]
        self.assertIn(payload[:6], (b"GIF89a", b"GIF87a"))
        self.assertEqual(struct.unpack("<HH", payload[6:10]), (800, 450))

    @unittest.skipUnless(shutil.which("ffprobe"), "ffprobe is not installed")
    def test_video_and_gif_timing(self):
        movie = probe(VIDEO)
        video = next(s for s in movie["streams"] if s["codec_name"] == "h264")
        audio = next(s for s in movie["streams"] if s["codec_name"] == "aac")
        self.assertIsNotNone(audio)
        self.assertEqual((video["width"], video["height"]), (1280, 720))
        self.assertEqual(video["avg_frame_rate"], "30/1")
        self.assertAlmostEqual(float(movie["format"]["duration"]), 17.0, delta=.15)

        gif = probe(GIF)
        stream = gif["streams"][0]
        self.assertEqual((stream["width"], stream["height"]), (800, 450))
        self.assertEqual(int(stream["nb_frames"]), 255)
        self.assertAlmostEqual(float(gif["format"]["duration"]), 17.0, delta=.15)


if __name__ == "__main__":
    unittest.main()
