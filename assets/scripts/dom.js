function htmlFromFile(id, f) {
  fetch(f)
  .then(response => response.text())
  .then(text => document.getElementById(id).innerHTML = text.trim())
}
