#nama berkas: p_tcpser.py
#TCP Server untuk client p_tcpcli.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50009))
s.listen(5)
print "Automatic server is ready !!"
data = ''
kamus = {'NAME' : 'Mahardhika Bathiarto Dim Zarita',
          'NIM' : 'L200184134',
          'GENERATION' : '2018'}
while data.lower() != 'exit' :
       komm, addr = s.accept()
       while data.lower() != 'exit':
              data = komm.recv(1024)
              if data.lower() == 'exit' :
                     komm.send('ready!!')
                     s.close()
                     break
              print'Question: ', data
              if kamus.has_key(data):
                     komm.send(kamus[data])
              else:
                     komm.send('Your question is irrelevant') #data dikirim balik
