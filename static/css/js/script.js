// Function to update status message after form submission
const statusMessage = document.getElementById('status-message');

// Micro-interaction: Status message update after automation starts
const startButton = document.querySelector('.btn-cta');
startButton.addEventListener('click', () => {
  statusMessage.innerText = "Automation has started!";
  statusMessage.style.color = "#00ff88";
});
