# 搜索自动化测试

Playwright + Pytest 实现简单的电影搜索功能的自动化测试，数据驱动，失败截图，集成 Allure 报告。

## 功能覆盖
 正常搜索
 空搜索
 特殊字符搜索

## 快速开始

bash
pip install -r requirements.txt
playwright install chromium
pytest tests/test_search.py --headed
## 生成测试报告
bash
pytest --alluredir=allure-results
allure serve allure-results

## 技术栈

Playwright
Pytest
Allure
YAML
Logging
