import traceback
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import tempfile


class SeleniumScraper:
    def __init__(self, url: str) -> None:
        self.url = url

    def search(self, keywords: str) -> list:
        temp_profile_dir = tempfile.mkdtemp()

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")

        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

        results = []
        try:
            driver.get(self.url)
            sleep(3)

            input_element = driver.find_element(By.NAME, "txtTdPalvs")
            input_element.send_keys(keywords)

            submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Executa"]')
            submit_button.click()

            sleep(3)
            results = self._collect_data_per_page(driver)
        except Exception as ex:
            print("Erro durante a busca:", ex)
            print(traceback.format_exc())
        finally:
            driver.quit()
        return results

    def _collect_data_per_page(self, driver) -> list:
        registers = []
        while True:
            content = driver.find_elements(By.CLASS_NAME, "borda-superior")
            try:
                for c in content:
                    td = c.find_elements(By.CLASS_NAME, "small")
                    if 2 < len(td):
                        register = {
                            "Doc": td[0].find_element(By.TAG_NAME, "a").get_attribute("href"),
                            "Nº Processo": td[1].text,
                            "Data Autuação": td[2].text,
                            "Partes": [td[3].text, td[4].text],
                            "Matéria": td[5].text,
                            "URL": td[1].find_element(By.TAG_NAME, "a").get_attribute("href")
                        }
                        registers.append(register)

                next_page = driver.find_element(By.CLASS_NAME, "glyphicon-forward")
                next_page.click()
            except NoSuchElementException:
                print("Não há mais páginas disponíveis.")
                break
            except TimeoutException:
                print("Timeout ao carregar próxima página.")
            except Exception as ex:
                print("Erro durante a coleta de dados:", ex)
                print(traceback.format_exc())
                break
        return registers
