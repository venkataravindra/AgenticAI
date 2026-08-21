import { useRef, useState } from "react";
import { FileIcon, TrashIcon, UploadIcon } from "./Icons.jsx";

const ACCEPTED_EXTENSIONS = ".py,.js,.ts,.jsx,.tsx,.java,.cpp,.c,.cs,.go";

export default function FileUpload({ selectedFiles, onFilesSelected, onRemoveFile }) {
  const inputRef = useRef(null);
  const [isDragging, setIsDragging] = useState(false);

  function handleChange(event) {
    onFilesSelected(Array.from(event.target.files));
    event.target.value = ""; // allow re-selecting the same file later
  }

  function handleDrop(event) {
    event.preventDefault();
    setIsDragging(false);
    onFilesSelected(Array.from(event.dataTransfer.files));
  }

  return (
    <section className="card">
      <div className="card-heading">
        <span className="step-badge">1</span>
        <h2>Upload Code</h2>
      </div>

      <div
        className={`dropzone ${isDragging ? "dropzone-active" : ""}`}
        onClick={() => inputRef.current?.click()}
        onDragOver={(e) => {
          e.preventDefault();
          setIsDragging(true);
        }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={handleDrop}
      >
        <UploadIcon width={28} height={28} />
        <p>
          <strong>Click to browse</strong> or drag & drop files here
        </p>
        <span className="dropzone-hint">.py .js .ts .jsx .tsx .java .cpp .c .cs .go</span>
        <input
          ref={inputRef}
          type="file"
          multiple
          accept={ACCEPTED_EXTENSIONS}
          onChange={handleChange}
          hidden
        />
      </div>

      {selectedFiles.length > 0 && (
        <ul className="file-chip-list">
          {selectedFiles.map((file) => (
            <li key={file.name} className="file-chip">
              <FileIcon width={16} height={16} />
              <span className="file-chip-name">{file.name}</span>
              <button
                type="button"
                className="file-chip-remove"
                onClick={() => onRemoveFile(file.name)}
                aria-label={`Remove ${file.name}`}
              >
                <TrashIcon width={14} height={14} />
              </button>
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
