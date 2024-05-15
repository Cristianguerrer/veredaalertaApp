document.getElementById('addAlertButton').addEventListener('click', addOrUpdateAlert);

let isUpdating = false;
let currentAlertId = null;

function addOrUpdateAlert() {
    const message = document.getElementById('message').value;
    const level = document.getElementById('level').value;

    if (!message || !level) {
        alert('Por favor, completa todos los campos.');
        return;
    }

    const formData = new FormData();
    formData.append('message', message);
    formData.append('level', level);

    if (isUpdating && currentAlertId) {
        fetch(`/update_alert/${currentAlertId}`, {
            method: 'PUT',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                document.getElementById(currentAlertId).remove();
                const alert = {
                    _id: currentAlertId,
                    message: message,
                    level: level,
                    timestamp: new Date().toLocaleString()
                };
                addAlertToList(alert);
                resetForm();
            }
        });
    } else {
        fetch('/add_alert', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(alert => {
            addAlertToList(alert);
            resetForm();
        });
    }
}

function addAlertToList(alert) {
    const alertsList = document.getElementById('alertsList');
    const li = document.createElement('li');
    li.id = alert._id;
    li.innerHTML = `<strong>${alert.timestamp} - ${alert.level}</strong><br>${alert.message}
                    <button onclick="deleteAlert('${alert._id}')">Eliminar</button>
                    <button onclick="showUpdateForm('${alert._id}', '${alert.message}', '${alert.level}')">Actualizar</button>`;
    alertsList.appendChild(li);
}

function deleteAlert(alert_id) {
    fetch(`/delete_alert/${alert_id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            document.getElementById(alert_id).remove();
        }
    });
}

function showUpdateForm(alert_id, message, level) {
    const messageField = document.getElementById('message');
    const levelField = document.getElementById('level');
    messageField.value = message;
    levelField.value = level;

    isUpdating = true;
    currentAlertId = alert_id;

    document.getElementById('addAlertButton').textContent = 'Actualizar Alerta';
}

function resetForm() {
    document.getElementById('message').value = '';
    document.getElementById('level').value = 'Alto';
    document.getElementById('addAlertButton').textContent = 'Agregar Alerta';
    isUpdating = false;
    currentAlertId = null;
}

function filterAlerts() {
    const level = document.getElementById('filterLevel').value;
    const alertsList = document.getElementById('alertsList');
    alertsList.innerHTML = '';

    let url = '/get_alerts';
    if (level) {
        url = `/filter_alerts/${level}`;
    }

    fetch(url)
        .then(response => response.json())
        .then(alerts => {
            alerts.forEach(alert => addAlertToList(alert));
        });
}

window.onload = function() {
    fetch('/get_alerts')
        .then(response => response.json())
        .then(alerts => {
            alerts.forEach(alert => addAlertToList(alert));
        });
}
