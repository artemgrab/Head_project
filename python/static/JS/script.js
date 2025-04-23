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




document.addEventListener('DOMContentLoaded', function() {
    let editor = CodeMirror(document.getElementById('editor'), {
        mode: 'python',
        theme: 'default',
        lineNumbers: false,
        readOnly: false,
        lineWrapping: true
    });

    fetch('/get_function')
        .then(response => response.text())
        .then(code => {
            editor.setValue(code);
            setTimeout(() => makeInstructionsEditable(editor), 100);
        });

    function makeInstructionsEditable(editor) {
        const content = editor.getValue();
        const lines = content.split('\n');
        
        let instructionsLineNum = -1;
        let instructionsMatch = null;
        
        lines.forEach((line, index) => {
            if (line.includes('instructions =')) {
                instructionsLineNum = index;
                instructionsMatch = line.match(/instructions\s*=\s*["'](.*?)["']/);
            }
        });

        if (instructionsLineNum !== -1 && instructionsMatch) {
            const lineText = lines[instructionsLineNum];
            const valueStart = lineText.indexOf(instructionsMatch[1]);
            const beforeValue = lineText.substring(0, valueStart);

            editor.markText(
                {line: 0, ch: 0},
                {line: instructionsLineNum, ch: beforeValue.length},
                {readOnly: true, className: 'readonly-background'}
            );
            
            editor.markText(
                {line: instructionsLineNum, ch: beforeValue.length + instructionsMatch[1].length},
                {line: editor.lastLine(), ch: editor.getLine(editor.lastLine()).length},
                {readOnly: true, className: 'readonly-background'}
            );
        }
    }


    document.getElementById('saveButton').addEventListener('click', function() {
        const code = editor.getValue();
        fetch('/save_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: code,
                function_name: 'on_question_received'
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification('Збережено успішно!', 'success');
            } else {
                showNotification('Помилка: ' + data.message, 'error');
            }
        })
        .catch(error => {
            showNotification('Помилка збереження', 'error');
        });
    });

    function showNotification(message, type) {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
});