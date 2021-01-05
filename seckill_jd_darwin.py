import datetime
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_path = r"./chromedriver"
options = webdriver.ChromeOptions()  # 配置 chrome 启动属性
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
wait = WebDriverWait(browser, 10)  # 超时时长为10s


def login():
    browser.get("https://yushou.jd.com/member/qualificationList.action")
    print("1分钟后开抢!")
    time.sleep(60)

def buy(kill_time):
    i = 0
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now >= kill_time:
            browser.refresh()  # 刷新页面
            while True:
                try:
                    #  if browser.find_element_by_id("J_Go"):
                    #      browser.find_element_by_id("J_Go").click()
                    #      print("结算成功，准备提交订单")
                    # 点击提交订单按钮
                    if browser.find_element_by_link_text('抢购'):
                        browser.find_element_by_link_text('抢购').click()
                        print("抢购成功，请尽快付款")
                        return
                    if browser.find_element_by_link_text('立即抢购'):
                        browser.find_element_by_link_text('立即抢购').click()
                        print("抢购成功，请尽快付款")
                        return
                except:
                    #  print("browser error occur!")
                    pass
                i += 1
                #  print("再次尝试")
                if i > 500:
                    print("已尝试 500 次,退出!")
                    return
            #  else:
            #      time.sleep(0.01)


if __name__ == "__main__":
    login()
    buy('2021-01-06 00:00:00')
