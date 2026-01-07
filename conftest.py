import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-save-password-bubble")
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield
    driver.quit()


# 🔥 SCREENSHOT ON FAILURE
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.cls.driver

        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)

        screenshot_name = (
            report.nodeid.replace("::", "_")
            .replace("/", "_")
            .replace("\\", "_")
            + ".png"
        )

        screenshot_path = os.path.join(reports_dir, screenshot_name)
        driver.save_screenshot(screenshot_path)

        if pytest_html:
            html = f"""
            <div>
                <img src="{screenshot_path}"
                     alt="screenshot"
                     style="width:400px;height:250px;"
                     onclick="window.open(this.src)"
                     align="right"/>
            </div>
            """
            extra.append(pytest_html.extras.html(html))

        report.extra = extra
