document.addEventListener("DOMContentLoaded", function () {

    // ==========================
    // Elements
    // ==========================

    const chatToggle = document.getElementById("chat-toggle");
    const chatBox = document.getElementById("chat-box");
    const closeChat = document.getElementById("close-chat");
    const minimizeChat = document.getElementById("minimize-chat");

    const sendBtn = document.getElementById("send-btn");
   
  
let currentSpeech = null;

    const input = document.getElementById("user-message");
    const messages = document.getElementById("chat-messages");

    // ==========================
    // Open Chat
    // ==========================

    chatToggle.onclick = () => {

        chatBox.style.display = "flex";
        chatToggle.style.display = "none";

        input.focus();

    };

    // ==========================
    // Minimize
    // ==========================

    minimizeChat.onclick = () => {

        chatBox.style.display = "none";
        chatToggle.style.display = "flex";

    };

    // ==========================
    // Close
    // ==========================

    closeChat.onclick = () => {

        input.value = "";

        chatBox.style.display = "none";
        chatToggle.style.display = "flex";

    };

    // ==========================
    // Add Message
    // ==========================

    function addMessage(text, sender) {

        const div = document.createElement("div");

        div.className =
            sender === "user"
                ? "user-message"
                : "bot-message";

        div.innerHTML = text;

        messages.appendChild(div);

        messages.scrollTop = messages.scrollHeight;

    }

    // ==========================
    // Typing
    // ==========================

    function showTyping() {

        const typing = document.createElement("div");

        typing.className = "typing";

        typing.id = "typing";

        typing.innerHTML = `
            <span></span>
            <span></span>
            <span></span>
        `;

        messages.appendChild(typing);

        messages.scrollTop = messages.scrollHeight;

    }

    function hideTyping() {

        const typing = document.getElementById("typing");

        if (typing) typing.remove();

    }

    // ==========================
    // Send Message
    // ==========================

  // ==========================
// Send Message
// ==========================

async function sendMessage() {

    const text = input.value.trim();

    if (!text)
        return;

    // Stop previous AI voice
    window.speechSynthesis.cancel();

    addMessage(text, "user");

    input.value = "";

    showTyping();

    try {

        const response = await fetch("/chat/api/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: text
            })

        });

        const data = await response.json();

        hideTyping();

        addMessage(data.reply, "bot");

        // ==========================
        // AI Voice
        // ==========================

        
    }

    catch (error) {

        hideTyping();

        addMessage(
            "⚠️ Server Error. Please try again.",
            "bot"
        );

        console.error(error);

    }

}

    // ==========================
    // Send Button
    // ==========================

    sendBtn.onclick = sendMessage;

    // ==========================
    // Enter Key
    // ==========================

    input.addEventListener("keypress", function (e) {

        if (e.key === "Enter") {

            sendMessage();

        }

    });
    });

   

 

