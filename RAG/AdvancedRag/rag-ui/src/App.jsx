import { useEffect, useRef, useState } from 'react'
import Sidebar from './components/Sidebar.jsx'
import Entry from './components/Entry.jsx'
import Composer from './components/Composer.jsx'
import { uploadDocument, askQuestion } from './api.js'
import './App.css'

export default function App() {
  const [documents, setDocuments] = useState([])
  const [uploading, setUploading] = useState(false)
  const [uploadProgress, setUploadProgress] = useState(0)
  const [uploadError, setUploadError] = useState('')
  const [entries, setEntries] = useState([])
  const [asking, setAsking] = useState(false)
  const scrollRef = useRef(null)

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: 'smooth' })
  }, [entries])

  async function handleUpload(file) {
    setUploadError('')
    setUploading(true)
    setUploadProgress(0)
    try {
      const result = await uploadDocument(file, setUploadProgress)
      setDocuments((prev) => [...prev, { name: result.file, chunks: result.chunks, documents: result.documents }])
    } catch (err) {
      setUploadError(err?.response?.data?.detail || 'Could not index that file. Try again.')
    } finally {
      setUploading(false)
    }
  }

  async function handleAsk(question) {
    const id = crypto.randomUUID()
    setEntries((prev) => [...prev, { id, question, status: 'loading' }])
    setAsking(true)
    try {
      const result = await askQuestion(question)
      setEntries((prev) =>
        prev.map((e) =>
          e.id === id
            ? {
                ...e,
                status: 'done',
                answer: result.answer,
                sources: result.sources,
                generatedQueries: result.generated_queries,
                candidateCount: result.candidate_documents,
                selectedCount: result.selected_documents
              }
            : e
        )
      )
    } catch (err) {
      setEntries((prev) =>
        prev.map((e) =>
          e.id === id
            ? { ...e, status: 'error', error: err?.response?.data?.detail || 'The backend did not respond. Is it running?' }
            : e
        )
      )
    } finally {
      setAsking(false)
    }
  }

  return (
    <div className="shell">
      <Sidebar
        documents={documents}
        onUpload={handleUpload}
        uploading={uploading}
        uploadProgress={uploadProgress}
        uploadError={uploadError}
      />

      <main className="main">
        <div className="thread" ref={scrollRef}>
          {entries.length === 0 ? (
            <div className="hero">
              <p className="hero-eyebrow">Retrieval-augmented Q&amp;A</p>
              <h2 className="hero-title">
                Every answer, <em>traced back</em> to the page it came from.
              </h2>
              <p className="hero-body">
                Add a PDF or text file on the left. Ask a question below. Marginalia expands your
                query, searches the index from a few angles, re-ranks what it finds, and answers
                with the exact passages it used listed as footnotes underneath.
              </p>
            </div>
          ) : (
            entries.map((entry) => <Entry key={entry.id} entry={entry} />)
          )}
        </div>

        <Composer onAsk={handleAsk} disabled={asking} hasDocuments={documents.length > 0} />
      </main>
    </div>
  )
}
