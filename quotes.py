import csv
import json
from playwright.sync_api import sync_playwright


class QuotesScraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.quotes = []

    def _initialize_browser(self):
        self.browser = sync_playwright().start().chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def _close_browser(self):
        self.browser.close()

    def login(self):
        self._initialize_browser()
        self.page.goto('https://quotes.toscrape.com/login')
        self.page.fill('input#username', self.username)
        self.page.fill('input#password', self.password)
        self.page.click('input[type="submit"]')
        self.page.wait_for_load_state('networkidle')

    def scrape_quotes(self):
        quotes_data = []
        quotes_elements = self.page.query_selector_all('div.quote')

        for quote in quotes_elements:
            text = quote.query_selector('span.text').inner_text()
            author = quote.query_selector('small.author').inner_text()
            tags = [tag.inner_text() for tag in quote.query_selector_all('a.tag')]

            quotes_data.append({
                "quote": text,
                "author": author,
                "tags": tags
            })

        return quotes_data

    def scrape_all_pages(self):
        self.login()
        while True:
            self.quotes.extend(self.scrape_quotes())
            next_button = self.page.query_selector('li.next a')

            if next_button:
                next_button.click()
                self.page.wait_for_load_state('networkidle')
            else:
                break

        self._close_browser()

    def save_to_csv(self, filename='quotes.csv'):
        if not self.quotes:
            print("No quotes to save.")
            return

        keys = self.quotes[0].keys()
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.quotes)

    def save_to_json(self, filename='quotes.json'):
        if not self.quotes:
            print("No quotes to save.")
            return

        with open(filename, mode='w', encoding='utf-8') as file:
            json.dump(self.quotes, file, indent=4)

    def export_data(self):
        self.save_to_csv('quotes.csv')
        self.save_to_json('quotes.json')


class QuotesApp:
    def __init__(self, username, password):
        self.scraper = QuotesScraper(username, password)

    def run(self):
        self.scraper.scrape_all_pages()
        self.scraper.export_data()
        print("Data scraped and saved successfully.")


if __name__ == '__main__':
    USERNAME = 'qwert@abc.com'
    PASSWORD = 'Password@123'

    app = QuotesApp(USERNAME, PASSWORD)
    app.run()
