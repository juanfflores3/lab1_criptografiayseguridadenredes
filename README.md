# 🕵️‍♂️ Laboratorio 1 Criptografía y seguridad en redes: Cifrado y Análisis con Wireshark

Este proyecto permite cifrar un mensaje utilizando el cifrado César, enviarlo mediante paquetes ICMP, capturarlos con Wireshark y luego descifrarlo a partir de los datos obtenidos.

---

## 📦 Requisitos

- Python 3
- Wireshark

---

## 🚀 Instrucciones de Uso

1. **Clonar el repositorio**  
   Clona este repositorio y abre la carpeta `codigos`:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio/codigos
   ```

2. **Iniciar captura en Wireshark**  
   Abre Wireshark y comienza a capturar en la interfaz de red que estés utilizando (por ejemplo: `eth0`, `wlan0`, etc.).

3. **Cifrar el mensaje**  
   Ejecuta el script `cesar.py`, indicando el mensaje a cifrar y el desplazamiento (offset).  
   Ejemplo:
   ```bash
   python3 cesar.py "Mensaje a cifrar" 9
   ```

4. **Filtrar en Wireshark**  
   En Wireshark, aplica el siguiente filtro para ver solo los paquetes relevantes:
   ```
   icmp && ip.dst == 8.8.8.8
   ```

5. **Guardar la captura**  
   Guarda la captura como archivo `.pcap` desde **File > Save As** en Wireshark.

6. **Descifrar el mensaje**  
   Ejecuta el script `decode.py` para descifrar el mensaje desde los paquetes:
   ```bash
   python3 decode.py
   ```

---

## 📁 Estructura del Laboratorio

```
codigos/
├── cesar.py       # Cifra el mensaje y lo envía como paquetes ICMP
├── decode.py      # Lee la captura y descifra el mensaje
```



