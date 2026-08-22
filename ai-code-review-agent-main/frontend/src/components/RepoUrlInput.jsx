export default function RepoUrlInput({ repoUrl, branch, onRepoUrlChange, onBranchChange }) {
  return (
    <section className="card">
      <div className="card-heading">
        <span className="step-badge">1</span>
        <h2>Repository URL</h2>
      </div>

      <div className="repo-url-field">
        <label className="repo-url-label" htmlFor="repo-url">
          GitHub / Bitbucket URL
        </label>
        <input
          id="repo-url"
          type="text"
          className="text-input"
          placeholder="https://github.com/owner/repo"
          value={repoUrl}
          onChange={(e) => onRepoUrlChange(e.target.value)}
        />
      </div>

      <div className="repo-url-field">
        <label className="repo-url-label" htmlFor="repo-branch">
          Branch <span className="repo-url-optional">(optional, defaults to the repo's default branch)</span>
        </label>
        <input
          id="repo-branch"
          type="text"
          className="text-input"
          placeholder="main"
          value={branch}
          onChange={(e) => onBranchChange(e.target.value)}
        />
      </div>

      <span className="dropzone-hint">Public repositories only — github.com and bitbucket.org URLs</span>
    </section>
  );
}
