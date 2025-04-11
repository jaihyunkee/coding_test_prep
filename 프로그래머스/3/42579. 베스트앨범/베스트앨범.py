from collections import defaultdict
import heapq as pq
def solution(genres, plays):
    genre_to_song = defaultdict(list)
    genre_count = defaultdict(int)
    n = len(genres)
    
    for i in range(n):
        pq.heappush(genre_to_song[genres[i]], (-plays[i], i))
        genre_count[genres[i]] += plays[i]
        
    sort_genre = []
    for key in genre_count.keys():
        pq.heappush(sort_genre, (-genre_count[key], key))
    
    ans = []
    while sort_genre:
        _, genre = pq.heappop(sort_genre)
        for _ in range(2):
            if genre_to_song[genre]:
                song = pq.heappop(genre_to_song[genre])
                ans.append(song[1])
    return ans