import time
import sys

def pomodoro_clock(total_minutes, work_minutes, break_minutes):
    total_seconds = total_minutes * 60
    work_seconds = work_minutes * 60
    break_seconds = break_minutes * 60
    cycles = total_seconds // (work_seconds + break_seconds)

    print("专注时钟开始！按 Ctrl+C 终止。")
    try:
        for i in range(cycles):
            print(f"第 {i+1} 个工作周期，专注工作 {work_minutes} 分钟")
            sys.stdout.flush()
            time.sleep(work_seconds)
            print(f"工作时间结束！休息 {break_minutes} 分钟")
            sys.stdout.flush()
            time.sleep(break_seconds)
        
        print("专注时钟结束！")
    except KeyboardInterrupt:
        print("专注时钟已终止！")

# 设置总时长为30分钟，每个工作周期为25分钟，休息时间为5分钟
pomodoro_clock(total_minutes=30, work_minutes=25, break_minutes=5)
