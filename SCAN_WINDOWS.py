#                                                                                     DISCLAMER
# ENG                                                                       DO NOT USE FOR ILLEGAL ACTIONS
# IT                                                                        NON USARE PER AZIONI ILLEGALI 


import os
import time
import subprocess

class scan_windows():

    def configurazione(self):

        banner = r"""-------------------------------------------------------------------------------------------------------------------------------
                    | \-\           ___           /-/ |--|  |--\     |-|  |----\              /---\       |----\                                  |
                    |  \ \         / _ \         / /  |  |  |   \    | |  | |-\ \            / /-\ \      | |-\ \                                 |
                    |   \ \       / / \ \       / /   |  |  |    \   | |  | |  \ \          / /___\ \     | |  \ \                                |
                    |    \ \     / /   \ \     / /    |  |  |  |\ \  | |  | |   | |        / _______ \    | |   | |                               |
                    |     \ \   / /     \ \   / /     |  |  |  | \ \ | |  | |  / /        / /       \ \   | |  / /                                |
                    |      \ \_/ /       \ \_/ /      |  |  |  |  \ \| |  | |_/ /  __    / /         \ \  | |_/ /  __                             |
                    |       \___/         \___/       |__|  |__|   \___|  |____/  |__|  /_/           \_\ |____/  |__| SCAN / CREATO DA G.HACK    |
                    -------------------------------------------------------------------------------------------------------------------------------
        """
        print(banner)

        print("[FORNISCI LE VARIE INFO]")
        ip = input("FORNISCI IP:")
        dominio = input("FORNISCI DOMINIO:")
        nome_utente = input("FORNISCI NOME UTENTE:")
        password_utente = input("FORNISCI PASSWORD UTENTE:")
        configurazione_per_ldap = input("FORNISCI SOLO IL NOME DEL DOMINIO EX esempio.com => esempio FORNISCI:")
        configurazione_per_ldap2 = input("ORA FORNISCI SOLO LA FINE DEL DOMINIO EX esempio.com => com FORNISCI:")
        time.sleep(0.5)
        print("[CONFIGURAZIONE COMPLETATA CON SUCCESSO!]")
        print(f"[TRAGET IP: {ip}]")
        print(f"[TRAGET DNS: {dominio}]")
        print(f"[TRAGET NOME: {nome_utente}]")
        print(f"[TRAGET PASSWORD: {password_utente}]")
        print(f"[NOME DOMINIO: {configurazione_per_ldap}]")
        print(f"[FINE DOMINIO: {configurazione_per_ldap2}]")
        self.tempo_tgt(ip)
        self.tgt_emergenza(dominio, ip, nome_utente, password_utente)
        self.rinom_tgt(nome_utente)
        self.nmap_gobuster_ffuf_feroxbuster(ip, dominio)
        self.bloodyAD(ip, dominio, nome_utente, password_utente)
        self.nxc(ip, dominio, nome_utente, password_utente)
        self.ldap_search(ip, dominio, nome_utente, password_utente, configurazione_per_ldap, configurazione_per_ldap2)
        self.certipy(ip, dominio, nome_utente, password_utente)
        self.report(ip, dominio, nome_utente, password_utente)
        time.sleep(0.5)

    def tempo_tgt(self, ip):
        print("[REGOLO IL TEMPO PER TGT]")
        try:
            subprocess.run([f"sudo rdate -n {ip}"], check=True, shell=True)
        except subprocess.CalledProcessError:
            print("[NON E STATO POSSIBILE REGOLARE IL TEMPO]")

    def tgt_emergenza(self, dominio, ip, nome_utente, password_utente):
        print("[CREO UN TGT NEL CASO DI PASSWORD NON SUFFICENTE]")
        try:
            subprocess.run([f"impacket-getTGT {dominio}/{nome_utente}:{password_utente} -dc-ip {ip}"], shell=True, check=True)
            print("[TGT CREATO CON SUCCESSO]")
        except subprocess.CalledProcessError:
            print("[IL TGT NON E STATO CREATO PASSO ALLA RISOLUZIONE DEL PROBLEMA]")
            try:
                risoluzione = input("HAI AES CON TE? (y/n) :")
                if risoluzione.lower() == "y":
                    aes = input("INSERISCI LA TUA CHIAVE AES :")
                    time.sleep(1)
                    try:
                        print("[PROVO A CREARE IL TGT CON AES]")
                        subprocess.run([f"impacket-getTGT {dominio}/{nome_utente} -dc-ip {ip} -aesKey {aes}"], shell=True, check=True)
                        print("[TGT CON AES CREATO CON SUCCESSO]")
                    except subprocess.CalledProcessError:
                        print("[TGT CON AES FALLITO]")
                if risoluzione.lower() == "n":
                    print("[ELABORO UNALTRA RISOLUZIONE]")
                    risoluzione2 = input("[HAI UN HASH NTLM? (y/n)]")
                    if risoluzione2.lower() == "y":
                        ntlm = input("INSERISCI IL TUO NTLM :")
                        time.sleep(1)
                        try:
                            subprocess.run([f"impacket-getTGT {dominio}/{nome_utente} -dc-ip {ip} -hashes {ntlm}"], shell=True, check=True)
                            print("[TGT CON NTLM CREATO CON SUCCESSO]")
                        except subprocess.CalledProcessError:
                            print("[TGT CON NTLM FALLITO]")
                    if risoluzione2.lower() == "n":
                        print("[PROCEDO CON QUELLO CHE HO]")
            except:
                print("[LA RISOLUZIONE HA FALLITO]")
        except:
            print("[LA RISOLUZIONE HA FALLITO]")

    def rinom_tgt(self, nome_utente):
        rinomina = input("IL TGT LO HAI CREATO? (y/y) :")
        if rinomina.lower() == "y":
            print(f"IL TGT SI CHIAMA {nome_utente}.ccache?")
            self.rinomina2 = input("SE SI SCRIVI LO STESSO NOME SE NO SCRIVI IL NOME DIVERSO DIGITA:")
            print("[NOME DEL TGT MEMORIZZATO CON SUCCESSO]")
        else:
            self.rinomina2 = None

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
                    print("[IL DATO DOVREBBE ESSERE STATO PRESO]")
                    ass = input("[SE IL DATO E STATO PRESO DIGITARE y SE ASSENTE DIGITARE n]")
                    if ass.lower() == "y":
                        print("[PROCEDO CON LO STANDARD]")
                    elif ass.lower() == "n":
                        print("[RECUPERO IL DATO DI SCORTA]")
                        try:
                            subprocess.run([f"""curl -I -H "Host: xyz123random.{dominio}" http://{dominio} | grep HTTP"""])
                            print("[IL DATO E STATO PRESO CON SUCCESSO!]")
                        except subprocess.CalledProcessError:
                            print("[NON E STATO POSSIBILE RECUPERARE IL DATO]")
                    else:
                        print("[PROCEDO CON IL DATO STANDARD]")
                except :
                    print("[NON E STATO POSSIBILE PRENDERE I DATI NECESSARI CONTROLLA LA CONNESSIONE O CORREGGI IL LINK]")
                dato = input("INSERISCI IL NUMERO DOPO Content-Length: O SE SI HA AVUTO PROBLEMI SIGITARE IL NUMERO DOPO HTTP  DIGITA:")
                flag = input("INSERISCI LA FLAG DA USARE SE SI HA AVUTO PROBLEMI DIGITARE -fc SE TUTTO OK DIGITARE -fs  DIGITA:")
                print("[PARTO CON FFUF]")
                try:
                    subprocess.run([f"""ffuf -u http://{dominio} -H "Host: FUZZ.{dominio}" -w {percorso3} {flag} {dato}"""], shell=True, check=True)
                    print("[FFUF HA TERMINATO CON SUCCESSO]")
                except subprocess.CalledProcessError:
                    print("[FFUF E ANDATO IN ERRORE]")
            if "80/tcp" not in contenuto and "443/tcp" not in contenuto:
                print("[NESSUN SITO RILEVATO]")
        except subprocess.CalledProcessError:
            print("[SCAN NMAP FALLITO CONTROLLA LA CONNESSIONE]")
        except Exception as e:
            print(f"[ERRORE: {e}]")

    def bloodyAD(self, ip, dominio, nome_utente, password_utente, rinomina2=None):
        if rinomina2 is None:
            rinomina2 = getattr(self, "rinomina2", None)
        print("[PARTO CON BLOODYAD TIRIAMO FUORI PRIMA LE BASI POI LE INFO MIGLIORI]")
        print(f"[USO USERNAME {nome_utente} CON PASSWORD {password_utente}]")
        risposta = input("CONFERMI? (y/n):")
        if risposta.lower() == "y":
            print("[OK PROCEDO]")
            try:
                print("QUESTO E QUELLO CHE PUO SCRIVERE")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                subprocess.run([f"bloodyAD -u {nome_utente} -p '{password_utente}' -d {dominio}   --host {ip} get writable --otype USER --detail >> scrivibili.txt"], shell=True, check=True)
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(1)
                print("[TI FACCIO UNA PANORAMICA GENERALE DI TUTTO IL TRAGET]")
                print("[PRIMA REGOLO IL TIMER INSERISCI LA PASSWORD DI SUDO]")
                subprocess.run([f"sudo rdate -n {ip}"], shell=True, check=True)
                try:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    subprocess.run([f"bloodhound-python -u {nome_utente} -p '{password_utente}'   -d {dominio} -dc DC01.{dominio}   -ns {ip} -c All"], shell=True, check=True)
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    time.sleep(0.5)
                    print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                    files = []

                    for i in range(1, 8):
                        nome = input(f"INSERISCI {i}° FILE:")
                        files.append(nome)
                    time.sleep(0.5)
                    print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                    time.sleep(1)
                    try:
                        for file in files:
                            print(f"[STO ANALIZZANDO IL FILE: {file}]")
                            with open (f"{file}", "r") as f:
                                contenuto = f.read()
                            parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                            for parola in parole_sospette:
                                if parola in contenuto:
                                    print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                    except:
                        print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                except subprocess.CalledProcessError:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("[SONO STATI RISCONTRATI DEI PROBLEMI, RISOLUZIONE PROBLEMI IN CORSO...]")
                    domain_controller = input("NOME DEL DOMAIN CONTROLLER COMPLETO EX(dc.esempio.com): ")
                    try:
                        subprocess.run([f"bloodhound-python -u {nome_utente} -p '{password_utente}' -d {dominio} -dc {domain_controller} -gc {domain_controller} -ns {ip} -c All"], shell=True, check=True)
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        time.sleep(0.5)
                        print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                        files = []

                        for i in range(1, 8):
                            nome = input(f"INSERISCI {i}° FILE:")
                            files.append(nome)
                        time.sleep(0.5)
                        print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                        time.sleep(1)
                        try:
                            for file in files:
                                print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                with open (f"{file}", "r") as f:
                                    contenuto = f.read()
                                parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                for parola in parole_sospette:
                                    if parola in contenuto:
                                        print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                        except:
                            print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                    except subprocess.CalledProcessError:
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            except subprocess.CalledProcessError:
                print("[BLOODYAD HA RISCONTRATO DEI PROBLEMI CONTROLLA LA CONNESSIONE AD INTERNET]")
                print("[PROVO A RISOLVERE IL PROBLEMA...]")
                domain_c = input("FORNISCI IL DOMAIN CONTROLLER COMPLETO EX(dc.esempio.com):")
                try:
                    if rinomina2:
                        os.environ["KRB5CCNAME"] = rinomina2
                    else:
                        print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                    try:
                        subprocess.run([f"bloodyAD -u {nome_utente} -k -d {dominio} --host {domain_c} --dc-ip {ip} get writable --otype USER --detail"], shell=True, check=True)
                        print("[IL PROBLEMA E STATO RISOLTO CON SUCCESSO]")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        time.sleep(1)
                        print("[TI FACCIO UNA PANORAMICA GENERALE DI TUTTO IL TRAGET]")
                        print("[PRIMA REGOLO IL TIMER INSERISCI LA PASSWORD DI SUDO]")
                        subprocess.run([f"sudo rdate -n {ip}"], shell=True, check=True)
                        try:
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            subprocess.run([f"bloodhound-python -u {nome_utente} -k -d {dominio} -dc DC01.{dominio} --no-pass -ns {ip} -c All"], shell=True, check=True)
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            time.sleep(0.5)
                            print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                            files = []

                            for i in range(1, 8):
                                nome = input(f"INSERISCI {i}° FILE:")
                                files.append(nome)
                            time.sleep(0.5)
                            print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                            time.sleep(1)
                            try:
                                for file in files:
                                    print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                    with open (f"{file}", "r") as f:
                                        contenuto = f.read()
                                    parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                    for parola in parole_sospette:
                                        if parola in contenuto:
                                            print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                            except:
                                print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                        except subprocess.CalledProcessError:
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            print("[SONO STATI RISCONTRATI DEI PROBLEMI, RISOLUZIONE PROBLEMI IN CORSO...]")
                            try:
                                subprocess.run([f"bloodhound-python -u {nome_utente} -k --no-pass -d {dominio} -dc {domain_c} -gc {domain_c} -ns {ip} -c All"], shell=True, check=True)
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                                time.sleep(0.5)
                                print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                                files = []

                                for i in range(1, 8):
                                    nome = input(f"INSERISCI {i}° FILE:")
                                    files.append(nome)
                                time.sleep(0.5)
                                print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                                time.sleep(1)
                                try:
                                    for file in files:
                                        print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                        with open (f"{file}", "r") as f:
                                            contenuto = f.read()
                                        parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                        for parola in parole_sospette:
                                            if parola in contenuto:
                                                print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                                except:
                                    print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                            except subprocess.CalledProcessError:
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    except subprocess.CalledProcessError:
                        print("IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE")
                except subprocess.CalledProcessError:
                    print("[IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE]")
            except:
                print("[IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE]")
        elif risposta.lower() == "n":
            print("[OK RISCRIVI IL NUOVO NOME E PASSWORD]")
            nome = input("NUOVO NOME:")
            password = input("NUOVA PASSWORD:")
            print("[PERFETTO PROCEDO CON BLOODYAD]")
            try:
                print("QUESTO E QUELLO CHE PUO SCRIVERE")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                subprocess.run([f"bloodyAD -u {nome} -p '{password}' -d {dominio}   --host {ip} get writable --otype USER --detail >> scrivibili.txt"], shell=True, check=True)
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(1)
                print("[TI FACCIO UNA PANORAMICA GENERALE DI TUTTO IL TRAGET]")
                print("[PRIMA REGOLO IL TIMER INSERISCI LA PASSWORD DI SUDO]")
                subprocess.run([f"sudo rdate -n {ip}"], shell=True, check=True)
                try:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    subprocess.run([f"bloodhound-python -u {nome} -p '{password}'   -d {dominio} -dc DC01.{dominio}   -ns {ip} -c All"], shell=True, check=True)
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    time.sleep(0.5)
                    print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                    files = []

                    for i in range(1, 8):
                        nome = input(f"INSERISCI {i}° FILE:")
                        files.append(nome)
                    time.sleep(0.5)
                    print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                    time.sleep(1)
                    try:
                        for file in files:
                            print(f"[STO ANALIZZANDO IL FILE: {file}]")
                            with open (f"{file}", "r") as f:
                                contenuto = f.read()
                            parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                            for parola in parole_sospette:
                                if parola in contenuto:
                                    print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                    except:
                        print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                except subprocess.CalledProcessError:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("[SONO STATI RISCONTRATI DEI PROBLEMI, RISOLUZIONE PROBLEMI IN CORSO...]")
                    domain_controller = input("NOME DEL DOMAIN CONTROLLER COMPLETO EX(dc.esempio.com): ")
                    try:
                        subprocess.run([f"bloodhound-python -u {nome} -p '{password}' -d {dominio} -dc {domain_controller} -gc {domain_controller} -ns {ip} -c All"], shell=True, check=True)
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        time.sleep(0.5)
                        print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                        files = []

                        for i in range(1, 8):
                            nome = input(f"INSERISCI {i}° FILE:")
                            files.append(nome)
                        time.sleep(0.5)
                        print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                        time.sleep(1)
                        try:
                            for file in files:
                                print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                with open (f"{file}", "r") as f:
                                    contenuto = f.read()
                                parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                for parola in parole_sospette:
                                    if parola in contenuto:
                                        print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                        except:
                            print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                    except subprocess.CalledProcessError:
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            except subprocess.CalledProcessError:
                print("[BLOODYAD HA RISCONTRATO DEI PROBLEMI CONTROLLA LA CONNESSIONE AD INTERNET]")
                print("[PROVO A RISOLVERE IL PROBLEMA...]")
                domain_c = input("FORNISCI IL DOMAIN CONTROLLER COMPLETO EX(dc.esempio.com):")
                try:
                    if rinomina2:
                        os.environ["KRB5CCNAME"] = rinomina2
                    else:
                        print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                    try:
                        subprocess.run([f"bloodyAD -u {nome} -k -d {dominio} --host {domain_c} --dc-ip {ip} get writable --otype USER --detail"], shell=True, check=True)
                        print("[IL PROBLEMA E STATO RISOLTO CON SUCCESSO]")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        time.sleep(1)
                        print("[TI FACCIO UNA PANORAMICA GENERALE DI TUTTO IL TRAGET]")
                        print("[PRIMA REGOLO IL TIMER INSERISCI LA PASSWORD DI SUDO]")
                        subprocess.run([f"sudo rdate -n {ip}"], shell=True, check=True)
                        try:
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            subprocess.run([f"bloodhound-python -u {nome} -k -d {dominio} -dc DC01.{dominio} --no-pass -ns {ip} -c All"], shell=True, check=True)
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            time.sleep(0.5)
                            print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                            files = []

                            for i in range(1, 8):
                                nome = input(f"INSERISCI {i}° FILE:")
                                files.append(nome)
                            time.sleep(0.5)
                            print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                            time.sleep(1)
                            try:
                                for file in files:
                                    print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                    with open (f"{file}", "r") as f:
                                        contenuto = f.read()
                                    parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                    for parola in parole_sospette:
                                        if parola in contenuto:
                                            print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                            except:
                                print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                        except subprocess.CalledProcessError:
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            print("[SONO STATI RISCONTRATI DEI PROBLEMI, RISOLUZIONE PROBLEMI IN CORSO...]")
                            try:
                                subprocess.run([f"bloodhound-python -u {nome} -k --no-pass -d {dominio} -dc {domain_c} -gc {domain_c} -ns {ip} -c All"], shell=True, check=True)
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                                time.sleep(0.5)
                                print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                                files = []

                                for i in range(1, 8):
                                    nome = input(f"INSERISCI {i}° FILE:")
                                    files.append(nome)
                                time.sleep(0.5)
                                print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                                time.sleep(1)
                                try:
                                    for file in files:
                                        print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                        with open (f"{file}", "r") as f:
                                            contenuto = f.read()
                                        parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                        for parola in parole_sospette:
                                            if parola in contenuto:
                                                print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                                except:
                                    print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                            except subprocess.CalledProcessError:
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    except subprocess.CalledProcessError:
                        print("IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE")
                except subprocess.CalledProcessError:
                    print("[IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE]")
            except:
                print("[IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE]")
        else:
            print("[RISPOSTA NON VALAIDA PROCEDO CON I DATI STANDARD]")
            try:
                print("QUESTO E QUELLO CHE PUO SCRIVERE")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                subprocess.run([f"bloodyAD -u {nome_utente} -p '{password_utente}' -d {dominio}   --host {ip} get writable --otype USER --detail >> scrivibili.txt"], shell=True, check=True)
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                time.sleep(1)
                print("[TI FACCIO UNA PANORAMICA GENERALE DI TUTTO IL TRAGET]")
                print("[PRIMA REGOLO IL TIMER INSERISCI LA PASSWORD DI SUDO]")
                subprocess.run([f"sudo rdate -n {ip}"], shell=True, check=True)
                try:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    subprocess.run([f"bloodhound-python -u {nome_utente} -p '{password_utente}'   -d {dominio} -dc DC01.{dominio}   -ns {ip} -c All"], shell=True, check=True)
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    time.sleep(0.5)
                    print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                    files = []

                    for i in range(1, 8):
                        nome = input(f"INSERISCI {i}° FILE:")
                        files.append(nome)
                    time.sleep(0.5)
                    print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                    time.sleep(1)
                    try:
                        for file in files:
                            print(f"[STO ANALIZZANDO IL FILE: {file}]")
                            with open (f"{file}", "r") as f:
                                contenuto = f.read()
                            parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                            for parola in parole_sospette:
                                if parola in contenuto:
                                    print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                    except:
                        print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                except subprocess.CalledProcessError:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("[SONO STATI RISCONTRATI DEI PROBLEMI, RISOLUZIONE PROBLEMI IN CORSO...]")
                    domain_controller = input("NOME DEL DOMAIN CONTROLLER COMPLETO EX(dc.esempio.com): ")
                    try:
                        subprocess.run([f"bloodhound-python -u {nome_utente} -p '{password_utente}' -d {dominio} -dc {domain_controller} -gc {domain_controller} -ns {ip} -c All"], shell=True, check=True)
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        time.sleep(0.5)
                        print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                        files = []

                        for i in range(1, 8):
                            nome = input(f"INSERISCI {i}° FILE:")
                            files.append(nome)
                        time.sleep(0.5)
                        print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                        time.sleep(1)
                        try:
                            for file in files:
                                print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                with open (f"{file}", "r") as f:
                                    contenuto = f.read()
                                parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                for parola in parole_sospette:
                                    if parola in contenuto:
                                        print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                        except:
                            print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                    except subprocess.CalledProcessError:
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            except subprocess.CalledProcessError:
                print("[BLOODYAD HA RISCONTRATO DEI PROBLEMI CONTROLLA LA CONNESSIONE AD INTERNET]")
                print("[PROVO A RISOLVERE IL PROBLEMA...]")
                domain_c = input("FORNISCI IL DOMAIN CONTROLLER COMPLETO EX(dc.esempio.com):")
                try:
                    if rinomina2:
                        os.environ["KRB5CCNAME"] = rinomina2
                    else:
                        print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                    try:
                        subprocess.run([f"bloodyAD -u {nome_utente} -k -d {dominio} --host {domain_c} --dc-ip {ip} get writable --otype USER --detail"], shell=True, check=True)
                        print("[IL PROBLEMA E STATO RISOLTO CON SUCCESSO]")
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        time.sleep(1)
                        print("[TI FACCIO UNA PANORAMICA GENERALE DI TUTTO IL TRAGET]")
                        print("[PRIMA REGOLO IL TIMER INSERISCI LA PASSWORD DI SUDO]")
                        subprocess.run([f"sudo rdate -n {ip}"], shell=True, check=True)
                        try:
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            subprocess.run([f"bloodhound-python -u {nome_utente} -k -d {dominio} -dc DC01.{dominio} --no-pass -ns {ip} -c All"], shell=True, check=True)
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            time.sleep(0.5)
                            print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                            files = []

                            for i in range(1, 8):
                                nome = input(f"INSERISCI {i}° FILE:")
                                files.append(nome)
                            time.sleep(0.5)
                            print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                            time.sleep(1)
                            try:
                                for file in files:
                                    print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                    with open (f"{file}", "r") as f:
                                        contenuto = f.read()
                                    parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                    for parola in parole_sospette:
                                        if parola in contenuto:
                                            print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                            except:
                                print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                        except subprocess.CalledProcessError:
                            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                            print("[SONO STATI RISCONTRATI DEI PROBLEMI, RISOLUZIONE PROBLEMI IN CORSO...]")
                            try:
                                subprocess.run([f"bloodhound-python -u {nome_utente} -k --no-pass -d {dominio} -dc {domain_c} -gc {domain_c} -ns {ip} -c All"], shell=True, check=True)
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                                time.sleep(0.5)
                                print("[INSERISCI IL NOME DI TUTTI I 7 FILE ESTRATTI]")
                    
                                files = []

                                for i in range(1, 8):
                                    nome = input(f"INSERISCI {i}° FILE:")
                                    files.append(nome)
                                time.sleep(0.5)
                                print("[PERFETTO ORA CHE HO TUTTI I FILE PASSO ALL'ANALISI]")
                                time.sleep(1)
                                try:
                                    for file in files:
                                        print(f"[STO ANALIZZANDO IL FILE: {file}]")
                                        with open (f"{file}", "r") as f:
                                            contenuto = f.read()
                                        parole_sospette = ["ForceChangePassword", "User-Force-Change-Password", "GenericAll", "GenericWrite", "WriteDacl", "WriteOwner", "Owns", "AdminTo", "HasSession", "CanRDP", "CanPSRemote", "HasSIDHistory", "AllowedToDelegate", "AllowedToAct", "HasSPN", "MemberOf", "PasswordNotReq", "PasswordNeverExpires", "UnconstrainedDelegation", "DumpSMSAPassword", "AllExtendedRights"]
                                        for parola in parole_sospette:
                                            if parola in contenuto:
                                                print(f"[SONO STATE TROVATE DELLE PAROLE SOSPETTE NEL FILE {file} LE PAROLE SONO: {parola}]")
                                except:
                                    print(f"[NON E STATO POSSIBILE ANALIZZARE I FILE {files}]")
                            except subprocess.CalledProcessError:
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    except subprocess.CalledProcessError:
                        print("IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE")
                except subprocess.CalledProcessError:
                    print("[IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE]")
            except:
                print("[IL PROBLEMA NON E STATO RISOLTO CONTROLLA LA CONNESSIONE]")

    def nxc(self, ip, dominio, nome_utente, password_utente, rinomina2=None):
        if rinomina2 is None:
            rinomina2 = getattr(self, "rinomina2", None)
        print("[PROCEDO CON NXC ED ANALIZZO PRIMA SMB E POI LDAP]")
        time.sleep(0.5)
        print("[ANALIZZO SMB]")
        try:
            time.sleep(0.5)
            print(f"[ENUMERO I GRUPPI LOCALI SU {nome_utente}]")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            subprocess.run([f"nxc smb {ip}/24 -u {nome_utente} -p '{password_utente}' --local-group >> gruppi_locali.txt"], shell=True, check=True)
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"[ENUMERAZIONE DEI GRUPPI LOCALI SULL'UTENTE {nome_utente} E AVVENUTA CON SUCCESSO PROCEDO CON L'ENUMERAZIONE GENERALE DEGLI UTENTI]")
        except subprocess.CalledProcessError:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"[NON E STATO POSSIBILE ENUMERARE I GRUPPI LOCALI DELL'UTENTE {nome_utente} CONTROLLA LA CONNESSIONE]")
            time.sleep(0.5)
            print("[RISOLUZIONE PROBLEMI IN CORSO...]")
            try:
                if rinomina2:
                    os.environ["KRB5CCNAME"] = rinomina2
                else:
                    print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                subprocess.run([f"nxc smb {ip}/24 -u {nome_utente} --use-kcache -k --local-group >> gruppi_locali.txt"], shell=True, check=True)
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("[LA RISOLUZIONE DEI PROBLEMI HA RISOLTO]")
            except subprocess.CalledProcessError:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("[LA RISOLUZIONE PROBLEMI HA FALLITO] (RAGIONE: TGT INESISTENTE)")
            print("[PROCEDO CON L'ENUMERAZIONE GENERALE DEGLI UTENTI PRESENTI]")
        try:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            subprocess.run([f"nxc smb {ip} -u {nome_utente} -p '{password_utente}' --users-export utenti_smb.txt"], shell=True, check=True)
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print("[ENUMERAZIONE GENERALE DEGLI UTENTI AVVENUTA CON SUCCESSO PROCEDO CON L'ENUM DI LDAP]")
        except subprocess.CalledProcessError:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print("[NON E STATO POSSIBILE ENUMERARE GLI UTENTI CONTROLLA LA CONNESSIONE]")
            time.sleep(0.5)
            print("[RISOLUZIONE PROBLEMI IN CORSO...]")
            try:
                if rinomina2:
                    os.environ["KRB5CCNAME"] = rinomina2
                else:
                    print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                subprocess.run([f"nxc smb {ip} -u {nome_utente} --use-kcache -k --users-export utenti_smb.txt"], shell=True, check=True)
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("[LA RISOLUZIONE DEI PROBLEMI HA RISOLTO]")
            except subprocess.CalledProcessError:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("[LA RISOLUZIONE PROBLEMI HA FALLITO] (RAGIONE: TGT INESISTENTE)")
        time.sleep(0.5)
        print("[PROCEDO CON L'ENUM DI LDAP]")
        time.sleep(0.5)
        print("[ENUMERO I GRUPPI]")
        try:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            subprocess.run([f"nxc ldap {ip} -u {nome_utente} -p '{password_utente}' --groups >> gruppi_generali.txt"], shell=True, check=True)
            print("")
            subprocess.run(["cat gruppi_generali.txt | grep DC"], shell=True)
            print("[QUESTI SONO TUTTI I GRUPPI PUOI CERCARE CHI C'E DENTRO SCRIVI TRE GRUPPI CHE VUOI CURIOSARE SE MENO CLICCA SOLO INVIO]")

            gruppis = []

            for i in range(1,4):
                gruppi = input("INSERISCI I NOMI DEI TRE GRUPPI:")
                gruppis.append(gruppi)
            print("[BENE ENUMERO I 3 GRUPPI]")
            try:
                for gruppi in gruppis:
                    print(f"[STO ENUMERANDO GLI UTENTI NEL GRUPPO: {gruppi}]")
                    try:
                        subprocess.run([f"""nxc ldap {ip} -u {nome_utente} -p '{password_utente}' --group '{gruppi}' >> utenti_su_gruppo.txt """], shell=True, check=True)
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        print(f"[IL GRUPPO {gruppi} E STATO ENUMERATO CON SUCCESSO]")
                        print("[L'ENUMERAZIONE DEGLI UTENTI NEI GRUPPI E AVVENUTA CON SUCCESSO!]")
                    except subprocess.CalledProcessError:
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        print(f"[SI E VERIFICATO UN ERRORE NELL'ENUMERARE {gruppi}]")
            except:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("[NON E STATO POSSIBILE ENUMERARE I TRE GRUPPI]")
        except subprocess.CalledProcessError:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print("[NON E STATO POSSIBILE ENUMERARE I GRUPPI]")
            time.sleep(0.5)
            print("[RISOLUZIONE PROBLEMI IN CORSO...]")
            try:
                if rinomina2:
                    os.environ["KRB5CCNAME"] = rinomina2
                else:
                    print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                try:
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    subprocess.run([f"nxc ldap {ip} -u {nome_utente} --use-kcache -k --groups >> gruppi_generali.txt"], shell=True, check=True)
                    print("")
                    subprocess.run(["cat gruppi_generali.txt | grep DC"], shell=True)
                    print("[QUESTI SONO TUTTI I GRUPPI PUOI CERCARE CHI C'E DENTRO SCRIVI TRE GRUPPI CHE VUOI CURIOSARE SE MENO CLICCA SOLO INVIO]")

                    gruppis = []

                    for i in range(1,4):
                        gruppi = input("INSERISCI I NOMI DEI TRE GRUPPI:")
                        gruppis.append(gruppi)
                    print("[BENE ENUMERO I 3 GRUPPI]")
                    try:
                        for gruppi in gruppis:
                            print(f"[STO ENUMERANDO GLI UTENTI NEL GRUPPO: {gruppi}]")
                            try:
                                subprocess.run([f"""nxc ldap {ip} -u {nome_utente} --use-kcache -k --group '{gruppi}' >> utenti_su_gruppo.txt """], shell=True, check=True)
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                                print(f"[IL GRUPPO {gruppi} E STATO ENUMERATO CON SUCCESSO]")
                                print("[L'ENUMERAZIONE DEGLI UTENTI NEI GRUPPI E AVVENUTA CON SUCCESSO!]")
                            except subprocess.CalledProcessError:
                                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                                print(f"[SI E VERIFICATO UN ERRORE NELL'ENUMERARE {gruppi}]")
                    except:
                        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                        print("[NON E STATO POSSIBILE ENUMERARE I TRE GRUPPI]")
                except subprocess.CalledProcessError:
                    print("[LA RISOLUZIONE PROBLEMI HA FALLITO]")
            except:
                print("[LA RISOLUZIONE PROBLEMI HA FALLITO] (RAGIONE: TGT INESISTENTE)")
        print("[PROCEDO CON L'ENUMERAZIONE DEGLI UTENTI GMSA SU LDAP]")
        try:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            subprocess.run([f"nxc ldap {ip} -u {nome_utente} -p '{password_utente}' --gmsa >> enum_gmsa.txt"], shell=True, check=True)
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print("[ENUMERAZIONE DEGLI UTENTI GMSA AVVENUTA CON SUCCESSO!]")
        except subprocess.CalledProcessError:
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            print("[ENUMERAZIONE DEGLI UTENTI GMSA NON RIUSCITA]")
            time.sleep(0.5)
            print("[RISOLUZIONE PROBLEMI IN CORSO...]")
            try:
                if rinomina2:
                    os.environ["KRB5CCNAME"] = rinomina2
                else:
                    print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                subprocess.run([f"nxc ldap {ip} -u {nome_utente} --use-kcache -k --gmsa >> enum_gmsa.txt"], shell=True, check=True)
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("[LA RISOLUZIONE DEI PROBLEMI HA RISOLTO]")
            except subprocess.CalledProcessError:
                print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                print("[LA RISOLUZIONE PROBLEMI HA FALLITO] (RAGIONE: TGT INESISTENTE)")

    def ldap_search(self, ip, dominio, nome_utente, password_utente, configurazione_per_ldap, configurazione_per_ldap2):
        print("[INIZIO LO SCAN CON LDAPSEARCH]")
        time.sleep(0.5)
        print("[CONTROLLO SE E PRESENTE UN RODC O UN DC SCRIVIBILE]")
        try:
            subprocess.run([f""" ldapsearch -x -H ldap://{ip} -D "{nome_utente}@{dominio}" -w '{password_utente}'  -b "DC={configurazione_per_ldap},DC={configurazione_per_ldap2}" "(&(objectClass=computer)(|(primaryGroupID=516)(primaryGroupID=521)))"  cn dNSHostName primaryGroupID >> controllo_ldap_search.txt"""], shell=True, check=True)
            print("[PERFETTO ORA CONTROLLO DENTRO IL FILE controllo_ldap_search.txt SE RISULTA POSITIVO TI ELENCO I RODC E HAI UN MAX DI 3 RODC DA POTER CONTROLLARE]")
            print("[SE DOVESSE RISULTARE NEGATIVO SKIPPO E PASSO AL REPORT]")
            time.sleep(1)
            try:
                with open ("controllo_ldap_search.txt", "r") as f:
                    analisi = f.read()
                if "cn:" in analisi:
                    print("[POSITIVO PASSO ALLO STEP SUCESSIVO]")
                    time.sleep(0.5)
                    print("[TI MOSTRO I RODC TROVATI]")
                    try:
                        subprocess.run([""" cat controllo_ldap_search.txt | grep cn: """], shell=True)
                        print("[RODC ELENCATI CON SUCCESSO]")
                        print("[ELENCA IL NUMERO DI RODC CHE TE LI ENUMERO]")
                        print("[SCRIVI IL COMANDO PER IL NUMERO DI RODC CHE TI SERVE EX SE 3 SCRIVI 1,4]")
                        try:
                            numero_rodc = input("SCRIVI IL NUMERO:")
                            inizio,fine = map(int, numero_rodc.split(","))

                            rodc_nome = []

                            for i in range(inizio,fine):
                                rodc = input("SRIVI I NOMI DEI RODC:")
                                rodc_nome.append(rodc)
                            print("[NOMI SALVATI ORA ENUMERO]")
                            try:
                                for rodc in rodc_nome:
                                    print(f"[STO ENUMERANDO: {rodc}]")
                                    try:
                                        subprocess.run([f"""ldapsearch -x -H ldap://{ip} -D "{nome_utente}@{dominio}" -w '{password_utente}'  -b "DC={configurazione_per_ldap},DC={configurazione_per_ldap2}" "(cn={rodc})"  cn msDS-RevealedUsers msDS-NeverRevealGroup msDS-RevealOnDemandGroup >> nomi_rodc_enum.txt"""], shell=True, check=True)
                                        print(f"[HO ENUMERATO CON SUCCESSO: {rodc}]")
                                    except subprocess.CalledProcessError:
                                        print(f"NON E STATO POSSIBILE ENUMERARE: {rodc}")
                            except:
                                print("[NON E STATO POSSIBILE ENUMERARE I RODC]")
                        except:
                            print("[IL COMANDO NON E STATO ACCETTATO CONTROLLA IL FORMATO CHE DEVE ESSERE ESATTAMENTE 1,#]")
                    except subprocess.CalledProcessError:
                        print("[C'E STATO UN ERRORE NELL'ELENCARE I RODC FAI UN CONTROLLO MANUALE E DIMMI IL NUMERO DI RODC PRESENTI CHE LI ENUMERO]")
                        print("[SCRIVI IL COMANDO PER IL NUMERO DI RODC CHE TI SERVE EX SE 3 SCRIVI 1,4]")
                        try:
                            numero_rodc = input("SCRIVI IL NUMERO:")
                            inizio,fine = map(int, numero_rodc.split(","))

                            rodc_nome = []

                            for i in range(inizio,fine):
                                rodc = input("SRIVI I NOMI DEI RODC:")
                                rodc_nome.append(rodc)
                            print("[NOMI SALVATI ORA ENUMERO]")
                            try:
                                for rodc in rodc_nome:
                                    print(f"[STO ENUMERANDO: {rodc}]")
                                    try:
                                        subprocess.run([f"""ldapsearch -x -H ldap://{ip} -D "{nome_utente}@{dominio}" -w '{password_utente}'  -b "DC={configurazione_per_ldap},DC={configurazione_per_ldap2}" "(cn={rodc})"  cn msDS-RevealedUsers msDS-NeverRevealGroup msDS-RevealOnDemandGroup >> nomi_rodc_enum.txt"""], shell=True, check=True)
                                        print(f"[HO ENUMERATO CON SUCCESSO: {rodc}]")
                                    except subprocess.CalledProcessError:
                                        print(f"NON E STATO POSSIBILE ENUMERARE: {rodc}")
                            except:
                                print("[NON E STATO POSSIBILE ENUMERARE I RODC]")
                        except:
                            print("[IL COMANDO NON E STATO ACCETTATO CONTROLLA IL FORMATO CHE DEVE ESSERE ESATTAMENTE 1,#]")
                if "cn:" not in analisi:
                    print("[NEGATIVO PASSO AD CERTIPY]")
            except:
                print("[NON E STATO POSSIBILE CONTROLLARE IL FILE controllo_ldap_search.txt]")
        except subprocess.CalledProcessError:
            print("[NON E STATO POSSIBILE CONTROLLARE LA PRESENZA DI UN RODC CONTROLLA LA CONNESSIONE]")
            print("[RISOLUZIONE PROBLEMI IN CORSO...]")
            try:
                subprocess.run([f"""LDAPTLS_REQCERT=never ldapsearch -x -H ldap://{ip} -D "{nome_utente}@{dominio}" -w '{password_utente}' -Z -b "DC={configurazione_per_ldap},DC={configurazione_per_ldap2}" "(&(objectClass=computer)(|(primaryGroupID=516)(primaryGroupID=521)))"  cn dNSHostName primaryGroupID >> controllo_ldap_search.txt"""], shell=True, check=True)
                print("[PERFETTO ORA CONTROLLO DENTRO IL FILE controllo_ldap_search.txt SE RISULTA POSITIVO TI ELENCO I RODC E HAI UN MAX DI 3 RODC DA POTER CONTROLLARE]")
                print("[SE DOVESSE RISULTARE NEGATIVO SKIPPO E PASSO AL REPORT]")
                time.sleep(1)
                try:
                    with open ("controllo_ldap_search.txt", "r") as f:
                        analisi = f.read()
                    if "cn:" in analisi:
                        print("[POSITIVO PASSO ALLO STEP SUCESSIVO]")
                        time.sleep(0.5)
                        print("[TI MOSTRO I RODC TROVATI]")
                        try:
                            subprocess.run([""" cat controllo_ldap_search.txt | grep cn: """], shell=True)
                            print("[RODC ELENCATI CON SUCCESSO]")
                            print("[ELENCA IL NUMERO DI RODC CHE TE LI ENUMERO]")
                            print("[SCRIVI IL COMANDO PER IL NUMERO DI RODC CHE TI SERVE EX SE 3 SCRIVI 1,4]")
                            try:
                                numero_rodc = input("SCRIVI IL NUMERO:")
                                inizio,fine = map(int, numero_rodc.split(","))

                                rodc_nome = []

                                for i in range(inizio,fine):
                                    rodc = input("SRIVI I NOMI DEI RODC:")
                                    rodc_nome.append(rodc)
                                print("[NOMI SALVATI ORA ENUMERO]")
                                try:
                                    for rodc in rodc_nome:
                                        print(f"[STO ENUMERANDO: {rodc}]")
                                        try:
                                            subprocess.run([f"""LDAPTLS_REQCERT=never ldapsearch -x -H ldap://{ip} -D "{nome_utente}@{dominio}" -w '{password_utente}' -Z -b "DC={configurazione_per_ldap},DC={configurazione_per_ldap2}" "(cn={rodc})"  cn msDS-RevealedUsers msDS-NeverRevealGroup msDS-RevealOnDemandGroup >> nomi_rodc_enum.txt"""], shell=True, check=True)
                                            print(f"[HO ENUMERATO CON SUCCESSO: {rodc}]")
                                        except subprocess.CalledProcessError:
                                            print(f"NON E STATO POSSIBILE ENUMERARE: {rodc}")
                                except:
                                    print("[NON E STATO POSSIBILE ENUMERARE I RODC]")
                            except:
                                print("[IL COMANDO NON E STATO ACCETTATO CONTROLLA IL FORMATO CHE DEVE ESSERE ESATTAMENTE 1,#]")
                        except subprocess.CalledProcessError:
                            print("[C'E STATO UN ERRORE NELL'ELENCARE I RODC FAI UN CONTROLLO MANUALE E DIMMI IL NUMERO DI RODC PRESENTI CHE LI ENUMERO]")
                            print("[SCRIVI IL COMANDO PER IL NUMERO DI RODC CHE TI SERVE EX SE 3 SCRIVI 1,4]")
                            try:
                                numero_rodc = input("SCRIVI IL NUMERO:")
                                inizio,fine = map(int, numero_rodc.split(","))

                                rodc_nome = []

                                for i in range(inizio,fine):
                                    rodc = input("SRIVI I NOMI DEI RODC:")
                                    rodc_nome.append(rodc)
                                print("[NOMI SALVATI ORA ENUMERO]")
                                try:
                                    for rodc in rodc_nome:
                                        print(f"[STO ENUMERANDO: {rodc}]")
                                        try:
                                            subprocess.run([f"""LDAPTLS_REQCERT=never ldapsearch -x -H ldap://{ip} -D "{nome_utente}@{dominio}" -w '{password_utente}' -Z -b "DC={configurazione_per_ldap},DC={configurazione_per_ldap2}" "(cn={rodc})"  cn msDS-RevealedUsers msDS-NeverRevealGroup msDS-RevealOnDemandGroup >> nomi_rodc_enum.txt"""], shell=True, check=True)
                                            print(f"[HO ENUMERATO CON SUCCESSO: {rodc}]")
                                        except subprocess.CalledProcessError:
                                            print(f"NON E STATO POSSIBILE ENUMERARE: {rodc}")
                                except:
                                    print("[NON E STATO POSSIBILE ENUMERARE I RODC]")
                            except:
                                print("[IL COMANDO NON E STATO ACCETTATO CONTROLLA IL FORMATO CHE DEVE ESSERE ESATTAMENTE 1,#]")
                    if "cn:" not in analisi:
                        print("[NEGATIVO PASSO AD CERTIPY]")
                except:
                    print("[NON E STATO POSSIBILE CONTROLLARE IL FILE controllo_ldap_search.txt]")
            except subprocess.CalledProcessError:
                print("[LA RISOLUZIONE HA FALLITO PASSO AD CERTIPY]")

    def certipy(self, ip, dominio, nome_utente, password_utente, rinomina2=None):
        if rinomina2 is None:
            rinomina2 = getattr(self, "rinomina2", None)
        print("[SCANALIZZO VULN ESC CON CERTIPY ATTENDI...]")
        try:
            subprocess.run([f"certipy-ad find -u '{nome_utente}' -p '{password_utente}' -d '{dominio}' -dc-ip {ip} -vulnerable >> certipy_scan.txt"], shell=True, check=True)
            print("[SCAN SALVATO CON SUCCESSO]")
        except subprocess.CalledProcessError:
            print("[SCAN FALLITO RISOLUZIONE PROBLEMI IN CORSO...]")
            try:
                if rinomina2:
                    os.environ["KRB5CCNAME"] = rinomina2
                else:
                    print("[NESSUN TGT DISPONIBILE, LA FALLBACK KERBEROS NON FUNZIONERA]")
                try:
                    subprocess.run([f"certipy-ad find -no-pass -k -u '{nome_utente}' -d '{dominio}' -dc-ip {ip} -vulnerable >> certipy_scan.txt "], shell=True, check=True)
                    print("[LA RISOLUZIONE PROBLEMI HA RISOLTO L'EQUIVOCO]")
                except subprocess.CalledProcessError:
                    print("[LA RISOLUZIONE PROBLEMI NON E RIUSCITA A RISOLVERE L'EQUIVOCO]")
                    print("[PASSO AL REPORT]")
            except:
                print("[LA RISOLUZIONE PROBLEMI HA FALLITO] (RAGIONE: TGT INESISTENTE)]")
                print("[PASSO AL REPORT]")
        print("[PASSO AL REPORT]")

    def report(self, ip, dominio, nome_utente, password_utente):
        print(r"===========================================================")
        print("|                      REPORT FINALE                        |")
        print(r"===========================================================")
        print("|                     RISULTATI SUL WEB                     |")
        print(r"===========================================================")
        with open ("nmap_scan.txt", "r") as f:
            risultato = f.read()
        if "80/tcp" in risultato or "443/tcp" in risultato:
            print("[+]---E PRESENTE UN SITO WEB")
        else:
            print("[-]---NON E PRESENTE NESSUN SITO")
        try:
            with open ("gobuster_scan.txt", "r") as f:
                gob = f.read()
            if "Status" in gob:
                print("=====================RISULTATI GOBUSTER====================")
                subprocess.run(["cat gobuster_scan.txt"], shell=True)
                print("===========================================================")
            if "Status" not in gob:
                print("[-]---GOBUSTER NON HA TROVATO NULLA")
        except:
            print("[-]---LO SCAN DI GOBUSTER NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        try:
            with open ("ferox_scan.txt", "r") as f:
                fer = f.read()
            if "/" in fer:
                print("====================RISULTATI FEROXBUSTER==================")
                subprocess.run(["cat ferox_scan.txt"], shell=True)
                print("===========================================================")
            if "/" not in fer:
                print("[-]---FEROXBUSTER NON HA TROVATO NULLA")
        except:
            print("[-]---LO SCAN DI FEROXBUSTER NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("")
        print("")
        print(r"===========================================================")
        print("|                   RISULTATI SUL TRAGET                    |")
        print(r"===========================================================")
        print("")
        print("")
        try:
            with open ("scrivibili.txt", "r") as f:
                scr = f.read()
            if "WRITE" in scr:
                print("=====================RISULTATI BLOODYAD====================")
                subprocess.run(["cat scrivibili.txt"], shell=True)
                print("===========================================================")
            if "WRITE" not in scr:
                print("[-]---BLOODYAD NON HA TROVATO NULLA")
        except:
            print("[-]---LO SCAN DI BLOODYAD NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("[INFO]---PER CONTROLLARE LA MODALITA ALL VAI ALLA SEZIONE DI BLOODYAD")
        print("===========================================================")
        print("")
        print("=======================RISULTATI NXC=======================")
        print("=======================GRUPPI LOCALI=======================")
        try:
            with open ("gruppi_locali.txt", "r") as f:
                scr = f.read()
            if "SMB" in scr:
                subprocess.run(["cat gruppi_locali.txt"], shell=True)
            if "SMB" not in scr:
                print("[-]---NXC NON HA TROVATO NULLA SUI GRUPPI LOCALI")
        except:
            print("[-]---LO SCAN DI NXC SUL PRIMO PROCESSO NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("==========================UTENTI===========================")
        try:
            with open ("utenti_smb.txt", "r") as f:
                ut = f.read()
            if "Administrator" in ut:
                subprocess.run(["cat utenti_smb.txt"], shell=True)
            if "Administrator" not in ut:
                print("[-]---NXC NON HA TROVATO UTENTI ")
        except:
            print("[-]---LO SCAN DI NXC SUL SECONDO PROCESSO NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("======================GRUPPI GENERALI======================")
        try:
            with open ("gruppi_generali.txt", "r") as f:
                gr = f.read()
            if "LDAP" in gr:
                subprocess.run(["cat gruppi_generali.txt | grep DC"], shell=True)
            if "LDAP" not in gr:
                print("[-]---NXC NON HA TROVATO I GRUPPI GENERALI ")
        except:
            print("[-]---LO SCAN DI NXC SUL TERZO PROCESSO NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("=====================UTENTI SU GRUPPO/I====================")
        try:
            with open ("utenti_su_gruppo.txt", "r") as f:
                nt = f.read()
            if "LDAP" in nt:
                subprocess.run(["cat utenti_su_gruppo.txt | grep DC"], shell=True)
            if "LDAP" not in nt:
                print("[-]---NXC NON HA TROVATO UTENTI SUL GRUPPO/I (PROVA A FARE IL CONTROLLO MANUALE SUL FILE)")
        except:
            print("[-]---LO SCAN DI NXC SUL QUARTO PROCESSO NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("=======================UTENTI SU GMSA======================")
        try:
            with open ("enum_gmsa.txt", "r") as f:
                sa = f.read()
            if "LDAP" in sa:
                subprocess.run(["cat enum_gmsa.txt"], shell=True)
            if "LDAP" not in sa:
                print("[-]---NXC NON HA TROVATO UTENTI GMSA")
        except:
            print("[-]---LO SCAN DI NXC SUL QUINTO PROCESSO NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("===========================================================")
        print("")
        print("===================RISULTATI LDAPSEARCH====================")
        print("===================RODC O DC SCRIVIBILI====================")
        try:
            with open ("controllo_ldap_search.txt", "r") as f:
                ld = f.read()
            if "dn:" in ld:
                subprocess.run(["cat controllo_ldap_search.txt"], shell=True)
            if "dn:" not in ld:
                print("[-]---LDAPSEARCH NON HA TROVATO RODC O DC SCRIVIBILI")
        except:
            print("[-]---LO SCAN DI LDAPSEARCH SUL PRIMO PROCESSO NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("========================ENUM DEI RODC======================")
        try:
            with open ("nomi_rodc_enum.txt", "r") as f:
                rc = f.read()
            if "dn:" in rc:
                subprocess.run(["cat nomi_rodc_enum.txt"], shell=True)
            if "dn:" not in rc:
                print("[-]---LDAPSEARCH NON E RIUSCITO AD ENUMERARE I RODC")
        except:
            print("[-]---LO SCAN DI LDAPSEARCH SUL SECONDO PROCESSO NON E STATO AVVIATO O E ANDATO IN FALLIMENTO")
        print("====================RISULTATI CERTIPY======================")
        try:
            with open ("certipy_scan.txt", "r") as f:
                cr = f.read()
            if "[!] Vulnerabilities" in cr:
                subprocess.run(["cat certipy_scan.txt"], shell=True)
            if "[!] Vulnerabilities" not in cr:
                print("[-]---CERTIPY NON HA TROVATO VULN")
        except:
            print("[-]---LO SCAN DI CERTIPY NON SI E AVVIATO O E ANDATO IN ERRORE")
        print("===========================================================")
        print("REPORT TERMINATO CON SUCCESSO!")
        print("ENUM TERMINATA CON SUCCESSO!")
        print("GRAZIE PER AVER USATO IL TOOL!")
        print("  .   . ")
        print(r" \\___//")
        print("===========================================================")
scanner = scan_windows()
scanner.configurazione()
