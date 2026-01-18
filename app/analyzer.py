class HeaderAnalyzer:
    """Analyzes HTTP headers and generates a security score."""
    
    # güvenlik kontrol aşamalrı
    SECURITY_HEADERS = {
        "Strict-Transport-Security": 20,  # SSL zorunluluğu
        "Content-Security-Policy": 25,    # XSS koruması***
        "X-Frame-Options": 15,            # Clickjacking koruması
        "X-Content-Type-Options": 10,     # MIME-sniffing koruması
        "Referrer-Policy": 10,            # Veri sızıntısı kontrol
        "Permissions-Policy": 10          # Tarayıcı özellikleri izni
    }

    def analyze(self, raw_data):
        analyzed_data = []
        
        for item in raw_data:
            score = 0
            missing_headers = []
            present_headers = []
            
            # Bağlantı hatası kontrolü/kodu kontrol et
            if item["error"]:
                analyzed_data.append({
                    "url": item["url"],
                    "score": 0,
                    "grade": "F",
                    "status": "FAIL",
                    "missing_headers": "Connection Error"
                })
                continue

            headers = {k.lower(): v for k, v in item["headers"].items()}

            for sec_header, points in self.SECURITY_HEADERS.items():
                if sec_header.lower() in headers:
                    score += points
                    present_headers.append(sec_header)
                else:
                    missing_headers.append(sec_header)

            analyzed_data.append({
                "url": item["url"],
                "score": min(score, 100),
                "grade": self._calculate_grade(score),
                "status": item["status"],
                "missing_headers": ", ".join(missing_headers) if missing_headers else "None"
            })
            
        return analyzed_data

    def _calculate_grade(self, score):
        """Letter grades based on the score.."""
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 60: return "C"
        elif score >= 40: return "D"
        else: return "F"