# SCAN LINUX
#Produttore g.hack

import time
import subprocess


class scan_linux():

    def configurazione(self):
        ip = input("INSERISCI IP:")
        dominio = input("INSERISCI DOMINIO:")
        self.nmap_gobuster_ffuf_feroxbuster(ip, dominio)
        self.smb_anon(ip, dominio)

    def nmap_gobuster_ffuf_feroxbuster(self, ip, dominio):
        print("[SCAN NMAP COMPLETO O STANDARD SE COMPLETO DIGITA -p- SE STANDARD PREMI SOLO INVIO]")
        opzione = input("MODALITA:")
        print("[SCAN INIZIATO ATTENDI...]")
        try:
            subprocess.run([f"nmap {opzione} {ip} >> nmap_scan.txt"], shell=True, check=True)
            print("[SCAN NMAP CONCLUSO CON SUCCESSO!]")
            time.sleep(0.5)
            print("[OUTPUT DI NMAP SALVATO SULLA HOME IN nmap_scan.txt]")
            with open ("nmap_scan.txt", "r") as f:
                contenuto = f.read()
            if "80/tcp" in contenuto or "443/tcp" in contenuto:
                print("[UN SITO E STATO RILEVATO]")
                percorso = input("FORNISCI IL PERCORSO DELLA WORDLIST PER GOBUSTER:")
                percorso2 = input("FORNISCI IL PERCORSO DELLA WORDLIST PER FEROXBUSTER:")
                percorso3 = input("FORNISCI IL PERCORSO DELLA WORDLIST PER FFUF:")
                print("[SCAN CON GOBUSTER INIZIATO ATTENDI...]")
                try:
                    subprocess.run([f"gobuster dir -u http://{dominio} -w {percorso} -o gobuster_scan.txt"], shell=True, check=True)
                    print("[OUTPUT DI GOBUSTER SALVATO SULLA HOME IN gobuster_scan.txt]")
                except subprocess.CalledProcessError:
                    print("[GOBUSTER DA PROBLEMI LO SOSTITUISCO CON FEROXBUSTER]")
                    print("[SCAN CON FEROXBUSTER INIZIATO ATTENDI...]")
                    subprocess.run([f"feroxbuster -u http://{dominio} -w {percorso2} -t 50 -o ferox_scan.txt"], shell=True, check=True)
                except Exception as e:
                    print("[SIA GOBUSTER CHE FEROXBUSTER DANNO PROBLEMI ANALISI SALTATA]")
                print("[ESTRAGGO IL DATO PER LO SCAN DI FFUF ATTENDI...]")
                try:
                    subprocess.run([f"""curl -I -H "Host: xyz123random.{dominio}" http://{dominio} | grep Content-Length:"""], shell=True, check=True)
                    print("[DATO PRESO CON SUCCESSO!]")
                except subprocess.CalledProcessError:
                    print("[NON E STATO POSSIBILE PRENDERE IL DATO NECESSARIO CONTROLLA LA CONNESSIONE O CORREGGI IL LINK]")
                dato = input("[INSERISCI IL NUMERO DOPO Content-Length:]")
                print("[PARTO CON FFUF]")
                try:
                    subprocess.run([f"""ffuf -u http://{dominio} -H "Host: FUZZ.{dominio}" -w {percorso3} -fs {dato}"""], shell=True, check=True)
                    print("[FFUF HA TERMINATO CON SUCCESSO]")
                except subprocess.CalledProcessError:
                    print("[FFUF E ANDATO IN ERRORE]")
            if "80/tcp" not in contenuto or "443/tcp" not in contenuto:
                print("[NESSUN SITO RILEVATO]")
        except subprocess.CalledProcessError:
            print("[SCAN NMAP FALLITO CONTROLLA LA CONNESSIONE]")
        except Exception as e:
            print(f"[ERRORE: {e}]")
    
    def smb_anon(self, ip, dominio):
        print("[PROVO ACCESSO ANONIMO SU SMB]")
        try:
            subprocess.run(["smbclient "], shell=True, check=True)
            print("[TENTATIVO DI CONNESSIONE ANONIMA RIUSCITO]")
            print("[SCAN LINUX FINITO CON SUCCESSO!]")
        except subprocess.CalledProcessError:
            print("[TENTATIVO DI CONNESSIONE ANONIMA FALLITO]")
            print("[SCAN LINUX FINITO CON SUCCESSO]")
            
scan = scan_linux()
scan.configurazione()
