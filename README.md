# Seckill

This code only match for 1111 in 2020 taobao, I'll tidy up the project by free or in need on myself.

This code just pass test on MacOS 14. Windows and Linux guys should test it before.

Enjoy it! Good luck!

---

## Usage

- Mac OS: `python3 ./seckill_darwin.py`
- Windows: `py .\seckill_windows.py`
- Linux: `python3 ./seckill_linux.py`

---

## Steps

1. Python3
2. Selenium
3. ChromeDriver

> If your Chrome version equal to `86.0.4240.111`, just use these bin files I provide.

### Install Selenium
```python
pip3 install selenium --user
```

### Install ChromeDriver

> Reference: https://www.jianshu.com/p/39716ea15d99


#### 1. download driver

[This is the official ChromeDriver download address.](https://chromedriver.storage.googleapis.com/index.html)

[Taobao mirror of chromedriver](http://npm.taobao.org/mirrors/chromedriver/)

Check out the version of Chrome, view `chrome://settings/help` by your Chrome

Use The ChromeDriver download link to find the Chrome version and download it based on your computer’s platform type.

Download zip packages:

```
wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_mac64.zip
```

#### 2. setup it

Once the download is complete, UNZIP IT and place it in the **Scripts** folder under the Python installation path, or copy driver file to `/usr/bin` on MacOS.

Windows: `<your python root folder>\\Scripts`  
Mac OS: `/usr/bin`

**Notice:**  On mac, it can't copy anything to the folder, so, copy it to any place your python can invoke it.

### Modify Python Code

Last line: `buy('2020-11-01 00:00:00')`

modify it for you need.


EOF
