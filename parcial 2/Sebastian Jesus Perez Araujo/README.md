# Momento Evaluativo 2 — Visión Artificial

Solución de los 5 puntos del taller de histogramas, filtrado espacial y
detección/realce de bordes (numpy, OpenCV y scikit-image).

## Requisitos

- Python 3
- Las dependencias listadas en `../requirements.txt` (numpy, opencv-contrib-python,
  scikit-image, matplotlib, pillow, jupyter) — es el mismo entorno compartido
  con `parcial 1`, ver el README en la raíz del repositorio.

## Instalación

Desde la raíz del repositorio (un nivel arriba de esta carpeta), crear el
entorno virtual:

```bash
python3 -m venv .venv
```

Activarlo:

```bash
# Linux / macOS
source .venv/bin/activate
```

```bat
:: Windows (cmd)
.venv\Scripts\activate.bat
```

```powershell
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Con el entorno activado, instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar solo desde `codigo/`

Cada punto tiene su propio script `.py` en `codigo/`, en el mismo orden que
el enunciado. Los scripts usan rutas relativas (`../images`, `../results`),
así que hay que ejecutarlos **desde dentro de `parcial 2/codigo/`**, con el
entorno virtual activado:

```bash
cd "parcial 2/codigo"
python 00_preparacion.py
python 01_punto1.py
python 02_punto2.py
python 03_punto3.py
python 04_punto4.py
python 05_punto5.py
```

`00_preparacion.py` debe correrse primero: carga la imagen generada con IA
(`images/mi_imagen.png`), que usan todos los demás puntos.

Cada script guarda sus imágenes resultado en `../results/` (es decir,
`results/` en esta misma carpeta del parcial).

## Contenido de cada script

| Script | Punto | Qué hace |
|---|---|---|
| `00_preparacion.py` | — | Carga la imagen generada con IA |
| `01_punto1.py` | 1 | Histograma, ecualización, niveles de intensidad más probables |
| `02_punto2.py` | 2 | Especificación de histograma contra `Referencia.tif` |
| `03_punto3.py` | 3 | Ruido (uniforme/gaussiano/sal y pimienta) + 9 filtros + tabla SSIM |
| `04_punto4.py` | 4 | Detección de bordes: Sobel (kernels dados) y Laplaciano de 8 vecinos |
| `05_punto5.py` | 5 | Realce de bordes: Laplaciano de 4 y 8 vecinos |

## Notebooks

El mismo código también está disponible como notebooks de Jupyter en
`notebooks/`, con el enunciado de cada punto en celdas de markdown. Para
usarlos:

```bash
jupyter notebook notebooks/
```
