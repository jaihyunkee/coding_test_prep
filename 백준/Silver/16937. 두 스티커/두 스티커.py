from itertools import combinations

H, W = map(int, input().split())
N = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(N)]

max_size = 0

for comb in combinations(stickers, 2):
    sticker1, sticker2 = comb
    # 스티커1 회전: (h1, w1), (w1, h1)
    s1_variants = [sticker1, (sticker1[1], sticker1[0])]
    # 스티커2 회전: (h2, w2), (w2, h2)
    s2_variants = [sticker2, (sticker2[1], sticker2[0])]

    for s1 in s1_variants:
        for s2 in s2_variants:
            h1, w1 = s1
            h2, w2 = s2
            # 수평 배치
            if max(h1, h2) <= H and w1 + w2 <= W:
                max_size = max(max_size, h1 * w1 + h2 * w2)
            # 수직 배치
            if max(w1, w2) <= W and h1 + h2 <= H:
                max_size = max(max_size, h1 * w1 + h2 * w2)

print(max_size)