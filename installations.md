# Lecture Summarizer - System Requirements

## Python Packages
- `Flask==2.3.5` — Web framework
- `torch==2.2.0` — PyTorch backend for Whisper and transformers
- `transformers==4.42.2` — Hugging Face pipeline for summarization
- `sentencepiece==0.1.99` — Tokenizer dependency for T5 summarizer
- `openai-whisper==20230314` — ASR for transcript generation
- `ffmpeg-python==0.2.0` — Python interface for FFmpeg
- Optional:
  - `pydub==0.26.0` — advanced audio handling
  - `tqdm==4.66.1` — progress bars for console output

## External Dependencies
- **FFmpeg**
  - Required for audio extraction from video.
  - Download: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
  - Add the `bin` folder to your system PATH.

- **GPU (Optional)**
  - NVIDIA GPU recommended for faster inference.
  - Install CUDA Toolkit and cuDNN compatible with PyTorch version.
  - Without GPU, app works on CPU (slower).

## System Specifications
- **RAM**: 4–8 GB minimum; more for long lectures or larger models
- **Disk Space**: Enough to store uploaded videos/audio
- **CPU**: Modern multi-core processor recommended

## Notes
- Long audio/video (~2 hours) will take longer to process on CPU.
- T5-small and Whisper-tiny are chosen to work on CPU with reasonable performance.
- Ensure Python 3.10+ is installed and added to PATH.
