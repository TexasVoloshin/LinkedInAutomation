
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait




def openLinkedin(input_name) -> object:
    input_name = str(input_name)
    driver = webdriver.Chrome()
    driver.get('https://www.linkedin.com')
    driver.fullscreen_window()
    driver.implicitly_wait(30)
    email = driver.find_element(By.NAME,'session_key')
    driver.implicitly_wait(30)
    email.send_keys('email.com')
    driver.implicitly_wait(30)
    password = driver.find_element(By.NAME,'session_password')
    driver.implicitly_wait(30)
    password.send_keys('password')
    driver.implicitly_wait(30)
    driver.find_element(By.CLASS_NAME,'sign-in-form__submit-button').click()
    search = driver.find_element(By.XPATH,"//div/div/input[contains(@class,'search-global-typeahead__input always-show-placeholder')]")
    driver.implicitly_wait(30)
    search.send_keys(input_name,Keys.ENTER)
    WebDriverWait(driver, 1000)
    finding_result_xpath = "//div[contains(@class,'search-nec__hero-kcard-v2')]/div/div/div/span/span[1]/a[contains(@class,'app-aware-link')]"
    finding_result = driver.find_element(By.XPATH,finding_result_xpath).text
    print("finding_result " + finding_result)
    print("input_name " + input_name)
    desription = " nie znalziono opisu lub firma nie ma profilu na LinkedIn "
    try:
        finding_result == input_name

        driver.find_element(By.XPATH, finding_result_xpath).click()
        print(driver.current_url)
        desription = driver.find_element(By.XPATH,
                                       "//section/div/div/div[contains(@class,'t-14 t-black--light full-width break-words lt-line-clamp lt-line-clamp--multi-line ember-view')]").text
        print("opis istnieje")

    except TypeError:
        print("Nie znaleziono firmy na LinkedIn")
    else:
        input_name == finding_result
        driver.find_element(By.XPATH, finding_result_xpath).click()
        cur_link =driver.current_url
        desription = driver.find_element(By.XPATH,
                                         "//section/div/div/div[contains(@class,'t-14 t-black--light full-width break-words lt-line-clamp lt-line-clamp--multi-line ember-view')]").text
        print("opis istnieje")

    finally:
        return desription




def printDescription():

    try:
        with open("company.txt", "r") as input_file:
            with open("description.txt", "a") as output_file:
                for line in input_file.readlines():
                    try:
                        result = openLinkedin(line)
                        output_file.write(line + ";" + str(result) + "\n")
                        print("opis powinien być w pliku: " + result)

                    except:
                        print(line + " nie udało sie zapisac do pilku")
    except:
        print("nie udało sie otworzyć pliku")


    input_file.close()
    output_file.close()

printDescription()