import logo from "../assets/logo.jpeg";

export default function Header() {
  return (
    <header className="site-header">
      <div className="site-header-inner">
        <img src={logo} alt="vPro Skills" className="logo" />
        <div className="site-header-text">
          <h1>AI Code Review Agent</h1>
          <p>Structured, AI-assisted reviews powered by RAG + MCP</p>
        </div>
      </div>
    </header>
  );
}
