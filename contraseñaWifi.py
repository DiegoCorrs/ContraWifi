
import subprocess

nombre_wifi = input("ingresa el nombre de la red wifi: ")

try:

    resultados = subprocess.check_output(
        ["netsh", "wlan", "show", "profile", nombre_wifi, "key=clear"],
        shell=True).decode("utf-8", errors="backslashreplace")

    # si el sistema está en ingles se ingresa "Key Content"    
    if "Contenido de la clave" in resultados:
        for line in resultados.split("\n"):
            if "Contenido de la clave" in line:
                password = line.split(":")[1].strip()
                print(f"la contraseña de la red {nombre_wifi} es: {password}")
                break
    else:
        print(f"no se pudo encontrar la contraseña para la red {nombre_wifi}")

except subprocess.CalledProcessError:
    print(f"no se pudo obtener la información del perfil {nombre_wifi}")

                




