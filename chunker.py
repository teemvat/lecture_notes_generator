import uuid
import tempfile
import os
from pydub import AudioSegment


# A function used to chop long text into smaller pieces for processing.
def chunk_text(text: str, max_words: int = 300):

    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


# A function used to chop long audio files into segments for whisper transcription.
def chunk_audio(
    audio_path: str,
    chunk_length_ms: int = 60_000,    # 60 seconds
    overlap_ms: int = 3_000           # 3 seconds overlap
):

    audio = AudioSegment.from_file(audio_path)
    duration = len(audio)

    chunks = []
    start = 0

    while start < duration:
        end = min(start + chunk_length_ms, duration)

        chunk = audio[start:end]

        # Export to temporary files
        tmp_path = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}.wav")
        chunk.export(tmp_path, format="wav")
        chunks.append(tmp_path)

        # Move start forward with overlap
        start = end - overlap_ms

        if start < 0:
            start = 0

        if end == duration:
            break

    return chunks
