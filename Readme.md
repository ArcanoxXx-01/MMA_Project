# MMA Project – Evaluador Automático de Respuestas Académicas

## 🧩 Definición del problema a resolver

El proyecto busca facilitar la evaluación de respuestas académicas abiertas (por ejemplo, preguntas teóricas o conceptuales) que tradicionalmente requieren tiempo y criterio subjetivo por parte de los profesores. Los objetivos principales son:

- Reducir la carga de trabajo en la corrección de respuestas escritas.
- Aumentar la objetividad y consistencia en las evaluaciones.
- Ofrecer retroalimentación automática y rápida al estudiante.

---

### 💡 Propuesta de solución

Se diseñó una aplicación web dividida en dos módulos principales:

1. **Backend** que gestiona problemas académicos y usa modelos de lenguaje (LLMs) para evaluar las respuestas.
2. **Frontend** que permite a los usuarios (profesores) gestionar preguntas, filtrar por criterios, y visualizar resultados.

La evaluación automática se realiza a través de un LLM instructivo (modelo chat) de Fireworks.ai, con prompts diseñados para evaluar la respuesta del estudiante en base al tema, tipo de pregunta, solución esperada y criterios de evaluación.

---

<!-- ## ✨ Características

**El sistema se desarrollo principalmente para**:

- Gestionar problemas académicos con metadatos (tema, tipo, criterio, créditos…) # Con gestionar nos referimos a crear, guardar, editar, etc...
- Evaluación automática de respuestas usando LLMs. # Usando los metadatos de los problemas como parte del contexto y las respuestas de los estudiantes se formula un prompt para que un LLM genere una evaluacion, la cual incluye una nota de 0 a 100, y una explicacion en caso de ser necesaria. -->

## 🧠 Tecnologías

### 🖥️ Frontend

