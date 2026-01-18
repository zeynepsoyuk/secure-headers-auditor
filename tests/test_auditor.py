import pytest
from app.analyzer import HeaderAnalyzer

@pytest.fixture
def mock_data():
    return [
        {
            "url": "https://secure.com",
            "error": None,
            "status": 200,
            "headers": {
                "Strict-Transport-Security": "max-age=31536000",
                "Content-Security-Policy": "default-src 'self'",
                "X-Frame-Options": "DENY",
                "X-Content-Type-Options": "nosniff"
            }
        },
        {
            "url": "https://insecure.com",
            "error": None,
            "status": 200,
            "headers": {} 
        }
    ]

def test_security_score_high(mock_data):
    """A secure site needs to receive a high rating.."""
    analyzer = HeaderAnalyzer()
    results = analyzer.analyze(mock_data)
    # 4 başlık var: 20+25+15+10 = 70 puan
    assert results[0]["score"] == 70
    assert results[0]["grade"] == "C"

def test_security_score_zero(mock_data):
    """An unsafe site should receive a score of 0."""
    analyzer = HeaderAnalyzer()
    results = analyzer.analyze(mock_data)
    assert results[1]["score"] == 0
    assert results[1]["grade"] == "F"

def test_missing_headers_detection(mock_data):
    """Correct identification of missing headings."""
    analyzer = HeaderAnalyzer()
    results = analyzer.analyze(mock_data)
    missing = results[1]["missing_headers"]
    assert "Content-Security-Policy" in missing

def test_error_handling():
    """It shouldn't crash in case of a connection error."""
    analyzer = HeaderAnalyzer()
    error_input = [{"url": "bad.com", "error": "Timeout", "status": 0, "headers": {}}]
    results = analyzer.analyze(error_input)
    assert results[0]["status"] == "FAIL"
    assert results[0]["score"] == 0

def test_empty_input():
    """When empty data is received, an empty list should be returned."""
    analyzer = HeaderAnalyzer()
    assert analyzer.analyze([]) == []