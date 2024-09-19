/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './portfolio/templates/portfolio/*.html',
  ],
  darkMode: 'class',
  theme: {
    colors: {
      'f-blue': '#89b4fa',
      'f-lavender': '#b4befe',
      'f-pink': '#f5c2e7',
      'f-red': '#f38ba8',
      'f-peach': '#fab387',
      'f-teal': '#94e2d5',
      'f-yellow': '#f9e2af',
      'f-gray-dark': '#181825',
      'f-gray': '#1e1e2e',
      'f-gray-light': '#313244',
      'f-white': '#cdd6f4',
      'l-blue': '#1e66f5',
      'l-lavender': '#7287fd',
      'l-pink': '#ea76cb',
      'l-maroon': '#e64553',
      'l-rosewater': '#dc8a78',
      'l-teal': '#179299',
      'l-yellow': '#df8e1d',
      'l-gray-dark': '#4c4f69',
      'l-gray': '#5c5f77',
      'l-gray-light': '#9ca0b0',
      'l-white': '#eff1f5',
      'l-crust': '#dce0e8',
      'black': '#11111b'
    },
    fontFamily: {
      jetbrainsmono:["JetBrains Mono", 'monospace']
    },
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/container-queries'),
  ]
}
