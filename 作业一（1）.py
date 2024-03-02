a,b,c,d=map(int,input().split())
m1=(c-a)*60+(d-b)
h=m1//60
m=m1%60
hour=str(int((h)))
min=str(m)
print(hour,':',min)