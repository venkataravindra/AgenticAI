import { useState, useEffect, useRef, useCallback } from 'react'
import './App.css'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const STAGES = [
  { key: 'retrieve', label: 'Retrieve', hint: 'PDF + web sources' },
  { key: 'grade', label: 'Grade', hint: 'Relevance check' },
  { key: 'correct', label: 'Correct', hint: 'Re-query if weak' },
  { key: 'answer', label: 'Answer', hint: 'Final response' },
]

function StatusDot({ status }) {
  return <span className={`status-dot status-dot--${status}`} />
}

function Pipeline({ stageIndex, correctionCount, running }) {
  const wasCorrected = correctionCount > 0
  return (
    <div className="pipeline" aria-label="Correction pipeline">
      {STAGES.map((stage, i) => {
        const isCorrectStage = stage.key === 'correct'
        const passed = i < stageIndex || (!running && stageIndex === STAGES.length)
        const active = running && i === stageIndex
        const flagged = isCorrectStage && wasCorrected && (passed || (!running && stageIndex >= STAGES.length))
        return (
          <div className="pipeline__item" key={stage.key}>
            <div className="pipeline__node-wrap">
              <div
                className={
                  'pipeline__node' +
                  (active ? ' pipeline__node--active' : '') +
                  (passed && !flagged ? ' pipeline__node--done' : '') +
                  (flagged ? ' pipeline__node--flagged' : '')
                }
              >
                {flagged ? correctionCount : i + 1}
              </div>
              {i < STAGES.length - 1 && (
                <div className={'pipeline__line' + (passed ? ' pipeline__line--done' : '')} />
              )}
            </div>
            <div className="pipeline__label">{stage.label}</div>
            <div className="pipeline__hint">{stage.hint}</div>
          </div>
        )
      })}
    </div>
  )
}

export default function App() {
  const [question, setQuestion] = useState('')
  const [history, setHistory] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [health, setHealth] = useState('checking')
  const [stageIndex, setStageIndex] = useState(0)
  const [lastCorrectionCount, setLastCorrectionCount] = useState(0)
  const timerRef = useRef(null)
  const scrollRef = useRef(null)

  const checkHealth = useCallback(async () => {
    try {
      const res = await fetch(`${API_BASE}/health`)
      if (!res.ok) throw new Error('bad status')
      const data = await res.json()
      setHealth(data.status === 'UP' ? 'up' : 'down')
    } catch {
      setHealth('down')
    }
  }, [])

  useEffect(() => {
    checkHealth()
    const id = setInterval(checkHealth, 15000)
    return () => clearInterval(id)
  }, [checkHealth])

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight
    }
  }, [history, loading])

  const runFakeProgress = () => {
    setStageIndex(0)
    let i = 0
    timerRef.current = setInterval(() => {
      i += 1
      setStageIndex(i)
      if (i >= STAGES.length - 1) {
        clearInterval(timerRef.current)
      }
    }, 550)
  }

  const stopProgress = (finalCount) => {
    if (timerRef.current) clearInterval(timerRef.current)
    setStageIndex(STAGES.length)
    setLastCorrectionCount(finalCount)
  }

  async function handleSubmit(e) {
    e.preventDefault()
    const q = question.trim()
    if (!q || loading) return

    setError(null)
    setLoading(true)
    setQuestion('')
    runFakeProgress()

    try {
      const res = await fetch(`${API_BASE}/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q }),
      })

      const data = await res.json().catch(() => null)

      if (!res.ok) {
        throw new Error(data?.detail || `Request failed (${res.status})`)
      }

      stopProgress(data.correction_count ?? 0)
      setHistory((prev) => [
        ...prev,
        {
          question: data.question ?? q,
          answer: data.answer,
          correctionCount: data.correction_count ?? 0,
          id: Date.now(),
        },
      ])
    } catch (err) {
      stopProgress(0)
      setError(err.message || 'Something went wrong reaching the API.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="page">
      <header className="header">
        <div className="header__inner">
          <div className="header__title-row">
            <p className="eyebrow">Self-correcting retrieval &middot; PDF + Web</p>
            <div className="health" title={`API ${health}`}>
              <StatusDot status={health} />
              <span className="health__label font-mono">
                {health === 'checking' ? 'checking…' : health === 'up' ? 'api online' : 'api offline'}
              </span>
            </div>
          </div>
          <h1 className="title">Ravindra Corrective Rag</h1>
          <p className="subtitle">
            Ask a question and watch it retrieve, grade, and — when a source falls short — correct
            itself before answering.
          </p>
        </div>
      </header>

      <main className="layout">
        <section className="panel panel--pipeline">
          <h2 className="panel__title">Pipeline</h2>
          <Pipeline stageIndex={stageIndex} correctionCount={lastCorrectionCount} running={loading} />

          <form className="ask-form" onSubmit={handleSubmit}>
            <label className="ask-form__label" htmlFor="question">
              Your question
            </label>
            <textarea
              id="question"
              className="ask-form__input"
              placeholder="e.g. What does the ingestion pipeline do with a new PDF?"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault()
                  handleSubmit(e)
                }
              }}
              rows={3}
              disabled={loading}
            />
            <div className="ask-form__row">
              <span className="ask-form__hint">Enter to ask &middot; Shift+Enter for a new line</span>
              <button type="submit" className="ask-form__submit" disabled={loading || !question.trim()}>
                {loading ? 'Working…' : 'Ask'}
              </button>
            </div>
          </form>

          {error && <div className="error-banner">{error}</div>}
        </section>

        <section className="panel panel--history">
          <div className="panel__header-row">
            <h2 className="panel__title">Conversation</h2>
            {history.length > 0 && (
              <span className="panel__count font-mono">{history.length} answered</span>
            )}
          </div>

          <div className="history" ref={scrollRef}>
            {history.length === 0 && !loading && (
              <div className="empty-state">
                <p>Nothing asked yet.</p>
                <p className="empty-state__sub">Your questions and their sourced answers will appear here.</p>
              </div>
            )}

            {history.map((item) => (
              <article className="qa-card" key={item.id}>
                <p className="qa-card__question">{item.question}</p>
                <p className="qa-card__answer">{item.answer}</p>
                <div className="qa-card__meta">
                  {item.correctionCount > 0 ? (
                    <span className="badge badge--corrected">
                      {item.correctionCount} correction{item.correctionCount > 1 ? 's' : ''} applied
                    </span>
                  ) : (
                    <span className="badge badge--clean">retrieved on first pass</span>
                  )}
                </div>
              </article>
            ))}

            {loading && (
              <article className="qa-card qa-card--pending">
                <p className="qa-card__question">{history.length === 0 ? question || 'Thinking…' : 'Thinking…'}</p>
                <div className="typing-dots">
                  <span />
                  <span />
                  <span />
                </div>
              </article>
            )}
          </div>
        </section>
      </main>

      <footer className="footer">
        <span>Built by Ravindra &middot; FastAPI + React</span>
      </footer>
    </div>
  )
}
