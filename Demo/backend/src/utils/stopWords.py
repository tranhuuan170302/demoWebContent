import asyncio

# Global variable to store stopwords
_stopwords = None
_stopwords_lock = asyncio.Lock()

async def load_stopwords(file_path):
    """Load stopwords from file and store in the global variable."""
    global _stopwords
    async with _stopwords_lock:
        if _stopwords is None:  # Load only if stopwords has not been loaded yet
            with open(file_path, 'r', encoding='utf-8') as f:
                _stopwords = {line.strip() for line in f}
    return _stopwords

async def get_stopwords(file_path='stopwords.txt'):
    """Return the stopwords, load from file if not already loaded."""
    if _stopwords is None:
        await load_stopwords(file_path)
    return _stopwords
