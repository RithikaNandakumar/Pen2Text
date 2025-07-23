function uploadImage() {
    let fileInput = document.getElementById("fileInput");
    let status = document.getElementById("status");
    let output = document.getElementById("output");

    if (fileInput.files.length === 0) {
        status.innerText = "⚠️ Please select an image.";
        return;
    }

    let formData = new FormData();
    formData.append("image", fileInput.files[0]);

    status.innerHTML = "⏳ Processing...";
    output.innerText = "";

    fetch("http://127.0.0.1:5000/process", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            status.innerText = "❌ Error: " + data.error;
        } else {
            status.innerText = "✅ Extraction Complete!";
            output.innerText = data.extracted_text;
        }
    })
    .catch(error => {
        status.innerText = "❌ Error: " + error;
    });
}

function downloadText() {
    let text = document.getElementById("output").innerText;
    if (!text) {
        alert("No text available to download!");
        return;
    }

    let blob = new Blob([text], { type: "text/plain" });
    let link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "extracted_text.txt";
    link.click();
}
