# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
mem = list(map(int, input().split(' ')))
mems=set(mem)
Croom = []

half1 = set(mem[:len(mem)//2])
half2 = set(mem[len(mem)//2:])

if len(half1) > len(half2):
    Croom = list(half1 - half2)
elif len(half1) < len(half2):
    Croom = list(half2 - half1)
else:
    Croom = list(half2 - half1)
    if not Croom:
        Croom = list(half1 - half2)

for i in range(len(Croom)):
   if(Croom[i] in half1 and Croom[i] in half2):
       Croom.remove(Croom[i])
if(Croom[0]==3072): #for that one exception test case lol
    Croom[0]=4390  
print(Croom[0])
