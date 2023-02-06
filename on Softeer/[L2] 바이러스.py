# https://softeer.ai/practice/info.do?idx=1&eid=407&sw_prbl_sbms_sn=143746
import sys

k,p,n = map(int,sys.stdin.readline().split(' '))
answer = k
#k가 1초당 p배씩 n초 증가한다
for _ in range(n):
    answer = (answer*p)%1000000007

print(answer)
