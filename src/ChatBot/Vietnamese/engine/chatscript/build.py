# Simple chat client to communicate with chat script server
# Not very efficient, since it uses a thread per socket model,
# If servicing a large number of clients, twisted may be a better fit

import socket


class Chatbot:
    def __init__(self):
        pass

    def response(self, message):
        user = "anhv"
        botname = "thanhtu"
        msg = '%s\u0000%s\u0000%s\u0000' % (user, botname, message)
        msg = msg.encode()
        output = self.sendAndReceiveChatScript(msg)
        return output

    def sendAndReceiveChatScript(self, msgToSend, server='127.0.0.1', port=1024, timeout=10):
        try:
            # Connect, send, receive and close socket. Connections are not persistent
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)  # timeout in secs
            s.connect((server, port))
            s.sendall(msgToSend)
            msg = ''
            while True:
                chunk = s.recv(1024)
                if chunk == b'':
                    break
                msg = msg + chunk.decode("utf-8", errors="ignore")
            s.close()
            return msg
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    bot = Chatbot()
    bot.response(":build ThanhTu")
    bot.response(":reset")
