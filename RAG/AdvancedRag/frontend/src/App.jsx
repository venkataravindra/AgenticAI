// ============================================================
// MAIN APPLICATION
// ============================================================

import { useState } from "react";


// Components

import Header from "./components/Header";

import FileUpload from "./components/FileUpload";

import ProcessingStatus from "./components/ProcessingStatus";

import QuestionBox from "./components/QuestionBox";

import AnswerCard from "./components/AnswerCard";

import Sources from "./components/Sources";

import Footer from "./components/Footer";


// API

import { askQuestion } from "./services/api";


// CSS

import "./App.css";


function App() {

    // ========================================================
    // STATE
    // ========================================================

    const [question, setQuestion] =
        useState("");


    const [answer, setAnswer] =
        useState("");


    const [sources, setSources] =
        useState([]);


    const [loading, setLoading] =
        useState(false);


    const [uploadLoading, setUploadLoading] =
        useState(false);


    const [error, setError] =
        useState("");


    const [candidateDocuments,
        setCandidateDocuments] =
        useState(0);


    const [selectedDocuments,
        setSelectedDocuments] =
        useState(0);


    // ========================================================
    // UPLOAD SUCCESS
    // ========================================================

    function handleUploadSuccess(result) {

        setError("");

        setCandidateDocuments(0);

        setSelectedDocuments(0);

        setAnswer("");

        setSources([]);
    }


    // ========================================================
    // ERROR
    // ========================================================

    function handleError(message) {

        setError(message);
    }


    // ========================================================
    // ASK QUESTION
    // ========================================================

    async function handleAsk() {

        if (!question.trim()) {

            setError(
                "Please enter a question."
            );

            return;
        }


        try {

            setLoading(true);

            setError("");

            setAnswer("");

            setSources([]);


            // Call FastAPI

            const result =
                await askQuestion(
                    question
                );


            // Store answer

            setAnswer(
                result.answer
            );


            // Store sources

            setSources(
                result.sources || []
            );


            // Store RAG statistics

            setCandidateDocuments(
                result.candidate_documents || 0
            );


            setSelectedDocuments(
                result.selected_documents || 0
            );


        } catch (error) {

            setError(
                error.message
            );


        } finally {

            setLoading(false);
        }
    }


    // ========================================================
    // UI
    // ========================================================

    return (

        <div className="app">


            {/* HEADER */}

            <Header />


            {/* MAIN */}

            <main className="main-container">


                {/* ERROR */}

                {error && (

                    <div className="error-message">

                        <span>
                            ⚠️
                        </span>

                        {error}

                    </div>

                )}


                {/* UPLOAD */}

                <FileUpload

                    onUploadSuccess={
                        handleUploadSuccess
                    }

                    onError={
                        handleError
                    }

                    onLoading={
                        setUploadLoading
                    }

                />


                {/* QUESTION */}

                <QuestionBox

                    question={
                        question
                    }

                    setQuestion={
                        setQuestion
                    }

                    onAsk={
                        handleAsk
                    }

                    loading={
                        loading
                    }

                />


                {/* PROCESSING */}

                <ProcessingStatus

                    isProcessing={
                        loading ||
                        uploadLoading
                    }

                    candidateDocuments={
                        candidateDocuments
                    }

                    selectedDocuments={
                        selectedDocuments
                    }

                />


                {/* ANSWER */}

                <AnswerCard

                    answer={
                        answer
                    }

                />


                {/* SOURCES */}

                <Sources

                    sources={
                        sources
                    }

                />

            </main>


            {/* FOOTER */}

            <Footer />


        </div>
    );
}


export default App;