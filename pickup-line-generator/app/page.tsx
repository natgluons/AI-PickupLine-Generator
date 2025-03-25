'use client';

import { useState } from 'react';
import { toast } from 'react-hot-toast';

const vibes = [
  { id: 'romantic', label: '💝 Romantic', emoji: '❤️' },
  { id: 'cheesy', label: '🧀 Cheesy', emoji: '😏' },
  { id: 'nerdy', label: '🤓 Nerdy', emoji: '🔬' },
  { id: 'cringe', label: '😬 Cringe', emoji: '😂' },
  { id: 'flirty', label: '😘 Flirty', emoji: '💋' },
];

export default function Home() {
  const [selectedVibe, setSelectedVibe] = useState(vibes[0].id);
  const [pickupLine, setPickupLine] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const generatePickupLine = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ vibe: selectedVibe }),
      });
      
      if (!response.ok) throw new Error('Failed to generate pickup line');
      
      const data = await response.json();
      setPickupLine(data.pickupLine);
    } catch (error) {
      toast.error('Failed to generate pickup line');
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(pickupLine);
      toast.success('Copied to clipboard!');
    } catch (error) {
      toast.error('Failed to copy');
    }
  };

  return (
    <main className="min-h-screen bg-pink-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-2xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-display font-bold text-pink-600 mb-4">
            💘 Pickup Line Generator
          </h1>
          <p className="text-gray-600">
            Generate fun, clever, or cringey pickup lines using SmolLM! Select a vibe and click generate to get started! 😏
          </p>
        </div>

        <div className="bg-white rounded-2xl shadow-xl p-8 space-y-6">
          <div className="space-y-4">
            <label htmlFor="vibe" className="block text-sm font-medium text-gray-700">
              Choose a vibe
            </label>
            <select
              id="vibe"
              value={selectedVibe}
              onChange={(e) => setSelectedVibe(e.target.value)}
              className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-pink-500 focus:border-pink-500 sm:text-sm rounded-md"
            >
              {vibes.map((vibe) => (
                <option key={vibe.id} value={vibe.id}>
                  {vibe.label}
                </option>
              ))}
            </select>
          </div>

          <button
            onClick={generatePickupLine}
            disabled={isLoading}
            className="w-full bg-gradient-to-r from-pink-500 to-pink-600 text-white py-3 px-4 rounded-lg font-medium hover:from-pink-600 hover:to-pink-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500 transition-all duration-200 shadow-md hover:shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? 'Generating...' : 'Generate Line'}
          </button>

          {pickupLine && (
            <div className="space-y-4">
              <div className="bg-pink-50 rounded-lg p-4">
                <p className="text-gray-800 text-lg">{pickupLine}</p>
              </div>
              
              <div className="flex space-x-4">
                <button
                  onClick={generatePickupLine}
                  className="flex-1 bg-white border border-pink-500 text-pink-500 py-2 px-4 rounded-lg font-medium hover:bg-pink-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500 transition-all duration-200"
                >
                  🔁 Generate Again
                </button>
                <button
                  onClick={copyToClipboard}
                  className="flex-1 bg-white border border-pink-500 text-pink-500 py-2 px-4 rounded-lg font-medium hover:bg-pink-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-pink-500 transition-all duration-200"
                >
                  📋 Copy
                </button>
              </div>
            </div>
          )}
        </div>

        <div className="mt-8 text-center text-gray-500">
          Built by Nath with SmolLM 🔥
        </div>
      </div>
    </main>
  );
} 