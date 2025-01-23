// Select all parts
const parts = document.querySelectorAll(".part");
const arrows = document.querySelectorAll(".arrow");

// Add click event to parts
parts.forEach((part) => {
    part.addEventListener("click", () => {
        // Reset all parts and arrows
        parts.forEach((p) => p.classList.remove("selected"));
        arrows.forEach((arrow) => arrow.classList.remove("highlight"));

        // Set selected state
        const color = part.getAttribute("data-color");
        part.classList.add("selected");

        // Update CSS variable for dynamic coloring
        document.documentElement.style.setProperty("--part-color", color);

        // Highlight arrows
        arrows.forEach((arrow) => arrow.classList.add("highlight"));
    });
});
