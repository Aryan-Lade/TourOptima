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

class OptimizeRequest(BaseModel):
    destinations: List[Destination]
    mode: str  # "time" or "budget"
    limit: float

class OptimizeResponse(BaseModel):
    selected_destinations: List[dict]
    total_value: float
    total_cost: float

def fractional_knapsack(destinations, limit):
    # Calculate value-to-cost ratio and sort
    items = [(d.name, d.value, d.cost, d.value/d.cost) for d in destinations]
    items.sort(key=lambda x: x[3], reverse=True)
    
    selected = []
    total_value = 0
    total_cost = 0
    
    for name, value, cost, ratio in items:
        if total_cost + cost <= limit:
            # Take full item
            selected.append({"name": name, "value": value, "cost": cost, "fraction": 1.0})
            total_value += value
            total_cost += cost
        else:
            # Take fractional item
            remaining = limit - total_cost
            if remaining > 0:
                fraction = remaining / cost
                selected.append({"name": name, "value": value * fraction, "cost": remaining, "fraction": fraction})
                total_value += value * fraction
                total_cost += remaining
            break
    
    return selected, total_value, total_cost

@app.post("/optimize", response_model=OptimizeResponse)
async def optimize_destinations(request: OptimizeRequest):
    selected, total_value, total_cost = fractional_knapsack(request.destinations, request.limit)
    
    return OptimizeResponse(
        selected_destinations=selected,
        total_value=total_value,
        total_cost=total_cost
    )
