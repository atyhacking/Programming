import hashlib

data = 0  # Inicia como un número entero

target_hash = "b026324c6904b2a9cb4b88d6d61c81d1"  # Hash objetivo

while True:
    # Convierte el número a cadena y calcula su hash
    hash_object = hashlib.md5(str(data).encode())
    hash_hex = hash_object.hexdigest()

    # Imprime el estado actual
    print(f"{hash_hex} - {target_hash}")

    # Si coincide, rompe el bucle
    if hash_hex == target_hash:
        print(f"¡Coincidencia encontrada! {data}")
        break

    # Incrementa el valor de data
    data += 1
