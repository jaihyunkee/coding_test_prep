from itertools import combinations
from collections import Counter

word = input()
n = int(input())
book_price = {}
books = []
for _ in range(n):
    price, name = input().split()
    book_price[name] = int(price)
    books.append(name)

word_counter = Counter(word)
ans = float('inf')

for i in range(1, n+1):
    for comb in combinations(books, i):
        total_letters = Counter()
        total_price = 0
        for book in comb:
            total_letters += Counter(book)
            total_price += book_price[book]
        if all(total_letters[c] >= word_counter[c] for c in word_counter):
            ans = min(ans, total_price)

print(ans if ans != float('inf') else -1)
