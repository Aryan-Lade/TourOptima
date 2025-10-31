from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Destination(BaseModel):
    name: str
    value: float
    cost: float
    time: float

class OptimizeRequest(BaseModel):
    destinations: List[Destination]
    mode: str  # "time" or "budget"
    limit: float

class OptimizeResponse(BaseModel):
    selected_destinations: List[dict]
    total_value: float
    total_cost: float

def fractional_knapsack(destinations, limit, mode):
    # Use cost or time based on mode
    if mode == "budget":
        items = [(d.name, d.value, d.cost, d.value/d.cost, d.time) for d in destinations]
    else:  # time mode
        items = [(d.name, d.value, d.time, d.value/d.time, d.cost) for d in destinations]
    
    items.sort(key=lambda x: x[3], reverse=True)
    
    selected = []
    total_value = 0
    total_constraint = 0
    
    for name, value, constraint_value, ratio, other_value in items:
        if total_constraint + constraint_value <= limit:
            # Take full item
            selected.append({
                "name": name, 
                "value": value, 
                "cost": other_value if mode == "time" else constraint_value,
                "time": constraint_value if mode == "time" else other_value,
                "fraction": 1.0
            })
            total_value += value
            total_constraint += constraint_value
        else:
            # Take fractional item
            remaining = limit - total_constraint
            if remaining > 0:
                fraction = remaining / constraint_value
                selected.append({
                    "name": name, 
                    "value": value * fraction, 
                    "cost": (other_value * fraction) if mode == "time" else remaining,
                    "time": remaining if mode == "time" else (other_value * fraction),
                    "fraction": fraction
                })
                total_value += value * fraction
                total_constraint += remaining
            break
    
    return selected, total_value, total_constraint

@app.post("/optimize", response_model=OptimizeResponse)
async def optimize_destinations(request: OptimizeRequest):
    selected, total_value, total_cost = fractional_knapsack(request.destinations, request.limit, request.mode)
    
    return OptimizeResponse(
        selected_destinations=selected,
        total_value=total_value,
        total_cost=total_cost
    )
