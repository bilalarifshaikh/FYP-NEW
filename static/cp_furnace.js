// Select all processes
const processes = document.querySelectorAll(".process");

// Define dependencies
const dependencies = {
    stamping: ["polishing"],
    "cold-forming": ["polishing"],
    "pin-cutting": ["polishing"],
    polishing: ["drying-1", "drying-2"],
    "drying-1": ["cp-furnace"],
    "drying-2": ["cp-furnace"],
    "cp-furnace": ["tumbler-polishing", "shot-peening"],
    "tumbler-polishing": ["drying-final"],
    "shot-peening": ["drying-final"],
    "drying-final": ["dispatch"],
};

// Function to create an arrow
function createArrow() {
    const arrow = document.createElement("div");
    arrow.classList.add("arrow");
    return arrow;
}

// Add arrows dynamically based on dependencies
processes.forEach((process) => {
    const processId = process.id;
    const arrowContainer = process.querySelector(".arrow-container");

    if (dependencies[processId]) {
        dependencies[processId].forEach(() => {
            arrowContainer.appendChild(createArrow());
        });
    }
});

// Highlight functionality for interaction
processes.forEach((process) => {
    process.addEventListener("click", () => {
        // Reset highlights
        processes.forEach((p) => p.classList.remove("selected"));
        document.querySelectorAll(".arrow").forEach((arrow) => arrow.classList.remove("highlight"));

        // Highlight the selected process
        process.classList.add("selected");

        // Highlight dependent processes and their arrows
        const processId = process.id;
        if (dependencies[processId]) {
            dependencies[processId].forEach((depId) => {
                document.getElementById(depId)?.classList.add("selected");
                document.querySelectorAll(`#${depId} .arrow`).forEach((arrow) => arrow.classList.add("highlight"));
            });
        }
    });
});
