/* ==========================================
   DEEPSHIELD AI - AUTH SYSTEM (FRONTEND ONLY)
   LocalStorage Based Simulation
========================================== */

document.addEventListener("DOMContentLoaded", () => {

    handleRegister();
    handleLogin();
    protectDashboard();

});

/* ==========================================
   REGISTER USER
========================================== */

function handleRegister() {

    const form = document.querySelector("form");

    if (!form || !window.location.href.includes("register")) return;

    form.addEventListener("submit", (e) => {

        e.preventDefault();

        const inputs = form.querySelectorAll("input");

        const name = inputs[0].value;
        const email = inputs[1].value;
        const password = inputs[2].value;
        const confirmPassword = inputs[3].value;

        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        const user = {
            name,
            email,
            password
        };

        localStorage.setItem("ds_user", JSON.stringify(user));

        alert("Account created successfully!");

        window.location.href = "login.html";

    });

}

/* ==========================================
   LOGIN USER
========================================== */

function handleLogin() {

    const form = document.querySelector("form");

    if (!form || !window.location.href.includes("login")) return;

    form.addEventListener("submit", (e) => {

        e.preventDefault();

        const inputs = form.querySelectorAll("input");

        const email = inputs[0].value;
        const password = inputs[1].value;

        const storedUser =
            JSON.parse(localStorage.getItem("ds_user"));

        if (!storedUser) {
            alert("No account found. Please register first.");
            return;
        }

        if (
            email === storedUser.email &&
            password === storedUser.password
        ) {

            localStorage.setItem("ds_logged_in", "true");

            alert("Login successful!");

            window.location.href = "../pages/dashboard.html";

        } else {
            alert("Invalid email or password!");
        }

    });

}

/* ==========================================
   PROTECT DASHBOARD PAGES
========================================== */

function protectDashboard() {

    const isDashboard =
        window.location.href.includes("dashboard.html");

    const isProtectedPage =
        window.location.href.includes("/pages/");

    const loggedIn =
        localStorage.getItem("ds_logged_in");

    if (isDashboard || isProtectedPage) {

        if (!loggedIn) {

            // Allow public pages only
            if (
                window.location.href.includes("login") ||
                window.location.href.includes("register") ||
                window.location.href.includes("forgot-password")
            ) {
                return;
            }

            // Redirect to login if not authenticated
            window.location.href = "login.html";

        }

    }

}

/* ==========================================
   LOGOUT FUNCTION (optional future use)
========================================== */

function logout() {

    localStorage.removeItem("ds_logged_in");

    alert("Logged out successfully!");

    window.location.href = "../pages/login.html";

}