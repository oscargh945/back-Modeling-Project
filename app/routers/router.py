from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.octave_runner import run_interpolation_lineal, run_no_lineal_interpolation, run_script_with_args, \
    run_portafolio, run_tir

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

@router.post("/punto-fijo/")
def metodo_punto_fijo(data: PuntoFijoInput):
    args = [str(data.x1), str(data.KIC), str(data.w), str(data.Sigma), str(data.TOL)]
    return run_script_with_args("MetPuntFijo.m", args)

@router.post("/newton-raphson/")
def metodo_newton_raphson(data: NewtonInput):
    args = [str(data.x1), str(data.TOL)]
    return run_script_with_args("N_R.m", args)

@router.post("/secante/")
def metodo_secante(data: SecanteInput):
    args = [str(data.x0), str(data.x1), str(data.TOL)]
    return run_script_with_args("Secante.m", args)

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
