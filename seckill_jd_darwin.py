import datetime
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_path = r"./chromedriver"
options = webdriver.ChromeOptions()  # 配置 chrome 启动属性
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
wait = WebDriverWait(driver, 10)  # 超时时长为10s


def login():
    driver.get("https://yushou.jd.com/member/qualificationList.action")
    print("1分钟后开抢!")
    time.sleep(60)


def buy(kill_time):
    i = 0
    item_url = driver.find_element_by_link_text('飞天 53%vol 500ml 贵州茅台酒（带杯）').get_attribute('href')
    add_times = 1
    while True:
        # 对比时间，时间到的话就点击结算
        if kill_time <= datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'):
            #  driver.refresh()  # 刷新页面
            driver.get(item_url)
            print("已尝试打开商品页!")

            while True:
                try:
                    while add_times > 0:
                        add = driver.find_element_by_css_selector('a.btn-add')
                        if add:
                            add.click()
                            print("商品数量+1")
                            add_times = add_times - 1

                    if driver.find_element_by_link_text('抢购'):
                        driver.find_element_by_link_text('抢购').click()
                        print("点击 抢购 1 次")
                        return
                except:
                    pass

                i += 1
                if i > 500:
                    print("已尝试 500 次,退出!")
                    return

if __name__ == "__main__":
    login()
    buy('2021-01-06 10:00:00')
