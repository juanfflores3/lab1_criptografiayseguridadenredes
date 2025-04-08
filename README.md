# 🕵️‍♂️ Proyecto de Cifrado y Análisis con Wireshark

Este proyecto permite cifrar un mensaje utilizando el cifrado César, enviarlo mediante paquetes ICMP, capturarlos con Wireshark y luego descifrarlo a partir de los datos obtenidos.

---

## 📦 Requisitos

- Python 3
- Wireshark

---

## 🚀 Instrucciones de Uso

1. **Clonar el repositorio**  
   Descarga el repositorio y abre la carpeta `codigos`.

2. **Iniciar captura en Wireshark**  
   Abre Wireshark y comienza a capturar en la interfaz de red correspondiente.

3. **Cifrar el mensaje**  
   Ejecuta el script `cesar.py`, ingresando el mensaje y el desplazamiento deseado.  
   ```bash
   python3 cesar.py "Mensaje a cifrar" 9
