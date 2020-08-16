import re
# st = 'saveChangesInTheEditor'
st = 'singleword'
pattern = re.compile(r'[A-Z]+')
mat = re.findall(pattern, st)
print(len(mat)+1)