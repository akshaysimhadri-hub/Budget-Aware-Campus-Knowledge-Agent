const API_URL = "https://budget-aware-campus-knowledge-agent-1.onrender.com/ask";

let processing = false;
let currentController = null;

// DOM Elements
const chat = document.getElementById("chat");
const history = document.getElementById("history");
const input = document.getElementById("input");
const sendBtn = document.getElementById("sendBtn");
const toggle = document.getElementById("toggle");
const suggestions = document.getElementById("suggestions");


const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");
const closeSidebar = document.getElementById("closeSidebar");

/* MOBILE SIDEBAR */
/* MOBILE SIDEBAR OPEN */
if (menuBtn) {

    menuBtn.onclick = () => {

        sidebar.classList.add("show-sidebar");
    };
}

/* MOBILE SIDEBAR CLOSE */
if (closeSidebar) {

    closeSidebar.onclick = () => {

        sidebar.classList.remove("show-sidebar");
    };
}


/* =========================
   THEME TOGGLE
========================= */
toggle.onclick = () => {

    document.body.classList.toggle("light");
    document.body.classList.toggle("dark");

    toggle.innerText =
        document.body.classList.contains("light")
            ? "🌙"
            : "☀️";
};

/* =========================
   SUGGESTION BUTTONS
========================= */
if (suggestions) {

    suggestions.addEventListener("click", (e) => {

        if (
            e.target.tagName === "BUTTON" &&
            !processing
        ) {

            input.value = e.target.innerText;

            send();
        }
    });
}

/* =========================
   SEND BUTTON
========================= */
sendBtn.onclick = () => {

    if (processing) {
        stopResponse();
    } else {
        send();
    }
};

/* =========================
   STOP RESPONSE
========================= */
function stopResponse() {

    if (currentController) {

        currentController.abort();

        processing = false;

        input.disabled = false;

        sendBtn.innerText = "➤";

        sendBtn.classList.remove("stop-active");

        // Remove loading indicators
        const loaders =
            document.querySelectorAll(".loading-msg");

        loaders.forEach(l => l.remove());

        // Stop message
        let stopMsg = document.createElement("div");

        stopMsg.className = "bot";

        stopMsg.style.color = "#ef4444";

        stopMsg.innerText = "🛑 Stopped.";

        chat.appendChild(stopMsg);
    }
}

/* =========================
   MAIN SEND FUNCTION
========================= */
async function send() {

    let text = input.value.trim();

    if (!text || processing) return;

    // Hide welcome
    const welcome = document.getElementById("welcome");

    if (welcome) {
        welcome.style.display = "none";
    }

    processing = true;

    input.disabled = true;

    input.value = "";

    // STOP button
    sendBtn.innerText = "■";

    sendBtn.classList.add("stop-active");

    /* =========================
       USER MESSAGE
    ========================= */
    let userDiv = document.createElement("div");

    userDiv.className = "user";

    userDiv.innerText = text;

    chat.appendChild(userDiv);

    userDiv.scrollIntoView({
        behavior: "smooth"
    });

    /* =========================
       LOADER
    ========================= */
    let loader = document.createElement("div");

    loader.className = "bot loading-msg";

    loader.innerText = "⏳ Thinking...";

    chat.appendChild(loader);

    /* =========================
       ABORT CONTROLLER
    ========================= */
    currentController = new AbortController();

    try {

        /* =========================
           API CALL
        ========================= */
        let res = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: text
            }),

            signal: currentController.signal
        });

        let data = await res.json();

        console.log("API RESPONSE:", data);

        loader.remove();

        /* =========================
           BOT MESSAGE
        ========================= */
        let botDiv = document.createElement("div");

        botDiv.className = "bot";

        // IMPORTANT FIX
        let answer =
            data.answer ||
            data.response ||
            data.error ||
            "No response received.";

        let content = `
            <div class="answer-text">
                ${answer}
            </div>
        `;

        /* =========================
           OPTIONAL SOURCES
        ========================= */
        if (
            data.sources &&
            Array.isArray(data.sources) &&
            data.sources.length > 0
        ) {

            content += `
                <div style="
                    margin-top:15px;
                    padding-top:10px;
                    border-top:1px solid rgba(255,255,255,0.1);
                ">
                    <strong>📚 Sources</strong>

                    <ul style="
                        margin-top:10px;
                        padding-left:20px;
                    ">
            `;

            data.sources.forEach(src => {

                content += `
                    <li style="margin-bottom:6px;">
                        ${src.source || "Unknown Source"}
                        ${src.page ? `(Page ${src.page})` : ""}
                    </li>
                `;
            });

            content += `
                    </ul>
                </div>
            `;
        }

        botDiv.innerHTML = content;

        chat.appendChild(botDiv);

        /* =========================
           SIDEBAR HISTORY
        ========================= */
        let histItem = document.createElement("div");

        histItem.innerText =
            text.length > 25
                ? text.substring(0, 25) + "..."
                : text;

        histItem.onclick = () => {

            userDiv.scrollIntoView({
                behavior: "smooth"
            });
        };

        history.appendChild(histItem);

        botDiv.scrollIntoView({
            behavior: "smooth"
        });

    } catch (err) {

        console.error(err);

        if (err.name === "AbortError") {

            console.log("User stopped request.");

        } else {

            loader.innerText =
                "❌ Connection Error.";
        }

    } finally {

        processing = false;

        input.disabled = false;

        sendBtn.innerText = "➤";

        sendBtn.classList.remove("stop-active");

        input.focus();
    }
}

/* =========================
   ENTER KEY SUPPORT
========================= */
input.addEventListener("keypress", (e) => {

    if (
        e.key === "Enter" &&
        !processing
    ) {

        send();
    }
});