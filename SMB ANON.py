import time
import subprocess

def smb_anon():
    print("[+]-[Inserisci ip]")
    ip = input()
    time.sleep(2)
    print("[+]-[Procedo con l'accesso anonimo]")
    try:
        subprocess.run(["smbclient", "-L", f"//{ip}", "-D", "/projects"], check=True)
        print("[+]-[Tentativo di connessione anonima riuscito]")
    except subprocess.CalledProcessError:
        print("[-]-[Tentativo di connessione anonima fallito]")
smb_anon()
