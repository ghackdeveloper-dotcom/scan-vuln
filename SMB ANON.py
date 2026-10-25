import time
import subprocess

def smb_anon():
    ip = input("[+]-[Inserisci ip] :")
    time.sleep(0.5)
    print("[+]-[Procedo con l'accesso anonimo]")
    try:
        subprocess.run([f"smbclient -L //{ip} "], check=True, shell=True)
        print("[+]-[Tentativo di connessione anonima riuscito]")
    except subprocess.CalledProcessError:
        print("[-]-[Tentativo di connessione anonima fallito]")
smb_anon()
