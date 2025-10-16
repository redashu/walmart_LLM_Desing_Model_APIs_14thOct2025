// Chatbot JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');
    
    if (chatForm && chatInput && chatMessages) {
        // Add welcome message
        addBotMessage('Hello! I am BLU, your Walmart assistant. How can I help you today?');
        
        chatForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const message = chatInput.value.trim();
            if (!message) return;
            
            // Add user message to chat
            addUserMessage(message);
            
            // Clear input
            chatInput.value = '';
            
            // Send message to server
            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ message: message })
                });
                
                const data = await response.json();
                
                // Add bot response
                setTimeout(() => {
                    addBotMessage(data.response);
                }, 500);
                
            } catch (error) {
                console.error('Error:', error);
                addBotMessage('Sorry, I encountered an error. Please try again.');
            }
        });
    }
});

function addUserMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    messageDiv.innerHTML = `<div class="message-content">${escapeHtml(message)}</div>`;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function addBotMessage(message) {
    const chatMessages = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot';
    messageDiv.innerHTML = `<div class="message-content">${escapeHtml(message)}</div>`;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function scrollToBottom() {
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
