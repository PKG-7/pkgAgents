const themeToggle = document.getElementById('theme-toggle')
const sunIcon = themeToggle.querySelector('.sun')
const moonIcon = themeToggle.querySelector('.moon')
const html = document.documentElement
const body = document.body
const elementsApi = document.querySelector('elements-api')

// Проверяем сохраненную тему
const savedTheme = localStorage.getItem('theme') || 'dark'
setTheme(savedTheme)

themeToggle.addEventListener('click', () => {
    const currentTheme = html.getAttribute('data-theme')
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark'
    setTheme(newTheme)
    localStorage.setItem('theme', newTheme)
})

function setTheme(theme) {
    html.setAttribute('data-theme', theme)
    body.setAttribute('data-theme', theme)
    elementsApi.setAttribute('appearance', theme)

    if (theme === 'dark') {
        sunIcon.style.display = 'block'
        moonIcon.style.display = 'none'
    } else {
        sunIcon.style.display = 'none'
        moonIcon.style.display = 'block'
    }
}
