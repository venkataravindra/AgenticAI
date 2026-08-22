import { useState } from "react";
import FileUpload from "./components/FileUpload.jsx";
import Header from "./components/Header.jsx";
import { AlertIcon, LinkIcon, UploadIcon } from "./components/Icons.jsx";
import RepoUrlInput from "./components/RepoUrlInput.jsx";
import ReviewOptions from "./components/ReviewOptions.jsx";
import ReviewResult from "./components/ReviewResult.jsx";
import { fetchRepoFromUrl, requestReview, uploadFiles } from "./services/api.js";

export default function App() {
  const [sourceMode, setSourceMode] = useState("upload"); // "upload" | "url"
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [repoUrl, setRepoUrl] = useState("");
  const [branch, setBranch] = useState("");
  const [reviewFocus, setReviewFocus] = useState("general");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  function addFiles(newFiles) {
    setSelectedFiles((prev) => {
      const existingNames = new Set(prev.map((f) => f.name));
      const merged = [...prev, ...newFiles.filter((f) => !existingNames.has(f.name))];
      return merged;
    });
  }

  function removeFile(name) {
    setSelectedFiles((prev) => prev.filter((f) => f.name !== name));
  }

  async function handleReviewClick() {
    setError(null);
    setResult(null);

    if (sourceMode === "upload" && selectedFiles.length === 0) {
      setError("Select at least one file first.");
      return;
    }
    if (sourceMode === "url" && !repoUrl.trim()) {
      setError("Enter a repository URL first.");
      return;
    }

    setLoading(true);
    try {
      // Step 1: get an upload_id, either by uploading files or cloning a repo URL.
      const uploadResponse =
        sourceMode === "upload"
          ? await uploadFiles(selectedFiles)
          : await fetchRepoFromUrl(repoUrl.trim(), branch.trim());
      // Step 2: send the review request for all staged files.
      const reviewResponse = await requestReview(
        uploadResponse.upload_id,
        uploadResponse.files,
        reviewFocus
      );
      setResult(reviewResponse);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-shell">
      <Header />

      <main className="app-main">
        <div className="segmented-control source-toggle" role="radiogroup" aria-label="Code source">
          <button
            type="button"
            role="radio"
            aria-checked={sourceMode === "upload"}
            className={`segment ${sourceMode === "upload" ? "segment-active" : ""}`}
            onClick={() => setSourceMode("upload")}
          >
            <UploadIcon width={16} height={16} />
            Upload Files
          </button>
          <button
            type="button"
            role="radio"
            aria-checked={sourceMode === "url"}
            className={`segment ${sourceMode === "url" ? "segment-active" : ""}`}
            onClick={() => setSourceMode("url")}
          >
            <LinkIcon width={16} height={16} />
            Repository URL
          </button>
        </div>

        {sourceMode === "upload" ? (
          <FileUpload selectedFiles={selectedFiles} onFilesSelected={addFiles} onRemoveFile={removeFile} />
        ) : (
          <RepoUrlInput
            repoUrl={repoUrl}
            branch={branch}
            onRepoUrlChange={setRepoUrl}
            onBranchChange={setBranch}
          />
        )}

        <ReviewOptions reviewFocus={reviewFocus} onChange={setReviewFocus} />

        <section className="card review-action-card">
          <button className="review-button" onClick={handleReviewClick} disabled={loading}>
            {loading && <span className="spinner" />}
            {loading ? "Reviewing..." : "Review My Code"}
          </button>
          {error && (
            <p className="error">
              <AlertIcon width={16} height={16} />
              {error}
            </p>
          )}
        </section>

        <ReviewResult result={result} />
      </main>

      <footer className="site-footer">
        <span>AI Code Review Agent</span>
        <span className="dot">•</span>
        <span>Powered by vPro Skills</span>
      </footer>
    </div>
  );
}
