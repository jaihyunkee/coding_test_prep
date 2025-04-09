import heapq

def solution(jobs):
    jobs.sort()  # 요청 시점 기준 정렬
    heap = []
    time = 0
    idx = 0
    total = 0
    n = len(jobs)

    while idx < n or heap:
        # 현재 시간에 실행 가능한 작업들을 heap에 넣음
        while idx < n and jobs[idx][0] <= time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))  # (작업시간, 요청시간)
            idx += 1
        
        if heap:
            work_time, request_time = heapq.heappop(heap)
            time += work_time
            total += time - request_time  # 대기 시간 + 작업 시간
        else:
            # 실행 가능한 작업이 없으면, 시간 점프
            time = jobs[idx][0]
    
    return total // n  # 정수 나누기
