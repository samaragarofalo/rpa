from rpa.app.infra.scraper import SeleniumScraper
from rpa.app.infra.db import MongoDBRepository
from rpa.app.infra.file_writer import save_results_to_json


class ScrapingService:
    def __init__(self, url: str) -> None:
        self.url = url
        self.scraper = SeleniumScraper(self.url)
        self.repository = MongoDBRepository()

    def perform_search(self, keywords: str) -> None:
        results = self.scraper.search(keywords)
        save_results_to_json(results, keywords)
        self.repository.insert_data(results)
