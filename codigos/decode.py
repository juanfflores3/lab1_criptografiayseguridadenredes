from scapy.all import rdpcap, ICMP, IP, Raw
import string

# Palabras comunes en español para detección básica
PALABRAS_CLAVE = {"el", "la", "de", "que", "y", "en", "a", "los", "se", "del", "al", "por", "es", "con", "un"}

def cesar_descifrar(texto, desplazamiento):
    resultado = ''
    for c in texto:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base - desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado

def puntuar_texto(texto):
    palabras = texto.lower().split()
    coincidencias = sum(1 for p in palabras if p in PALABRAS_CLAVE)
    espacios = texto.count(' ')
    imprimibles = sum(1 for c in texto if c in string.printable)
    puntuacion_total = coincidencias * 10 + espacios + imprimibles / len(texto)
    return puntuacion_total

def analizar_paquetes(pcap_file):
    paquetes = rdpcap(pcap_file)
    letras = []

    for pkt in paquetes:
        if IP in pkt and pkt[IP].dst == "8.8.8.8" and ICMP in pkt and Raw in pkt:
            raw_payload = bytes(pkt[Raw].load)
            if len(raw_payload) > 16:
                letra = chr(raw_payload[16])  # Byte 17
                letras.append(letra)

    if not letras:
        print("No se detectaron caracteres en los paquetes.")
        return

    texto_cifrado = ''.join(letras)
    print(f"\nTexto cifrado detectado: {texto_cifrado}\n")
    print("Posibles combinaciones César (0–25):\n")

    candidatos = []
    for d in range(26):
        descifrado = cesar_descifrar(texto_cifrado, d)
        score = puntuar_texto(descifrado)
        candidatos.append((score, d, descifrado))

    candidatos.sort(reverse=True)
    mejor_puntaje = candidatos[0][0]

    for score, d, descifrado in candidatos:
        if score == mejor_puntaje:
            print(f"\033[92m[{d:02d}] {descifrado}\033[0m")  # verde
        else:
            print(f"[{d:02d}] {descifrado}")

if __name__ == '__main__':
    analizar_paquetes("paquetes.pcapng")


