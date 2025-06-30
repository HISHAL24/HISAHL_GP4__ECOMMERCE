const apiUrl = 'http://localhost:5000/catalogues';

function showSection(id) {
  document.querySelectorAll('.section').forEach(s => s.style.display = 'none');
  document.getElementById(id).style.display = 'flex';
}

function createCatalogue() {
  const data = {
    catalogue_name: document.getElementById('c_name').value,
    catalogue_description: document.getElementById('c_desc').value,
    effective_from: document.getElementById('c_from').value,
    effective_to: document.getElementById('c_to').value,
    status: document.getElementById('c_status').value
  };
  fetch(apiUrl, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }).then(() => alert("Catalogue Created Successfully"));
}


function getCatalogueById() {
  const id = document.getElementById('get_id').value;
  fetch(`${apiUrl}/${id}`)
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById('get_result');
      container.innerHTML = ""; // Clear previous result

      if (data.error) {
        container.innerHTML = `<p style="color:red;">${data.error}</p>`;
        return;
      }

      const card = document.createElement('div');
      card.className = 'card';
      card.innerHTML = `
        <h3>${data.catalogue_name} <span class="badge">#${data.catalogue_id}</span></h3>
        <p><strong>Description:</strong> ${data.catalogue_description}</p>
        <p><strong>Status:</strong> <span class="status ${data.status.toLowerCase()}">${data.status}</span></p>
        <p><strong>From:</strong> ${formatDate(data.effective_from)}</p>
        <p><strong>To:</strong> ${formatDate(data.effective_to)}</p>
      `;
      container.appendChild(card);
    });
}

  

function updateCatalogue() {
  const id = document.getElementById('u_id').value;
  const data = {
    catalogue_name: document.getElementById('u_name').value,
    catalogue_description: document.getElementById('u_desc').value,
    effective_from: document.getElementById('u_from').value,
    effective_to: document.getElementById('u_to').value,
    status: document.getElementById('u_status').value
  };
  fetch(`${apiUrl}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }).then(() => alert("Catalogue Updated Successfully"));
}

function deleteCatalogue() {
  const id = document.getElementById('del_id').value;
  fetch(`${apiUrl}/${id}`, { method: 'DELETE' })
    .then(() => alert("Catalogue Deleted Successfully"));
}


function formatDate(dateStr) {
  const date = new Date(dateStr);
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0'); // months are 0-based
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
}


function getAllCatalogues() {
  fetch(apiUrl)
    .then(res => res.json())
    .then(data => {
      showSection('all_catalogues');
      const container = document.getElementById('all_data');
      container.innerHTML = ""; // Clear existing content

      if (data.length === 0) {
        container.innerHTML = "<p>No catalogues found.</p>";
        return;
      }

      data.forEach(c => {
        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
          <h3>${c.catalogue_name} <span class="badge">#${c.catalogue_id}</span></h3>
          <p><strong>Description:</strong> ${c.catalogue_description}</p>
          <p><strong>Status:</strong> <span class="status ${c.status.toLowerCase()}">${c.status}</span></p>
          <p><strong>From:</strong> ${formatDate(c.effective_from)}</p>
          <p><strong>To:</strong> ${formatDate(c.effective_to)}</p>


        `;
        container.appendChild(card);
      });
    });
}


function exitApp() {
  alert("Exiting application...");
  location.reload();
}









