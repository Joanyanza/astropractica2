Datos: Adjunto encontrará los datos para la práctica de reducción y fotometría. 

Objetivo: El trabajo consiste en esencia en realizar la reducción completa para el cúmulo MEL25 y hacer la fotometría en los filtros BV tomados con la CCD-FLI ML0900 (alias TUCAN) instalada en el observatorio de La Silla (Observatory= la silla)

Usted tendrá acceso a una serie de imágenes de calibración que consta de:
1. Una serie de imágenes Bias
2. Una serie de domeFlat para filtro B (Exptime=90sec) y V (Exptime=40sec)*
3. Una serie de Darks
4. Dos imágenes del cúmulo MEL25 en los filtros BV  (Exptime=90sec)

Nota: *Hacer caso omiso a la diferencia de tiempo, no es lo ideal.

El trabajo de ustedes consiste en realizar la reducción de datos de la manera más rigurosa posible.

PASO 1. Reconstruya la(s) noche(s) de observación hora a hora a partir de los datos.

Analice los datos que se le proveen. Construya una tabla que resuma los datos que dispone y sus características principales: Archivo, tipo de objeto, cantidad de archivos, tiempo de exposición, fecha de observación, hora de observación, observatorio, cámara y demás  información que considere pertinente.

Aviso importante: Para graficar las imágenes completas en el ds9 agregue al final de la línea lo siguiente: fill+ zscale-

Por ejemplo:   display imagen1.fits 1 fill+ zscale-


PASO 2. Con las imágenes que tiene determine la ganancia y el ruido de
lectura para cada filtro, lo necesitarán para la fotometria (Recuerden que esto lo hicieron en una práctica anterior)


PASO 3. Ajuste y sustracción del overscan
-Las imágenes poseen dos overscan, uno sobre las líneas y otro sobre las columnas.
-Estudie qué hacen las tareas colbias y linebias.
-Tome una de las imágenes domeflat y analice muy bien la primera región del overscan con implot (no tenga en cuenta todavía la segunda región de overscan). Use colbias sobre los rangos definidos para la trim section y la bias section.
-Sobre la imagen del resultado anterior, use linebias para ajustar y sustraer la segunda región de overscan (Nota: debe usar nuevamente implot para analizar la segunda región del overscan).
-Si el resultado le satisface, haga lo mismo para todas las imágenes (Recuerde que se pueden usar listas).


PASO 4a. Contrucción de supercalibraciones: Masterbias

    Revise la ayuda de iraf/pyraf para las tareas imcombine, zerocombine, darkcombine, flatcombine y describa qué hace cada una de ellas. ¿Necesitan esas tareas parámetros que se encuentren en el header de las imágenes?
    -Use las tareas para construir el Masterbias. Analice la imagen resultante.
    PASO 4b. Contrucción de supercalibraciones: Masterdark
    Use las tareas para construir el Masterdark. Analice la imagen resultante.
    PASO 4c. Contrucción de supercalibraciones: Masterflat
    Separe cada domeflat según el filtro.
    -Visualice cada imagen del conjunto en el ds9. Fíjese que en cada imagen la posición de las estrellas haya cambiado. Elimine las imágenes donde no ocurra esto o donde hayan imágenes saturadas.
    -Use flatcombine para combinar todas las imágenes en cada filtro.
    PASO 5. REDUCCIÓN DE IMÁGENES DE CIENCIA
    -Reduzca las imagenes por bias y por dark
    -Normalice los Flats respecto a la moda y aplique las correcciones de Flat a las imágenes de ciencia.
    -Analice los resultados finales.
    Pd. Se adjunta una imagen del resultado esperado en la reducción
    ENTREGABLE: 
    Un informe de carácter técnico (máximo 6 páginas) que contenga estrictamente los siguientes 5 items:
    1: Tabla de Bitácora de Observación completada tras explorar las cabeceras FITS con hselect / imhead.
    2: Tabla con la Ganancia y Ruido de Lectura calculados por filtro (B y V).
    3: Perfiles de implot (antes y después) demostrando el ajuste y sustracción del overscan bidimensional (colbias y linebias).
    4: Tabla de imstat e inspección visual de los Masterbias, Masterdark, Masterflats B y V.
    5: Muestra visual en DS9 de la imagen de Mel25 antes y después de ccdproc, junto con el cálculo de la reducción del ruido de fondo.
    Comprimido ZIP con los datos calibrados (Ejemplo: Mel25_Reducidos.zip):
    Deberán incluir únicamente los dos archivos FITS de ciencia finales calibrados:
    mel25_B_red_apellidosgrupo.fits
    mel25_V_red_apellidosgrupo.fits

