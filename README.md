# Tourist Destination Optimization

A web application that uses the Fractional Knapsack Algorithm to optimize tourist destination selection based on budget or time constraints.

## Live Preview:  
https://tour-optima.vercel.app/

## Setup

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend (React + Tailwind)
```bash
cd frontend
npm install
npm run dev
```

## Usage

1. Add tourist destinations with their value (satisfaction score) and cost (money/time)
2. Choose optimization mode (Budget or Time constraint)
3. Set your limit
4. Click "Optimize Destinations" to see the optimal selection
5. View results in charts and summary cards

The algorithm maximizes value while staying within your constraints, using fractional selection when needed.
