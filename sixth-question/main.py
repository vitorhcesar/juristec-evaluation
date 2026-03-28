from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from datetime import datetime

class INMETScraper:
    driver: WebDriver
    url: str = "https://portal.inmet.gov.br/"

    def __init__(self):
        # Headless mode
        options = Options()
        options.add_argument("--headless")

        self.driver = WebDriver(options=options)
        self.driver.set_window_position(0, 0)

    def __open_browser(self):
        print("Abrindo navegador...")
        self.driver.get(self.url)
        self.driver.maximize_window()

    def __search_city(self, city: str, state: str):
        print("Procurando a cidade...")
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="search"]'))
        )
        search_input.click()
        sleep(1)
        search_input.send_keys(f"{city.strip()}")
        sleep(5)
        search_input.send_keys(Keys.ARROW_DOWN)
        search_input.send_keys(Keys.ENTER)

    def __get_current_hour(self) -> str:
        current_hour = datetime.now().strftime("%H:%M")
        return current_hour

    def __get_data(self):
        print("Coletando dados do INMET...")
        trend = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="previsao"]/div[1]/div[2]/div[2]/div[1]/b'))
        )

        humidity = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="previsao"]/div[1]/div[4]/div[2]/div/b'))
        )

        trend2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="previsao"]/div[1]/div[2]/div[3]/div[1]/b'))
        )

        humidity2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="previsao"]/div[1]/div[4]/div[3]/div/b'))
        )

        return {
            "current_hour": self.__get_current_hour(),
            "values": {
                "trend-1": (trend.text, humidity.text),
                "trend-2": (trend2.text, humidity2.text)
            }
        }
        
    

    def scrap_data(self, city: str, state: str) -> dict:
        self.__open_browser()
        self.__search_city(city, state)
        data = self.__get_data()
        return data


if __name__ == "__main__":
    city = input("Digite o nome da cidade (Se for vazio, padrão é 'Belo Horizonte'): ")
    if city == "":
        city = "Belo Horizonte"
    state = input("Digite a sigla do estado (Se for vazio, padrão é 'MG'): ")
    if state == "":
        state = "MG"

    print("")

    scraper = INMETScraper()
    data = scraper.scrap_data(city, state)
    print("")
    print("Dados coletados:")
    print(data)