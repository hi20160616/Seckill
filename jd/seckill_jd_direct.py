from datetime import datetime  # , timedelta
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Config
login_url = "javascript:login();"
watched_url = "https://item.jd.com/100012043978.html"
kill_sec = '2021-01-19 10:00:00'
chromedriver_path = r"./drivers/chromedriver"


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(
    executable_path=chromedriver_path, options=options, desired_capabilities=capa)
wait = WebDriverWait(driver, 10)  # 超时时长为10s
err_count = 3

def login():
    driver.get(watched_url)
    wait.until(
        EC.presence_of_element_located(
            (By.PARTIAL_LINK_TEXT, "登录"))
    ).click()
    print("登录！")
    print("1分钟后开始!")
    time.sleep(30)
    print("开始!")


def clickbtn():
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.btn-add"))
    ).click()
    print("数量 增加 1 次")
    wait.until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "抢购"))
    ).click()
    print("点击 抢购 1 次")


def buy(kill_time, err_count):
    if err_count == 0:
        return
    while True:
        # 对比时间，时间到的话就点击结算
        if kill_time <= datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]:
            #  time.sleep(0.101)
            #  driver.refresh()
            print("刷新!")
            try:
                clickbtn()
                return
            except Exception as ex:
                print(ex)
                err_count -= 1
                buy(kill_time, err_count)


if __name__ == "__main__":
    login()
    buy(kill_sec, err_count)
