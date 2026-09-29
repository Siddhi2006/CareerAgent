const analyzeJdButton =
    document.getElementById("analyzeJdButton");

const analyzeSkillsButton =
    document.getElementById("analyzeSkillsButton");

const generateInterviewButton =
    document.getElementById("generateInterviewButton");

const generatePreparationButton =
    document.getElementById("generatePreparationButton");


const jdAnalysis =
    document.getElementById("jdAnalysis");

const skillsAnalysis =
    document.getElementById("skillsAnalysis");

const interviewQuestions =
    document.getElementById("interviewQuestions");

const preparationPlan =
    document.getElementById("preparationPlan");


const jdStatus =
    document.getElementById("jdStatus");

const skillsStatus =
    document.getElementById("skillsStatus");

const interviewStatus =
    document.getElementById("interviewStatus");

const preparationStatus =
    document.getElementById("preparationStatus");


function showLoading(element, message) {

    element.innerHTML = `
        <p class="loading-text">
            ${message}
        </p>
    `;
}


function showError(element, message) {

    element.innerHTML = `
        <p class="error-text">
            ${message}
        </p>
    `;
}


function setButtonLoading(button, loadingText) {

    button.disabled = true;

    button.dataset.originalText =
        button.textContent;

    button.textContent =
        loadingText;
}


function restoreButton(button) {

    button.disabled = false;

    button.textContent =
        button.dataset.originalText;
}


function createList(items) {

    if (
        !items ||
        !Array.isArray(items) ||
        items.length === 0
    ) {

        return `
            <p class="not-specified">
                Not specified
            </p>
        `;
    }


    return `
        <ul class="dashboard-list">

            ${items.map(item => `
                <li>${escapeHtml(item)}</li>
            `).join("")}

        </ul>
    `;
}


function escapeHtml(value) {

    const div =
        document.createElement("div");

    div.textContent =
        value;

    return div.innerHTML;
}


function createInfoCard(
    title,
    value
) {

    return `
        <div class="info-card">

            <h3>
                ${title}
            </h3>

            <p>
                ${escapeHtml(
                    value || "Not specified"
                )}
            </p>

        </div>
    `;
}


function displayJdAnalysis(data) {

    jdAnalysis.innerHTML = `

        <div class="dashboard-grid">

            ${createInfoCard(
                "Job Title",
                data.job_title
            )}

            ${createInfoCard(
                "Experience",
                data.experience_required
            )}

        </div>


        <div class="dashboard-section">

            <h3>
                Education
            </h3>

            <p>
                ${escapeHtml(
                    data.education_required ||
                    "Not specified"
                )}
            </p>

        </div>


        <div class="dashboard-section">

            <h3>
                Key Responsibilities
            </h3>

            ${createList(
                data.key_responsibilities
            )}

        </div>


        <div class="dashboard-section">

            <h3>
                Technical Skills
            </h3>

            ${createList(
                data.technical_skills
            )}

        </div>


        <div class="dashboard-section">

            <h3>
                Tools and Technologies
            </h3>

            ${createList(
                data.tools_and_technologies
            )}

        </div>


        <div class="dashboard-section">

            <h3>
                Soft Skills
            </h3>

            ${createList(
                data.soft_skills
            )}

        </div>


        <div class="dashboard-section">

            <h3>
                Other Requirements
            </h3>

            ${createList(
                data.other_requirements
            )}

        </div>
    `;
}


function displaySkills(data) {

    skillsAnalysis.innerHTML = `

        <div class="skill-category">

            <h3>
                Programming Languages
            </h3>

            ${createList(
                data.programming_languages
            )}

        </div>


        <div class="skill-category">

            <h3>
                Frameworks and Libraries
            </h3>

            ${createList(
                data.frameworks_and_libraries
            )}

        </div>


        <div class="skill-category">

            <h3>
                Databases
            </h3>

            ${createList(
                data.databases
            )}

        </div>


        <div class="skill-category">

            <h3>
                Backend and APIs
            </h3>

            ${createList(
                data.backend_and_apis
            )}

        </div>


        <div class="skill-category">

            <h3>
                Tools and Technologies
            </h3>

            ${createList(
                data.tools_and_technologies
            )}

        </div>


        <div class="skill-category">

            <h3>
                Other Technical Skills
            </h3>

            ${createList(
                data.other_technical_skills
            )}

        </div>


        <div class="skill-category">

            <h3>
                Soft Skills
            </h3>

            ${createList(
                data.soft_skills
            )}

        </div>
    `;
}


