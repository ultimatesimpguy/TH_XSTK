import itertools
list_M=['M'+str(i) for i in range(4)]
list_P=['P'+str(i) for i in range(3)]
list_C =['C'+str(i) for i in range(2)]
list_L=['L'+str(i) for i in range(1)]
U3_M=list(itertools.permutations(list_M))
U3_P=list(itertools.permutations(list_P))
U3_C=list(itertools.permutations(list_C))
U3_L=list(itertools.permutations(list_L))

def cross_join(A,B,C,D):
  return {(a,b,c,d) for a in A for b in B for c in C for d in D }

U3=list(cross_join(U3_M,U3_P,U3_C,U3_L))

for i in range(len(U3)):
  U3[i]=list(U3[i])
  U3[i]=list(itertools.chain(*U3[i]))
print(U3)

