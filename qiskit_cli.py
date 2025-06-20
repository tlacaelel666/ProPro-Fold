#!/usr/bin/env python3
# Colaboracion y Desarrollo
#
# Para un proyecto más grande, se deben estructurar pruebas de la siguiente manera:
#
# /tests
#   ├── test_analyzer.py      # Pruebas unitarias para la clase principal
#   └── test_circuits.py      # Pruebas para la generación de circuitos
#
# Esta estructura facilitaría el mantenimiento, la colaboración y la implementación
# de un sistema de integración continua (CI) con herramientas como pytest.
"""
Analizador Cuántico de Proteínas
Herramienta interactiva para el análisis cuántico de estructuras proteicas.

Este script unificado combina la lógica de análisis con una interfaz de
línea de comandos robusta, aplicando mejoras en validación de entradas,
manejo de errores, visualización configurable y modularidad.

by SmokAppSoftware jako with Claude AI & Gemini AI
Versión 1.0
"""

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS
# Aseguramos que todos los módulos necesarios estén importados al inicio.
# -----------------------------------------------------------------------------
import sys
import time
import warnings
from typing import Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Pauli, SparsePauliOp, Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_aer import AerSimulator

# Suprimir warnings de depreciación de Qiskit para una salida más limpia
warnings.filterwarnings('ignore', category=DeprecationWarning)

