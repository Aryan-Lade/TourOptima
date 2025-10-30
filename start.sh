#!/bin/bash

# Start backend in background
cd backend
pip install -r requirements.txt > /dev/null 2>&1
uvicorn main:app --reload --port 8000 &

# Start frontend
cd ../frontend
npm install > /dev/null 2>&1
npm run dev
