import copy as cp
l1=[[10,20,30],[40,"sathya",60],[70,80,90]]
l2=cp.deepcopy(l1)
print(l1)
print(l2)
l1[1][1]=100
print(l1)
print(l2)