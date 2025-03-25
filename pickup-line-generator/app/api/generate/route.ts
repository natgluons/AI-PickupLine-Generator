import { NextResponse } from 'next/server';
import { getVibeGuidance } from '@/lib/prompts';

export async function POST(request: Request) {
  // Handle CORS
  if (request.method === 'OPTIONS') {
    return new NextResponse(null, {
      status: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      },
    });
  }

  try {
    const { vibe } = await request.json();
    
    // Get the vibe guidance
    const vibeGuide = getVibeGuidance(vibe);
    
    // Create the prompt
    const prompt = `Instructions: Generate a pickup line with a ${vibe} vibe.\n${vibeGuide}`;
    
    // TODO: Replace this with actual model inference
    // For now, return a mock response
    const mockResponses = {
      romantic: "Are you a magician? Because whenever I look at you, everyone else disappears. ❤️",
      cheesy: "Are you a parking ticket? Because you've got FINE written all over you! 😏",
      nerdy: "Are you made of copper and tellurium? Because you're Cu-Te! 🔬",
      cringe: "Are you a dictionary? Because you're adding meaning to my life! 📚",
      flirty: "Is your name Google? Because you've got everything I've been searching for! 😏"
    };

    const response = NextResponse.json({ pickupLine: mockResponses[vibe as keyof typeof mockResponses] });
    
    // Add CORS headers to the response
    response.headers.set('Access-Control-Allow-Origin', '*');
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    
    return response;
  } catch (error) {
    console.error('Error generating pickup line:', error);
    const errorResponse = NextResponse.json(
      { error: 'Failed to generate pickup line' },
      { status: 500 }
    );
    
    // Add CORS headers to the error response
    errorResponse.headers.set('Access-Control-Allow-Origin', '*');
    errorResponse.headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    errorResponse.headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    
    return errorResponse;
  }
} 