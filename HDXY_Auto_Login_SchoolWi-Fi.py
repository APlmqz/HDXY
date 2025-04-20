#   UFT -8
#   HDXY Auto Login School Wi-Fi    哈尔滨华德学院自动登录校园网
#   version 0.1.1 Beta Art
#   Writing time 2025-4-19
#   嘉兴村长 JiaXing(APlmqz)

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



 # 报错字设置 红色背景 白色字体 加粗
Error_Font_Settings = "\033[1;37;41m" # {Error_Font_Settings}
Normal_Font_Settings ="\033[1;37;44m" # {Normal_Font_Settings}
Reset = "\033[0m"               # {Reset}


def  Art_Print_One():
    print("           __                    __");             # 0
    print("           \\ \\                  / /");           # 1
    print("             \\ \\              / /");             # 2
    print("               \\ \\          / /");               # 3
    print("     ____________\\ \\______/ /______________");   # 4
    print("   /               \\ \\  / /               /|");  # 5
    print("  /_____________________________________ / |");    # 6
    print(" |  _________________________________   |  |");    # 7
    print(" | /                                 \\  |  |");   # 8
    print(" | |   HDXY Auto Login School Wi-Fi  |  |  |");    # 9
    print(" | |                                 |  |  |");    # 10
    print(" | |                                 |  |  |");    # 11
    print(" | |                                 |  |  |");    # 12
    print(" | \\_________________________________/  |  /");   # 13
    print(" | <____________________________ . . >  | /");     # 14
    print(" |______________________________________|/");      # 15

def  Art_Print_Two():
    print("           __                    __");             # 0
    print("           \\ \\                  / /");           # 1
    print("             \\ \\              / /");             # 2
    print("               \\ \\          / /");               # 3
    print("     ____________\\ \\______/ /______________");   # 4
    print("   /               \\ \\  / /               /|");  # 5
    print("  /_____________________________________ / |");    # 6
    print(" |  _________________________________   |  |");    # 7
    print(" | /                                 \\  |  |");   # 8
    print(" | |   HDXY Auto Login School Wi-Fi  |  |  |");    # 9
    print(" | |                                 |  |  |");    # 10
    print(" | |             Wait . . .          |  |  |");    # 11
    print(" | |                                 |  |  |");    # 12
    print(" | \\_________________________________/  |  /");   # 13
    print(" | <____________________________ . . >  | /");     # 14
    print(" |______________________________________|/");      # 15

def  Art_Print_Success():
    print("           __                    __");             # 0
    print("           \\ \\                  / /");           # 1
    print("             \\ \\              / /");             # 2
    print("               \\ \\          / /");               # 3
    print("     ____________\\ \\______/ /______________");   # 4
    print("   /               \\ \\  / /               /|");  # 5
    print("  /_____________________________________ / |");    # 6
    print(" |  _________________________________   |  |");    # 7
    print(" | /                                 \\  |  |");   # 8
    print(" | |   HDXY Auto Login School Wi-Fi  |  |  |");    # 9
    print(" | |                                 |  |  |");    # 10
    print(f" | |       {Normal_Font_Settings}✓{Reset}  Login successful!      |  |  |");    # 11
    print(" | |                                 |  |  |");    # 12
    print(" | \\_________________________________/  |  /");   # 13
    print(" | <____________________________ . . >  | /");     # 14
    print(" |______________________________________|/");      # 15


def  Art_Print_Failed():
    print("           __                    __");             # 0
    print("           \\ \\                  / /");           # 1
    print("             \\ \\              / /");             # 2
    print("               \\ \\          / /");               # 3
    print("     ____________\\ \\______/ /______________");   # 4
    print("   /               \\ \\  / /               /|");  # 5
    print("  /_____________________________________ / |");    # 6
    print(" |  _________________________________   |  |");    # 7
    print(" | /                                 \\  |  |");   # 8
    print(" | |   HDXY Auto Login School Wi-Fi  |  |  |");    # 9
    print(" | |                                 |  |  |");    # 10
    print(f" | |         {Error_Font_Settings}✗{Reset} Login failed!         |  |  |");    # 11
    print(" | |                                 |  |  |");    # 12
    print(" | \\_________________________________/  |  /");   # 13
    print(" | <____________________________ . . >  | /");     # 14
    print(" |______________________________________|/");      # 15


def  Art_Print_Over():
    print("           __                    __");             # 0
    print("           \\ \\                  / /");           # 1
    print("             \\ \\              / /");             # 2
    print("               \\ \\          / /");               # 3
    print("     ____________\\ \\______/ /______________");   # 4
    print("   /               \\ \\  / /               /|");  # 5
    print("  /_____________________________________ / |");    # 6
    print(" |  _________________________________   |  |");    # 7
    print(" | /                                 \\  |  |");   # 8
    print(" | |                                 |  |  |");    # 9
    print(" | |      === Program  Over ===      |  |  |");    # 10
    print(" | |                                 |  |  |");    # 11
    print(" | |                                 |  |  |");    # 12
    print(" | \\_________________________________/  |  /");   # 13
    print(" | <____________________________ . . >  | /");     # 14
    print(" |______________________________________|/");      # 15
 # 清屏函数
def clear_screen():
    """清空终端屏幕（兼容 Windows/Linux/macOS）"""
    os.system('cls' if os.name == 'nt' else 'clear')

