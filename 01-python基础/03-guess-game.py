import random

num = random.randint(1, 10)

attempts = 5
score = 0

print("🎮 猜数字 + 分数系统开始！")
print("规则：猜对 +10分，猜错 -2分，最多5次")

while attempts > 0:
    print(f"\n你还有 {attempts} 次机会")
    guess = int(input("请输入数字（1-10）："))

    if guess == num:
        print("🎉 猜对了！+10分")
        score += 10
        break
    elif guess > num:
        print("📉 太大了 -2分")
        score -= 2
    else:
        print("📈 太小了 -2分")
        score -= 2

    attempts -= 1

if attempts == 0 and guess != num:
    print(f"\n❌ 游戏结束，正确答案是 {num}")

print(f"\n🏁 最终得分：{score}")
