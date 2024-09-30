/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',   // Ensure Tailwind scans all HTML files in templates folder
    './main/**/*.html',        // Add your app's HTML folder (adjust as needed)
    './templates/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'depe' : '#0a9680',
      },
      spacing: {
        '96': '24rem',
        '84' : '21rem',
        '72' : '18rem',
        '60' : '15rem',
        '48' : '12rem',
        '36' : '9rem',
      },
      fontFamily: {
        fredoka: 'Fredoka',  // Add Fredoka as a custom font family
      },
    },
  },
  plugins: [],
}
