import { NextResponse } from 'next/server';
import { generatePickupLine } from '@/lib/model';

export async function POST(request: Request) {
  try {
    const { vibe } = await request.json();
    
    if (!vibe) {
      return NextResponse.json(
        { error: 'Vibe is required' },
        { status: 400 }
      );
    }

    const pickupLine = await generatePickupLine(vibe);
    return NextResponse.json({ pickupLine });
  } catch (error) {
    console.error('Error:', error);
    return NextResponse.json(
      { error: 'Failed to generate pickup line' },
      { status: 500 }
    );
  }
} 