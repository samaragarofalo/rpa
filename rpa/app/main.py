from rpa.app.application.scraping_service import ScrapingService


def main() -> None:
    url = "https://www.tce.sp.gov.br/jurisprudencia/"
    keywords = "fraude escola"

    service = ScrapingService(url)
    service.perform_search(keywords)


if __name__ == "__main__":
    main()
