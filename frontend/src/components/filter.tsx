'use client'

import { useEffect, useMemo, useState } from 'react'
import { Problem } from '@types'

export type ProblemFilters = {
  titulo: string
  tema: string
  tipo: string
  criterio: string
  creditos: string
}

type Props = {
  problems: Problem[]
  onChange: (filters: ProblemFilters) => void
}

export default function ProblemFilters({ problems, onChange }: Props) {
  const [filters, setFilters] = useState<ProblemFilters>({
    titulo: '',
    tema: '',
    tipo: '',
    criterio: '',
    creditos: ''
  })

  // Obtener listas únicas de valores
  const temas = useMemo(() => [...new Set(problems.map(p => p.tema))], [problems])
  const tipos = useMemo(() => [...new Set(problems.map(p => p.tipo))], [problems])
  const criterios = useMemo(() => [...new Set(problems.map(p => p.criterio))], [problems])
  const creditos = useMemo(() => [...new Set(problems.map(p => p.creditos.toString()))], [problems])

  // Avisar al padre de cada cambio
  useEffect(() => {
    onChange(filters)
  }, [filters, onChange])

  return (
    <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-4 grid gap-4 md:grid-cols-3">
      {/* Filtro por título */}
      <input
        type="text"
        placeholder="Buscar por título..."
        className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
        value={filters.titulo}
        onChange={e => setFilters({ ...filters, titulo: e.target.value })}
      />

      {/* Filtro por tema */}
      <select
        className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
        value={filters.tema}
        onChange={e => setFilters({ ...filters, tema: e.target.value })}
      >
        <option value="">Todos los temas</option>
        {temas.map((t, i) => <option key={i} value={t}>{t}</option>)}
      </select>

      {/* Filtro por tipo */}
      <select
        className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
        value={filters.tipo}
        onChange={e => setFilters({ ...filters, tipo: e.target.value })}
      >
        <option value="">Todos los tipos</option>
        {tipos.map((t, i) => <option key={i} value={t}>{t}</option>)}
      </select>

      {/* Filtro por criterio */}
      <select
        className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
        value={filters.criterio}
        onChange={e => setFilters({ ...filters, criterio: e.target.value })}
      >
        <option value="">Todos los criterios</option>
        {criterios.map((c, i) => <option key={i} value={c}>{c}</option>)}
      </select>

      {/* Filtro por créditos */}
      <select
        className="border px-3 py-2 rounded-lg bg-white dark:bg-gray-700 border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-indigo-400"
        value={filters.creditos}
        onChange={e => setFilters({ ...filters, creditos: e.target.value })}
      >
        <option value="">Todos los créditos</option>
        {creditos.map((c, i) => <option key={i} value={c}>{c}</option>)}
      </select>
    </div>
  )
}
