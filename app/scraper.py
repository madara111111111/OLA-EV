import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
URLS = [
    "https://www.bikedekho.com/ola-electric/s1-pro/reviews",
    "https://www.bikewale.com/ola-bikes/s1-pro/reviews/",
    "https://www.bikedekho.com/ola-electric/s1x/reviews",
    "https://www.quora.com/What-is-your-honest-review-on-the-Ola-Electric-S1-bike-Is-it-worth-buying",
    "https://www.mouthshut.com/category/ola-electric-bikes-reviews-926175582",
    "https://www.reddit.com/r/indianbikes/comments/1b5zjx2/ola_s1_pro_15_years_15_000_kms_ama/",
    "https://www.zigwheels.com/user-reviews/ola-electric/2025-s1-pro"
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def scrape_comments():
    comments = []
    for url in URLS:
        try:
            r = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(r.content, 'html.parser')

            # Basic generic scraping - user may need to customize per site
            # Example: get all <p> tags with possible comments
            for p in soup.find_all('p'):
                text = p.get_text(strip=True)
                if text and len(text) > 20:  # Filter short texts
                    comments.append({'source': url, 'text': text})
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return comments
