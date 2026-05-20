function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="user"><strong>You:</strong> ${message}</div>`;
  input.value = "";

  fetch(`/ask/?message=${encodeURIComponent(message)}`)
  .then(res => res.json())
  .then(data => {
    chatBox.innerHTML += `<div class="bot"><strong>Bot:</strong> ${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  })
  .catch(err => {
    console.error("JSON error:", err);  // ✅ LOG ERROR
    chatBox.innerHTML += `<div class="bot"><strong>Error:</strong> Could not get a response.</div>`;
  });

}