import { AlertIcon, CheckCircleIcon, SparklesIcon, ToolIcon } from "./Icons.jsx";

const FOCUS_OPTIONS = [
  { value: "general", label: "General", icon: SparklesIcon },
  { value: "bugs", label: "Bugs", icon: AlertIcon },
  { value: "security", label: "Security", icon: ToolIcon },
  { value: "performance", label: "Performance", icon: CheckCircleIcon },
];

export default function ReviewOptions({ reviewFocus, onChange }) {
  return (
    <section className="card">
      <div className="card-heading">
        <span className="step-badge">2</span>
        <h2>Review Focus</h2>
      </div>

      <div className="segmented-control" role="radiogroup" aria-label="Review focus">
        {FOCUS_OPTIONS.map(({ value, label, icon: Icon }) => (
          <button
            key={value}
            type="button"
            role="radio"
            aria-checked={reviewFocus === value}
            className={`segment ${reviewFocus === value ? "segment-active" : ""}`}
            onClick={() => onChange(value)}
          >
            <Icon width={16} height={16} />
            {label}
          </button>
        ))}
      </div>
    </section>
  );
}
