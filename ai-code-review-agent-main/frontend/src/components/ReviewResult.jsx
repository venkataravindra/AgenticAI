import { CheckCircleIcon, DatabaseIcon, ToolIcon } from "./Icons.jsx";

const RADIUS = 42;
const CIRCUMFERENCE = 2 * Math.PI * RADIUS;

function scoreColor(score) {
  if (score >= 80) return "#1F9D55";
  if (score >= 50) return "#F2760E";
  return "#D64545";
}

function ScoreRing({ score }) {
  const offset = CIRCUMFERENCE * (1 - score / 100);
  return (
    <div className="score-ring">
      <svg width="110" height="110" viewBox="0 0 110 110">
        <circle cx="55" cy="55" r={RADIUS} className="score-ring-track" />
        <circle
          cx="55"
          cy="55"
          r={RADIUS}
          stroke={scoreColor(score)}
          strokeWidth="10"
          fill="none"
          strokeLinecap="round"
          strokeDasharray={CIRCUMFERENCE}
          strokeDashoffset={offset}
          transform="rotate(-90 55 55)"
        />
      </svg>
      <div className="score-ring-label">
        <span className="score-value">{score}</span>
        <span className="score-max">/100</span>
      </div>
    </div>
  );
}

function severityBadgeClass(severity) {
  return `badge severity-${severity}`;
}

export default function ReviewResult({ result }) {
  if (!result) return null;

  return (
    <section className="card result-card">
      <div className="card-heading">
        <span className="step-badge">3</span>
        <h2>Review Result</h2>
      </div>

      <div className="score-row">
        <ScoreRing score={result.score} />
        <div className="score-summary">
          <h3>Summary</h3>
          <p>{result.summary}</p>
        </div>
      </div>

      <h3 className="section-title">Issues ({result.issues.length})</h3>
      {result.issues.length === 0 ? (
        <p className="empty-state">No issues found.</p>
      ) : (
        <div className="table-wrapper">
          <table className="issues-table">
            <thead>
              <tr>
                <th>Severity</th>
                <th>Category</th>
                <th>File</th>
                <th>Line</th>
                <th>Message</th>
                <th>Suggestion</th>
              </tr>
            </thead>
            <tbody>
              {result.issues.map((issue, index) => (
                <tr key={index}>
                  <td>
                    <span className={severityBadgeClass(issue.severity)}>{issue.severity}</span>
                  </td>
                  <td>
                    <span className="badge category">{issue.category}</span>
                  </td>
                  <td className="mono">{issue.file}</td>
                  <td className="mono">{issue.line ?? "—"}</td>
                  <td>{issue.message}</td>
                  <td className="suggestion-cell">{issue.suggestion}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <h3 className="section-title">Improvements</h3>
      <ul className="improvement-list">
        {result.improvements.map((item, index) => (
          <li key={index}>
            <CheckCircleIcon width={16} height={16} className="improvement-icon" />
            <span>{item}</span>
          </li>
        ))}
      </ul>

      <div className="meta-row">
        <span className="meta-chip">
          <DatabaseIcon width={15} height={15} />
          RAG context used: <strong>{result.rag_context_used ? "yes" : "no"}</strong>
        </span>
        <span className="meta-chip">
          <ToolIcon width={15} height={15} />
          MCP tools: <strong>{result.mcp_tools_used.length > 0 ? result.mcp_tools_used.join(", ") : "none"}</strong>
        </span>
      </div>
    </section>
  );
}
