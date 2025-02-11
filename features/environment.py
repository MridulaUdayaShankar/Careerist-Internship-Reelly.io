from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from support.logger import logger
from app.application import Application
from selenium.webdriver.firefox.service import Service as FirefoxService

#Google Chrome Setting
from selenium.webdriver.chrome.options import Options

#firefox setting
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

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
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


    # Mobile testing
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    # mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = Options()
    # chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)


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
    context.driver.quit()