# --- Clase para colores en la consola (inspirado en tu script de CLI) ---
class Colors:
    """Clase para definir colores de texto ANSI para la consola."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header():
    """Imprime el encabezado de la aplicación con colores."""
    header = f"""
{Colors.OKCYAN}╔══════════════════════════════════════════════════════════════════════════════╗
║                    {Colors.BOLD}🧬 ANALIZADOR CUÁNTICO DE PROTEÍNAS 🧬{Colors.ENDC}{Colors.OKCYAN}                    ║
║                                                                              ║
║          {Colors.OKBLUE}Análisis cuántico avanzado de estructuras proteicas{Colors.ENDC}{Colors.OKCYAN}                ║
║               {Colors.HEADER}by SmokAppSoftware jako with Claude AI & Gemini AI{Colors.ENDC}{Colors.OKCYAN}               ║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.ENDC}
"""
    print(header)

class QuantumProteinAnalyzer:
    """
    Clase principal para el análisis cuántico de proteínas.

    Esta clase encapsula la creación de circuitos, simulación, generación de
    operadores y visualización de resultados para el estudio de proteínas
    mediante computación cuántica.

    Args:
        verbose (bool): Si es True, imprime mensajes detallados durante la ejecución.
    """
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.simulator = AerSimulator()
        self.current_circuit: Optional[QuantumCircuit] = None
        self.current_operator: Optional[SparsePauliOp] = None
        self.results_history: List[Dict] = []
        
        if self.verbose:
            print(f"{Colors.OKGREEN}🔬 Inicializando Analizador Cuántico de Proteínas...{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Simulador cuántico listo.{Colors.ENDC}")

    def create_protein_quantum_circuit(self, num_qubits: int = 5, custom_gates: bool = True) -> QuantumCircuit:
        """
        Crea un circuito cuántico que representa una estructura proteica simplificada.

        Args:
            num_qubits: Número de qubits (representa grados de libertad). Debe estar entre 2 y 10.
            custom_gates: Si es True, aplica puertas que simulan interacciones complejas.

        Returns:
            El circuito cuántico configurado.

        Raises:
            ValueError: Si el número de qubits está fuera del rango permitido.

        Example:
            >>> analyzer = QuantumProteinAnalyzer()
            >>> qc = analyzer.create_protein_quantum_circuit(num_qubits=4)
        """
        if self.verbose:
            print(f"\n{Colors.BOLD}🔧 Creando circuito cuántico para proteína con {num_qubits} qubits...{Colors.ENDC}")
        
        # 2. VALIDACIÓN DE ENTRADAS
        # Se agrega una excepción clara para entradas inválidas.
        if not 2 <= num_qubits <= 10:
            raise ValueError("El número de qubits debe estar entre 2 y 10 para este modelo.")
        
        qc = QuantumCircuit(num_qubits, num_qubits)
        
        if self.verbose: print("  📐 Configurando estado inicial (conformación base)...")
        qc.x(0)
        qc.h(1)
        if num_qubits >= 3: qc.x(2)
        if num_qubits >= 4: qc.h(3)
        if num_qubits >= 5: qc.x(4)
        
        if custom_gates:
            if self.verbose: print("  🔄 Aplicando interacciones complejas entre residuos...")
            qc.barrier()
            # Interacciones locales (ej. electrostáticas, van der Waals)
            for i in range(num_qubits - 1):
                qc.rxx(np.pi / 4, i, i + 1)
                qc.rzz(np.pi / 8, i, i + 1)
            
            qc.barrier()
            # Intercambio conformacional entre extremos (si es suficientemente largo)
            if num_qubits >= 4:
                qc.swap(0, num_qubits - 1)
            
            qc.barrier()
            # Enlaces peptídicos simulados con CNOTs
            for i in range(num_qubits - 1):
                qc.cx(i, i + 1)
        
        qc.measure_all()
        self.current_circuit = qc
        
        if self.verbose:
            print(f"{Colors.OKGREEN}  ✅ Circuito creado con {qc.num_qubits} qubits y profundidad {qc.depth()}.{Colors.ENDC}")
        
        return qc

    def visualize_circuit(self, circuit: Optional[QuantumCircuit] = None, style: str = "mpl", gui: bool = True):
        """
        Visualiza el circuito cuántico.

        Args:
            circuit: Circuito a visualizar. Usa el circuito actual si es None.
            style: Estilo de visualización ('mpl' o 'text').
            gui: Si es False, fuerza la salida de texto, útil para entornos sin GUI.
        """
        circuit = circuit or self.current_circuit
        if not circuit:
            print(f"{Colors.FAIL}❌ No hay circuito para visualizar. Crea uno primero.{Colors.ENDC}")
            return
        
        if self.verbose: print(f"\n{Colors.BOLD}🎨 Visualizando circuito cuántico...{Colors.ENDC}")
        
        # 4. VISUALIZACIÓN CONFIGURABLE
        if not gui or style == "text":
            if not gui and self.verbose:
                print(f"{Colors.WARNING}  ⚠️ Visualización gráfica desactivada. Mostrando versión de texto.{Colors.ENDC}")
            print("\n" + "="*60)
            print("REPRESENTACIÓN TEXTUAL DEL CIRCUITO:")
            print("="*60)
            print(circuit.draw(output='text', fold=-1))
        else:
            try:
                fig = circuit.draw(output='mpl', style='iqp', fold=-1)
                fig.suptitle("🧬 Circuito Cuántico de Proteína", fontsize=16, fontweight='bold')
                plt.tight_layout(rect=[0, 0, 1, 0.96])
                plt.show()
            # 1. BLOQUES VACÍOS Y CONTROL DE FLUJO
            except Exception as e:
                print(f"{Colors.FAIL}⚠️ Error al crear visualización gráfica (¿ejecutando en un entorno sin GUI?): {e}{Colors.ENDC}")
                print(f"{Colors.WARNING}Mostrando versión de texto como alternativa.{Colors.ENDC}")
                print(circuit.draw(output='text', fold=-1))

    def simulate_protein_dynamics(self, circuit: Optional[QuantumCircuit] = None, shots: int = 1024) -> Optional[Dict]:
        """
        Simula la dinámica cuántica de la proteína ejecutando el circuito.

        Args:
            circuit: Circuito a simular. Usa el actual si es None.
            shots: Número de mediciones a realizar.

        Returns:
            Un diccionario con los resultados o None si falla.
        """
        circuit = circuit or self.current_circuit
        if not circuit:
            print(f"{Colors.FAIL}❌ No hay circuito para simular. Crea uno primero.{Colors.ENDC}")
            return None
        
        if self.verbose:
            print(f"\n{Colors.BOLD}🚀 Simulando dinámica proteica con {shots} mediciones...{Colors.ENDC}")
        start_time = time.time()
        
        try:
            transpiled_circuit = transpile(circuit, self.simulator)
            job = self.simulator.run(transpiled_circuit, shots=shots)
            result = job.result()
            counts = result.get_counts()
            
            simulation_time = time.time() - start_time
            
            result_data = {
                'counts': counts,
                'shots': shots,
                'simulation_time': simulation_time,
                'circuit_depth': circuit.depth(),
                'num_qubits': circuit.num_qubits
            }
            self.results_history.append(result_data)
            
            if self.verbose:
                print(f"  ✅ Simulación completada en {simulation_time:.3f} segundos.")
                sorted_states = sorted(counts.items(), key=lambda item: item[1], reverse=True)
                prob = (sorted_states[0][1] / shots) * 100
                print(f"  🎯 Estado más probable: {Colors.OKCYAN}{sorted_states[0][0]}{Colors.ENDC} ({prob:.2f}%)")
            
            return result_data
        # 1. BLOQUES VACÍOS Y CONTROL DE FLUJO
        except Exception as e:
            print(f"{Colors.FAIL}❌ Error durante la simulación: {e}{Colors.ENDC}")
            return None

    def visualize_results(self, results: Optional[Dict] = None, gui: bool = True):
        """
        Visualiza los resultados de la simulación con gráficos.

        Args:
            results: Resultados a visualizar. Usa los últimos si es None.
            gui: Si es False, solo imprime una tabla en texto.
        """
        results = results or (self.results_history[-1] if self.results_history else None)
        if not results:
            print(f"{Colors.FAIL}❌ No hay resultados para visualizar.{Colors.ENDC}")
            return
        
        counts = results.get('counts', {})
        if not counts:
            print(f"{Colors.WARNING}⚠️ Los resultados no contienen datos de conteo para visualizar.{Colors.ENDC}")
            return

        if self.verbose: print(f"\n{Colors.BOLD}📊 Visualizando resultados de la simulación...{Colors.ENDC}")
        
        # 4. VISUALIZACIÓN CONFIGURABLE
        if gui:
            try:
                plot_histogram(counts, figsize=(12, 6), color='skyblue', title='Distribución de Estados Conformacionales de la Proteína')
                plt.show()
            except Exception as e:
                print(f"{Colors.FAIL}⚠️ Error al crear histograma gráfico: {e}{Colors.ENDC}")
                print(f"{Colors.WARNING}Mostrando tabla de resultados como alternativa.{Colors.ENDC}")
                self._print_results_table(counts, results['shots'])
        else:
            if self.verbose:
                print(f"{Colors.WARNING}  ⚠️ Visualización gráfica desactivada. Mostrando tabla de texto.{Colors.ENDC}")
            self._print_results_table(counts, results['shots'])
            
        # Imprimir estadísticas adicionales
        print(f"\n{Colors.BOLD}📈 Estadísticas de la simulación:{Colors.ENDC}")
        print(f"  • Total de shots: {results['shots']}")
        print(f"  • Estados únicos medidos: {len(counts)}")
        print(f"  • Tiempo de simulación: {results['simulation_time']:.3f}s")
        print(f"  • Profundidad del circuito: {results['circuit_depth']}")

    def _print_results_table(self, counts: Dict[str, int], total_shots: int):
        """Imprime una tabla de resultados como alternativa a los gráficos."""
        print(f"\n{Colors.BOLD}📋 RESULTADOS DE LA SIMULACIÓN (Top 10):{Colors.ENDC}")
        print("-" * 50)
        print(f"{'Estado':<15} {'Conteo':<10} {'Probabilidad (%)'}")
        print("-" * 50)
        sorted_results = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        for state, count in sorted_results[:10]:
            prob = (count / total_shots) * 100
            print(f"{state:<15} {count:<10} {prob:>15.2f}")
        print("-" * 50)

    def create_polarity_operator(self, s_tensor: np.ndarray, lambda_scalar: float = 1.0) -> SparsePauliOp:
        """
        Crea un operador Hamiltoniano basado en un tensor de polaridad.

        Args:
            s_tensor: Tensor de polaridad S_μν (debe ser cuadrado, al menos 4x4).
            lambda_scalar: Parámetro de acoplamiento para escalar los coeficientes.

        Returns:
            El operador Hamiltoniano como un SparsePauliOp.

        Raises:
            ValueError: Si las dimensiones del tensor son inválidas.
        """
        num_qubits = s_tensor.shape[0] -1
        if self.verbose:
            print(f"\n{Colors.BOLD}🔬 Creando operador Hamiltoniano con {num_qubits} qubits...{Colors.ENDC}")
            print(f"  Tensor shape: {s_tensor.shape}, Lambda: {lambda_scalar}")

        # 2. VALIDACIÓN DE ENTRADAS
        if s_tensor.shape[0] != s_tensor.shape[1]:
            raise ValueError("El tensor de polaridad debe ser una matriz cuadrada.")
        if s_tensor.shape[0] < 2:
            raise ValueError("El tensor debe ser al menos de 2x2 para definir 1 qubit.")
        
        pauli_terms = []
        paulis = ['X', 'Y', 'Z'] # Asignación a ejes espaciales

        # Términos de un solo qubit
        for i in range(num_qubits):
            for j, pauli_op in enumerate(paulis):
                # Usar elementos diagonales del tensor para términos de un solo cuerpo
                coeff = lambda_scalar * s_tensor[i + 1, i + 1]
                if abs(coeff) > 1e-9:
                    pauli_str = 'I' * i + pauli_op + 'I' * (num_qubits - 1 - i)
                    pauli_terms.append((pauli_str, coeff))

        # Términos de interacción de dos qubits
        for i in range(num_qubits):
            for j in range(i + 1, num_qubits):
                # Usar elementos fuera de la diagonal para interacciones
                coeff = lambda_scalar * s_tensor[i + 1, j + 1]
                if abs(coeff) > 1e-9:
                    # Ejemplo de interacción ZZ, se puede hacer más complejo
                    pauli_str = 'I' * i + 'Z' + 'I' * (j - i - 1) + 'Z' + 'I' * (num_qubits - 1 - j)
                    pauli_terms.append((pauli_str, coeff))

        if not pauli_terms:
            print(f"{Colors.WARNING}⚠️ No se generaron términos Pauli significativos. El operador será nulo.{Colors.ENDC}")
            return SparsePauliOp('I' * num_qubits, 0)
            
        operator = SparsePauliOp.from_list(pauli_terms)
        self.current_operator = operator
        
        if self.verbose:
            print(f"{Colors.OKGREEN}  ✅ Operador creado con {len(operator)} términos.{Colors.ENDC}")
        return operator

    def analyze_operator(self, operator: Optional[SparsePauliOp] = None):
        """
        Analiza e imprime las propiedades de un operador cuántico.
        
        Args:
            operator: Operador a analizar. Usa el actual si es None.
        """
        operator = operator or self.current_operator
        if not operator:
            print(f"{Colors.FAIL}❌ No hay operador para analizar. Créalo primero.{Colors.ENDC}")
            return
        
        print(f"\n{Colors.BOLD}🔍 ANÁLISIS DEL OPERADOR HAMILTONIANO:{Colors.ENDC}")
        print("=" * 50)
        print(f"📊 Número de términos Pauli: {len(operator)}")
        print(f"🔢 Número de qubits: {operator.num_qubits}")
        
        coeffs = np.abs(operator.coeffs)
        print(f"\n{Colors.BOLD}🎯 Top 5 términos más significativos (por magnitud):{Colors.ENDC}")
        print("-" * 50)
        sorted_indices = np.argsort(coeffs)[::-1]
        for i, idx in enumerate(sorted_indices[:5]):
            pauli_str = operator.paulis[idx].to_label()
            coeff_val = operator.coeffs[idx]
            print(f"  {i+1}. {pauli_str:<15}: {coeff_val.real:12.6f}")
        print("-" * 50)

def create_example_protein_tensor(size: int = 5) -> np.ndarray:
    """Crea un tensor de polaridad de ejemplo para una proteína."""
    print(f"{Colors.OKBLUE}INFO: Generando tensor de polaridad de ejemplo de {size}x{size}...{Colors.ENDC}")
    # Tensor de ejemplo basado en propiedades fisicoquímicas simuladas
    # Dimensión 0: "Tiempo" o energía base
    # Dimensiones 1..N: Propiedades espaciales/fisicoquímicas
    np.random.seed(42) # Para reproducibilidad
    base_tensor = np.random.rand(size, size)
    s_tensor = (base_tensor + base_tensor.T) / 2 # Simetrizar
    np.fill_diagonal(s_tensor, np.random.uniform(0.5, 2.5, size)) # Diagonales más fuertes
    return s_tensor

# -----------------------------------------------------------------------------
# MENÚ INTERACTIVO 
# -----------------------------------------------------------------------------
def interactive_menu():
    """Menú interactivo principal para controlar el analizador."""
    analyzer = QuantumProteinAnalyzer(verbose=True)
    gui_enabled = True # Por defecto, la visualización gráfica está activada

    while True:
        print("\n" + "="*70)
        print(f"        {Colors.HEADER}{Colors.BOLD}🧬 MENÚ PRINCIPAL - ANALIZADOR CUÁNTICO DE PROTEÍNAS 🧬{Colors.ENDC}")
        print("="*70)
        print("--- Simulación de Circuito ---")
        print("1. 🔧 Crear/Recrear Circuito Cuántico")
        print("2. 🎨 Visualizar Circuito Actual")
        print("3. 🚀 Simular Dinámica Proteica")
        print("4. 📊 Visualizar Resultados de Simulación")
        print("\n--- Análisis de Hamiltoniano ---")
        print("5. 🔬 Crear Operador Hamiltoniano (desde tensor)")
        print("6. 🔍 Analizar Operador Actual")
        print("\n--- Utilidades ---")
        print(f"7. 🖥️  Activar/Desactivar GUI (Actual: {'Activada' if gui_enabled else 'Desactivada'})")
        print("8. 📋 Ver Historial de Simulaciones")
        print("9. ❌ Salir")
        print("-"*70)
        
        choice = input(f"{Colors.BOLD}🤔 Selecciona una opción (1-9): {Colors.ENDC}").strip()
        
        try:
            if choice == '1':
                num_qubits = int(input("🔢 Número de qubits (2-10, por defecto 5): ") or "5")
                custom = input("🎛️  Aplicar puertas complejas? (s/n, por defecto s): ").lower().strip() != 'n'
                analyzer.create_protein_quantum_circuit(num_qubits, custom)
            
            elif choice == '2':
                analyzer.visualize_circuit(gui=gui_enabled)
            
            elif choice == '3':
                shots = int(input("🎯 Número de shots (por defecto 1024): ") or "1024")
                if analyzer.simulate_protein_dynamics(shots=shots):
                    print(f"{Colors.OKGREEN}✅ Simulación completada con éxito.{Colors.ENDC}")
            
            elif choice == '4':
                analyzer.visualize_results(gui=gui_enabled)
            
            elif choice == '5':
                size = int(input("📏 Tamaño del tensor (N+1, por defecto 5): ") or "5")
                s_tensor = create_example_protein_tensor(size)
                print("Tensor generado:\n", s_tensor)
                lambda_val = float(input("⚡ Valor de lambda (acoplamiento, por defecto 1.0): ") or "1.0")
                analyzer.create_polarity_operator(s_tensor, lambda_val)
            
            elif choice == '6':
                analyzer.analyze_operator()

            elif choice == '7':
                gui_enabled = not gui_enabled
                status = "Activada" if gui_enabled else "Desactivada"
                color = Colors.OKGREEN if gui_enabled else Colors.WARNING
                print(f"{color}✅ Visualización gráfica ahora está {status}.{Colors.ENDC}")

            elif choice == '8':
                if analyzer.results_history:
                    print(f"\n{Colors.BOLD}📋 HISTORIAL DE SIMULACIONES ({len(analyzer.results_history)} en total):{Colors.ENDC}")
                    print("-" * 60)
                    for i, r in enumerate(analyzer.results_history, 1):
                        print(f"  {i}. Qubits: {r['num_qubits']}, Shots: {r['shots']}, "
                              f"Tiempo: {r['simulation_time']:.3f}s, Estados: {len(r['counts'])}")
                else:
                    print(f"{Colors.WARNING}📭 El historial de simulaciones está vacío.{Colors.ENDC}")
            
            elif choice == '9':
                print(f"\n{Colors.OKBLUE}👋 ¡Gracias por usar el Analizador Cuántico de Proteínas!{Colors.ENDC}")
                sys.exit(0)
            
            else:
                print(f"{Colors.FAIL}❌ Opción inválida. Por favor, selecciona un número del 1 al 9.{Colors.ENDC}")
                
        except ValueError as e:
            print(f"{Colors.FAIL}❌ Error de entrada: {e}. Por favor, introduce un valor válido.{Colors.ENDC}")
        except KeyboardInterrupt:
            print(f"\n\n{Colors.WARNING}⚠️ Operación cancelada por el usuario. Volviendo al menú.{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}❌ Ocurrió un error inesperado: {e}{Colors.ENDC}")
        
        if choice != '9':
            input(f"\n{Colors.OKBLUE}⏸️  Presiona Enter para continuar...{Colors.ENDC}")


if __name__ == "__main__":
    print_header()
    interactive_menu()
