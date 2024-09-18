import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_data(url):
    """URL'den veriyi çekme ve pars etme"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"HTTP Hatası: {e}")
        return None

def parse_titles(soup):
    """HTML içeriğinden başlıkları çekme"""
    titles = [item.text for item in soup.find_all('h2', class_='headline')]
    return titles

def save_to_csv(data, filename='data/headlines.csv'):
    """Veriyi CSV dosyasına kaydetme"""
    df = pd.DataFrame(data, columns=['Title'])
    df.to_csv(filename, index=False)
