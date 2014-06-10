import requests
s = requests.Session()
a = requests.adapters.ZMQAdapter()
s.mount('tcp://127.0.0.1:5678', a)
x = s.get('tcp://127.0.0.1:5678')
print x.content
