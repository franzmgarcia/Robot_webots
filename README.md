# Simulación movimiento de articulación

Para este proyecto,se desarrollaron una serie de instrucciones a fin de permitir el movimiento del brazo robótico del robot Teo de la Universidad Carlos III de Madrid, mediante el software de código abierto Webots.

En este caso en particular, se trata de la solución de un problema de cinemática que consiste en el movimiento de una articulación, en este caso el brazo del robot, a través de dos funciones implementadas: fwdKin() que recibe como parámetros, para un caso de 2 grados de libertad, dos ángulos y la función invKin(), que recibe para un caso de 2 grados de libertad, 2 coordenadas. 

La función fwdKin se encarga de obtener la posición en X y Z dado un ángulo para el hombro y otro ángulo para el codo, ambos en radianes, mientras que también es posible a través de la función invKin(). obtener las posiciones X y Z en las que se va a encontrar el robot, de manera que si es imposible alcanzar dichos objetivos solo con el movimiento de la articulación, se obtenga un mensaje de error. 

Para el código desarrollado en, se tiene una secuencia de 10 movimientos, que van desde un movimiento de los brazos semi extendidos hacia arriba, hacia una posición completamente opuesta, simulando algunos movimientos y posiciones que puede tener un movimiento convencional de un brazo humano.

Para indicar el trazado de estos movimientos, se toma una posición inicial de 45 grados tanto para el ángulo del codo como del hombro, y se obtienen sus posiciones equivalentes en X y Z. A estas posiciones en X y Z, se le suma o resta, dependiendo del movimiento buscado, una cantidad, que debe asegurar que el movimiento buscado no se extienda fuera del alcance del robot, o que se encuentre en una posición que el robot no pueda realizar. En ambos casos, se tienen señales de error en caso de un error en las posiciones buscadas.



