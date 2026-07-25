import { useState, useRef, useEffect } from "react";

// Points at your FastAPI backend. Override at build/run time with
// VITE_API_BASE_URL=http://localhost:8000 if it runs somewhere else.
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

function App() {
  const [question, setQuestion] = useState("");
  const [history, setHistory] = useState([]); // [{ question, answer, error }]
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [history, loading]);

  const askQuestion = async (e) => {
    e.preventDefault();
    const trimmed = question.trim();
    if (!trimmed || loading) return;

    setLoading(true);
    setQuestion("");

    try {
      const url = new URL("/ask", API_BASE_URL);
      url.searchParams.set("question", trimmed);

      const res = await fetch(url.toString(), { method: "GET" });

      if (!res.ok) {
        throw new Error(`Server responded with ${res.status}`);
      }

      const data = await res.json();
      setHistory((prev) => [
        ...prev,
        { question: trimmed, answer: data.answer, error: false },
      ]);
    } catch (err) {
      setHistory((prev) => [
        ...prev,
        {
          question: trimmed,
          answer: `Could not reach the API: ${err.message}`,
          error: true,
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <header className="topbar">
        <div className="topbar-inner">
          <span className="dot" />
          <h1>Ask Console</h1>
          <span className="endpoint">GET {API_BASE_URL}/ask</span>
        </div>
      </header>

      <main className="transcript">
        {history.length === 0 && !loading && (
          <div className="empty-state">
            <p>No questions asked yet.</p>
            <p className="empty-sub">Type a question below and press Enter.</p>
          </div>
        )}

        {history.map((entry, i) => (
          <div className="exchange" key={i}>
            <div className="bubble question">
              <span className="label">You</span>
              <p>{entry.question}</p>
            </div>
            <div className={`bubble answer ${entry.error ? "error" : ""}`}>
              <span className="label">{entry.error ? "Error" : "AI"}</span>
              <p>{entry.answer}</p>
            </div>
          </div>
        ))}

        {loading && (
          <div className="exchange">
            <div className="bubble answer pending">
              <span className="label">AI</span>
              <div className="typing">
                <span />
                <span />
                <span />
              </div>
            </div>
          </div>
        )}

        <div ref={bottomRef} />
      </main>

      <form className="composer" onSubmit={askQuestion}>
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              askQuestion(e);
            }
          }}
          placeholder="Ask something..."
          rows={2}
        />
        <button type="submit" disabled={loading || !question.trim()}>
          {loading ? "Asking..." : "Ask"}
        </button>
      </form>
    </div>
  );
}

export default App;
