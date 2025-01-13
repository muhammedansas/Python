import copy

a = [1, [2, 3]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)

print(shallow)
print(deep)