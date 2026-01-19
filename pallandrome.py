l1 = [1,2,3,4,5,4,3,2,1]
left = 0
rightp = len(l1) -1
# l2 = l1.reverse()
# print(l1)
while left<=rightp: 
   if(l1[left]!=l1[rightp]):
       print("not palandrom")
       break
   left +=1
   rightp-=1
else:
       print("not")
# if(l1 == l2):
#     print("yes")
# else:
#     print("no")   
