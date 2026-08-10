import axios from 'axios'

// All requests go through /api, which vite.config.js proxies to
// the FastAPI backend at http://localhost:8000
const client = axios.create({
  baseURL: '/api',
  timeout: 120000
})

export async function uploadDocument(file, onProgress) {
  const formData = new FormData()
  formData.append('file', file)
  const { data } = await client.post('/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
    onUploadProgress: (evt) => {
      if (onProgress && evt.total) {
        onProgress(Math.round((evt.loaded / evt.total) * 100))
      }
    }
  })
  return data
}

export async function askQuestion(question) {
  const { data } = await client.post('/ask', { question })
  return data
}
