import logging
import os
from datetime import datetime

# 确保 logs 目录存在
os.makedirs("logs", exist_ok=True)


def setup_logger():
    """配置并返回 logger 实例"""
    logger = logging.getLogger("douban_test")
    logger.setLevel(logging.INFO)

    # 避免重复添加 handler（防止多次初始化导致重复日志）
    if logger.hasHandlers():
        return logger

    # 文件处理器：写入 logs/test.log
    file_handler = logging.FileHandler(
        f"logs/test_{datetime.now().strftime('%Y%m%d')}.log",
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # 控制台处理器：实时输出
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 全局 logger 实例
logger = setup_logger()