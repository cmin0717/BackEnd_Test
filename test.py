import hashlib

m = hashlib.sha256()
m.update('2y54rey'.encode('utf-8'))
print(type(m.hexdigest()))