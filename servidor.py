import socket
import sys


HOST = "167.71.243.238"
PORT = 9802

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Listening ...")



while True:
    conn, addr = s.accept()
    print("conectado: ", addr)


    # f_send = "200819010_servidor.wav"
    # print(len(f_send))
    # with open(f_send, "rb") as f:
    #     print("[+] Sending file...")
    #     print(f)
    #     data = f.read()
    #     conn.sendall(data)
        
    
    # break

            
conn.close() 
f.close()       
print("[-] Disconnected")
sys.exit(0)

