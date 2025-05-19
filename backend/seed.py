# seed.py

from app import create_app
from app.models import db
from app.models.problem import Problem

app = create_app()

with app.app_context():
    # Borrar y crear tablas (solo para desarrollo)
    db.drop_all()
    db.create_all()

    problems = [
        Problem(
            titulo="Suma de Números Naturales",
            enunciado="¿Cuál es la suma de los primeros 100 números naturales?",
            solucion="La fórmula para sumar los primeros n números naturales es: n(n + 1)/2. Por tanto, 100(100 + 1)/2 = 5050.",
            tema="Álgebra",
            tipo="Respuesta Abierta",
            creditos=4,
            criterio="Razonamiento",
        ),
        Problem(
            titulo="Ángulo en Triángulo Equilátero",
            enunciado="¿Verdadero o Falso? En un triángulo equilátero, cada ángulo interior mide 60 grados.",
            solucion="Verdadero. En un triángulo equilátero los tres ángulos son iguales y suman 180 grados, por lo tanto cada uno mide 60°.",
            tema="Geometría",
            tipo="Verdadero/Falso",
            creditos=2,
            criterio="Exactitud",
        ),
        Problem(
            titulo="Derivada de una Función",
            enunciado="Calcula la derivada de f(x) = x^3 + 2x^2 - 5x + 1.",
            solucion="La derivada es f'(x) = 3x^2 + 4x - 5.",
            tema="Cálculo",
            tipo="Respuesta Abierta",
            creditos=4,
            criterio="Claridad",
        ),
        Problem(
            titulo="Probabilidad con Dados",
            enunciado="¿Cuál es la probabilidad de obtener una suma de 7 al lanzar dos dados?",
            solucion="Existen 6 combinaciones que suman 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). Como hay 36 combinaciones posibles, la probabilidad es 6/36 = 1/6.",
            tema="Probabilidades",
            tipo="Selección Múltiple",
            creditos=3,
            criterio="Justificación",
        ),
        Problem(
            titulo="Orden de Complejidad",
            enunciado="¿Cuál es la complejidad temporal del algoritmo de búsqueda binaria en el peor caso?",
            solucion="La complejidad es O(log n), ya que el tamaño del problema se reduce a la mitad en cada paso.",
            tema="Programación",
            tipo="Selección Múltiple",
            creditos=3,
            criterio="Exactitud",
        ),
        Problem(
            titulo="Demostrar Paridad",
            enunciado="Demuestra que la suma de dos números pares es siempre par.",
            solucion="Sea a = 2m y b = 2n, donde m y n son enteros. Entonces a + b = 2m + 2n = 2(m + n), que es divisible por 2, por lo tanto par.",
            tema="Lógica",
            tipo="Demostración",
            creditos=5,
            criterio="Justificación",
        ),
        Problem(
            titulo="Área de un Círculo",
            enunciado="¿Verdadero o Falso? El área de un círculo con radio r es A = πr².",
            solucion="Verdadero. Es una fórmula básica de geometría plana.",
            tema="Geometría",
            tipo="Verdadero/Falso",
            creditos=2,
            criterio="Exactitud",
        ),
        Problem(
            titulo="Integral de una Función Lineal",
            enunciado="Calcula la integral indefinida de f(x) = 3x + 2.",
            solucion="∫(3x + 2) dx = (3/2)x^2 + 2x + C, donde C es la constante de integración.",
            tema="Cálculo",
            tipo="Respuesta Abierta",
            creditos=4,
            criterio="Claridad",
        ),
        Problem(
            titulo="Conjuntos y Elementos",
            enunciado="Sea A = {1, 2, 3} y B = {3, 4, 5}. ¿Cuál es A ∩ B?",
            solucion="A ∩ B es el conjunto de los elementos comunes, por tanto: {3}.",
            tema="Álgebra",
            tipo="Selección Múltiple",
            creditos=3,
            criterio="Razonamiento",
        ),
        Problem(
            titulo="Recursión y Factorial",
            enunciado="Escribe una función recursiva que calcule el factorial de un número n.",
            solucion="def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n - 1)",
            tema="Programación",
            tipo="Respuesta Abierta",
            creditos=5,
            criterio="Claridad",
        )
    ]

    db.session.add_all(problems)
    db.session.commit()

    print("🌱 Base de datos poblada con problemas de ejemplo.")