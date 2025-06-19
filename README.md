# ⏰ Conversión de Hora: Formato 12H a 24H

Este proyecto contiene una función en Python que convierte una hora desde el formato de 12 horas (AM/PM) al formato de 24 horas (también llamado formato militar).

---

## 📌 Ejemplo de entrada y salida

| Entrada (12h) | Salida esperada (24h) |
|---------------|------------------------|
| 07:05:45PM    | 19:05:45               |
| 12:01:00PM    | 12:01:00               |
| 12:01:00AM    | 00:01:00               |
| 01:00:00AM    | 01:00:00               |
| 11:59:59PM    | 23:59:59               |
| 04:30:00AM    | 04:30:00               |
| 08:15:45PM    | 20:15:45               |

---

## 🧠 Lógica de la conversión

- Si el formato es **AM** y la hora es `12`, se convierte a `00`.
- Si el formato es **PM** y la hora **no** es `12`, se le suman `12` horas.
- En cualquier otro caso, la hora se mantiene igual.

---

## 🧪 Cómo ejecutar el programa

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. Abre una terminal y navega hasta la carpeta del proyecto.

3. Ejecuta el archivo `.py` con el siguiente comando:
