import subprocess

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

        print("STDOUT:", result.stdout)
        return result.stdout.strip()
    except Exception as e:
        print("EXCEPTION:", str(e))
        return f"Error: {str(e)}"
