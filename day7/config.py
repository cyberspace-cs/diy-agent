# config.py

import os
from pathlib import Path
from dotenv import load_dotenv

def load_config()->None:
    """加载配置文件，检查必要项是否存在。"""
    env_path=Path(__file__).parent/".env"

    if not env_path.exists():
        env_path=Path(__file__).parent.parent/"/.env"
    
    load_dotenv(dotenv_path=env_path)

    if not os.environ.get("OPENAI_API_KEY"):
        raise EnvironmentError(
            "\n错误：缺少OPENAI_API_KEY环境变量\n\n"
            "解决方法:\n"
            "1.复制.env.example文件并重命名为.env(cp .env.example .env)\n"
            "2.在.env文件中填写OPENAI_API_KEY和OPENAI_BASE_URL\n"
            "3.重新运行\n"
        )

def get_model()->str:
    return os.environ.get("OPENAI_MODE","deepseek")

def get_base_url()->str:
    return os.environ.get("OPENAI_BASE_URL","https://api.deepseek.com")