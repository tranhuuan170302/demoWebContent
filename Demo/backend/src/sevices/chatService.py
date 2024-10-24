from utils.stopWords import get_stopwords
from utils.dataProcessing import load_url, clean_text
import nest_asyncio

nest_asyncio.apply()

class ChatService:
    async def processChatMessage(self, message, filePath="D:\\WorkSpace\\PythonWebCrawlData\\Demo\\backend\\stopWord.txt"):
        
        data_load_url = await load_url(message)
        stopword = await get_stopwords(filePath)
        # print(message)
        filterMessage = await clean_text(data_load_url, stopword)
        
        return filterMessage