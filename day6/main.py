from agent_loop import ReactAgent
from planner import make_plan, print_plan
from executor import execute_plan

def main():

    print("=== 手搓的第一个Agent Day6: 规划+执行 ===")
    print("命令：")
    print("  直接输入        → ReAct 对话模式")
    print("  /plan <任务>   → 规划并执行复杂任务")
    print("/clear 清除记忆 | quit 退出\n")
    
    agent=ReactAgent(max_steps=5)

    while True:
        user_input=input("你：").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit","exit"):
            print("Goodbye！")
            break
        if user_input.startswith("/plan"):
            task = user_input[6:].strip()
            if not task:
                print("用法：/plan 你的任务描述。")
                continue
            print("\n正在制定计划...")
            plan = make_plan(task)
            print_plan(plan)
            confirm = input("确认执行？(y/n):").strip().lower()
            if confirm == "y":
                result = execute_plan(plan)
                print(f"\nAgent：{result}\n")
            else:
                print("已取消执行。")
            continue
        if user_input.lower()=="/clear":
            agent.clear()
            print("记忆已清除，开始新对话。\n")
            continue

        # 普通React对话模式
        result=agent.run(user_input)
        print(f"\nAgent:{result}")
        

if __name__=="__main__":
    main()