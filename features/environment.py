from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from support.logger import logger
from app.application import Application

# Sauce labs
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Google Chrome Setting
from selenium.webdriver.chrome.options import Options

#Firefox setting
from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """
    #Google Chrome
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    #Firefox
    # driver_path = GeckoDriverManager().install()
    # driver_path = webdriver.FirefoxService()
    # service = FirefoxService(driver_path)
    # firefox_options = Options()
    # context.driver = webdriver.Firefox(service=service, options=firefox_options)

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###

    # bs_user = 'mridulaudayashan_SE249K'
    # bs_key = '6dNpk8ycqcGC4nFQaozC'
    # url = f'https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'edge',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    ###################################################
    # Mobile testing
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    #     "clientHints": {"platform": "Android", "mobile": True}}
    #
    # chrome_options = Options()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(options=chrome_options)

    # # context.driver.get("https://www.saucedemo.com")
    # # options = ChromeOptions()
    # # options.browser_version = 'latest'
    # # options.platform_name = 'Windows 11'
    # # sauce_options = {'username': 'oauth-mridu.sh92-3be5f', 'accessKey': 'f1bfb67e-2c8b-477a-8bd2-6c9b92e0aae5',
    # #                  'build': 'selenium-build-DZK8U', 'name': 'Reelly.io'}
    # # options.set_capability('sauce:options', sauce_options)
    # #
    # # url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')

def after_scenario(context, feature):
    browser_logs = context.driver.get_log('browser')
    with open("browser_logs.txt", "w") as log_file:
        for log_entry in browser_logs:
            log_file.write(f"{log_entry['level']} - {log_entry['timestamp']} - {log_entry['message']}\n")
    print("Browser logs have been saved to browser_logs.txt")

    # title = context.driver.title
    # title_is_correct = "Swag Labs" in title
    # job_status = "passed" if title_is_correct else "failed"
    #
    # context.driver.execute_script("sauce:job-result=" + job_status)
    context.driver.quit()
