// Thin fetch wrapper around the FastAPI backend. No axios — plain fetch
// is enough for two endpoints and keeps the dependency list minimal.
//
// VITE_BACKEND_URL is baked in at build time (see frontend/Dockerfile and
// docker-compose.yml). Locally it falls back to localhost:8000; in a
// deployed build it points at the public backend URL instead — the
// browser runs on the visitor's machine, so "localhost" would otherwise
// mean their machine, not the server.
const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

async function parseErrorMessage(response, fallback) {
  const body = await response.json().catch(() => ({}));
  return body.detail || fallback;
}

export async function uploadFiles(files) {
  const formData = new FormData();
  for (const file of files) {
    formData.append("files", file);
  }

  const response = await fetch(`${BACKEND_URL}/api/files/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error(await parseErrorMessage(response, "File upload failed."));
  }
  return response.json();
}

export async function fetchRepoFromUrl(repoUrl, branch) {
  const response = await fetch(`${BACKEND_URL}/api/files/from-url`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ repo_url: repoUrl, branch: branch || null }),
  });

  if (!response.ok) {
    throw new Error(await parseErrorMessage(response, "Fetching repository failed."));
  }
  return response.json();
}

export async function requestReview(uploadId, fileNames, reviewFocus) {
  const response = await fetch(`${BACKEND_URL}/api/review`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      upload_id: uploadId,
      file_names: fileNames,
      review_focus: reviewFocus,
    }),
  });

  if (!response.ok) {
    throw new Error(await parseErrorMessage(response, "Review request failed."));
  }
  return response.json();
}
