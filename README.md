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
   git clone <repo-url>
2. Навигирайте до папката на проекта и създайте виртуална среда:
   python -m venv env
3. Активирайте виртуалната среда:
   - Windows: env\Scripts\activate
   - Mac/Linux: source env/bin/activate
4. Инсталирайте зависимостите директно чрез pip:
   pip install requests beautifulsoup4 pandas
5. Стартирайте crawler-a:
   python src/crawler.py
6. Проверете CSV файла в папката `data/` за резултати.