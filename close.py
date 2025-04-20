from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC

# 设置 Edge 浏览器驱动
options = Options()
options.add_argument("window-position=500,300")
options.add_argument("window-size=800,800")
# options.add_argument("--headless")  # 无头模式，不显示浏览器窗口
driver = webdriver.Edge(options=options)  # 使用 Edge 浏览器

try:
    # 打开网页
    url = "http://172.200.200.200/srun_portal_success?ac_id=1&theme=pro"
    driver.get(url)
    
    # 等待页面加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="logout"]'))
    )
    
    # 尝试找到注销按钮并点击（使用 XPath 定位）
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logout"]'))
    )
    # 点击注销按钮
    logout_button.click()

    # 尝试找到确定注销按钮并点击（使用 XPath 定位）
    confirm_logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/button[1]'))
    )
    # 点击确定注销
    confirm_logout_button.click()
    print("注销按钮已点击")
    
except Exception as e:
    print(f"发生错误: {e}")
    
finally:
    # 关闭浏览器
    driver.quit()