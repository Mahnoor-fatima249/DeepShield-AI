/* =====================================================
   DEEPSHIELD AI - DASHBOARD JAVASCRIPT
===================================================== */

document.addEventListener("DOMContentLoaded", () => {

    initializeSidebar();
    initializeQuickScan();
    initializeNotifications();
    initializeThreatAnimation();
    initializeActivityUpdates();

});

/* =====================================================
   SIDEBAR ACTIVE STATE
===================================================== */

function initializeSidebar() {

    const menuItems = document.querySelectorAll(".sidebar-menu li");

    menuItems.forEach(item => {

        item.addEventListener("click", () => {

            menuItems.forEach(li => {
                li.classList.remove("active");
            });

            item.classList.add("active");

        });

    });

}

/* =====================================================
   NOTIFICATIONS
===================================================== */

function initializeNotifications() {

    const notificationBtn =
        document.querySelector(".notification-btn");

    if (!notificationBtn) return;

    notificationBtn.addEventListener("click", () => {

        alert(
            "🔔 Notifications\n\n" +
            "• New scan completed\n" +
            "• Report generated\n" +
            "• Threat level updated"
        );

    });

}

/* =====================================================
   QUICK SCAN
===================================================== */

function initializeQuickScan() {

    const uploadZone =
        document.querySelector(".upload-zone");

    const scanButton =
        document.querySelector(".scan-btn");

    if (!uploadZone) return;

    uploadZone.addEventListener("dragover", (e) => {

        e.preventDefault();

        uploadZone.style.borderColor = "#00E5FF";
        uploadZone.style.transform = "scale(1.02)";

    });

    uploadZone.addEventListener("dragleave", () => {

        uploadZone.style.borderColor =
            "rgba(0,229,255,.25)";

        uploadZone.style.transform = "scale(1)";

    });

    uploadZone.addEventListener("drop", (e) => {

        e.preventDefault();

        const file = e.dataTransfer.files[0];

        if (!file) return;

        startScan(file.name);

    });

    if (scanButton) {

        scanButton.addEventListener("click", () => {

            startScan("sample_media.mp4");

        });

    }

}

/* =====================================================
   SCAN SIMULATION
===================================================== */

function startScan(fileName) {

    const uploadZone =
        document.querySelector(".upload-zone");

    if (!uploadZone) return;

    uploadZone.innerHTML = `
        <i class="fa-solid fa-microchip"></i>
        <p>AI Analysis Started</p>
        <h3>${fileName}</h3>
        <div class="progress-wrapper">
            <div class="progress-bar"></div>
        </div>
        <div class="progress-text">0%</div>
    `;

    const progressBar =
        document.querySelector(".progress-bar");

    const progressText =
        document.querySelector(".progress-text");

    let progress = 0;

    const interval = setInterval(() => {

        progress += 2;

        progressBar.style.width =
            progress + "%";

        progressText.textContent =
            progress + "%";

        if (progress >= 100) {

            clearInterval(interval);

            finishScan(fileName);

        }

    }, 80);

}

/* =====================================================
   FINISH SCAN
===================================================== */

function finishScan(fileName) {

    const uploadZone =
        document.querySelector(".upload-zone");

    const scores = [92, 88, 95, 83, 90];
    const score =
        scores[Math.floor(Math.random() * scores.length)];

    uploadZone.innerHTML = `
        <i class="fa-solid fa-circle-check"></i>
        <h3>Scan Complete</h3>
        <p>${fileName}</p>
        <p>Authenticity Score: ${score}%</p>
    `;

    updateStats();
    addActivity(
        `${fileName} scan completed`
    );

}

/* =====================================================
   UPDATE STATS
===================================================== */

function updateStats() {

    const stats =
        document.querySelectorAll(".stat-card h3");

    if (stats.length < 1) return;

    let total =
        parseInt(
            stats[0].textContent.replace(/,/g, "")
        );

    total++;

    stats[0].textContent =
        total.toLocaleString();

}

/* =====================================================
   THREAT LEVEL ANIMATION
===================================================== */

function initializeThreatAnimation() {

    const threatCircle =
        document.querySelector(".threat-circle");

    if (!threatCircle) return;

    const states = [

        {
            level: "LOW",
            color: "#00ff9d"
        },

        {
            level: "MEDIUM",
            color: "#f59e0b"
        },

        {
            level: "HIGH",
            color: "#ff4d6d"
        }

    ];

    let index = 2;

    setInterval(() => {

        const current =
            states[index];

        threatCircle.textContent =
            current.level;

        threatCircle.style.borderColor =
            current.color;

        threatCircle.style.boxShadow =
            `0 0 30px ${current.color}`;

        index++;

        if (index >= states.length) {
            index = 0;
        }

    }, 6000);

}

/* =====================================================
   RECENT ACTIVITY
===================================================== */

function initializeActivityUpdates() {

    setInterval(() => {

        const randomActivities = [

            "Image analysis completed",
            "Video scan generated",
            "Threat score updated",
            "Report exported",
            "Metadata verification finished",
            "GAN analysis executed"

        ];

        const activity =
            randomActivities[
                Math.floor(
                    Math.random() *
                    randomActivities.length
                )
            ];

        addActivity(activity);

    }, 25000);

}

/* =====================================================
   ADD ACTIVITY
===================================================== */

function addActivity(message) {

    const activityCard =
        document.querySelector(".activity-card");

    if (!activityCard) return;

    const item =
        document.createElement("div");

    item.classList.add("activity-item");

    item.innerHTML = `
        ${message}
        <span>Just now</span>
    `;

    activityCard.appendChild(item);

    const activities =
        activityCard.querySelectorAll(
            ".activity-item"
        );

    if (activities.length > 8) {

        activities[0].remove();

    }

}

/* =====================================================
   CHART AUTO REFRESH EVENT
===================================================== */

setInterval(() => {

    console.log(
        "Analytics synchronized"
    );

}, 30000);

/* =====================================================
   DASHBOARD READY
===================================================== */

console.log(
    "DeepShield AI Dashboard Ready"
);