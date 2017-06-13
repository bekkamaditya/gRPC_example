import app_pb2
import app_pb2_grpc
import grpc
import sys
import time

def getResponse( stub ):
    request = app_pb2.AppRequest()
    request.name = raw_input("Enter your name:")
    response = stub.GetResponse(request)
    print response.email

def getStreamedResponse( stub ):
    request = app_pb2.AppRequest()
    request.name = raw_input("Enter your name:")
    responses = stub.GetStreamedResponse(request)
    for response  in responses:
	print response.email

def getResponseIterator(stub): 
    print "Enter the list of names followed by a empty line: "
    while True:
	name = raw_input()
	if name == '' :
	    break
	request = app_pb2.AppRequest()
	request.name = name
	yield request

def getResponse1(stub):
    request_list = getResponseIterator(stub)
    response = stub.GetResponse1(request_list)
    print response 
        
def multipleExchange(stub):
    request_list = getResponseIterator(stub)    
    responses = stub.MultipleStream(request_list)
    for response  in responses:
	print response.email

def run():
    channel = grpc.insecure_channel('localhost: 50051') 
    stub = app_pb2_grpc.ApplicationStub(channel)
    getStreamedResponse( stub )  
    getResponse1(stub) 
    multipleExchange(stub)

if __name__ == '__main__' :
    run()
