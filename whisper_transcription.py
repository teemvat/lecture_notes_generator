from openai import OpenAI
import os
from dotenv import load_dotenv

# Transcription uses OpenAI Whisper model via the api, so api key is required.
load_dotenv()
api_key = os.getenv('GPT_KEY')
client = OpenAI(api_key=api_key)


# Transcribes audio file using Whisper model.
def transcribe_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )
    return transcript.text
