from datetime import datetime, timedelta
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Key values
watched_url = "https://yushou.jd.com/member/qualificationList.action"
link_text = '飞天 53%vol 500ml 贵州茅台酒（带杯）'
#  good_url = "https://item.jd.com/100012043978.html"
kill_sec = '2021-01-08 10:00:00'
chromedriver_path = r"./drivers/chromedriver"
wait_login = 30

options = webdriver.ChromeOptions()  # 配置 chrome 启动属性
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# 懒加载模式变量准备，不等待页面加载完毕
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"  
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options, desired_capabilities=capa)
#  driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)


wait = WebDriverWait(driver, 10)  # 超时时长为10s
delay = timedelta.microseconds


def login():
    driver.get(watched_url)
    print("1分钟后开始!")
    time.sleep(wait_login)
    print("开始!")


def buy(kill_time):
    item_url = driver.find_element_by_link_text(
        link_text).get_attribute('href')
    while True:
        # 对比时间，时间到的话就点击结算
        if kill_time <= datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]:
            a = datetime.now()
            #  启动懒加载，driver.get() will not be blocked.
            driver.get(item_url)
            print("已尝试打开商品页!")

            try:
                wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "a.btn-add"))
                ).click()
                print("数量 增加 1 次")
                wait.until(
                    EC.presence_of_element_located(
                        (By.LINK_TEXT, "抢购"))
                        #  (By.LINK_TEXT, "开始预约"))
                ).click()
                print("点击 抢购 1 次")
                b = datetime.now()
                delay = (a-b).seconds
                print(f"Your net delay for {delay}ms!")
                return
            except Exception as ex:
                print(ex)
                driver.quit()
                return


if __name__ == "__main__":
    login()
    #  get_delay()
    buy(kill_sec)
    #  driver.quit()
