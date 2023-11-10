Equipo: Qutips

Integrantes:
Areli Yesareth Guerrero Estrada
Janeth De Anda Gil
Miguel Alejandro Medina Armendariz
Edgar Omar Mendoza Lopez

En el archivo main.ipynb se encuentra la propuesta desarrollada


Las redes neuronales hibridas funcionan combinando capas de redes neuronales clásicas con circuitos cuánticos. Las redes neuronales híbridas nos permiten aprovechar las fortalezas de la computación cuántica y clásica. Al integrar elementos cuánticos en redes neuronales, podemos aprovechar la ventaja cuántica para tareas específicas. Esta característica es crucial para abordar desafíos complejos del mundo real.

Aprendizaje automático: Las redes neuronales híbridas pueden mejorar los modelos clásicos de aprendizaje automático, haciéndolos más capaces de manejar tareas complejas y grandes conjuntos de datos.

Qiskit cuenta con una biblioteca que permite integrar los circuitos cuánticos dentro de las capas de las redes neuronales. 

Para poder implementar se debe tomar en cuenta:

1. Importar las bibliotecas necesarias:
- Importar Qiskit para creación y ejecución de circuitos cuánticos.
- Importar bibliotecas de PyTorch para operaciones clásicas de redes neuronales.

2. Definir el circuito cuántico:
- Crear un circuito cuántico en Qiskit.
- Definir lo elementos a parametrizar que desean optimizar.

3. Crear la red neuronal clásica:
- Utilizando una librería PyTorch, diseñar la parte clásica de la red neuronal.
- Define la arquitectura de la red neuronal, incluidas capas, funciones de activación y objetivos
de optimización.

4. Combinar redes clásicas y cuánticas:
- Dependiendo del modelo específico, se requiere definir la capa en la que se introduce el circuito cuántico.

5. Establecer una función de costo:
- Es necesario definir una función de costo que cuantifique el error entre las predicciones de la
red y los datos reales.
- Esta función de costos se utiliza para guiar el proceso de optimización.

6. Entrenar la red híbrida:
- Optimizar los parámetros en el circuito cuántico (y potencialmente en la red clásica) utilizando
técnicas de optimización.

7. Evaluar y utilizar el modelo:
- Después del entrenamiento, puede evaluar el rendimiento del modelo híbrido en datos de
prueba.
- Utilice el modelo para diversas tareas de aprendizaje automático, como clasificación,
regresión u optimización.

Referencias:
https://qiskit.org/ecosystem/machine-learning/index.html
Rieffel, E. G., & Polak, W. H. (2011). Quantum computing: A gentle introduction. MIT Press.
Koch, D., Patel, S., Wessing, L. y Alsing, P. Fundamentals In Quantum Algorithms: A tutorial seriesl using Qiskit continued