document.addEventListener("DOMContentLoaded", () => {

    const links = document.querySelectorAll("nav a");

    links.forEach(link => {
        link.addEventListener("mouseenter", () => {
            link.style.textShadow = "0 0 10px #00E5FF";
        });

        link.addEventListener("mouseleave", () => {
            link.style.textShadow = "none";
        });
    });

});