import app_pb2 
import app_pb2_grpc
import grpc 
from concurrent import futures
import sys
import time

_ONE_DAY_IN_SECONDS = 24*60*60

def getResponse( request ):
    return app_pb2.AppResponse(email='{}@nutanix.com'.format(request.name)) 

class ApplicationServicer( app_pb2_grpc.ApplicationServicer ):
    def __init__(self):
        print "Server started"

    def GetResponse( self,request,context ):
        response = getResponse(request)
	return response

    def GetStreamedResponse(self, request, context):
	for i in range(10) :
	    yield app_pb2.AppResponse(email='{}-{}@nutanix.com'.format(request.name,i))		

    def GetResponse1( self,request_iterator,context):
	name = "" 
	for request in request_iterator	:
	    name = name + request.name + '-' 
	return app_pb2.AppResponse(email='{}@nutanix.com'.format(name)) 

    def MultipleStream(self,request_iterator,context):
	name = "" 
	for request in request_iterator	:
	    yield app_pb2.AppResponse(email='{}@nutanix.com'.format(request.name)) 
		


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    app_pb2_grpc.add_ApplicationServicer_to_server(ApplicationServicer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

