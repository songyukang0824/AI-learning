import random

answer = random.randint(1, 10)
attempts = 0

print("🎯 猜数字游戏开始！（1-10）")

while True:
    guess = int(input("请输入你的猜测："))
    attempts += 1

    if guess > answer:
        print("📈 太大了")
    elif guess < answer:
        print("📉 太小了")
    else:
        print(f"🎉 猜对了！你用了 {attempts} 次")
        break
