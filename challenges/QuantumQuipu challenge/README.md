# QuantumChallenge
Reto para el Qiskit Fall Fest Latino, Escuela en Español de Computación Cuántica

### Reto: Decodificar y Clasificar

Este proyecto se enfoca en codificar los archivos [challenge_train.csv](https://github.com/QuantumQuipu/QuantumChallenge/blob/main/challenge_train.csv) y [challenge_test.csv](https://github.com/QuantumQuipu/QuantumChallenge/blob/main/challenge_test.csv) en al menos dos formas diferentes en un circuito cuántico (estas podrían ser codificaciones basadas en ángulos, amplitud, kernel, aleatorias o personalizadas).

Diseña un circuito cuántico variacional para cada una de las codificaciones. Utiliza la columna "Target" como el objetivo, la cual es una clase binaria 0 y 1. Debes utilizar los datos de las columnas F1, F2, F3 y F4 para tu clasificador propuesto.

Considera el ansatz que diseñes como una capa y determina cuántas capas son necesarias para alcanzar el mejor rendimiento.

Analiza y discute los resultados obtenidos.

Siéntete libre de utilizar frameworks existentes (por ejemplo, PennyLane, Qiskit) para la creación y entrenamiento de los circuitos.

Este demo de PennyLane puede ser útil: [Entrenamiento de un circuito cuántico con PyTorch](https://pennylane.ai/qml/demos/tutorial_state_preparation/).

Este tutorial de Quantum Tensorflow puede ser útil: [Entrenamiento de un circuito cuántico con Tensorflow](https://www.tensorflow.org/quantum/tutorials/mnist).

Para el circuito variacional, puedes probar cualquier circuito que desees, incluso comenzar con uno que tenga una capa de RX, RZ y CNOTs.

**El ganador será el que llegue a obtener el mejor accuracy con su modelo propuesto.**

Premios:

- IBM Quantum swag oficial.
- Oportunidad de desarrollar un proyecto de investigación dentro de QuantumQuipu como Quantum Interns.
- Voucher para tomar el examen de certificación de Qiskit Quantum Developer (Descuento del 100% del pago).
