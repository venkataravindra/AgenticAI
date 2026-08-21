import { useState } from "react";
import FileUpload from "./components/FileUpload.jsx";
import Header from "./components/Header.jsx";
import { AlertIcon } from "./components/Icons.jsx";
import ReviewOptions from "./components/ReviewOptions.jsx";
import ReviewResult from "./components/ReviewResult.jsx";
import { requestReview, uploadFiles } from "./services/api.js";

export default function App() {
  const [selectedFiles, setSelectedFiles] = useState([]);
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

    if (selectedFiles.length === 0) {
      setError("Select at least one file first.");
      return;
    }

    setLoading(true);
    try {
      // Step 1: upload the selected files to get an upload_id.
      const uploadResponse = await uploadFiles(selectedFiles);
      // Step 2: send the review request for all uploaded files.
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
        <FileUpload selectedFiles={selectedFiles} onFilesSelected={addFiles} onRemoveFile={removeFile} />
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
