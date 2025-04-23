from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.octave_runner import run_interpolation_lineal

router = APIRouter()

class InterpolationInput(BaseModel):
    x: float
    X: list[float]
    Y: list[float]

@router.post("/interpolate-lineal/")
def interpolate_lineal(data: InterpolationInput):
    result = run_interpolation_lineal(data.x, data.X, data.Y)
    if result.startswith("Error"):
        raise HTTPException(status_code=500, detail=result)
    return {"y": result}
