// ============================================================
// ANSWER CARD
// ============================================================

function AnswerCard({
    answer
}) {

    if (!answer) {

        return null;
    }


    return (

        <section className="card answer-card">

            <div className="answer-header">

                <div className="answer-icon">
                    🤖
                </div>

                <div>

                    <h2>
                        Claude's Answer
                    </h2>

                    <p>
                        Generated using retrieved context
                    </p>

                </div>

            </div>


            <div className="answer-content">

                {answer}

            </div>

        </section>
    );
}


export default AnswerCard;