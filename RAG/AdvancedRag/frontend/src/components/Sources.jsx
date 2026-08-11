// ============================================================
// SOURCES COMPONENT
// ============================================================

function Sources({
    sources
}) {

    if (!sources ||
        sources.length === 0) {

        return null;
    }


    return (

        <section className="card">

            <div className="section-title">

                <span className="source-icon">
                    📚
                </span>

                <div>

                    <h2>
                        Sources
                    </h2>

                    <p>
                        Documents used to generate the answer.
                    </p>

                </div>

            </div>


            <div className="sources-list">

                {sources.map(
                    (source, index) => (

                        <div
                            className="source-item"
                            key={index}
                        >

                            <div className="source-info">

                                <span className="pdf-icon">
                                    📄
                                </span>

                                <div>

                                    <strong>
                                        {source.source}
                                    </strong>

                                    <span>
                                        Retrieved document
                                    </span>

                                </div>

                            </div>


                            <div className="score">

                                <span>
                                    Relevance
                                </span>

                                <strong>
                                    {source.score}
                                </strong>

                            </div>

                        </div>

                    )
                )}

            </div>

        </section>
    );
}


export default Sources;