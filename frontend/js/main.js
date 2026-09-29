const fileInput =
    document.getElementById("jdFile");

const analyzeButton =
    document.getElementById("analyzeButton");

const statusMessage =
    document.getElementById("statusMessage");


analyzeButton.addEventListener(
    "click",
    async () => {

        const file =
            fileInput.files[0];


        if (!file) {

            statusMessage.textContent =
                "Please select a PDF file.";

            return;
        }


        if (
            !file.name
                .toLowerCase()
                .endsWith(".pdf")
        ) {

            statusMessage.textContent =
                "Please select a PDF file.";

            return;
        }


        const formData =
            new FormData();

        formData.append(
            "file",
            file
        );


        try {

            analyzeButton.disabled =
                true;

            analyzeButton.textContent =
                "Processing...";

            statusMessage.textContent =
                "Uploading and processing the job description...";


            const response =
                await fetch(
                    "/api/upload",
                    {
                        method: "POST",
                        body: formData
                    }
                );


            const result =
                await response.json();


            if (
                !response.ok ||
                result.status !== "success"
            ) {

                throw new Error(
                    result.message ||
                    "Failed to process the document."
                );
            }


            statusMessage.textContent =
                `Document processed successfully. Created ${result.chunk_count} text chunks.`;


            analyzeButton.textContent =
                "Open Analysis";


            analyzeButton.disabled =
                false;


            analyzeButton.onclick =
                function () {

                    window.location.href =
                        "/analysis";
                };


        } catch (error) {

            console.error(error);

            statusMessage.textContent =
                error.message;

            analyzeButton.disabled =
                false;

            analyzeButton.textContent =
                "Analyze JD";
        }
    }
);