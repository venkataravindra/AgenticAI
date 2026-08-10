import { useRef, useState } from 'react'

export default function Sidebar({ documents, onUpload, uploading, uploadProgress, uploadError }) {
  const inputRef = useRef(null)
  const [dragOver, setDragOver] = useState(false)

  function handleFiles(files) {
    const file = files?.[0]
    if (file) onUpload(file)
  }

  return (
    <aside className="sidebar">
      <div className="brand">
        <span className="brand-mark">§</span>
        <div>
          <h1 className="brand-name">Marginalia</h1>
          <p className="brand-tagline">Answers, footnoted</p>
        </div>
      </div>

      <div
        className={`dropzone ${dragOver ? 'is-dragover' : ''}`}
        onDragOver={(e) => {
          e.preventDefault()
          setDragOver(true)
        }}
        onDragLeave={() => setDragOver(false)}
        onDrop={(e) => {
          e.preventDefault()
          setDragOver(false)
          handleFiles(e.dataTransfer.files)
        }}
        onClick={() => inputRef.current?.click()}
        role="button"
        tabIndex={0}
        onKeyDown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') inputRef.current?.click()
        }}
      >
        <input
          ref={inputRef}
          type="file"
          accept=".pdf,.txt"
          hidden
          onChange={(e) => handleFiles(e.target.files)}
        />
        <span className="dropzone-icon">＋</span>
        <p className="dropzone-title">Add a source</p>
        <p className="dropzone-hint">PDF or TXT — drop it here or click to browse</p>
        {uploading && (
          <div className="upload-progress">
            <div className="upload-progress-track">
              <div className="upload-progress-bar" style={{ width: `${uploadProgress}%` }} />
            </div>
            <span>Indexing… {uploadProgress}%</span>
          </div>
        )}
        {uploadError && <p className="dropzone-error">{uploadError}</p>}
      </div>

      <div className="library">
        <p className="library-label">Library — {documents.length}</p>
        {documents.length === 0 && (
          <p className="library-empty">No sources yet. Add a document to start asking questions.</p>
        )}
        <ul className="library-list">
          {documents.map((doc) => (
            <li key={doc.name} className="library-item">
              <span className="library-icon">{doc.name.toLowerCase().endsWith('.pdf') ? 'PDF' : 'TXT'}</span>
              <div className="library-meta">
                <span className="library-name" title={doc.name}>
                  {doc.name}
                </span>
                <span className="library-chunks">{doc.chunks} chunks indexed</span>
              </div>
            </li>
          ))}
        </ul>
      </div>

      <p className="sidebar-footnote">
        Retrieval: FAISS + MiniLM · Re-ranked with a cross-encoder · Answered by Claude
      </p>
    </aside>
  )
}
