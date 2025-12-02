from openai import OpenAI
from chunker import chunk_text
import os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

# Text processing uses OpenAI api, so a key is required.
load_dotenv()
api_key = os.getenv('GPT_KEY')
client = OpenAI(api_key=api_key)


# Clean a single chunk
def clean_chunk(text: str) -> str:
    prompt = (
        "Clean the transcription: fix casing, remove filler words if meaningless, "
        "remove noise, normalize spacing. Keep content faithful.\n\n"
        f"Text:\n{text}"
    )

    resp = client.responses.create(
        model="gpt-5-nano",
        input=prompt
    )
    return resp.output_text


# Summarize a single chunk. Default length is 3 sentences.
def summarize_chunk(text: str) -> str:
    resp = client.responses.create(
        model="gpt-5-nano",
        input=f"Summarize the following cleaned transcription:\n\n{text}"
    )
    return resp.output_text


# Full pipeline: clean, summarize chunks, then summarize summaries
def clean_and_summarize_full(text: str) -> dict:
    chunks = chunk_text(text, max_words=300)

    # Use ThreadPoolExecutor to process chunks concurrently
    with ThreadPoolExecutor(max_workers=5) as executor:
        cleaned_chunks = list(executor.map(clean_chunk, chunks))
        summary_chunks = list(executor.map(summarize_chunk, cleaned_chunks))

    # Final synthesis (still sequential, single call)
    final_summary = client.responses.create(
        model="gpt-5-nano",
        input=(
                "You are creating concise lecture notes from the following partial summaries:\n\n"
                + "\n\n".join(summary_chunks)
                + "\n\nInstructions:\n"
                  "- Summarize the content into clear lecture notes.\n"
                  "- Use headings and bullet points where appropriate.\n"
                  "- Keep sentences short and precise.\n"
                  "- Include only the main points; remove filler words.\n"
                  "- Highlight key terms or concepts.\n"
                  "- Group related points together under subheadings.\n"
                  "- Use 1–2 sentence explanations per point.\n"
                  "- Organize logically so that someone reading the notes understands the topic quickly."

        )
    ).output_text

    return {
        "chunks": chunks,
        "cleaned": cleaned_chunks,
        "chunk_summaries": summary_chunks,
        "final_summary": final_summary
    }
