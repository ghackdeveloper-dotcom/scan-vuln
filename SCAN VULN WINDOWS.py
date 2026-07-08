#PER WINDOWS SCAN DI VULN AUTOMATICO
#produttore: g.hackdeveloper

import time
import subprocess

class ScanVuln():
    
    def nmap():
        print("[BENVENUTO NEL TUO ENUMERATORE DI VULN PERSONALE PER WINDOWS CON QUALCHE MODIFICA RISPETTO A LINIX]")
        time.sleep(2)
        print("[INIZIAMO LO SCAN CON NMAP COMPLETO + IL CONTROLLO VERSIONE DELLE PORTE ESPOSTE]")
        time.sleep(1)
        print("[INSERISCI IP DEL TRAGET]")
        ip = input()
        time.sleep(1)
        print("[ATTENDI...]")
        try:
            subprocess.run([f"nmap -sC -sV -p- {ip}  >> analisi_macchina.txt"], shell=True, check=True)
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
                    print("[PASSO A SMB ANONIMO...]")
            except subprocess.CalledProcessError:
                print("[QUALCOSA CON FFUF E ANDATO STORTO CONTROLLA CHE IL LINK SIA VALIDO O LA CONNESSIONE]")
                time.sleep(1)
                print("[PASSO A SMB ANONIMO...]")
        except subprocess.CalledProcessError:
            print("[I DATI SONO INVALIDI O LA CONNESIONE E SALTATA]")
            time.sleep(1)
            print("[PASSO A SMB ANONIMO...]")
    ffuf()

    def smb_anon():
        print("[PASSAGGIO A SMB ANONIMO AVVENUTO CON SUCCESSO]")
        time.sleep(0.5)
        print("[INSERISCI IP DEL TRAGET]")
        risposta = input()
        time.sleep(0.5)
        print("[TENTO SMB ANONIMO...]")
        try:
            subprocess.run(["smbclient", "-L", f"//{risposta}", "-N"], check=True)
            print("[TENTATIVO DI CONNESSIONE ANONIMA RIUSCITO]")
        except subprocess.CalledProcessError:
            print("[TENTATIVO DI CONNESSIONE ANONIMA FALLITO]")
    smb_anon()

    def persistere():
        print("[CONTROLLA analisi_macchina.txt PER VEDERE SE E PRESENTE QUALCHE PROGRAMMA SOSPETTO]")
        time.sleep(1)
        print("[I PROGRAMMI CHE POSSONO ESSERE CONTROLLATI AL MOMENTO SONO: mqtt, evil-winrm, ftp, ssh, telnet, wsdapi]")
        time.sleep(0.5)
        print("[LE SCANSIONI PER QUESTI SERVIZI SONO DIVERSE PER OGNIUNO DI ESSI PER PROMETTERE UNA MAGGIORE EFFICENZA]")
        time.sleep(0.5)
        print("[DIGITA IL NOME DEL SERVIZIO]")
        servizio = input()
        print("[DIGITA IP DEL TRAGET]")
        ip = input()
        if servizio.lower() == "mqtt":
            try:
                subprocess.run([f"mosquitto_sub -h {ip} -t '#' -v >> analisi_macchina.txt"], shell=True, check=True)
                print("[TENTATIVO DI CONNESSIONE ANONIMA RIUSCITO CONTROLLA analisi_macchina.txt]")
                time.sleep(0.5)
                print("[PROVO AD ENUMERARE I TOPIC DI SISTEMA]")
                try:
                    subprocess.run([f"mosquitto_sub -h {ip} -p 1883 -t '$SYS/#' -v >> analisi_macchina.txt"], shell=True, check=True)
                    print("[TENTATIVO DI ENUMERAZIONE RIUSCITO CONTROLLA analisi_macchina.txt]")
                except subprocess.CalledProcessError:
                    print("[TENTATIVO DI ENUMERAZIONE FALLITO]")
            except subprocess.CalledProcessError:
                print("[TENTATIVO DI CONNESSIONE ANONIMA FALLITO]")
        elif servizio.lower() == "evil-winrm":
            try:
                subprocess.run([f"evil-winrm -i {ip} -u 'anonymous' -p '' -c 'ls' >> analisi_macchina.txt"], shell=True, check=True)
                print("[TENTATIVO DI CONNESSIONE ANONIMA  SU EVIL-WINRM RIUSCITO CONTROLLA analisi_macchina.txt]")
            except subprocess.CalledProcessError:
                print("[TENTATIVO DI CONNESSIONE ANONIMA SU EVIL-WINRM FALLITO]")
        elif servizio.lower() == "ftp":
            try:
                print(f"[PROVO A STABILIRE UNA CONNESSIONE ANONIMA SU {ip}]")
                time.sleep(0.5)
                print("[SE CHIEDE USERNAME DIGITARE anonymous E SE CHIEDE PASSWORD PREMERE INVIO]")
                subprocess.run([f"ftp {ip}"], shell=True, check=True)
            except subprocess.CalledProcessError:
                print("[TENTATIVO DI CONNESSIONE ANONIMA SU FTP FALLITO]")
        elif servizio.lower() == "ssh":
            try:
                print(f"[PROVO A STABILIRE UNA CONNESSIONE ANONIMA SU {ip}]")
                time.sleep(0.5)
                subprocess.run([f"ssh -o StrictHostKeyChecking=no anonymous@{ip}"], shell=True, check=True)
            except subprocess.CalledProcessError:
                print("[TENTATIVO DI CONNESSIONE ANONIMA SU SSH FALLITO]")
        elif servizio.lower() == "telnet":
            try:
                print(f"[PROVO A STABILIRE CONNESSIONE ANONIMA SU {ip}]")
                time.sleep(0.5)
                subprocess.run([f"nc {ip} 23 -t -v"], shell=True, check=True)
            except subprocess.CalledProcessError:
                print("[TENTATIVO DI CONNESSIONE ANONIMA SU TELNET FALLITO]")
        elif servizio.lower() == "wsdapi":
            try:
                print(f"[TESTO WSDAPI SU {ip}]")
                time.sleep(0.5)
                subprocess.run([f"curl -v http://{ip}:5357/ >> analisi_macchina.txt"], shell=True, check=True)
                print("[TENTATIVO DI CONNESSIONE SU WSDAPI RIUSCITO CONTROLLA analisi_macchina.txt]")
                time.sleep(0.5)
                print("[PROVO AD INVIARE SOAP XML PER PROVARE AD ENUMERARE METADATI SENSIBILI]")
                time.sleep(0.5)
                print("[CREO FILE XML PER INVIARE LA RICHIESTA DI METADATI]")
                try:
                    subprocess.run(['echo "<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope"> <s:Header/> <a:Action s:mustUnderstand="1">http://schemas.xmlsoap.org/ws/2004/09/transfer/Get</a:Action> <s:Header/> <s:Body> <w:Get xmlns:w="http://schemas.dmtf.org/wbem/wsman/1/wsman.xsd"/> </s:Body> </s:Envelope>" >> richiesta.xml'], shell=True, check=True)
                    print("[IL FILE E STATO CREATO CON SUCCESSO]")
                    time.sleep(0.5)
                    print("[INVIO DEL FILE XML PER ENUMERARE I METADATI]")
                    try:
                        subprocess.run([f"""curl -X POST -H "Content-Type: application/soap+xml; charset=UTF-8" -H "SOAPAction: http://schemas.xmlsoap.org/ws/2004/09/transfer/Get" -d @richiesta.xml -v http://{ip}:5357/ """], shell=True, check=True)
                        print("[TENTATIVO DI ENUMERAZIONE RIUSCITO CONTROLLA analisi_macchina.txt]")
                    except subprocess.CalledProcessError:
                        print("[TENTATIVO DI ENUMERAZIONE FALLITO]")
                except subprocess.CalledProcessError:
                    print("[QUALCOSA E ANDATO STORTO NELLA CREAZIONE DEL FILE XML]")
            except subprocess.CalledProcessError:
                print("[TENTATIVO DI CONNESSIONE SU WSDAPI FALLITO]")
        else:
            print("[IL CONTROLLO PER QUESTO SERVIZIO NON E PRESENTE PROVA CON UNALTRO SERVIZIO]")
    persistere()
ScanVuln()


