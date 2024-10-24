import re
import asyncio
import httpx
from selectolax.parser import HTMLParser

async def load_url(url):
    """_summary_

    Args:
        url (_type_): url

    Returns:
        str: content of the webpage
    """
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        if r.status_code == 200:
            tree = HTMLParser(r.text)

            # Loại bỏ các thẻ không mong muốn
            for tag in tree.css('script'):
                tag.decompose()

            content = tree.body.text()
            cleaned_html = re.sub(r'\s{2,}', ' ', content).replace('\n', '')
            return cleaned_html.lower().strip()

async def clean_text(text: str, stopwords: list):
    """
    Xử lý văn bản tiếng Việt: Loại bỏ các ký tự không mong muốn và stopwords dạng từ đơn hoặc cụm từ.
    """
    async with httpx.AsyncClient() as client:
        # Loại bỏ các ký tự đặc biệt nhưng giữ lại dấu tiếng Việt
        text = re.sub(r'[^\w\s]', '', text)

        # Đưa về chữ thường
        text = text.lower()

        # Loại bỏ stopwords
        for stopword in stopwords:
            # Sử dụng re.sub để loại bỏ stopword (dạng từ hoặc cụm từ) khỏi văn bản
            pattern = r'\b' + re.escape(stopword) + r'\b'
            text = re.sub(pattern, '', text)

        # Loại bỏ khoảng trắng thừa do việc loại bỏ stopwords
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    return none
