N = int(input())
cnt = 0
## 개 쓰레기코드 이딴식으로 짜면 암데도 취업 못함
if(N>=500):
  cnt += int(N/500)
  N = N-int(N/500)*500
  if(N>=100):
    cnt += int(N/100)
    N = N-int(N/100)*100
    if(N>=50):
      cnt += int(N/50)
      N = N-int(N/50)*50
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10
    else:
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10
  else:
    if(N>=50):
      cnt += int(N/50)
      N = N-int(N/50)*50
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10
    else:
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10
else:
  if(N>=100):
    cnt += int(N/100)
    N = N-int(N/100)*100
    if(N>=50):
      cnt += int(N/50)
      N = N-int(N/50)*50
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10
    else:
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10
  else:
    if(N>=50):
      cnt += int(N/50)
      N = N-int(N/50)*50
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10
    else:
      if(N>=10):
        cnt += int(N/10)
        N = N-int(N/10)*10

print(N, cnt)