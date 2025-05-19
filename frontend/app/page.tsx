"use client"

import { useEffect, useMemo, useState } from "react"
import Link from "next/link"
import { Problem, ProblemFilters } from "@types"

export default function HomePage() {
  const [problems, setProblems] = useState<Problem[]>([])
  const [filters, setFilters] = useState<ProblemFilters>({
    titulo: '', tema: '', tipo: '', criterio: '', creditos: ''
  })
  const [currentPage, setCurrentPage] = useState(1)
  const perPage = 6

  useEffect(() => {
    fetch("http://localhost:5000/api/problems")
      .then(res => res.json())
      .then(data => setProblems(data))
  }, [])

  const filtered = useMemo(() => {
    return problems.filter(p =>
      (!filters.titulo || p.titulo.toLowerCase().includes(filters.titulo.toLowerCase())) &&
      (!filters.tema || p.tema === filters.tema) &&
      (!filters.tipo || p.tipo === filters.tipo) &&
      (!filters.criterio || p.criterio === filters.criterio) &&
      (!filters.creditos || p.creditos.toString() === filters.creditos)
    )
  }, [problems, filters])

  const totalPages = Math.ceil(filtered.length / perPage)
  const paged = filtered.slice((currentPage - 1) * perPage, currentPage * perPage)

  useEffect(() => { setCurrentPage(1) }, [filters])

  const unique = (key: keyof Problem) => [...new Set(problems.map(p => p[key]))]

  return (
    <main className="max-w-6xl mx-auto p-6 space-y-6">
      <header className="space-y-2">
        <h1 className="text-4xl font-extrabold text-gray-800 dark:text-gray-100">Problemas Académicos 🤌🏻</h1>
        <p className="text-gray-600 dark:text-gray-400">Filtra, busca y navega tus desafíos.</p>
      </header>

      <div className="grid md:grid-cols-3 gap-4 bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-4">
        <input
          type="text"
          placeholder="Buscar por título..."
          className="selector"
          value={filters.titulo}
          onChange={e => setFilters({ ...filters, titulo: e.target.value })}
        />
        <select
          className="selector"
          value={filters.tema}
          onChange={e => setFilters({ ...filters, tema: e.target.value })}
        >
          <option value="">Todos los temas</option>
          {unique('tema').map((val, i) => <option key={i} value={val as string}>{val}</option>)}
        </select>
        <select
          className="selector"
          value={filters.tipo}
          onChange={e => setFilters({ ...filters, tipo: e.target.value })}
        >
          <option value="">Todos los tipos</option>
          {unique('tipo').map((val, i) => <option key={i} value={val as string}>{val}</option>)}
        </select>
        <select
          className="selector"
          value={filters.criterio}
          onChange={e => setFilters({ ...filters, criterio: e.target.value })}
        >
          <option value="">Todos los criterios</option>
          {unique('criterio').map((val, i) => <option key={i} value={val as string}>{val}</option>)}
        </select>
        <select
          className="selector"
          value={filters.creditos}
          onChange={e => setFilters({ ...filters, creditos: e.target.value })}
        >
          <option value="">Todos los créditos</option>
          {unique('creditos').map((val, i) => <option key={i} value={val.toString()}>{val}</option>)}
        </select>
      </div>

      <div className="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
        {paged.map(p => (
          <Link key={p.id} href={`/problems/${p.id}`} className="block max-h-40 overflow-auto bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-6 transition">
            <h2 className="text-xl font-semibold text-indigo-600 dark:text-indigo-400 mb-1">{p.titulo}</h2>
            <p className="text-sm text-gray-500 dark:text-gray-400 mb-2 italic">{p.tema} — {p.tipo}</p>
            <p className="text-sm text-gray-700 dark:text-gray-300 mb-2 line-clamp-3">{p.enunciado}</p>
            <p className="text-sm text-gray-600 dark:text-gray-400">Créditos: <span className="text-gray-900 dark:text-gray-100 font-semibold">{p.creditos}</span></p>
          </Link>
        ))}
      </div>

      <div className="flex justify-center gap-4 pt-4">
        <button
          onClick={() => setCurrentPage(p => Math.max(p - 1, 1))}
          disabled={currentPage === 1}
          className="button"
        >Anterior</button>
        <span className="self-center text-sm text-gray-700 dark:text-gray-300">Página {currentPage} de {totalPages}</span>
        <button
          onClick={() => setCurrentPage(p => Math.min(p + 1, totalPages))}
          disabled={currentPage === totalPages}
          className="button"
        >Siguiente</button>
      </div>
    </main>
  )
}
