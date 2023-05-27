// Establish socket connection
const socket = io.connect();

// DOM elements
const statusElement = document.getElementById('status');
const messagesElement = document.getElementById('messages');
const messageInput = document.getElementById('message');

// Handle socket events
socket.on("connect", () => {
  statusElement.classList.add('online');
});

socket.on("disconnect", () => {
  statusElement.classList.remove('online');
});

socket.on('broadcast', (data) => {
  const time = getCurrentTime();

  const messageElement = document.createElement('div');
  messageElement.classList.add('message', 'left');
  messageElement.innerHTML = `
    <div class='container'>
      <p>
        <span class='username'>${data.username}</span>${data.message}
      </p>
      <p class='timeStamp left'>${time}</p>
    </div>
  `;

  messagesElement.appendChild(messageElement);
  scrollToBottom();
});

// Send message on Enter key press
document.addEventListener('keyup', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

// Get current time in HH:MM format
function getCurrentTime() {
  const today = new Date();
  const hours = today.getHours();
  const minutes = today.getMinutes();
  const formattedHours = hours.toString().padStart(2, '0');
  const formattedMinutes = minutes.toString().padStart(2, '0');
  return `${formattedHours}:${formattedMinutes}`;
}

// Send message
function sendMessage() {
  const message = messageInput.value.trim();
  messageInput.value = '';

  if (message !== '') {
    const json = {
      message: message
    };

    socket.emit('send', json);

    const today = new Date();
    const time = getCurrentTime();

    const messageElement = document.createElement('div');
    messageElement.classList.add('message', 'right');
    messageElement.innerHTML = `
      <div class='container'>
        <p>${message}</p>
        <p class='timeStamp right'>${time}</p>
      </div>
    `;

    messagesElement.appendChild(messageElement);
    scrollToBottom();
  }
}

// Scroll to the bottom of the messages container
function scrollToBottom() {
  const lastMessage = messagesElement.lastElementChild;
  lastMessage.scrollIntoView({ behavior: 'smooth' });
}
