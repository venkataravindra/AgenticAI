// ============================================================
// PROCESSING STATUS COMPONENT
// ============================================================

function ProcessingStatus({
    isProcessing,
    candidateDocuments,
    selectedDocuments
}) {

    if (!isProcessing &&
        candidateDocuments === 0 &&
        selectedDocuments === 0) {

        return null;
    }


    return (

        <section className="card">

            <div className="section-title">

                <span className="step-number">
                    3
                </span>

                <div>

                    <h2>
                        RAG Processing
                    </h2>

                    <p>
                        See how Advanced RAG processes
                        your question.
                    </p>

                </div>

            </div>


            <div className="processing-flow">


                <div className="process-item">

                    <span className="process-icon">
                        🔎
                    </span>

                    <div>

                        <strong>
                            Query Expansion
                        </strong>

                        <p>
                            Claude generates alternative
                            search queries.
                        </p>

                    </div>

                </div>


                <div className="process-arrow">
                    ↓
                </div>


                <div className="process-item">

                    <span className="process-icon">
                        📚
                    </span>

                    <div>

                        <strong>
                            Vector Retrieval
                        </strong>

                        <p>
                            ChromaDB searches relevant chunks.
                        </p>

                    </div>

                </div>


                <div className="process-arrow">
                    ↓
                </div>


                <div className="process-item">

                    <span className="process-icon">
                        🎯
                    </span>

                    <div>

                        <strong>
                            Re-Ranking
                        </strong>

                        <p>
                            Cross-Encoder selects the
                            most relevant chunks.
                        </p>

                    </div>

                </div>


                <div className="process-arrow">
                    ↓
                </div>


                <div className="process-item">

                    <span className="process-icon">
                        🤖
                    </span>

                    <div>

                        <strong>
                            Claude
                        </strong>

                        <p>
                            Generates a grounded answer.
                        </p>

                    </div>

                </div>

            </div>


            {(candidateDocuments > 0) && (

                <div className="statistics">

                    <div className="stat">

                        <strong>
                            {candidateDocuments}
                        </strong>

                        <span>
                            Candidate Chunks
                        </span>

                    </div>


                    <div className="stat">

                        <strong>
                            {selectedDocuments}
                        </strong>

                        <span>
                            Selected Chunks
                        </span>

                    </div>

                </div>

            )}

        </section>
    );
}


export default ProcessingStatus;