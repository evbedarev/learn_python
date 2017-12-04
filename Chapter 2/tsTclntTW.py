from twisted.internet import protocol, reactor

HOST = '172.29.98.0'
PORT = 21566

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('...sending {0} ...'.format(data))
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data)
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()
