import grpc
import todo_pb2_grpc
import todo_pb2


def call_add():
    channel = grpc.insecure_channel("localhost:8001")
    stub = todo_pb2_grpc.TaskServiceStub(channel)
    task = todo_pb2.Task()
    task.done = False
    task.text = "hello world!"
    res = stub.Add(task)


def call_list():
    channel = grpc.insecure_channel("localhost:8001")
    stub = todo_pb2_grpc.TaskServiceStub(channel)
    res = stub.List(todo_pb2.Void())


if __name__ == "__main__":
    # call_add()
    call_list()
