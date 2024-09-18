const body = document.querySelector("body")
const hamburgerMenu = document.querySelector("#hamburger-menu")
const dropdownMenu = document.querySelector("#dropdown-menu")
const themeMode = document.querySelector("#theme-mode")
const menuLinks = document.querySelectorAll("#dropdown-menu a")

hamburgerMenu.addEventListener("click", ()=>{
    dropdownMenu.classList.toggle("hidden")
})

menuLinks.forEach(link => {
    link.addEventListener("click", () => {
        dropdownMenu.classList.add("hidden")
    })
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
