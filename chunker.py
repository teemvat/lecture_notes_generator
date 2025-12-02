# A function used to chop long text into smaller pieces for processing.
def chunk_text(text: str, max_words: int = 300):

    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks
