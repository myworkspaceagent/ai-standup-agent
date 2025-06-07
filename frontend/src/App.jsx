import { useState } from "react";
import "./App.css";

function App() {
  const [context, setContext] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    setLoading(true);
    const res = await fetch("http://localhost:5000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_context: context }),
    });
    const data = await res.json();
    setResult(data.output);
    setLoading(false);
  };

  return (
    <div className="app">
      <h1>AI Agent: Daily Update Generator</h1>
      <textarea
        value={context}
        onChange={(e) => setContext(e.target.value)}
        placeholder="Add any extra context (optional)"
        rows={4}
      />
      <button onClick={handleGenerate} disabled={loading}>
        {loading ? "Generating..." : "Generate Update"}
      </button>

      {result && (
        <div className="output">
          <h3>Generated Output:</h3>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
