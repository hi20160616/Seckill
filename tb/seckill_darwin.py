import datetime
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_path = r"../drivers/chromedriver"
options = webdriver.ChromeOptions()  # 配置 chrome 启动属性
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
wait = WebDriverWait(browser, 10)  # 超时时长为10s


def login():
    browser.get("https://cart.taobao.com/cart.htm")
    print("请手动勾选需要购买的商品, 1分钟后开抢!")
    time.sleep(60)

def buy(kill_time):
    i = 0
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= kill_time:
            while True:
                try:
                    # 点击结算按钮
                    if browser.find_element_by_id("J_Go"):
                        browser.find_element_by_id("J_Go").click()
                        print("结算成功，准备提交订单")
                    # 点击提交订单按钮
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        print("抢购成功，请尽快付款")
                        return
                except:
                    #  print("browser error occur!")
                    pass
                i += 1
                print("再次尝试")
                if i > 10:
                    print("已尝试 10 次,退出!")
                    return
        #  else:
        #      time.sleep(0.01)


if __name__ == "__main__":
    login()
    buy('2020-11-11 00:00:00')
