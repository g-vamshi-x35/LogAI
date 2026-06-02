const API = "http://127.0.0.1:8000";

async function analyzeLog() {
    const fileInput = document.getElementById("fileInput");
    const loading = document.getElementById("loading");
    const results = document.getElementById("results");
    const aiResponse = document.getElementById("aiResponse");

    if (!fileInput.files[0]) {
        alert("Please select at least one log file!");
        return;
    }

    // Show loading
    loading.style.display = "block";
    results.style.display = "none";
    aiResponse.innerHTML = "";

    // Loop through all selected files
    for (let i = 0; i < fileInput.files.length; i++) {
        const file = fileInput.files[i];

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch(`${API}/analyze`, {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            // Show result for each file
            aiResponse.innerHTML += `
                <div class="file-result">
                    <h3>📄 ${file.name}</h3>
                    <p>${data.analysis}</p>
                    <hr>
                </div>
            `;

        } catch (error) {
            aiResponse.innerHTML += `
                <div class="file-result error">
                    <h3>❌ ${file.name} — Failed</h3>
                    <p>Could not analyze this file.</p>
                    <hr>
                </div>
            `;
        }
    }

    // Show results
    loading.style.display = "none";
    results.style.display = "block";
}