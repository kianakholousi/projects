# frozen set
A = frozenset([1, 2, 3, 4])
B = frozenset({3, 4, 5, 6})
C = frozenset((5, 6, 7, 8))
# print(A,B,C)
D=frozenset()#empty frozenset
D=A.copy()
print(A.difference(B))
print(B.intersection(C))
print(A.symmetric_difference(C))
print(A.union(C))

print(A.isdisjoint(C)) 
print(C.issubset(B)) 
print(B.issuperset(C))