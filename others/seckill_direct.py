from datetime import datetime  # , timedelta
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Config
login_url = "http://yey.tianshancloud.org:9112/ch_Children/list.jspx"
watched_url = "http://yey.tianshancloud.org:9112/ch_Children/list.jspx"
kill_sec = '2021-01-21 10:00:00'
chromedriver_path = r"./drivers/chromedriver"


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation'])
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(
    executable_path=chromedriver_path, options=options, desired_capabilities=capa)
wait = WebDriverWait(driver, 10)  # 超时时长为10s
err_count = 30

def login():
    driver.get(watched_url)
    print("登录！")
    print("1分钟后开始!")
    time.sleep(60)
    print("开始!")


def clickbtn():
    wait.until(
        EC.presence_of_element_located(
            (By.ID, "bm_5"))
    ).click()
    print("报名1次")


def do(kill_time, err_count):
    if err_count == 0:
        return
    while True:
        # 对比时间，时间到的话就点击
        if kill_time <= datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]:
            #  time.sleep(0.101)
            #  driver.refresh()
            #  print("刷新!")
            try:
                clickbtn()
                return
            except Exception as ex:
                print(ex)
                err_count -= 1
                do(kill_time, err_count)


if __name__ == "__main__":
    login()
    do(kill_sec, err_count)