- [Next.js](https://nextjs.org/)
- TypeScript
- TailwindCSS

> Estas tecnologías fueron seleccionadas por su eficiencia en el desarrollo de interfaces modernas, su ecosistema bien integrado y la posibilidad de desplegar fácilmente la aplicación de forma gratuita en plataformas como [Vercel](https://vercel.com/).

### 🧪 Backend

- [Flask](https://flask.palletsprojects.com/)
- Flask-SQLAlchemy
- Flask-Migrate
- [Fireworks API](https://nextjs.org/)
- Python 3.12+

> Se optó por estas herramientas debido a su simplicidad, rapidez de desarrollo y bajo overhead, ideales para un backend ligero centrado en una única funcionalidad principal: evaluar respuestas mediante LLMs.

---

## 🧠 Justificación de herramientas

| Herramienta         | Razón de uso                                                                 |
|---------------------|------------------------------------------------------------------------------|
| **Flask**           | Microframework simple, ideal para construir APIs RESTful rápidamente.        |
| **SQLAlchemy**      | ORM robusto para mantener independencia de la base de datos.                 |
| **Fireworks.ai**    | Proveedor de LLMs con buena calidad y facilidad de uso.                      |
| **Next.js**         | Framework moderno de React con SSR/SSG, ideal para apps rápidas y SEO ready. |
| **TailwindCSS**     | Permite diseñar interfaces limpias y responsivas sin salir del HTML.         |
| **TypeScript**      | Mejora la mantenibilidad del frontend mediante tipado estático.              |

> Se optó por estas herramientas debido a su simplicidad, rapidez de desarrollo y bajo overhead, ideales para un backend ligero centrado en una única funcionalidad principal: evaluar respuestas mediante LLMs.

---

## ⚙️ Instalación (ejemplo en Linux-Ubuntu)

### 1. Clona el repositorio

```bash
git clone https://github.com/ArcanoxXx-01/MMA_Project.git
cd MMA_Project/backend
```

### 2. Configura el Backend

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Configura las variables de entorno en un archivo .env:

```bash
FIREWORKS_API_KEY=tu-api-key
```

Ejecuta la app:

```bash
python run.py
```

La API se levantará en <http://localhost:5000>.

### 3. Configura el Frontend

*duplica la terminal, y en la nueva ejecuta los siguientes comandos:

```bash
cd ../frontend
npm install
npm run dev
```

La app estará disponible en <http://localhost:3000>.

    Asegúrate de que el backend está corriendo en el puerto 5000 para que las peticiones funcionen correctamente.

---

## 🔍 Estructura del proyecto

```bash
MMA_Project/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── llm/
│   │   └── config.py
│   ├── run.py
│   └── requirements.txt
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   └── problems/
│   │       ├── [id]/page.tsx
│   │       └── create/page.tsx
|   ├── public/images/
|   ├── src/
│   |   ├── api/
|   |   ├── components/
│   │   └── types/
|   ├── package.json
|   ├── ...
│   └── tsconfig.json
└── README.md
```

---

## 📐 Arquitectura y Diseño

La aplicación sigue una arquitectura **desacoplada**, separando frontend y backend en módulos independientes. Esto permite:

- Despliegue más flexible y escalable.
- Desarrollo paralelo entre equipo frontend y backend.
- Mejor mantenibilidad del código.

### 🔄 Comunicación con LLMs

El backend no se comunica directamente con la API de Fireworks.ai, sino a través de una **interfaz abstracta `BaseLLM`**, lo que permite:

- Sustituir Fireworks por otro proveedor (ej. OpenAI, Cohere, Mistral...) sin afectar el resto del código.
- Mantener una estructura uniforme para operaciones como `generate()` y `evaluate()`.
- Aislar detalles de implementación, lo que facilita pruebas, mantenibilidad y futura extensibilidad.

Actualmente, la clase `FireworksModel` implementa esta interfaz usando modelos **instructivos tipo chat**, ideales para tareas de evaluación textual guiadas por prompt.

---

## 🧪 Evaluación con Fireworks.ai

La app se comunica con modelos LLM usando la API de Fireworks:

- El backend prepara un prompt detallado con:

  - Tema
  - Tipo de pregunta
  - Solución esperada
  - Respuesta del estudiante
  - Criterio de evaluación

- El modelo devuelve un razonamiento y una puntuación.

**Puedes ver o modificar el prompt en:**
`backend/app/llm/prompts.py`

---

## 📥 Poblado de la base de datos (opcional)

Puedes usar un script `seed.py` en el backend para poblar la base de datos con ejemplos. Asegúrate de que esté dentro del contexto de aplicación.

---

## 📊 Análisis del Proyecto

### ✅ Lo que funcionó

- La **arquitectura desacoplada** entre frontend y backend facilitó el desarrollo modular, permitiendo trabajar de forma independiente y simplificando el despliegue y la mantenibilidad.
- El uso de una **interfaz abstracta (`BaseLLM`)** para la comunicación con modelos de lenguaje demostró ser una decisión acertada.
- El sistema **evalúa correctamente preguntas de tipo opción múltiple y verdadero/falso**, ya que estas no requieren razonamiento profundo.
- La interfaz web es intuitiva y funcional, con filtros, paginación y modo oscuro, lo que mejora la experiencia del usuario.

---

### ❌ Lo que no funcionó (aún)

- Actualmente, el sistema **no guarda las evaluaciones generadas** por el modelo, lo que impide hacer trazabilidad, validaciones cruzadas o análisis posterior.
- **Las preguntas abiertas** (ej. justificar, explicar, demostrar) no siempre son bien evaluadas por el modelo.
- No se realizó comparación sistemática entre la evaluación automática y la evaluación humana.
- No se implementó un sistema de colas o tareas en segundo plano, lo cual puede afectar el rendimiento si se escalan las peticiones de evaluación.

---

## 🛠️ Contribuciones y Futuro del Proyecto

Este proyecto está en evolución constante y hay múltiples formas de contribuir o ampliarlo:

### 🔧 Mejoras recomendadas

- **Persistencia de evaluaciones**: guardar los resultados generados por el modelo para permitir trazabilidad y análisis estadístico.
- **Historial por estudiante y por problema**: para observar la evolución individual y validar el comportamiento del modelo.
- **Afinar los prompts**: utilizando ejemplos (few-shot) y validación con respuestas reales para mejorar la calidad de las evaluaciones.
- **Agregar autenticación y control de acceso**: para gestionar roles de profesores, administradores o instituciones.
- **Soporte para múltiples modelos**: integrar fácilmente otros proveedores (OpenAI, Cohere, Mistral…) usando la interfaz `BaseLLM`.
- **Exportación y visualización de resultados**: generar reportes en PDF, Excel u otros formatos para seguimiento académico.
- **Implementar feedback visual**: mostrar de forma clara al usuario el razonamiento del modelo, su puntuación y sugerencias.

### 🤝 Cómo contribuir

¡Tu ayuda es bienvenida! Algunas formas de colaborar:

- Agregar nuevos tipos de problemas y criterios de evaluación.
- Mejorar la interfaz web o la experiencia de usuario.
- Optimizar el rendimiento o refactorizar componentes.
- Proponer nuevas funcionalidades o integraciones.

---

## 🧑‍💻 Autor

Darío López Falcón — estudiante de Ciencias de la Computación de la Universidad de La Habana

---

## 📄 Licencia

MIT License.
