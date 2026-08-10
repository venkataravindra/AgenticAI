import { useState } from 'react'

function ScoreBar({ score }) {
  // Cross-encoder scores are unbounded logits; squash to a 0-100 display bar.
  const pct = Math.max(4, Math.min(100, Math.round((1 / (1 + Math.exp(-score))) * 100)))
  return (
    <div className="score-bar-track" aria-hidden="true">
      <div className="score-bar-fill" style={{ width: `${pct}%` }} />
    </div>
  )
}

export default function Entry({ entry }) {
  const [trailOpen, setTrailOpen] = useState(false)

  return (
    <article className="entry">
      <p className="entry-question">{entry.question}</p>

      {entry.status === 'loading' && (
        <div className="entry-loading">
          <span className="dot" />
          <span className="dot" />
          <span className="dot" />
          <span className="entry-loading-label">Searching sources and drafting an answer…</span>
        </div>
      )}

      {entry.status === 'error' && <p className="entry-error">{entry.error}</p>}

      {entry.status === 'done' && (
        <>
          <p className="entry-answer">{entry.answer}</p>

          {entry.generatedQueries?.length > 1 && (
            <div className="search-trail">
              <button className="search-trail-toggle" onClick={() => setTrailOpen((v) => !v)}>
                {trailOpen ? '– ' : '+ '}Search trail ({entry.generatedQueries.length} queries,{' '}
                {entry.candidateCount} candidates)
              </button>
              {trailOpen && (
                <ul className="search-trail-list">
                  {entry.generatedQueries.map((q, i) => (
                    <li key={i}>{q}</li>
                  ))}
                </ul>
              )}
            </div>
          )}

          {entry.sources?.length > 0 && (
            <div className="footnotes">
              <p className="footnotes-label">Sources</p>
              <ol className="footnotes-list">
                {entry.sources.map((s, i) => (
                  <li key={i} className="footnote">
                    <span className="footnote-index">{i + 1}</span>
                    <div className="footnote-body">
                      <span className="footnote-source">{s.source}</span>
                      <ScoreBar score={s.score} />
                    </div>
                  </li>
                ))}
              </ol>
            </div>
          )}
        </>
      )}
    </article>
  )
}
