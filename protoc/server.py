import socket
import msg_pb2
import struct


def echo_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8080
    server_socket.bind((host, port))
    print("server start: %s:%d" % (host, port))
    server_socket.listen(128)
    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024)
        # read message size
        size = int.from_bytes(data[:4], byteorder='little')

        # read message
        data = data[4:]
        msg = msg_pb2.Msg()
        msg.ParseFromString(data[:size])
        print("echo %s: \n\tname: %s\n\tmessage: %s\n" % (addr, msg.user, msg.text))
        data = struct.pack('i' + str(size) + 's', size, msg.SerializeToString())
        client_socket.send(data)
        client_socket.close()


if __name__ == "__main__":
    echo_server()
