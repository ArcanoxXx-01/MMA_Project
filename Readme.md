# MMA Project – Evaluador Automático de Respuestas Académicas

Este proyecto es una aplicación web diseñada para ayudar a profesores a evaluar automáticamente respuestas de estudiantes usando modelos de lenguaje de Fireworks.ai.

## ✨ Características

- Gestión de problemas académicos con metadatos (tema, tipo, criterio, créditos…).
- Evaluación automática de respuestas usando LLMs vía Fireworks.ai.
- Interfaz moderna con filtros, modo oscuro, y paginación.
- Arquitectura desacoplada: Frontend (Next.js) + Backend (Flask).

---

## 🧠 Tecnologías

### 🖥️ Frontend
- [Next.js](https://nextjs.org/)
- TypeScript
- TailwindCSS

### 🧪 Backend
- [Flask](https://flask.palletsprojects.com/)
- Flask-SQLAlchemy
- Flask-Migrate
- Fireworks API
- Python 3.12+

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/MMA_Project.git
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
FIREWORKS_API_KEY=sk-tu-api-key
```

Ejecuta la app:

```bash
python run.py
```

La API se levantará en http://localhost:5000.

### 3. Configura el Frontend

```bash
cd ../frontend
npm install
npm run dev
```

La app estará disponible en http://localhost:3000.

    Asegúrate de que el backend está corriendo en el puerto 5000 para que las peticiones funcionen correctamente.

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
│   ├── components/
│   │   └── ProblemFilters.tsx
│   └── tailwind.config.ts
└── README.md

```

## 🧪 Evaluación con Fireworks.ai

La app se comunica con modelos LLM usando la API de Fireworks:

* El backend prepara un prompt detallado con:

  * Tema

   * Tipo de pregunta

   * Solución esperada

   * Respuesta del estudiante

   * Criterio de evaluación

* El modelo devuelve un razonamiento y una puntuación.

**Puedes ver o modificar el prompt en:**
`backend/app/llm/prompts.py`

## 📥 Poblado de la base de datos (opcional)

Puedes usar un script seed.py en el backend para poblar la base de datos con ejemplos. Asegúrate de que esté dentro del contexto de aplicación.

## ✍️ Contribuciones

¡Se aceptan contribuciones! Puedes:

* Agregar tipos de problemas nuevos

* Implementar soporte para múltiples LLMs

* Mejorar el sistema de feedback visual

* Agregar exportación de resultados o historial

## 🧑‍💻 Autor

Darío López Falcón— estudiante de Ciencias de la Computación de la Universidad de La Habana

## 📄 Licencia

MIT License.