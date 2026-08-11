// ============================================================
// QUESTION BOX COMPONENT
// ============================================================

function QuestionBox({
    question,
    setQuestion,
    onAsk,
    loading
}) {

    function handleSubmit(event) {

        event.preventDefault();

        onAsk();
    }


    return (

        <section className="card">

            <div className="section-title">

                <span className="step-number">
                    2
                </span>

                <div>

                    <h2>
                        Ask a Question
                    </h2>

                    <p>
                        Ask anything based on
                        your uploaded documents.
                    </p>

                </div>

            </div>


            <form
                onSubmit={handleSubmit}
                className="question-form"
            >

                <textarea

                    value={question}

                    onChange={(event) =>
                        setQuestion(
                            event.target.value
                        )
                    }

                    placeholder={
                        "Example: What is Advanced RAG?"
                    }

                    rows="5"

                />


                <div className="question-footer">

                    <span>
                        Powered by Claude
                    </span>


                    <button
                        type="submit"
                        className="primary-button"
                        disabled={
                            loading ||
                            !question.trim()
                        }
                    >

                        {loading
                            ? "Thinking..."
                            : "Ask Claude"
                        }

                    </button>

                </div>

            </form>

        </section>
    );
}


export default QuestionBox;