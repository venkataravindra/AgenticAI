// ============================================================
// API CONFIGURATION
// ============================================================

// Get backend URL from Vite environment variable.
//
// .env:
// VITE_API_URL=http://localhost:8000

const API_URL = import.meta.env.VITE_API_URL;


// ============================================================
// UPLOAD DOCUMENT
// ============================================================

export async function uploadDocument(file) {

    // FormData is used because we are uploading a file.

    const formData = new FormData();

    formData.append("file", file);


    // Send file to FastAPI

    const response = await fetch(
        `${API_URL}/upload`,
        {
            method: "POST",
            body: formData
        }
    );


    // Check whether API request failed

    if (!response.ok) {

        const error = await response.json();

        throw new Error(
            error.detail || "Upload failed"
        );
    }


    // Convert response to JSON

    return response.json();
}


// ============================================================
// ASK QUESTION
// ============================================================

export async function askQuestion(question) {

    const response = await fetch(
        `${API_URL}/ask`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        }
    );


    if (!response.ok) {

        const error = await response.json();

        throw new Error(
            error.detail || "Question failed"
        );
    }


    return response.json();
}