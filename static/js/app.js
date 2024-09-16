const body = document.querySelector("body")
const hamburgerMenu = document.querySelector("#hamburger-menu")
const dropdownMenu = document.querySelector("#dropdown-menu")
const themeMode = document.querySelector("#theme-mode")

hamburgerMenu.addEventListener("click", ()=>{
    dropdownMenu.classList.toggle("hidden")
})

themeMode.addEventListener("click", ()=>{
    body.classList.toggle("dark")
    if (body.classList.contains("dark")) {
        themeMode.src = lightModeIcon
        themeMode.alt = "Light mode"
    } else {
        themeMode.src = darkModeIcon
        themeMode.alt = "Dark mode"
    }
})
