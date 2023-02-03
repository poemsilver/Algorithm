# https://softeer.ai/practice/info.do?idx=1&eid=395&sw_prbl_sbms_sn=142606
import sys
from heapq import heappush,heappop

w,m = map(int,input().split(" "))
value = []
answer = 0
# m가지 보석의 무게당 가격 heapq에 넣기, 최대힙 구현
for _ in range(m):
    w2,c = map(int,input().split(" "))
    heappush(value,(-c,w2))

while value and w > 0:
    c, w2 = heappop(value)

    if w >= w2:
        answer += w2 * -c
        w -= w2
    else:
        answer += w * -c
        w = 0

print(answer)
