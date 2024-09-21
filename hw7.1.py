# start

participants_number: int = 0
sum_number: int = 0
number: int = 0
maximum_tries: int = 10
while participants_number < maximum_tries:
    number = int(input('enter number:'))
    if number == -999:
        break
    if number < -1_000 or number > 1_000:
        print('illegal number, try again')
        continue
    participants_number += 1
    sum_number += number
else:
    print( )
for i in range(-1_000, 1_000 + 1):
    if i % 7 == 0:
        continue
    print(i, end="  ")

avg_number: float = sum_number / participants_number
print(f"total of {participants_number}, average = {avg_number:.2f}")
