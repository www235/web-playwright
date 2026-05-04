
import pytest
import os
from playwright.sync_api import sync_playwright
from utils.logger import logger


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # headless=False 让浏览器可见
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # 只在测试调用阶段失败时处理
    if rep.when == "call" and rep.failed:
        # 获取测试用例中的 page fixture
        page = getattr(item, "_page", None)
        if page is None and "page" in item.funcargs:
            page = item.funcargs["page"]
            item._page = page
        if page:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}_{rep.when}.png"
            page.screenshot(path=screenshot_path)
            logger.error(f"测试失败，截图保存至: {screenshot_path}")


