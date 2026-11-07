import numpy as np
from astropy.io import fits

def calcular_g_rn(flat1_path, flat2_path, bias1_path, bias2_path, filtro):
    print(f"\n{'='*15} Filtro {filtro} {'='*15}")
    
    # 1. Leer imágenes y recortar la región central [1000:2000, 1000:2000]
    # Convertimos a 'float' inmediatamente. Esto es CRÍTICO porque las imágenes 
    # originales son 'ushort' (enteros sin signo) y al restar darían errores de 
    # desbordamiento (números negativos gigantes) si no las pasamos a float.
    flat1 = fits.getdata(flat1_path)[1000:2000, 1000:2000].astype(float)
    flat2 = fits.getdata(flat2_path)[1000:2000, 1000:2000].astype(float)
    bias1 = fits.getdata(bias1_path)[1000:2000, 1000:2000].astype(float)
    bias2 = fits.getdata(bias2_path)[1000:2000, 1000:2000].astype(float)
    
    # 2. Medias de un flat y un bias
    mean_F = np.mean(flat1)
    mean_B = np.mean(bias1)
    S = mean_F - mean_B  # Señal neta en ADU
    
    # 3. Diferencias (eliminan el polvo, viñeteo y estructura espacial)
    dflat = flat1 - flat2
    dbias = bias1 - bias2
    
    # 4. Varianzas de las diferencias (ddof=1 para usar varianza muestral, igual que IRAF)
    var_dflat = np.var(dflat, ddof=1)
    var_dbias = np.var(dbias, ddof=1)
    
    # 5. Varianzas de una sola imagen (la varianza de la resta es la suma de las varianzas)
    var_F = var_dflat / 2.0
    var_B = var_dbias / 2.0
    
    # 6. Cálculo de Ganancia (g) y Ruido de Lectura (RN)
    ganancia = S / (var_F - var_B)
    ruido_lectura = ganancia * np.sqrt(var_B)
    
    # Impresión de resultados
    print(f"Media Flat (ADU):       {mean_F:.2f}")
    print(f"Media Bias (ADU):       {mean_B:.2f}")
    print(f"Señal (F - B) (ADU):    {S:.2f}")
    print(f"Varianza Flat (ADU^2):  {var_F:.4f}")
    print(f"Varianza Bias (ADU^2):  {var_B:.4f}")
    print(f"--> Ganancia (g):       {ganancia:.3f} e-/ADU")
    print(f"--> Ruido de Lectura:   {ruido_lectura:.2f} e-")
    
    return ganancia, ruido_lectura

# ==============================
# Ejecución para Filtro B
# ==============================
g_B, rn_B = calcular_g_rn(
    flat1_path='domeflat_B/domeflat_Flat_B_90_secs_001.fits',
    flat2_path='domeflat_B/domeflat_Flat_B_90_secs_002.fits',
    bias1_path='Bias/domeflat_Bias_1_secs_019.fits',
    bias2_path='Bias/domeflat_Bias_1_secs_020.fits',
    filtro='B'
)

# ==============================
# Ejecución para Filtro V
# ==============================
g_V, rn_V = calcular_g_rn(
    flat1_path='domeflat_V/domeflat_Flat_V_40_secs_001.fits',
    flat2_path='domeflat_V/domeflat_Flat_V_40_secs_002.fits',
    bias1_path='Bias/domeflat_Bias_1_secs_023.fits',
    bias2_path='Bias/domeflat_Bias_1_secs_024.fits',
    filtro='V'
)
