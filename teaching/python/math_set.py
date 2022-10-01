# math set
A={5,2,26,4,65,92,41,86}
B={2,4,23,45,5,3}
print(A.union(B))#AUB
print(A|B)
print(A.intersection(B))#A∩B
print(A & B)
print(A.difference(B))#A-B
print(A-B)
print(B.difference(A))#B-A
print(B-A)
print(A.symmetric_difference(B))#AΔB=(A∪B)-(A∩B)=(A-B)U(B-A)
print(A ^ B)
print(B.issubset(A))#B⊆A
print(A.issuperset(B))#A⊃B
C={1,2,3,4,5,6,7,8,9}
D={2,4,6,8,}
print(D.issubset(C))#D⊆C
print(C.issuperset(D))#C⊃D
# ===================================