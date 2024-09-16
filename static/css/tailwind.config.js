/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./**/*.html', './**/*.js',],
  darkMode: false,
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ]
}