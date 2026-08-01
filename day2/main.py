from agent import run_agent

def main():

    print("=== 手搓的第一个Agent Day2 ===")
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

if __name__=="__main__":
    main()