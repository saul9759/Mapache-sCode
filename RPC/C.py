import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://192.168.100.85:8000', verbose=True)

print("add:")
print(s.add(5, 2))
print("sus:")
print(s.sus(5, 2))
print("mul:")
print(s.mul(5, 2))
print("div:")
print(s.div(5, 2))
