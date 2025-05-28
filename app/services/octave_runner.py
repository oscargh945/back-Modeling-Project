import subprocess
import re
from typing import List, Literal
import numpy as np


def run_script_with_args(script_name: str, args: list[str]) -> dict:
    try:
        result = subprocess.run(
            ["octave", "--quiet", script_name] + args,
            capture_output=True,
            text=True,
            cwd="octave"
        )

        if result.returncode != 0:
            print("STDERR:", result.stderr)
            raise RuntimeError(result.stderr)

        root_match = re.search(r"ROOT=([\d\.\-eE]+)", result.stdout)
        iter_match = re.search(r"ITER=(\d+)", result.stdout)

        if not root_match or not iter_match:
            raise ValueError("No se pudo parsear la salida de Octave.")

        return {
            "root": float(root_match.group(1)),
            "iterations": int(iter_match.group(1))
        }

    except Exception as e:
        print("EXCEPTION:", str(e))
        raise RuntimeError(f"Octave error: {str(e)}")


def run_interpolation_lineal(x: float, X: list[float], Y: list[float]) -> str:
    try:
        x_str = str(x)
        X_str = "[" + " ".join(map(str, X)) + "]"
        Y_str = "[" + " ".join(map(str, Y)) + "]"

        result = subprocess.run(
            ["octave", "--quiet", "IntLineal.m", x_str, X_str, Y_str],
            capture_output=True,
            text=True,
            cwd="octave"
        )

        if result.returncode != 0:
            print("STDERR:", result.stderr)
            raise RuntimeError(result.stderr)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def run_no_lineal_interpolation(x: float, X: list[float], Y: list[float]) -> float:
    try:
        x_str = str(x)
        X_str = "[" + " ".join(map(str, X)) + "]"
        Y_str = "[" + " ".join(map(str, Y)) + "]"

        result = subprocess.run(
            ["octave", "--quiet", "InterpNoLineal.m", x_str, X_str, Y_str],
            capture_output=True,
            text=True,
            cwd="octave"
        )

        if result.returncode != 0:
            print("STDERR:", result.stderr)
            raise RuntimeError(result.stderr)

        output_line = result.stdout.strip().splitlines()[-1]
        return float(output_line)
    except Exception as e:
        print("EXCEPTION:", str(e))
        raise RuntimeError(f"Octave error: {str(e)}")

def run_tir(x1: float, tol: float, inversion: float, flujos: list[float]) -> dict:
    args = [
        str(x1),
        str(tol),
        str(inversion),
        "[" + " ".join(map(str, flujos)) + "]"
    ]
    return run_script_with_args("N_R_TIR.m", args)

def run_portafolio(e1: float, e2: float, ep: float) -> dict:
    args = [str(e1), str(e2), str(ep)]
    result = subprocess.run(
        ["octave", "--quiet", "Portafolio.m"] + args,
        capture_output=True,
        text=True,
        cwd="octave"
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    w1 = re.search(r"W1=([\d\.\-eE]+)", result.stdout)
    w2 = re.search(r"W2=([\d\.\-eE]+)", result.stdout)
    if not w1 or not w2:
        raise ValueError("No se pudo obtener los pesos.")

    return {
        "w1": float(w1.group(1)),
        "w2": float(w2.group(1))
    }


def solve_edo(
        W0: float,
        f: str,
        t0: float,
        T: float,
        N: int,
        metodo: Literal["euler", "rk2", "rk4"]
) -> dict:
    """
    Resuelve dW/dt = f(t, W) con métodos numéricos en Python.
    """

    # Preparamos la función a partir de string (cuidado con seguridad si viene de usuario)
    # Aquí, como ejemplo, usamos eval con entorno controlado
    # Renombrar el parámetro para uso interno
    f_expr = f.strip()

    def f_func(t, W):
        return eval(f_expr, {"t": t, "W": W, "np": np})

    h = (T - t0) / N
    t = np.linspace(t0, T, N + 1).tolist()
    W = [W0]

    for i in range(N):
        Wi = W[i]
        ti = t[i]
        if metodo == "euler":
            Wip1 = Wi + h * f_func(ti, Wi)
        elif metodo == "rk2":
            k1 = f_func(ti, Wi)
            k2 = f_func(ti + h, Wi + h * k1)
            Wip1 = Wi + h / 2 * (k1 + k2)
        elif metodo == "rk4":
            k1 = f_func(ti, Wi)
            k2 = f_func(ti + h / 2, Wi + h / 2 * k1)
            k3 = f_func(ti + h / 2, Wi + h / 2 * k2)
            k4 = f_func(ti + h, Wi + h * k3)
            Wip1 = Wi + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        else:
            raise ValueError(f"Método no soportado: {metodo}")

        W.append(Wip1)
    return {"t": t, "W": W}


def calcular_opcion(data: dict) -> dict:
    try:
        args = [
            str(data["K"]),
            str(data["r"]),
            str(data["T"]),
            str(data["S0"]),
            str(data["sigma"])
        ]

        result = subprocess.run(
            ["octave", "--quiet", "valor_opcion.m"] + args,
            capture_output=True,
            text=True,
            cwd="octave"
        )

        if result.returncode != 0:
            print("STDERR:", result.stderr)
            raise RuntimeError(result.stderr)

        valor = float(result.stdout.strip().splitlines()[-1])
        return {"valor_opcion": valor}

    except Exception as e:
        print("EXCEPTION:", str(e))
        raise RuntimeError(f"Octave error: {str(e)}")
