# Ejecución — Parcial 2 (código)

Scripts `.py` del Momento Evaluativo 2, uno por punto, equivalentes a los
notebooks en `../notebooks/`.

## Requisitos

Entorno virtual compartido del repositorio, activado (ver el README en la
raíz):

```bash
source ../../.venv/bin/activate   # Linux/macOS
# ..\..\.venv\Scripts\activate    # Windows
```

## Ejecutar

Los scripts usan rutas relativas (`../images`, `../results`), así que hay
que correrlos **desde dentro de esta carpeta**, en orden:

```bash
python 00_preparacion.py
python 01_punto1.py
python 02_punto2.py
python 03_punto3.py
python 04_punto4.py
python 05_punto5.py
```

`00_preparacion.py` debe ir primero: carga la imagen generada con IA
(`../images/mi_imagen.png`) que usan todos los demás puntos.

Cada script guarda sus imágenes de resultado en `../results/`.

## Contenido de cada script

| Script | Punto | Qué hace |
|---|---|---|
| `00_preparacion.py` | — | Carga la imagen generada con IA |
| `01_punto1.py` | 1 | Histograma, ecualización, niveles más probables |
| `02_punto2.py` | 2 | Especificación de histograma contra `Referencia.tif` |
| `03_punto3.py` | 3 | Ruido (uniforme/gaussiano/sal y pimienta) + 9 filtros + tabla SSIM |
| `04_punto4.py` | 4 | Detección de bordes: Sobel y Laplaciano de 8 vecinos |
| `05_punto5.py` | 5 | Realce de bordes: Laplaciano de 4 y 8 vecinos |
