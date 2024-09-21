# start

world_record: float = 6.23
score: float = 0
participants: int = 7
sum_score: float = 0
for _ in range(7):
    while True:
        score = float(input('enter the athlete recent score:'))
        if 5.79 < score:
            break
        if score > 6.23:
            print('congratulations you have broken the WR!')
            participants += 1
            sum_score += score
        continue
    else:
        print("good score")
avg_score: float = score / participants
print(f"total of {participants}, average is: {avg_score:.2f}")
