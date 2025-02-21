async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatWindow = document.getElementById("chat-window");
    const query = input.value.trim();
    if (!query) return;

    // Display user message
    chatWindow.innerHTML += `<div class="user-message">${query}</div>`;
    input.value = "";
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Fetch bot response
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query })
    });
    const data = await response.json();

    // Display bot response
    chatWindow.innerHTML += `<div class="bot-message">${data.response}</div>`;
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

document.getElementById("user-input").addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
});