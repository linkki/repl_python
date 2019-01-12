function htmlFromFile(f) {
  fetch(f + '.html')
  .then(response => response.text())
  .then(text => document.getElementById(f).innerHTML = text.trim())
}
