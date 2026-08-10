import { useState } from 'react'

export default function Composer({ onAsk, disabled, hasDocuments }) {
  const [value, setValue] = useState('')

  function submit(e) {
    e.preventDefault()
    const q = value.trim()
    if (!q || disabled) return
    onAsk(q)
    setValue('')
  }

  return (
    <form className="composer" onSubmit={submit}>
      <textarea
        className="composer-input"
        placeholder={hasDocuments ? 'Ask something about your documents…' : 'Add a document first, then ask away…'}
        value={value}
        rows={1}
        onChange={(e) => setValue(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) {
            submit(e)
          }
        }}
      />
      <button className="composer-submit" type="submit" disabled={disabled || !value.trim()}>
        Ask
      </button>
    </form>
  )
}
