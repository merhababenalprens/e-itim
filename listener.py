import socket
from colorama import Fore,Back,Style,init
init()

port=int(input("lütfen bağlanmka istedğiinz port:"))
baglantı=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
baglantı.bind(("0.0.0.0",port))
print("sunucu dinleniyor........")
baglantı.listen(1)
conn,addr=baglantı.accept()
print(conn,addr)

while True:
    emir=input(Fore.RED+"PRENS>"+Fore.RESET)
    conn.send(emir.encode("utf-8"))
    response=conn.recv(16384).decode("utf-8")
    print(response)