def ReadSetting():
    """
    读取用户名、地址和密码
    :return: 用户名、地址和密码的元组
    """
    path = os.getcwd()# 获取当前脚本所在的目录
    setting_file = os.path.join(path, "Setting.txt")
    settings = {}
    try:
        with open(setting_file, 'r', encoding='utf-8') as file:
            for line in file:
                if "Username=" in line:
                    settings['Username'] = line[len("Username="):].strip()# 去除行首和行尾的空白字符
                if "Adress=" in line:
                    settings['Adress'] = line[len("Adress="):].strip()
                if "Password=" in line:
                    settings['Password'] = line[len("Password="):].strip()
    except FileNotFoundError:
        print(f"{Error_Font_Settings}文件{Reset} {setting_file} {Error_Font_Settings}未找到捏_(:з」∠)_{Reset}")
    except Exception as e:
        print(f"{Error_Font_Settings}读取文件时出错撸 7^7 :{Reset} {e}")
    return settings.get('Username', ''), settings.get('Adress', ''), settings.get('Password', '')

def AutoOption(driver, Username, Password):
    """
    自动填写用户名和密码并进行登录操作
    :param driver: WebDriver 实例
    :param Username: 用户名
    :param Password: 密码
    """
    try:
        # 等待用户名输入框加载
        inputUsername = WebDriverWait(driver, 30).until(  #等待用户元素加载，最多等待30秒
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))  #定位用户名输入框的XPATH路径
        )
        
        inputUsername.send_keys(Username + Keys.RETURN )

        # 定位密码输入框
        pwd = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        pwd.send_keys(Password + Keys.RETURN)# 模拟回车键敲击
        
        # 添加登录成功检查（通过注销按钮判断）
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="logout"]'))#//*[@id="logout"]根据注销的XPATH路径来判断是否登录成功
            )
            return True
        except:
            return False

    except Exception as e:
        print(f"{Error_Font_Settings}操作出错了捏 o(╥﹏╥)o:{Reset} \n{e}")
        driver.save_screenshot('error.png')# 保存错误截图

def Load(Username, Adress, Password):
    """
    加载网页并执行自动登录操作
    :param Username: 用户名
    :param Adress: 地址
    :param Password: 密码
    """

    option = webdriver.EdgeOptions() # 创建EdgeOptions实例

    option.add_experimental_option('excludeSwitches', ['enable-logging'])  # 隐藏驱动日志

    option.add_experimental_option("detach", True)# 保持浏览器窗口打开
    option.use_chromium = True  # 使用Chromium内核
    option.add_argument("--disable-extensions") # 禁用扩展
    #option.add_argument("--headless")  # 无头模式，不显示浏览器窗口


    # 直接使用默认值（大多数1080p屏幕适用）较快
    option.add_argument("window-position=500,300")
    option.add_argument("window-size=800,600")



#居中显示慢一点
# ###################################################################################################
#     #在创建driver前先计算好窗口位置和大小
#     try:
#         # 使用虚拟屏幕尺寸计算位置，避免闪动
#         screen_width = 1920  # 默认值，实际会被覆盖
#         screen_height = 1080  # 默认值，实际会被覆盖
        
#         # 临时创建一个隐藏的driver来获取真实屏幕尺寸
#         temp_option = webdriver.EdgeOptions()
#         temp_option.add_argument("headless")
#         temp_driver = webdriver.Edge(options=temp_option)
#         screen_width = temp_driver.execute_script("return window.screen.width;")
#         screen_height = temp_driver.execute_script("return window.screen.height;")
#         temp_driver.quit()
        
#         # 计算窗口位置和大小 (1/4窗口居中显示)
#         window_width = screen_width // 2
#         window_height = screen_height // 2
#         window_x = (screen_width - window_width) // 2
#         window_y = (screen_height - window_height) // 2
        
#         # 设置初始窗口位置和大小
#         option.add_argument(f"window-position={window_x},{window_y}")
#         option.add_argument(f"window-size={window_width},{window_height}")
        
#     except Exception as e:
#         print(f"{Error_Font_Settings}获取屏幕尺寸出错了捏 o(╥﹏╥)o ，使用默认值:{Reset} {e}")
#         # 使用默认居中位置
#         option.add_argument("window-position=500,300")
#         option.add_argument("window-size=800,600")

# ###################################################################################################

# 创建无日志服务
    service = webdriver.EdgeService(
        log_path=os.devnull,    # 日志重定向到黑洞
        service_args=["--verbose=0", "--append-log"]  # 静默模式
    )

    driver = webdriver.Edge(options=option, service=service)# 启动 Microsoft Edge 浏览器
    clear_screen()# 清屏
    Art_Print_One()
    time.sleep(2)
    clear_screen()
    Art_Print_Two()

    try:
        driver.set_page_load_timeout(60)
        driver.get(Adress)
        # 等待页面加载完成
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))  # 等待用户名输入框出现
        )
        # 获取登录结果并立即显示
        if AutoOption(driver, Username, Password):
            clear_screen()
            Art_Print_Success()
        else:
            clear_screen()
            Art_Print_Failed()

        # driver.minimize_window()  # 最小化窗口
        time.sleep(1)   # 等待1秒
        driver.quit()  # 关闭浏览器窗口
        return  # 直接返回，不执行后续代码

    except Exception as e:
        print(f"{Error_Font_Settings}页面加载出错了捏 o(╥﹏╥)o : {Reset}{e}")
    finally:
        driver.quit()

def top():
    """
    主函数，读取设置并启动加载过程
    """
    # time.sleep(1)
    Username, Adress, Password = ReadSetting()
    if Username and Adress and Password:
        # print(f"{Normal_Font_Settings}=== 正在尝试登录... ==={Reset}\n")
        Load(Username, Adress, Password)
        clear_screen()
        Art_Print_Over()
    else:
        print(f"{Error_Font_Settings}没得找到有效的用户名、地址或密码{Reset}")

if __name__ == "__main__":
    top()
