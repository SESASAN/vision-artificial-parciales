import numpy as np

# Tabla parula(64) de MATLAB, copiada de https://github.com/BIDS/colormap/blob/master/parula.py
# (los derechos son de The MathWorks; matplotlib no trae este mapa de color).
PARULA = np.array([
    [0.2081, 0.1663, 0.5292],
    [0.2116, 0.1898, 0.5777],
    [0.2123, 0.2138, 0.6270],
    [0.2081, 0.2386, 0.6771],
    [0.1959, 0.2645, 0.7279],
    [0.1707, 0.2919, 0.7792],
    [0.1253, 0.3242, 0.8303],
    [0.0591, 0.3598, 0.8683],
    [0.0117, 0.3875, 0.8820],
    [0.0060, 0.4086, 0.8828],
    [0.0165, 0.4266, 0.8786],
    [0.0329, 0.4430, 0.8720],
    [0.0498, 0.4586, 0.8641],
    [0.0629, 0.4737, 0.8554],
    [0.0723, 0.4887, 0.8467],
    [0.0779, 0.5040, 0.8384],
    [0.0793, 0.5200, 0.8312],
    [0.0749, 0.5375, 0.8263],
    [0.0641, 0.5570, 0.8240],
    [0.0488, 0.5772, 0.8228],
    [0.0343, 0.5966, 0.8199],
    [0.0265, 0.6137, 0.8135],
    [0.0239, 0.6287, 0.8038],
    [0.0231, 0.6418, 0.7913],
    [0.0228, 0.6535, 0.7768],
    [0.0267, 0.6642, 0.7607],
    [0.0384, 0.6743, 0.7436],
    [0.0590, 0.6838, 0.7254],
    [0.0843, 0.6928, 0.7062],
    [0.1133, 0.7015, 0.6859],
    [0.1453, 0.7098, 0.6646],
    [0.1801, 0.7177, 0.6424],
    [0.2178, 0.7250, 0.6193],
    [0.2586, 0.7317, 0.5954],
    [0.3022, 0.7376, 0.5712],
    [0.3482, 0.7424, 0.5473],
    [0.3953, 0.7459, 0.5244],
    [0.4420, 0.7481, 0.5033],
    [0.4871, 0.7491, 0.4840],
    [0.5300, 0.7491, 0.4661],
    [0.5709, 0.7485, 0.4494],
    [0.6099, 0.7473, 0.4337],
    [0.6473, 0.7456, 0.4188],
    [0.6834, 0.7435, 0.4044],
    [0.7184, 0.7411, 0.3905],
    [0.7525, 0.7384, 0.3768],
    [0.7858, 0.7356, 0.3633],
    [0.8185, 0.7327, 0.3498],
    [0.8507, 0.7299, 0.3360],
    [0.8824, 0.7274, 0.3217],
    [0.9139, 0.7258, 0.3063],
    [0.9450, 0.7261, 0.2886],
    [0.9739, 0.7314, 0.2666],
    [0.9938, 0.7455, 0.2403],
    [0.9990, 0.7653, 0.2164],
    [0.9955, 0.7861, 0.1967],
    [0.9880, 0.8066, 0.1794],
    [0.9789, 0.8271, 0.1633],
    [0.9697, 0.8481, 0.1475],
    [0.9626, 0.8705, 0.1309],
    [0.9589, 0.8949, 0.1132],
    [0.9598, 0.9218, 0.0948],
    [0.9661, 0.9514, 0.0755],
    [0.9763, 0.9831, 0.0538],
])


def _a_unitario(img):
    arr = np.asarray(img)
    if arr.dtype == np.uint8:
        return arr.astype(np.float64) / 255.0
    return arr.astype(np.float64)


def _a_uint8(unitario):
    return np.clip(np.round(unitario * 255.0), 0, 255).astype(np.uint8)


def rgb_to_cmy(rgb):
    return 1.0 - _a_unitario(rgb)


def cmy_to_rgb(cmy):
    return _a_uint8(1.0 - cmy)


def rgb_to_cmyk(rgb):
    x = _a_unitario(rgb)
    k = 1.0 - x.max(axis=2)
    denom = 1.0 - k
    sin_negro = denom == 0
    seguro = np.where(sin_negro, 1.0, denom)
    cmy = (1.0 - x - k[..., None]) / seguro[..., None]
    cmy = np.where(sin_negro[..., None], 0.0, cmy)
    return np.dstack([cmy, k])


def cmyk_to_rgb(cmyk):
    c = cmyk[..., :3]
    k = cmyk[..., 3:4]
    return _a_uint8((1.0 - c) * (1.0 - k))


def rgb_to_hsi(rgb):
    x = _a_unitario(rgb)
    r, g, b = x[..., 0], x[..., 1], x[..., 2]
    i = (r + g + b) / 3.0
    con_brillo = i > 0
    s = np.where(con_brillo, 1.0 - x.min(axis=2) / np.where(con_brillo, i, 1.0), 0.0)
    num = 0.5 * ((r - g) + (r - b))
    den = np.sqrt((r - g) ** 2 + (r - b) * (g - b))
    con_tono = den > 1e-12
    coseno = np.where(con_tono, num / np.where(con_tono, den, 1.0), 1.0)
    theta = np.degrees(np.arccos(np.clip(coseno, -1.0, 1.0)))
    h = np.where(b <= g, theta, 360.0 - theta)
    h = np.where(con_tono, h, 0.0)
    return np.dstack([h / 360.0, s, i])


def hsi_to_rgb(hsi):
    h = hsi[..., 0] * 360.0
    s = hsi[..., 1]
    i = hsi[..., 2]
    hh = np.mod(h, 120.0)
    plano = i * (1.0 - s)
    rampa = i * (1.0 + s * np.cos(np.radians(hh)) / np.cos(np.radians(60.0 - hh)))
    resto = 3.0 * i - (plano + rampa)
    sector1 = h < 120.0
    sector2 = (h >= 120.0) & (h < 240.0)
    r = np.where(sector1, rampa, np.where(sector2, plano, resto))
    g = np.where(sector1, resto, np.where(sector2, rampa, plano))
    b = np.where(sector1, plano, np.where(sector2, resto, rampa))
    return _a_uint8(np.dstack([r, g, b]))
