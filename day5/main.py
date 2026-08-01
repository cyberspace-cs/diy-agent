from agent_loop import ReactAgent

def main():

    print("=== 手搓的第一个Agent Day5: React ===")
    print("命令：/clear 清除记忆 | quit 退出\n")
    
    agent=ReactAgent()

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
        result=agent.run(user_input)
        print(f"Agent:{result}")
        

if __name__=="__main__":
    main()