analyzeJdButton.addEventListener(
    "click",
    async () => {

        try {

            jdStatus.textContent =
                "Analyzing";

            showLoading(
                jdAnalysis,
                "Analyzing the job description..."
            );

            setButtonLoading(
                analyzeJdButton,
                "Analyzing..."
            );


            const response =
                await fetch(
                    "/api/analyze-jd",
                    {
                        method: "POST"
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
                    "Failed to analyze the job description."
                );
            }


            displayJdAnalysis(
                result.analysis
            );


            jdStatus.textContent =
                "Completed";


        } catch (error) {

            console.error(error);

            jdStatus.textContent =
                "Error";

            showError(
                jdAnalysis,
                error.message
            );


        } finally {

            restoreButton(
                analyzeJdButton
            );

        }
    }
);


analyzeSkillsButton.addEventListener(
    "click",
    async () => {

        try {

            skillsStatus.textContent =
                "Analyzing";

            showLoading(
                skillsAnalysis,
                "Identifying required skills..."
            );

            setButtonLoading(
                analyzeSkillsButton,
                "Analyzing..."
            );


            const response =
                await fetch(
                    "/api/analyze-skills",
                    {
                        method: "POST"
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
                    "Failed to analyze skills."
                );
            }


            displaySkills(
                result.skills
            );


            skillsStatus.textContent =
                "Completed";


        } catch (error) {

            console.error(error);

            skillsStatus.textContent =
                "Error";

            showError(
                skillsAnalysis,
                error.message
            );


        } finally {

            restoreButton(
                analyzeSkillsButton
            );

        }
    }
);


generateInterviewButton.addEventListener(
    "click",
    async () => {

        try {

            interviewStatus.textContent =
                "Generating";

            showLoading(
                interviewQuestions,
                "Generating interview questions..."
            );

            setButtonLoading(
                generateInterviewButton,
                "Generating..."
            );


            const response =
                await fetch(
                    "/api/generate-interview",
                    {
                        method: "POST"
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
                    "Failed to generate interview questions."
                );
            }


            interviewQuestions.innerHTML = "";

            const content =
                document.createElement("div");

            content.className =
                "generated-content";

            content.textContent =
                result.interview_questions;

            interviewQuestions.appendChild(
                content
            );


            interviewStatus.textContent =
                "Completed";


        } catch (error) {

            console.error(error);

            interviewStatus.textContent =
                "Error";

            showError(
                interviewQuestions,
                error.message
            );


        } finally {

            restoreButton(
                generateInterviewButton
            );

        }
    }
);


generatePreparationButton.addEventListener(
    "click",
    async () => {

        try {

            preparationStatus.textContent =
                "Generating";

            showLoading(
                preparationPlan,
                "Generating preparation plan..."
            );

            setButtonLoading(
                generatePreparationButton,
                "Generating..."
            );


            const response =
                await fetch(
                    "/api/generate-preparation",
                    {
                        method: "POST"
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
                    "Failed to generate preparation plan."
                );
            }


            preparationPlan.innerHTML = "";

            const content =
                document.createElement("div");

            content.className =
                "generated-content";

            content.textContent =
                result.preparation_plan;

            preparationPlan.appendChild(
                content
            );


            preparationStatus.textContent =
                "Completed";


        } catch (error) {

            console.error(error);

            preparationStatus.textContent =
                "Error";

            showError(
                preparationPlan,
                error.message
            );


        } finally {

            restoreButton(
                generatePreparationButton
            );

        }
    }
);