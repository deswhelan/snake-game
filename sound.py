import math
import random
import struct
import wave
from pathlib import Path

try:
    import winsound
except ImportError:
    # winsound is Windows only - elsewhere the game simply runs without sound
    winsound = None

CHOMP_FILE = Path(__file__).parent / "chomp.wav"
SAMPLE_RATE = 22050
# Start time and length (in seconds) of each bite in the chomp
BITES = [(0.0, 0.08), (0.11, 0.09)]


def create_chomp_sound():
    """Synthesises a two-bite crunch and saves it as a wav file"""
    rng = random.Random(7)
    length = int(SAMPLE_RATE * (BITES[-1][0] + BITES[-1][1]))
    samples = [0.0] * length

    for start, duration in BITES:
        filtered_noise = 0.0
        for i in range(int(SAMPLE_RATE * duration)):
            t = i / SAMPLE_RATE
            envelope = min(1.0, t / 0.004) * math.exp(-t / (duration / 4))
            # Low-passed noise for the crunch, plus a falling low tone for the thud of the jaws
            filtered_noise += 0.35 * (rng.uniform(-1, 1) - filtered_noise)
            thud = math.sin(2 * math.pi * (160 - 500 * t) * t)
            samples[int(SAMPLE_RATE * start) + i] += envelope * (0.8 * filtered_noise + 0.5 * thud)

    with wave.open(str(CHOMP_FILE), "w") as chomp:
        chomp.setnchannels(1)
        chomp.setsampwidth(2)
        chomp.setframerate(SAMPLE_RATE)
        chomp.writeframes(b"".join(struct.pack("<h", int(max(-1.0, min(1.0, s)) * 26000)) for s in samples))


def play_chomp():
    """Plays the chomp sound without pausing the game"""
    if winsound is None:
        return
    if not CHOMP_FILE.exists():
        create_chomp_sound()
    winsound.PlaySound(str(CHOMP_FILE), winsound.SND_FILENAME | winsound.SND_ASYNC)
