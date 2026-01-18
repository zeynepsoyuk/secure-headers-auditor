import sys
import os
import asyncio

# app'i bulamazsa ekle
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)


from app.utils import setup_logger
from app.scanner import AsyncScanner
from app.analyzer import HeaderAnalyzer
from app.reporter import Reporter

TARGET_URLS = [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
    "http://testphp.vulnweb.com",
    "https://example.com",
    "https://paypal.com",
    "https://www.dropbox.com",
]

async def main():
    setup_logger()
    print(">>> Starting Secure Headers Auditor...")
    
    print(f">>> {len(TARGET_URLS)} URL's are scanning...")
    scanner = AsyncScanner(TARGET_URLS)
    raw_results = await scanner.scan_all()
    
    print(">>> Data is being analyzed...")
    analyzer = HeaderAnalyzer()
    final_results = analyzer.analyze(raw_results)
    
    Reporter.generate_report(final_results, "final_security_report.csv")
    print(">>> Transaction completed.")

if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nTransaction stopped.")