// Handle alert messages
document.addEventListener('DOMContentLoaded', function() {
  const messages = document.querySelectorAll('.alert');
  messages.forEach(message => {
    const messageText = message.textContent.trim();
    if (message.classList.contains('alert-success')) {
      alert(messageText || 'Form submitted successfully!');
    } else if (message.classList.contains('alert-error') || message.classList.contains('alert-danger')) {
      alert('Error: ' + (messageText || 'There was an error submitting the form.'));
    }
  });
});
