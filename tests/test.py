import os
import logging
import pytest
from dotenv import load_dotenv
import openai
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from src.tools.get_weather import GetWeatherTool


class TestChatGPTFunctionCalling:
    @pytest.fixture(autouse=True)
    def setup(self) -> ChatOpenAI:
        load_dotenv()
        openai_api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = openai_api_key  # APIキーの認証
        # 使用するモデルを定義
        return ChatOpenAI(model='gpt-3.5-turbo-0613', temperature=0)

    def test__get_current_weather(self, setup: ChatOpenAI):
        request = '東京の天気を教えてくれますか？'

        llm = setup
        # 使用するツールをリストとして定義
        tools = [GetWeatherTool()]
        # エージェントを初期化
        agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.OPENAI_FUNCTIONS,
            verbose=True)
        # 自然言語のリクエストを実行し、結果を出力
        response = agent.run(request)
        breakpoint()
        logging.debug(response)
