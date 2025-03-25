import type { Metadata } from 'next';
import { Inter, Lobster } from 'next/font/google';
import { Toaster } from 'react-hot-toast';
import './globals.css';

const inter = Inter({ subsets: ['latin'], variable: '--font-inter' });
const lobster = Lobster({ 
  weight: '400',
  subsets: ['latin'],
  variable: '--font-lobster',
});

export const metadata: Metadata = {
  title: 'Pickup Line Generator',
  description: 'Generate fun, clever, or cringey pickup lines using SmolLM!',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${lobster.variable} font-sans`}>
        {children}
        <Toaster position="bottom-center" />
      </body>
    </html>
  );
} 