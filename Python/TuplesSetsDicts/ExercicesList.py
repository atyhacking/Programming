#Lista de ejercicios basicos de python
#Aqui ire realizando todos los ejercicios de clase por apartados y orden


#----------------------------------------------------------------------------------------------------------------------------------------------
#Ejercicios sobre tuplas, diccionarios y sets 
#Ejercicios de https://campus.enti.cat/pluginfile.php/30228/mod_resource/content/1/Exercises____Introduction_to_Programming__Python_.pdf
#ExercicesList.pdf

def Ejercicio1_Tuplas():
    #Las tuplas son inmutables y ordenadas
    admin_credentials = ("admin", "root", "P@ssw0rd")
    print("La tupla es: ",admin_credentials)
    print("La longitud de la tupla es: ",{len(admin_credentials)})
    return

def Ejercicio2_Tuplas():
    ports = (22, 443, 80, 21, 8080)
    print("The first port is: ",ports[0], ", And the last port is: ",ports[-1])
    if 22 in ports:
        print("El puerto 22 esta en la lista de puertos")
    else:
        print("El puerto 22 no esta en la lista de puertos")
    return   

def Ejercicio3_Tuplas():
    user_roles = ("admin", "user", "guest")
    try:
        user_roles[1] = "superuser"
    except TypeError as e:
        print(f"Error: {e}")
    return

def Ejercicio4_Tuplas():
    server_info = ("192.168.1.10", "web_server", "active")
    ip, role, status = server_info 
    print(f"La ip es {ip}")
    print(f"El rol es: {role}")
    print(f"El estado es: {status}")
    return

def Ejercicio5_Diccionarios():
    #Los diccionarios son mutables y desordenados. Siempre tienen clave-valor
    firewall_rules = {"inbound" : ["SSH", "HTTPS"],"outbound" : ["DNS", "SMTP"]}
    print(firewall_rules)
    return

def Ejercicio6_Diccionarios():
    firewall_rules = {"inbound" : ["SSH", "HTTPS"],"outbound" : ["DNS", "SMTP"]}
    print(firewall_rules["inbound"], firewall_rules["outbound"])
    blocked_rules =  firewall_rules.get("blocked")
    if blocked_rules is None:
        print("There is none blocked rules")
    else:
        print("There is blocked rules")
    return

def Ejercicio7_Diccionarios():
    firewall_rules = {"inbound" : ["SSH", "HTTPS"],"outbound" : ["DNS", "SMTP"]}
    print(firewall_rules["inbound"], firewall_rules["outbound"])
    firewall_rules["blocked"] = {"FTP","Telnet"}
    blocked_rules =  firewall_rules.get("blocked")
    if blocked_rules is None:
        print("There is none blocked rules")
    else:
        print("There is blocked rules")
    return

def Ejercicio8_Diccionarios():
    attack_signatures = {"SQL InjectionDenial of Service (DoS)" : ["SQL Query"], 
                         "Cross-Site Scripting (XSS)" : ["JavaScript code"],
                         "Denial of Service (DoS)" : ["traffic overload"]}
    attack_signatures["Brute Force"] = {"Multiple failed logging attempts"}
    return

def Ejercicio9_Sets():
    #Los conjuntos son desordenados, sin duplicados y mutables
    detected_ips = {"192.168.1.1", "10.0.0.2","192.168.1.1"}
    print(detected_ips)
    return

def Ejercicio10_Sets():
    secure_ips = {"192.168.1.1", "10.0.0.2"}
    insecure_ips = {"10.0.0.2", "172.16.0.1"}
    union_ips = secure_ips | insecure_ips
    print("Union IPs: ", union_ips)
    return

def Ejercicio11_Sets():
    secure_ips = {"192.168.1.1", "10.0.0.2"}
    insecure_ips = {"10.0.0.2", "172.16.0.1"} 
    difference_ips = secure_ips - insecure_ips
    print(f"Las IPs seguras que no estan en las IPs inseguras son: ", difference_ips) 
    return

def Ejercicio12_Sets():
    known_hashes = {"abc123", "def456", "ghi789"}
    suspicious_hashes = {"ghi789", "xyz123", "abc123"}
    common_hashes = known_hashes & suspicious_hashes
    difference_hashes = suspicious_hashes - known_hashes
    print(f"Los hashes comunes son: ", common_hashes)
    print(f"Los hashes que estan el sospicious pero no en common son: ", difference_hashes)
    return

#----------------------------------------------------------------------------------------------------------------------------------------------
#Para ejecutar ejercicio ejecuta la funcion correspondiente al ejercicio

Ejercicio12_Sets()
