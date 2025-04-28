async function greet() {
    const name = document.getElementById('nameInput').value || 'World'; // input value or default World
    const response = away fetch(`/api/hello?name=${encodeURIComponent(name)}`) // API call 
    const data = await response.json() // JSON response parse
    document.getElementById('response').textContent = data.message; // display the response

}

fetch('/api/health')
    .then(res => res.json())
    .then(data => console.log('Backend status', data.status));