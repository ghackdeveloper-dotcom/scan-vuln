import time
import subprocess

def nmap():
    print("[BENVENUTO NEL TUO ENUMERATORE DI VULN PERSONALE]")
    time.sleep(2)
    print("[INIZIAMO LO SCAN CON NMAP + IL CONTROLLO VERSIONE E SCAN DI OGNI SINGOLA PORTA UN CLASSICO]")
    time.sleep(1)
    print("[INSERISCI IP DEL TRAGET]")
    ip = input()
    time.sleep(1)
    print("[ATTENDI...]")
    try:
        subprocess.run([f"nmap -sC -sV -p- {ip} | grep open >> analisi_macchina.txt"], shell=True, check=True)
        print("[LE VERSIONI SONO STATE SALVATE IN: analisi_macchina.txt]")
        time.sleep(1)
        print("[PASSAGGIO A GOBUSTER...]")
        time.sleep(2)
    except subprocess.CalledProcessError:
        print("[QUALCOSA CON NMAP E ANDATO STORTO CONTROLLA LA CONNESSIONE O INSERISCI TRAGET VALIDO]")
        time.sleep(1)
        print("[PASSAGGIO A GOBUSTER...]")
        time.sleep(2)
nmap()

def gobuster():
    print("[IL PASSAGGIO A GOBUSTER E AVVENUTO CON SUCCESSO]")
    time.sleep(2)
    print("[FORNISCI IL LINK DEL TRAGET ES: https://esempio.com]")
    link = input()
    print("[ATTENDI...]")
    try:
        subprocess.run([f"gobuster dir -u {link} -w /usr/share/dirb/wordlists/common.txt | grep Status >> analisi_macchina.txt"], shell=True, check=True)
        print("\n[LE DIR SONO STATE SALVATE IN: analisi_macchina.txt]")
        time.sleep(1)
        print("[PASSAGGIO A FFUF...]")
        time.sleep(2)
    except subprocess.CalledProcessError:
        print("[QUALCOSA CON GOBUSTER E ANDATO STORTO CONTROLLA CHE IL LINK SIA VALIDO O LA CONNSESSIONE FUNZIONI]")
        time.sleep(1)
        print("[PASSAGGIO A FFUF...]")
        time.sleep(2)
gobuster()

def ffuf():
    print("[IL PASSAGGIO A FFUF E AVVENUTO CON SUCCESSO]")
    time.sleep(2)
    print("[FORNISCI IL LINK ES: https://esempio.com]")
    link2 = input()
    print("[ORA FORNISCI IL NOME + COM O IT ES: esempio.com]")
    link3 = input()
    print(f"[PRENDO I DATI NECCESSARI DA {link2} ATTENDI...]")
    try:
        subprocess.run([f"""curl -I -H "Host: xyz123random.{link3}" {link2} | grep Content-Length:"""], shell=True, check=True)
        subprocess.run([f"""curl -I -H "Host: xyz123random.{link3}" {link2} | grep HTTP"""], shell=True, check=True)
        time.sleep(1)
        print("[SE IL NUMERO E PRESENTE DIGITARE -fs + IL NUMERO A TRE CIFRE DOPO Content-Length]")
        time.sleep(1)
        print("[SE IL NUMERO NON E PRESENTE DIGITARE -fc + IL NUMERO A TRE CIFRE DOPO HTTP]")
        time.sleep(1)
        print("[INSERISCI IL FLAG CHE VUOI USARE (-fs/-fc)]")
        flag = input()
        print("[ORA INSERISCI IL NUMERO]")
        numero = input()
        print("[INIZIALIZZAZIONE DI FFUF ATTENDI...]")
        time.sleep(2)
        try:
            print("[SE INIZIA AD IMPAZZIRE PREMI ctrl+C VUOLDIRE CHE IL NUMERO NON E VALIDO]")
            time.sleep(1)
            subprocess.run([f"""ffuf -u {link2} -H "Host: FUZZ.{link3}" -w /usr/share/wordlists/subdomains.txt {flag} {numero}"""], shell=True, check=True)
            print("[FFUF HA SCANALIZZATO CON SUCCESSO]")
            time.sleep(1)
            print("[TI TROVO ALTRI DATI SUL SERVER]")
            try:
                subprocess.run([f"""curl -I -H "Host: xyz123random.{link3}" {link2} >> analisi_macchina.txt"""], shell=True, check=True)
                print("[I DATI SONO STATI SALVATI IN analisi_macchina.txt]")
            except:
                print("[QUALCOSA E ANDATO STORTO CONTROLLA CHE IL LINK SIA VALIDO O LA CONNESSIONE]")
                time.sleep(1)
                print("[ENUM FINITA]")
        except subprocess.CalledProcessError:
            print("[QUALCOSA CON FFUF E ANDATO STORTO CONTROLLA CHE IL LINK SIA VALIDO O LA CONNESSIONE]")
            time.sleep(1)
            print("[ENUM FINITA]")
    except subprocess.CalledProcessError:
        print("[I DATI SONO INVALIDI O LA CONNESIONE E SALTATA]")
        time.sleep(1)
        print("[ENUM FINITA]")
ffuf()
