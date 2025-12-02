import os
import tempfile

from flask import Flask, render_template, request, jsonify
from extract_audio import extract_audio
from whisper_transcription import transcribe_audio
from gpt_processing import clean_and_summarize_full

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Allowed file types
AUDIO_EXT = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
VIDEO_EXT = {".mp4", ".mkv", ".mov", ".avi"}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400

    filename = file.filename.lower()
    ext = os.path.splitext(filename)[1]

    # Store uploaded file temporarily
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, filename)
        file.save(input_path)

        # AUDIO
        if ext in AUDIO_EXT:
            audio_path = input_path

        # VIDEO to Extract audio
        elif ext in VIDEO_EXT:
            audio_path = os.path.join(tmpdir, "extracted_audio.mp3")
            extract_audio(input_path, audio_path)
            print("Audio extract complete.")

        else:
            return jsonify({"error": "Unsupported file type"}), 400

        # Whisper transcription
        result = transcribe_audio(audio_path)
        transcript = result
        print("Transcription complete")

        # Chunking and processing pipeline
        transcript = clean_and_summarize_full(transcript)

        return render_template(
            "index.html",
            summary=transcript["final_summary"]
        )


if __name__ == "__main__":
    app.run(debug=True)
