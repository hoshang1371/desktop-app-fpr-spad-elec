
from product import Main
import socket

class NetworkServer(Main):#Main

    def __init__(self, parent, child):
        super(Main, self).__init__(parent)
        self.parentWindow = parent
        self.child = child
        # self.child.setText("dataGetFromscript")

    def server(self):
        s = socket.socket()        
        # print ("Socket successfully created")
        port = 54321               
        s.bind(('127.0.0.1', port))        
        # print ("socket binded to %s" %(port))
        s.listen(5)    
        # print ("socket is listening")           
        c, addr = s.accept() 
        finalData =''  
        # self.parentWindow.smallDescription.clicked.disconnect()
        # self.parentWindow.description.clicked.disconnect()
        # self.parentWindow.smallDescription.clicked.disconnect()
        while True:
            # print ('Got connection from', addr )
            data =c.recv(8)
            finalData +=str(data, 'UTF-8')#str(data, 'UTF-8')
            # print(data)
            if not data:
                # if data is not received break
                c.close()
                # print("from connected user: " + str(data))
                # print(type(data))
                print(f'finalData = {finalData}')
                # self.parentWindow.description.setText(finalData)
                self.child.setText(finalData)

                # self.parentWindow.description.clicked.connect(lambda: self.desc(self.parentWindow.smallDescription), QtCore.Qt.DirectConnection)
                # self.parentWindow.smallDescription.clicked.connect(lambda: self.desc(self.parentWindow.smallDescription), QtCore.Qt.DirectConnection)
                # self.parentWindow.smallDescription.clicked.connect(lambda: print("oklambda"), QtCore.Qt.DirectConnection)
                # self.parentWindow.description.setText(finalData)
                break
 