#Lista de ejercicios basicos de python
#Aqui ire realizando todos los ejercicios de clase por apartados y orden


#----------------------------------------------------------------------------------------------------------------------------------------------
#Ejercicios sobre tuplas, diccionarios y sets 
#Ejercicios de https://campus.enti.cat/pluginfile.php/30228/mod_resource/content/1/Exercises____Introduction_to_Programming__Python_.pdf
#ExercicesList.pdf

#----------------------------------------------------------------------------------------------------------------------------------------------
#Para ejecutar ejercicio ejecuta la funcion correspondiente al ejercicio


def Exercice1_Tuples():
    admin_credentials = ("admin", "root", "P@ssword")
    print(f"La tupla es: {admin_credentials}")
    print(f"La longitud de la tupla es: {len(admin_credentials)}")

def Exercice2_Tuples():
    ports = (22, 443, 80, 21, 8080)

    print(f"El primer elemento es {ports[0]} , y el ultimo elemento es {ports[len(ports)-1]}")
    if 22 in ports:
        print("El puerto 22 esta activado")
    else:
        print("El puerto 22 no esta activado")

def Exercice3_Tuples():
    user_roles = ("admin", "user", "guest")
    try:
        user_roles[1] = "superuser"
    except TypeError:
        print("Error: No puedes modificar la tupla")

def Exercice4_Tuples():
    server_info = ("192.168.1.10", "web_server", "active")
    ip, role, status = server_info
    print(f"IP: {ip}, Role: {role}, Status: {status}")

def Exercice5_Dictionaries():
    firewall_rules = {"inbound":["SSH", "HTTPS"], "outbound":["DNS", "SMTP"]}
    print(firewall_rules)

def Exercice6_Dicctionaries():
    firewall_rules = {"inbound":["SSH", "HTTPS"], "outbound":["DNS", "SMTP"]}
    print(firewall_rules["inbound"], firewall_rules["outbound"])
    blocked = firewall_rules.get("blocked")
    if blocked is None:
        print("There is not blocked")
    else:
        print("There is blocked")
    
def Exercice7_Dictionaries():
    firewall_rules = {"inbound":["SSH", "HTTPS"], "outbound":["DNS", "SMTP"]}
    firewall_rules["blocked"] = {"FTP","Telnet"}
    print(firewall_rules)

def Exercice8_Dictionaries():
    attack_signatures = {"SQL Injection": ["SQL query"],
                        "Cross-Site Scripting(XSS)": ["Javascript"], 
                        "Denial of Service (DoS) code":"traffic overload"}
    attack_signatures["Brute Force"] = {"Multiple failed logging attempts"}
    print(attack_signatures)

def Exercice9_Sets():
    detected_ips = {"192.168.1.1", "10.0.0.2", "192.168.1.1"}
    print(detected_ips)

def Exercice10_Sets():
    secure_ips = {"192.168.1.1", "10.0.0.2"}
    insecure_ips = {"10.0.0.2", "172.16.0.1"}

    all_ips = secure_ips | insecure_ips
    print(f"Todas las IPs son {all_ips}")

def Exercice11_Sets():
    secure_ips = {"192.168.1.1", "10.0.0.2"}
    insecure_ips = {"10.0.0.2", "172.16.0.1"}  
    difference_ips = secure_ips - insecure_ips
    print(f"La diferencia de ips son: {difference_ips}")

def Exercice12_Sets():
    known_hashes = {"abc123", "def456", "ghi789"}
    suspicious_hashes = {"ghi789", "xyz123", "abc123"}
    common_hashes = known_hashes & suspicious_hashes
    difference_hashes = suspicious_hashes - known_hashes

    print(f"Common: {common_hashes}, Difference: {difference_hashes}")


#Ejecución
Exercice12_Sets()
