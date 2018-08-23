from . import todo_pb2_grpc


class TaskService(todo_pb2_grpc.TaskServiceServicer):
    pass
    # python -m grpc_tools.protoc --proto_path=.  --python_out=. --grpc_python_out=. todo.proto
