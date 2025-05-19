'use client'

import { useState, useEffect } from 'react'
import { useParams } from 'next/navigation'
import Link from 'next/link'
import { Problem, EvaluationResult } from '@types'

export default function ProblemPage() {
  const { id } = useParams()
  const [problem, setProblem] = useState<Problem | null>(null)
  const [answer, setAnswer] = useState('')
  const [result, setResult] = useState<EvaluationResult | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    fetch('http://localhost:5000/api/problems')
      .then(res => res.json())
      .then((data: Problem[]) => {
        const found = data.find(p => p.id === Number(id))
        if (!found) throw new Error('Problema no encontrado')
        setProblem(found)
      })
      .catch(err => setError(err.message))
  }, [id])

  const handleEvaluate = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!problem) return
    setError(null)
    setLoading(true)
    try {
      const res = await fetch(`http://localhost:5000/api/evaluate/${problem.id}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ respuesta: answer })
      })
      if (!res.ok) {
        const text = await res.text()
        throw new Error(text || 'Error al evaluar')
      }
      const data: EvaluationResult = await res.json()
      setResult(data)
    } catch (err: any) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  if (error) {
    return (
      <main className="p-6 max-w-2xl mx-auto">
        <div className="bg-red-50 border border-red-200 text-red-700 p-4 rounded-lg">
          <p>Error: {error}</p>
        </div>
        <Link href="/" className="inline-block text-indigo-600 mt-4 hover:underline">
          👈🏻 Volver al listado
        </Link>
      </main>
    )
  }

  if (!problem) {
    return (
      <main className="p-6 max-w-2xl mx-auto">
        <p className="text-gray-500">Cargando problema...</p>
      </main>
    )
  }

  return (
    <main className="p-6 max-w-4xl mx-auto space-y-8">
      <Link href="/" className="text-indigo-600 hover:underline">👈🏻 Volver al listado</Link>

      {/* Tarjeta del problema */}
      <section className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-6 space-y-2">
        <h1 className="text-3xl font-bold text-gray-800 dark:text-gray-100">{problem.titulo}</h1>
        <p className="text-sm text-gray-500 dark:text-gray-400 italic">Tema: {problem.tema} | Tipo: {problem.tipo}</p>
        <p className="text-sm text-gray-500 dark:text-gray-400">Créditos: <span className="font-semibold">{problem.creditos}</span></p>
        <p className="text-gray-700 dark:text-gray-300 mt-4 whitespace-pre-wrap">{problem.enunciado}</p>
        <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">Criterio de evaluación: <span className="font-medium text-gray-800 dark:text-white">{problem.criterio}</span></p>
      </section>

      {/* Formulario de respuesta */}
      <form onSubmit={handleEvaluate} className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-6 space-y-4">
        <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100">Tu respuesta</h2>
        <textarea
          value={answer}
          onChange={e => setAnswer(e.target.value)}
          className="w-full h-40 border border-gray-300 dark:border-gray-600 rounded-lg p-3 bg-white dark:bg-gray-700 text-gray-800 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-400"
          placeholder="Escribe aquí tu respuesta..."
          required
        />
        <button
          type="submit"
          disabled={loading}
          className="bg-indigo-600 text-white font-medium px-6 py-2 rounded-lg hover:bg-indigo-700 disabled:opacity-50 transition"
        >
          {loading ? 'Evaluando...' : 'Evaluar respuesta'}
        </button>
      </form>

      {/* Resultado */}
      {result && (
        <section className="bg-gray-50 dark:bg-gray-900 border border-gray-200 dark:border-gray-700 rounded-xl p-6 space-y-4 shadow">
          <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100">Resultado de la evaluación</h2>
          <div className="space-y-2">
            <h3 className="font-medium text-gray-700 dark:text-gray-300">Razonamiento del modelo:</h3>
            <pre className="whitespace-pre-wrap bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 p-4 rounded-lg border border-gray-100 dark:border-gray-600">
              {result.razonamiento}
            </pre>
          </div>
          {typeof result.evaluacion.score === 'number' && (
            <p className="text-lg font-medium text-indigo-600 dark:text-indigo-400">
              Puntuación: <span className="text-2xl">{result.evaluacion.score}</span> / 100
            </p>
          )}
        </section>
      )}
    </main>
  )
}
