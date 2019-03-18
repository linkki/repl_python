function toggleShowReplExercise(id, name) {
  var el = document.getElementById(id)
  var button = document.getElementById(id + "Button")
  console.log(el.style.visibility)
  if (el.classList.contains("exerciseHidden")) {
    button.innerHTML = name + ' (piilota)'
    el.classList.remove("exerciseHidden")
    el.classList.add("exerciseVisible")
  } else {
    button.innerHTML = name
    el.classList.remove("exerciseVisible")
    el.classList.add("exerciseHidden")
  }
}

function createReplExercise(content, id, name, src) {
  const f = `toggleShowReplExercise('${id}', '${name}')`
  const button = `
  <div class="centered">
    <button id="${id}Button" class="btn replToggleButton" onclick="${f}">
      ${name}
    </button>
  </div>`

  const frame = `
    <iframe height="1000px" width="100%" src="${src}" scrolling="no" frameborder="no"
    allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals">
    </iframe>
   </br>`

  document.write(button + `<div id="${id}" class="exerciseHidden">` + content + frame + '</div>')
}
