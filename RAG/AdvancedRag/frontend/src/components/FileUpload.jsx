// ============================================================
// FILE UPLOAD COMPONENT
// ============================================================

import { useState } from "react";

import { uploadDocument } from "../services/api";


function FileUpload({
    onUploadSuccess,
    onError,
    onLoading
}) {

    const [file, setFile] = useState(null);

    const [status, setStatus] = useState("");


    // ========================================================
    // FILE SELECTION
    // ========================================================

    function handleFileChange(event) {

        const selectedFile =
            event.target.files[0];


        if (!selectedFile) {

            setFile(null);

            return;
        }


        setFile(selectedFile);

        setStatus("");

        onError("");
    }


    // ========================================================
    // UPLOAD
    // ========================================================

    async function handleUpload() {

        if (!file) {

            onError(
                "Please select a PDF or TXT file."
            );

            return;
        }


        try {

            onLoading(true);

            onError("");

            setStatus(
                "Uploading and indexing..."
            );


            const result =
                await uploadDocument(file);


            setStatus(
                `Successfully indexed ${result.file}. ` +
                `${result.chunks} chunks created.`
            );


            // Inform parent component

            onUploadSuccess(result);


        } catch (error) {

            setStatus("");

            onError(
                error.message
            );


        } finally {

            onLoading(false);
        }
    }


    return (

        <section className="card">

            <div className="section-title">

                <span className="step-number">
                    1
                </span>

                <div>

                    <h2>
                        Upload Document
                    </h2>

                    <p>
                        Add a PDF or TXT document
                        to the RAG knowledge base.
                    </p>

                </div>

            </div>


            <div className="upload-box">

                <div className="upload-icon">
                    📄
                </div>


                <input
                    type="file"
                    accept=".pdf,.txt"
                    onChange={handleFileChange}
                    id="file-upload"
                />


                <label
                    htmlFor="file-upload"
                    className="file-label"
                >
                    Choose PDF / TXT
                </label>


                {file && (

                    <div className="selected-file">

                        <span>
                            📄
                        </span>

                        <strong>
                            {file.name}
                        </strong>

                    </div>

                )}


                <button
                    className="primary-button"
                    onClick={handleUpload}
                    disabled={
                        !file
                    }
                >
                    Upload & Index
                </button>


                {status && (

                    <div className="success-message">

                        ✓ {status}

                    </div>

                )}

            </div>

        </section>
    );
}


export default FileUpload;