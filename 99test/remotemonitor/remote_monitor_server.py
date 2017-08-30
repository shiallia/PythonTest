from socketserver import ThreadingTCPServer, StreamRequestHandler
import logging
import traceback


class MyStreamRequestHandler(StreamRequestHandler):
    def handle(self):
        try:
            data = self.rfile.readline().strip().decode(encoding="utf-8")
            print(f"receive from {self.client_address}:{data}")
            #data = data.encode(encoding='utf-8')
            #self.wfile.write(data)
        except Exception as e:
            traceback.print_exc()



if __name__ == "__main__":
    host = "127.0.0.1"  # 主机名，可以是ip,像localhost的主机名,或""
    port = 9999  # 端口
    addr = (host, port)

    # ThreadingTCPServer从ThreadingMixIn和TCPServer继承
    # class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass
    server = ThreadingTCPServer(addr, MyStreamRequestHandler)
    server.serve_forever()

