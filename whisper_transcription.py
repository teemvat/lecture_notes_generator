from openai import OpenAI
import os
from dotenv import load_dotenv
from chunker import chunk_audio

# Transcription uses OpenAI Whisper model via the api, so api key is required.
load_dotenv()
api_key = os.getenv('GPT_KEY')
client = OpenAI(api_key=api_key)


# Transcribes audio file using Whisper model.
def process_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text


# Function for longer audio files:
def transcribe_audio(audio_path: str) -> str:
    chunk_paths = chunk_audio(audio_path)

    full_text = []
    for path in chunk_paths:
        text = process_audio(path)
        full_text.append(text)

    for p in chunk_paths:
        try:
            os.remove(p)
        except:
            pass

    return " ".join(full_text)
