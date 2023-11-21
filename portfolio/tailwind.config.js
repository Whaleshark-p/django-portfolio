/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./main/templates/main/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'strato': '#439CFB',
        'meso': '#250032',
        'exo': '#210024',
        'strato-a': 'rgba(67, 156, 251, 0.5)',
        'meso-a': 'rgba(37,0,50,0.5)',
        'exo-a': 'rgba(33,0,36,0.8)',
        'exo-b': '#292338',
      },
      fontFamily: {
        'lexend': ['"Lexend"', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

