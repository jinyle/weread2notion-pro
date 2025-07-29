from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

def get_weread_token():
    # 配置无头浏览器
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://weread.qq.com")
        print("请扫码登录微信读书（等待 60 秒）...")
        time.sleep(60)  # 留出扫码登录时间
        
        # 获取所有 Cookie
        cookies = driver.get_cookies()
        token_data = {}
        
        # 提取关键 Token
        for cookie in cookies:
            if cookie['name'].startswith('wr_'):
                token_data[cookie['name']] = cookie['value']
        
        # 优先使用 wr_skey（新认证字段）
        if 'wr_skey' in token_data:
            return token_data['wr_skey']
        elif 'wr_vid' in token_data:
            return token_data['wr_vid']
        else:
            raise ValueError("未找到有效的 Token 字段")
    finally:
        driver.quit()

if __name__ == "__main__":
    token = get_weread_token()
    print(f"获取的 Token: {token}")
    with open('weread_token.json', 'w') as f:
        json.dump({"token": token}, f)
