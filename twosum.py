def twosum(n , t):
   i = 0
   t= 5
   while i < len(n) :
    j = i+1
    while j < len(n):
        if n[i]+n[j] == t :
            return[i,j]
        j += 1
    i +=1
   return []
n=[1,2,3,4]
print( "found at index ",twosum(n,9))



          




