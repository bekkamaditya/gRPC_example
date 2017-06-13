# gRPC_example

Compiling the .proto file to generate the python code:
python -m grpc_tools.protoc -I=$DIR --python_out=/target/dir --grpc_python_out=/target/dir $DIR/app.proto
  
Running server:
python server.py
  
Go to another terminal and connect to the server:
python client.py
