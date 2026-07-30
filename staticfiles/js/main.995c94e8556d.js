// ==============================
// FreshCuts - Main JavaScript
// ==============================

document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // Loader
    // ==========================

    const loader = document.getElementById("loader");

    if (loader) {
        window.addEventListener("load", () => {
            setTimeout(() => {
                loader.style.opacity = "0";
                loader.style.visibility = "hidden";
            }, 500);
        });
    }

    // ==========================
    // Sticky Navbar
    // ==========================

    const navbar = document.querySelector(".premium-navbar");

    if (navbar) {
        window.addEventListener("scroll", () => {

            if (window.scrollY > 50) {

                navbar.style.background = "rgba(17,24,39,.95)";
                navbar.style.boxShadow = "0 12px 30px rgba(0,0,0,.15)";

            } else {

                navbar.style.background = "rgba(17,24,39,.85)";
                navbar.style.boxShadow = "none";

            }

        });
    }

    // ==========================
    // Active Navigation
    // ==========================

    const current = window.location.pathname;

    document.querySelectorAll(".nav-link").forEach(link => {

        if (link.getAttribute("href") === current) {

            link.classList.add("active");

        }

    });

});
