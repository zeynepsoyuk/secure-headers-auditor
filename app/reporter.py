import pandas as pd
import logging

class Reporter:
    """Reports analysis results."""
    
    @staticmethod
    def generate_report(data, filename="security_report.csv"):
        if not data:
            logging.warning("Data not found.")
            return

        df = pd.DataFrame(data)
        
        print("\n" + "="*40)
        print("      SUMMARY OF SCAN RESULTS")
        print("="*40)
        print(df[["url", "score", "grade", "status"]].to_string(index=False))
        print("="*40)
        
        # CSV dönüştür kaydet
        try:
            df.to_csv(filename, index=False)
            print(f"\n[+] Detailed report saved: {filename}")
            logging.info(f"Report created successfully: {filename}")
        except Exception as e:
            logging.error(f"Error saving report: {e}")