from agent import Agent

def main():

    print("=== 手搓的第一个Agent Day4: 有记忆了 ===")
    print("命令：/clear 清除记忆 | quit 退出\n")
    
    agent=Agent()

    while True:
        user_input=input("你：").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit","exit"):
            print("Goodbye！")
            break
        if user_input.lower()=="/clear":
            agent.clear()
            print("记忆已清除，开始新对话。\n")
            continue
        result=agent.chat(user_input)
        print(f"Agent:{result}")
        print(f"（当前记忆：{agent.memory.count()} 条消息）\n")

if __name__=="__main__":
    main()