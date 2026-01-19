num = [1,2,3,4,5,4,3,2,1]
num [-1:]
num[::1]
print(num)

i = 0
t =3
for n in num:
    if ( n == t):
        print("found at index ",i)
        
    i +=1
else:
        print("not found")
for i in range (0,10,2):
  print(i ,  end=" ")
print()