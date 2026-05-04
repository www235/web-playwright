import pytest
import yaml
from playwright.sync_api import Page
from utils.logger import logger

def load_search_data():
    with open("data.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data["search_keywords"]

@pytest.mark.parametrize("case", load_search_data(), ids=lambda x: x["name"])
def test_search_movie(page: Page, case):
    keyword = case["keyword"]
    logger.info(f"========== 开始测试：关键词 = '{keyword}' ==========")

    logger.info("打开豆瓣电影首页")
    page.goto("https://movie.douban.com/")

    logger.info(f"在搜索框输入: {keyword}")
    page.fill("input[name='search_text']", keyword)

    logger.info("点击搜索按钮")
    page.click("input[type='submit']")

    logger.info("等待搜索结果出现")
    page.wait_for_selector("text=找到约")

    if keyword == "" or keyword == "@#$%":
        logger.info("执行断言：标题应包含 '豆瓣'")
        assert "错误" in page.title()
        logger.info("断言通过")
    else:
        logger.info(f"执行断言：标题应包含 '{keyword}'")
        assert keyword in page.title()
        logger.info("断言通过")

