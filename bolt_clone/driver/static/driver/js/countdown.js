document.addEventListener('DOMContentLoaded', function () {
  let countdownTime = 30;

  const countdownElement = document.getElementById('counter');
  const actionButton = document.getElementById('repeat-btn');
  const countdownContainer = document.getElementById("countdown");

  function updateCountdown() {
    countdownElement.textContent = countdownTime;
    if (countdownTime === 0) {
      actionButton.style.display = 'block';
      countdownContainer.style.display = "none";
    } else {
      countdownTime--;
      setTimeout(updateCountdown, 1000);
    }
  }
  updateCountdown();
});