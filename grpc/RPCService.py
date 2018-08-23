from . import todo_pb2_grpc


class TaskService(todo_pb2_grpc.TaskServiceServicer):
    def List(self, request, context):
        pass

    def Add(self, request, context):
        pass
    pass
    # python -m grpc_tools.protoc --proto_path=.  --python_out=. --grpc_python_out=. todo.proto
