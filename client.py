import zmq
import sys
import simplejson as json


def request(method,address,message):
	a=method.upper()
	if(a=='GET'):
		#print "here"
		return get(address,message)
	if(a=='POST'):
		return post(address,message)


def get(address,message):
	context = zmq.Context()
	sock = context.socket(zmq.REQ)
	sock.connect(address)
	sock.send(message)
	return sock.recv()


def post(address,message):
	context = zmq.Context()
	sock = context.socket(zmq.REQ)
	sock.connect(address)
	sock.send(message)
	return sock.recv()


print request('get','tcp://127.0.0.1:5678','hey man, first json !')


