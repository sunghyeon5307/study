import time
import random

WORD_LIST = [
    "집갈래",
    "그만",
    "배고파",
    "집 보내줘"
]

random.shuffle(WORD_LIST)

# for i in enumerate(['A', 'B', 'C']):
#     print(i)

for i in WORD_LIST:
    start_time = time.time()
    user_input = str(input(i+'\n')).strip()
    end_time = time.time()-start_time

    correct = 0
    for index, c in enumerate(user_input):
        if index >= len(i):
            break
        if c == i[index]:
            correct += 1

    total_len = len(i)
    c = correct/total_len*100
    e = (total_len-correct)/total_len*100
    speed = correct / end_time *60

    print("속도 : {:0.2f} 정확도 : {:0.2f} 오타율 {:0.2f}".
    format(speed, c, e))