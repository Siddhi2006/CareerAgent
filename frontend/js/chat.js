const questionInput =
    document.getElementById("questionInput");

const sendQuestionButton =
    document.getElementById("sendQuestionButton");

const chatMessages =
    document.getElementById("chatMessages");


function addMessage(
    sender,
    message,
    messageType
) {

    const messageElement =
        document.createElement("div");

    messageElement.className =
        `message ${messageType}`;

    messageElement.innerHTML = `
        <div class="message-label">
            ${sender}
        </div>

        <div class="message-content"></div>
    `;

    const contentElement =
        messageElement.querySelector(
            ".message-content"
        );

    contentElement.textContent = message;

    chatMessages.appendChild(
        messageElement
    );

    chatMessages.scrollTop =
        chatMessages.scrollHeight;

    return messageElement;
}


async function askQuestion() {

    const question =
        questionInput.value.trim();

    if (!question) {
        return;
    }

    addMessage(
        "You",
        question,
        "user-message"
    );

    questionInput.value = "";

    sendQuestionButton.disabled = true;

    const loadingMessage = addMessage(
        "CareerAgent",
        "Searching the job description...",
        "assistant-message"
    );

    try {

        const response = await fetch(
            "/api/search",
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

        const result =
            await response.json();

        if (
            !response.ok ||
            result.status !== "success"
        ) {

            throw new Error(
                result.message ||
                "Unable to process the question."
            );
        }

        const contentElement =
            loadingMessage.querySelector(
                ".message-content"
            );

        contentElement.textContent =
            result.answer;

    } catch (error) {

        console.error(error);

        const contentElement =
            loadingMessage.querySelector(
                ".message-content"
            );

        contentElement.textContent =
            error.message;

    } finally {

        sendQuestionButton.disabled = false;

        questionInput.focus();
    }
}


sendQuestionButton.addEventListener(
    "click",
    askQuestion
);


questionInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            askQuestion();
        }
    }
);