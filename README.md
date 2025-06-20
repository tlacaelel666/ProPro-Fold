# ·🧬 ProPro-Fold V1.0.0·

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Qiskit](https://img.shields.io/badge/Qiskit-0.45%2B-9657FF?logo=qiskit)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Dev: SmokAppSoftware](https://img.shields.io/badge/SmokApp-Software-red.svg)

## Analizador Cuántico de Proteínas 
Herramienta interactiva de línea de comandos para el análisis cuántico de estructuras proteicas simplificadas. Este script combina la lógica de análisis con una interfaz de usuario robusta, permitiendo la creación de circuitos cuánticos, simulación de dinámicas, generación de operadores Hamiltonianos y visualización de resultados.

**By jako with Claude AI & Gemini AI**

---

## 📜 Descripción General

El **Analizador Cuántico de Proteínas** es una herramienta educativa y de investigación que modela aspectos de la conformación y dinámica de proteínas utilizando los principios de la computación cuántica. A través de una interfaz de menú interactiva, los usuarios pueden:

-   Construir circuitos cuánticos que representan los grados de libertad de una cadena de aminoácidos.
-   Simular la evolución de estos estados cuánticos para encontrar las conformaciones más probables.
-   Generar y analizar operadores Hamiltonianos que modelan interacciones fisicoquímicas, como la polaridad.
-   Visualizar tanto los circuitos como los resultados de la simulación de forma gráfica o textual.

## ✨ Características Principales

-   **Interfaz de Menú Interactiva:** Fácil de usar, guiando al usuario a través de las diferentes funcionalidades.
-   **Creación de Circuitos Parametrizada:** Define el número de qubits (representando residuos o grados de libertad) y la complejidad de las interacciones.
-   **Simulación Cuántica:** Utiliza `Qiskit Aer` para una simulación de alto rendimiento de los circuitos cuánticos.
-   **Análisis de Hamiltoniano:** Genera un `SparsePauliOp` a partir de un tensor de "polaridad" de ejemplo para estudiar las propiedades energéticas del sistema.
-   **Visualización Configurable:** Ofrece salida gráfica (`matplotlib`) para entornos de escritorio y una alternativa de texto plano para terminales sin GUI.
-   **Manejo de Errores Robusto:** Valida las entradas del usuario y gestiona errores inesperados para una experiencia fluida.
-   **Código Modular y Documentado:** El script está bien estructurado en una clase `QuantumProteinAnalyzer` con docstrings y comentarios claros.

---

## 🎞️ Demostración de Uso

Una sesión típica con el analizador podría verse así:

```sh
$ python analizador_quantum_protein.py

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🧬 ANALIZADOR CUÁNTICO DE PROTEÍNAS 🧬                    ║
║                                                                              ║
║          Análisis cuántico avanzado de estructuras proteicas                ║
║               by SmokAppSoftware jako with Claude AI & Gemini AI               ║
╚══════════════════════════════════════════════════════════════════════════════╝

🔬 Inicializando Analizador Cuántico de Proteínas...
✅ Simulador cuántico listo.

======================================================================
        🧬 MENÚ PRINCIPAL - ANALIZADOR CUÁNTICO DE PROTEÍNAS 🧬
======================================================================
--- Simulación de Circuito ---
1. 🔧 Crear/Recrear Circuito Cuántico
2. 🎨 Visualizar Circuito Actual
...
9. ❌ Salir
----------------------------------------------------------------------
🤔 Selecciona una opción (1-9): 1
🔢 Número de qubits (2-10, por defecto 5): 3
🎛️  Aplicar puertas complejas? (s/n, por defecto s): s

🔧 Creando circuito cuántico para proteína con 3 qubits...
  ✅ Circuito creado con 3 qubits y profundidad 8.

⏸️  Presiona Enter para continuar...
```

### Visualización del Circuito (Opción 2)
Esto generará una ventana con el diagrama del circuito.
![FigureReadme](https://github.com/user-attachments/assets/6bd9e67a-5fa8-48f8-a294-fc502d704d16)


*Ejemplo de visualización gráfica generada por el script.*

### Simulación y Visualización de Resultados (Opciones 3 y 4)
```sh
🤔 Selecciona una opción (1-9): 3
🎯 Número de shots (por defecto 1024): 1024

🚀 Simulando dinámica proteica con 1024 mediciones...
  ✅ Simulación completada en 2.540 segundos.
  🎯 Estado más probable: 101 000 (38.77%)
✅ Simulación completada con éxito.

⏸️  Presiona Enter para continuar...
```
La opción 4 mostrará un histograma con la distribución de los estados medidos.
![Figure2readme](https://github.com/user-attachments/assets/81ab0528-f5dc-48a2-a094-a981949c5e28)


*Ejemplo de histograma de resultados generado por el script.*

---

## ⚙️ Instalación y Requisitos

### Prerrequisitos
-   Python 3.8 o superior.
-   `pip` y `venv` (generalmente incluidos con Python).

### Pasos de Instalación
1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/tlacaelel666/ProPro-Fold
    cd ProPro-Fold
    ```

2.  **Crea y activa un entorno virtual** (recomendado):
    ```bash
    # En Linux/macOS
    python3 -m venv .aenv
    source .aenv/bin/activate

    # En Windows
    python -m venv .aenv
    .\.aenv\Scripts\activate
    ```

3.  **Crea un archivo `requirements.txt`** con el siguiente contenido:
    ```txt
    qiskit
    qiskit-aer
    numpy
    matplotlib
    ```

4.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Cómo Ejecutar

Una vez que las dependencias estén instaladas y el entorno virtual activado, ejecuta el script desde la terminal:

```bash
python analizador_quantum_protein.py
```

Esto iniciará el menú interactivo donde podrás explorar todas las funcionalidades.

---

## 🛠️ Opciones del Menú

| Opción | Descripción                                                               |
| :----: | ------------------------------------------------------------------------- |
| **1**  | **Crear Circuito:** Construye un nuevo circuito cuántico para la proteína.  |
| **2**  | **Visualizar Circuito:** Muestra el diagrama del circuito actual.         |
| **3**  | **Simular Dinámica:** Ejecuta el circuito en un simulador cuántico.       |
| **4**  | **Visualizar Resultados:** Muestra un histograma de los resultados.       |
| **5**  | **Crear Operador:** Genera un Hamiltoniano desde un tensor de ejemplo.    |
| **6**  | **Analizar Operador:** Muestra las propiedades del Hamiltoniano actual.   |
| **7**  | **Activar/Desactivar GUI:** Cambia entre visualización gráfica y textual. |
| **8**  | **Ver Historial:** Lista un resumen de las simulaciones realizadas.       |
| **9**  | **Salir:** Cierra la aplicación.                                          |

---

## 🏗️ Estructura del Código y Mejoras Futuras

El código está contenido en un único script, `analizador_quantum_protein.py`, pero está diseñado con la modularidad en mente. El propio script sugiere una estructura más escalable para proyectos futuros:

```
/protein_analyzer
  ├─ qiskit_cli.py    # Contiene la clase QuantumProteinAnalyzer
  ├── python3 -m qiskit_cli               # comando de entrada, maneja el menú interactivo      
  ├---- Sigue las numeracion en orden para una mejor experincia     
  └----- Salir con las opciones de comandos            
/tests
  ├── test_analyzer.py      # Pruebas unitarias para la clase principal
  └── test_circuits.py      # Pruebas para la generación de circuitos
```
Esta estructura facilitaría el mantenimiento, la colaboración y la implementación de un sistema de integración continua (CI) con herramientas como `pytest`.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
