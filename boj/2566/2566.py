#L=[]
Max = -1 
x=0
y=0

for i in range(9):
    num=list(map(int, input().split()))
    #L.append(num)
    for j in range(9):
        if num[j] > Max:
            Max = num[j]
            x = i + 1
            y = j + 1
   
print(Max)
print(f"{x} {y}")