from itertools import permutations

def get_strike_and_ball(guess, answer):
    strike = sum([g == a for g, a in zip(guess, answer)])
    ball = len(set(guess) & set(answer)) - strike
    return strike, ball

# 입력
N = int(input())
questions = []
for _ in range(N):
    number, strike, ball = map(int, input().split())
    questions.append((str(number), strike, ball))

# 가능한 모든 세자리 수 후보 생성 (1~9 서로 다른 숫자)
candidates = [''.join(p) for p in permutations('123456789', 3)]

# 후보 검증
count = 0
for candidate in candidates:
    valid = True
    for q_num, q_strike, q_ball in questions:
        strike, ball = get_strike_and_ball(q_num, candidate)
        if strike != q_strike or ball != q_ball:
            valid = False
            break
    if valid:
        count += 1

print(count)
