'use client'

import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function CreateProblemPage() {
  const [titulo, setTitulo] = useState('')
  const [tema, setTema] = useState('')
  const [tipo, setTipo] = useState('')
  const [enunciado, setEnunciado] = useState('')
  const [solucion, setSolucion] = useState('')
  const [criterio, setCriterio] = useState('')
  const [creditos, setCreditos] = useState<number>(1)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError(null)
    setLoading(true)

    try {
      const res = await fetch('http://localhost:5000/api/problems', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ titulo, tema, tipo, enunciado, solucion, criterio, creditos }),
      })
      if (!res.ok) {
        const text = await res.text()
        throw new Error(text || 'Error al crear problema')
      }
      router.push('/')
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="max-w-4xl mx-auto p-6 space-y-6">
      <header className="text-center space-y-2">
        <h1 className="text-4xl font-extrabold text-gray-800 dark:text-white">Nuevo Problema</h1>
        <p className="text-gray-600 dark:text-gray-400">Llena el formulario para registrar un nuevo problema en la base de datos.</p>
      </header>

      {error && (
        <div className="bg-red-50 dark:bg-red-900 border border-red-200 dark:border-red-700 text-red-700 dark:text-red-200 p-4 rounded-lg">
          {error}
        </div>
      )}

      <form
        onSubmit={handleSubmit}
        className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-6 grid gap-6 shadow"
      >
        {/* Título */}
        <div className="flex flex-col">
          <label className="mb-1 font-medium text-gray-700 dark:text-gray-300">Título</label>
          <input
            type="text"
            value={titulo}
            onChange={e => setTitulo(e.target.value)}
            placeholder="Título descriptivo del problema"
            className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 text-gray-800 dark:text-white border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            required
          />
        </div>

        {/* Tema & Tipo */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="flex flex-col">
            <label className="mb-1 font-medium text-gray-700 dark:text-gray-300">Tema</label>
            <input
              type="text"
              value={tema}
              onChange={e => setTema(e.target.value)}
              placeholder="Álgebra, Geometría, Optimización..."
              className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 text-gray-800 dark:text-white border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
          <div className="flex flex-col">
            <label className="mb-1 font-medium text-gray-700 dark:text-gray-300">Tipo</label>
            <input
              type="text"
              value={tipo}
              onChange={e => setTipo(e.target.value)}
              placeholder="Respuesta abierta, V/F, Selección..."
              className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 text-gray-800 dark:text-white border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
        </div>

        {/* Enunciado */}
        <div className="flex flex-col">
          <label className="mb-1 font-medium text-gray-700 dark:text-gray-300">Enunciado</label>
          <textarea
            value={enunciado}
            onChange={e => setEnunciado(e.target.value)}
            placeholder="Describe aquí el texto completo del problema..."
            className="border px-3 py-2 rounded-lg h-32 resize-none bg-white dark:bg-gray-700 text-gray-800 dark:text-white border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            required
          />
        </div>

        {/* Solución & Criterio */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div className="flex flex-col">
            <label className="mb-1 font-medium text-gray-700 dark:text-gray-300">Solución esperada</label>
            <textarea
              value={solucion}
              onChange={e => setSolucion(e.target.value)}
              placeholder="¿Qué se espera como respuesta correcta?"
              className="border px-3 py-2 rounded-lg h-24 resize-none bg-white dark:bg-gray-700 text-gray-800 dark:text-white border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
          <div className="flex flex-col">
            <label className="mb-1 font-medium text-gray-700 dark:text-gray-300">Criterio de evaluación</label>
            <input
              type="text"
              value={criterio}
              onChange={e => setCriterio(e.target.value)}
              placeholder="Ej: debe justificar, mencionar conceptos, etc."
              className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 text-gray-800 dark:text-white border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
              required
            />
          </div>
        </div>

        {/* Créditos */}
        <div className="flex flex-col sm:w-1/2">
          <label className="mb-1 font-medium text-gray-700 dark:text-gray-300">Créditos</label>
          <input
            type="number"
            min={1}
            value={creditos}
            onChange={e => setCreditos(Number(e.target.value))}
            placeholder="Número de créditos asignados"
            className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 text-gray-800 dark:text-white border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
            required
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="self-end bg-indigo-600 text-white font-semibold px-6 py-2 rounded-lg hover:bg-indigo-700 disabled:opacity-50 transition"
        >
          {loading ? 'Guardando...' : 'Guardar Problema'}
        </button>
      </form>
    </main>
  )
}
