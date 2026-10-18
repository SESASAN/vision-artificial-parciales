# Momento Evaluativo 3 — Visión Artificial

Solución de los 8 puntos del taller de procesamiento del color: espacios de
color (CMY, CMYK, HSI, YCbCr, YIQ), transformaciones sobre componentes y
corrección de balance de color (numpy, OpenCV y scikit-image).

## Requisitos

- Python 3
- Las dependencias listadas en `../requirements.txt` (numpy, opencv-contrib-python,
  scikit-image, matplotlib, pillow, jupyter) — es el mismo entorno compartido
  con `parcial 1` y `parcial 2`, ver el README en la raíz del repositorio.

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
así que hay que ejecutarlos **desde dentro de `parcial 3/codigo/`**, con el
entorno virtual activado:

```bash
cd "parcial 3/codigo"
python 00_preparacion.py
python 01_punto1.py
python 02_punto2.py
python 03_punto3.py
python 04_punto4.py
python 05_punto5.py
python 06_punto6.py
python 07_punto7.py
python 08_punto8.py
```

`00_preparacion.py` debe correrse primero: recorta al centro la imagen generada
con IA (`images/mi_imagen_original.png`, de 1248x832), la redimensiona a
1024x1024x3 y la guarda como `images/mi_imagen.png`, que usan los puntos 1 a 7.
También valida las conversiones entre espacios de color.

Las conversiones que no existen en scikit-image (CMY, CMYK, HSI) viven en
`colorspaces.py`, en la raíz de esta carpeta; los notebooks y scripts lo
importan con `sys.path.append("..")`.

Cada script guarda sus imágenes resultado en `../results/` (es decir,
`results/` en esta misma carpeta del parcial).

## Contenido de cada script

| Script | Punto | Qué hace |
|---|---|---|
| `00_preparacion.py` | — | Recorta y redimensiona la imagen generada con IA a 1024x1024x3 y valida las conversiones entre espacios de color |
| `01_punto1.py` | 1 | Escala de grises con `rgb2gray` y negativo del mapa de color parula; RGB del nivel 170 |
| `02_punto2.py` | 2 | Componentes R, G, B, C, M, Y, K, Saturación, Tono e Intensidad |
| `03_punto3.py` | 3 | YCbCr: negativo de la log sobre Cr |
| `04_punto4.py` | 4 | YIQ: gamma γ=1.5 sobre Y y Q por -1 |
| `05_punto5.py` | 5 | CMY: lineal a trozos sobre Amarillo (r1=80, r2=210, s1=60, s2=120) |
| `06_punto6.py` | 6 | HSI: ecualización del histograma |
| `07_punto7.py` | 7 | Realce de bordes con Laplaciano de 4 vecinos sobre la imagen RGB |
| `08_punto8.py` | 8 | Corrección de balance de color en CMY (SSIM > 0.99 contra `imagen_objetivo.tiff`) |

## Notebooks

El mismo código también está disponible como notebooks de Jupyter en
`notebooks/`, con el enunciado de cada punto en celdas de markdown. Para
usarlos:

```bash
jupyter notebook notebooks/
```
