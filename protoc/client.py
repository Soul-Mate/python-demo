import socket
import struct
import msg_pb2


def echo_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    msg = msg_pb2.Msg()
    msg.user = "client"
    msg.text = "hello world"
    fmt = 'i' + str(msg.ByteSize()) + 's'
    data = struct.pack(fmt, msg.ByteSize(), msg.SerializeToString())
    client_socket.send(data)
    data = client_socket.recv(1024)
    # read message size
    size = int.from_bytes(data[:4], byteorder='little')

    # read message
    data = data[4:]
    recv_msg = msg_pb2.Msg()
    recv_msg.ParseFromString(data[:size])
    print("echo %s: \n\tname: %s\n\tmessage: %s\n" % (host + ":" + str(port), msg.user, msg.text))
    client_socket.close()


if __name__ == "__main__":
    echo_client(socket.gethostname(), 8080)
