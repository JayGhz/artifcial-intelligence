# Partes del Robot Choreographe

## Joints (Articulaciones)

### Cabeza
* **HeadYaw**: Rotación horizontal
* **HeadPitch**: Rotación vertical

### Hombro Izquierdo
* **LShoulderPitch**: Rotación frontal
* **LShoulderRoll**: Rotación lateral

### Codo Izquierdo
* **LElbowYaw**: Rotación del codo
* **LElbowRoll**: Flexión del codo

### Muñeca Izquierda
* **LWristYaw**: Rotación de la muñeca

### Mano Izquierda
* **LHand**: Apertura y cierre

### Cadera Izquierda
* **LHipYawPitch**: Rotación y elevación
* **LHipRoll**: Rotación lateral
* **LHipPitch**: Rotación frontal

### Rodilla Izquierda
* **LKneePitch**: Flexión de la rodilla

### Pie Izquierdo
* **LAnklePitch**: Flexión del tobillo
* **LAnkleRoll**: Rotación lateral del tobillo

> **Nota**: Las articulaciones del lado derecho siguen el mismo patrón, reemplazando 'L' por 'R' (Right)

## Sensores

### Sensores Táctiles
* 3 sensores capacitivos en la cabeza
  * Detección táctil para interacción
* 3 sensores táctiles en cada mano
  * Detección de contacto y manipulación

### Sensores de Impacto y Distancia
* 2 bumpers en los pies
  * Detección de colisiones
* 4 sonares en el pecho
  * Detección de obstáculos
  * Medición de distancia

### Sensores de Visión
* 2 cámaras en la cabeza
  * Cámara superior
  * Cámara inferior

### Sensores de Balance y Presión
* Sensores de fuerza en los pies (FSR)
  * Medición de presión y distribución del peso
* Giroscopio y acelerómetro
  * Control de equilibrio
  * Detección de orientación