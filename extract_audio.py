import subprocess
from pathlib import Path


# Using Ffmpeg tool to extract audio from a video file.
def extract_audio(video_path, audio_output):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-vn",  # remove video
        "-ac", "1",  # mono audio
        "-ar", "16000",  # 16 kHz sample rate
        "-f", "wav",    # to uncompressed wav file
        "-y",   # overwrite output
        audio_output
    ]

    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
