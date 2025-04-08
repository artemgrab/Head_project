document.querySelectorAll(".accordion-i").forEach(item => {
  item.addEventListener("click", (event) => {
      if (event.target.closest(".accordion-above") || event.target.closest(".accordion-t")) {
          item.classList.toggle("active");
      }
  });
});


document.getElementById('scriptToggle').addEventListener('click', function() {
  const button = this;
  const action = button.textContent === 'Увімкнути' ? 'start' : 'stop';
  
  fetch('/toggle_script', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ action: action })
  })
  .then(response => response.json())
  .then(data => {
      if (data.status === 'started' || data.status === 'stopped') {
          button.textContent = action === 'start' ? 'Вимкнути' : 'Увімкнути';
      }
  })
  .catch(error => console.error('Error:', error));
});