import argparse
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from tools.open_weather import GetCurrentWeatherTool


def setup():
    load_dotenv()


def run(prompt: str):
    # 使用するモデルを定義
    llm = ChatOpenAI(model='gpt-3.5-turbo-0613', temperature=0)
    # 使用するツールをリストとして定義
    tools = [GetCurrentWeatherTool()]
    # エージェントを初期化
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True)
    # 自然言語のリクエストを実行し、結果を出力
    response = agent.run(prompt)
    print(response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, default='東京の天気を教えてくれますか？')
    args = parser.parse_args()
    setup()
    run(prompt=args.prompt)
