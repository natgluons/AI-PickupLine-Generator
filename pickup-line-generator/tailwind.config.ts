import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--font-inter)'],
        display: ['var(--font-lobster)'],
      },
      colors: {
        pink: {
          50: '#fef6f9',
          500: '#ff69b4',
          600: '#ff1493',
          700: '#db2777',
        },
      },
    },
  },
  plugins: [],
};

export default config; 