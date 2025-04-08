import sys
import subprocess

def cifrado_cesar(texto, desplazamiento):
    resultado = ''
    for caracter in texto:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
        else:
            resultado += caracter
    return resultado

def enviar_icmp_por_caracter(texto_cifrado, relleno='espacio'):
    for c in texto_cifrado:
        char_hex = c.encode().hex()

        if relleno == 'espacio':
            filler = '20'
        else:
            filler = '00'

        payload = char_hex + filler * 19  # 1 carácter + 19 bytes de relleno = 20 bytes (40 caracteres hex)
        print(f"Enviando '{c}' con payload ICMP (hex: {payload})...")
        try:
            subprocess.run(["ping", "-c", "1", "-p", payload, "8.8.8.8"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Error al enviar '{c}': {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 cesar.py \"Texto plano\" [desplazamiento]")
        sys.exit(1)

    texto_plano = sys.argv[1]
    desplazamiento = 13  # por defecto

    if len(sys.argv) >= 3:
        try:
            desplazamiento = int(sys.argv[2])
        except ValueError:
            print("El desplazamiento debe ser un número entero.")
            sys.exit(1)

    texto_cifrado = cifrado_cesar(texto_plano, desplazamiento)
    print("Texto cifrado:", texto_cifrado)

    # Puedes cambiar a relleno='cero' si prefieres 0x00
    enviar_icmp_por_caracter(texto_cifrado, relleno='espacio')



