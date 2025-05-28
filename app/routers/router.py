from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.octave_runner import run_interpolation_lineal, run_no_lineal_interpolation, run_script_with_args, \
    run_portafolio, run_tir, calcular_opcion, solve_edo

router = APIRouter()

class InterpolationInput(BaseModel):
    x: float
    X: list[float]
    Y: list[float]


class PuntoFijoInput(BaseModel):
    x1: float
    KIC: float
    w: float
    Sigma: float
    TOL: float

class NewtonInput(BaseModel):
    x1: float
    TOL: float

class SecanteInput(BaseModel):
    x0: float
    x1: float
    TOL: float


class TIRInput(BaseModel):
    x1: float
    TOL: float
    inversion: float
    flujos: list[float]

class PortafolioInput(BaseModel):
    e1: float
    e2: float
    ep: float


class EdoInput(BaseModel):
    W0: float
    f: str
    t0: float
    T: float
    N: int
    metodo: Literal["euler", "rk2", "rk4"]


class OptionInput(BaseModel):
    K: float
    r: float
    T: float
    S0: float
    sigma: float


@router.post("/interpolate-lineal/")
def interpolate_lineal(data: InterpolationInput):
    result = run_interpolation_lineal(data.x, data.X, data.Y)
    if result.startswith("Error"):
        raise HTTPException(status_code=500, detail=result)
    return {"y": result}

@router.post("/interpolate-no-lineal/")
def interpolate_nonlinear(data: InterpolationInput):
    try:
        result = run_no_lineal_interpolation(data.x, data.X, data.Y)
        return {"y": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tir/")
def calcular_tir(data: TIRInput):
    try:
        return run_tir(data.x1, data.TOL, data.inversion, data.flujos)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/portafolio/")
def calcular_pesos(data: PortafolioInput):
    try:
        return run_portafolio(data.e1, data.e2, data.ep)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/resolver-edo/")
def resolver_edo(data: EdoInput):
    try:
        return solve_edo(**data.dict())
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/opcion/")
def calcular_valor_opcion(data: OptionInput):
    try:
        return calcular_opcion(data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
