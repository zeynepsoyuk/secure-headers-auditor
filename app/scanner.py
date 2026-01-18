import aiohttp
import asyncio
import logging
from app.utils import get_config

class AsyncScanner:
    """Scans the specified URL list asynchronously."""
    
    def __init__(self, urls):
        self.urls = urls
        self.results = []
        self.timeout = int(get_config("TIMEOUT", 10))
        self.headers = {'User-Agent': get_config("USER_AGENT", "PythonBot")}

    async def fetch_headers(self, session, url):
        """Extracts headers for a single URL."""
        try:
            logging.info(f"Scan started: {url}")
            async with session.get(url, timeout=self.timeout, ssl=False, headers=self.headers) as response:
                return {
                    "url": url,
                    "status": response.status,
                    "headers": dict(response.headers),
                    "error": None
                }
        except Exception as e:
            logging.error(f"Error. {url}: {str(e)}")
            return {"url": url, "status": 0, "headers": {}, "error": str(e)}

    async def scan_all(self):
        """Starts all URLs as asynchronous tasks."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_headers(session, url) for url in self.urls]
            self.results = await asyncio.gather(*tasks)
        return self.results