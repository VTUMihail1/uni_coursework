from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin
import pandas as pd
from pathlib import Path

def can_crawl(url, user_agent):
    robots_url = urljoin(url, "/robots.txt")
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp.can_fetch(user_agent, url)

def save_to_csv(data, filename="data.csv"):
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "uni_coursework\data"
    DATA_DIR.mkdir(exist_ok=True)
    CSV_PATH = DATA_DIR / filename

    df = pd.DataFrame(data)
    df.to_csv(CSV_PATH, index=False)
    print(f"Data saved to {CSV_PATH}")
    return CSV_PATH