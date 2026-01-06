# Прост уеб crawler

## Използвани технологии
- Python 3.9+
- requests
- BeautifulSoup4
- pandas
- urllib.robotparser

## Функционалности
- Обхожда една уеб страница (https://quotes.toscrape.com)
- Проверява robots.txt преди обхождане
- Извлича цитати, автори и тагове
- Записва данните локално в CSV и ги показва на екрана

## Настройка и стартиране локално
1. Клонирайте репозитория:
   git clone https://github.com/VTUMihail1/uni_coursework.git
2. Навигирай до папката cd uni_coursework
3. Инсталирайте зависимостите директно чрез pip:
   pip install requests beautifulsoup4 pandas
4. Стартирайте crawler-a:
   python src/crawler.py
5. Проверете CSV файла в папката `data/` за резултати.
