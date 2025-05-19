export default interface EvaluationResult {
    razonamiento: string
    evaluacion: {
        score?: number
        [key: string]: any
    }
}