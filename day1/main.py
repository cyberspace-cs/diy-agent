from agent import run_agent
from action import execute_action

def main():

    print("=== 手搓的第一个Agent ===")
    print("输入 quit 退出\n")

    while True:
        user_input=input("请输入你的问题：").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit","exit"):
            print("Goodbye！")
            break
        text=run_agent(user_input)
        print(f"[AI回答]:{text}")
        out=execute_action(text)
        print(f"[AI执行]:{out}")

if __name__=="__main__":
    main()