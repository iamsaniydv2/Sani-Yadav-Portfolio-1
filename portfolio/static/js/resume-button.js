// Handle resume button click
document.addEventListener('DOMContentLoaded', function() {
  const resumeButton = document.getElementById('resumeButton');
  if (resumeButton) {
    resumeButton.addEventListener('click', function(e) {
      e.preventDefault();
      const pdfUrl = this.getAttribute('data-pdf');
      if (pdfUrl) window.open(pdfUrl, '_blank');
    });
  }
});
