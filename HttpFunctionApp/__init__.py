import numpy as np
import azure.functions as func

def numIntegration(lower, upper, N):
    X = np.linspace(lower, upper, N, endpoint=False)
    dx = X[1] - X[0]
    integral_sum = np.sum(np.abs(np.sin(X)) * dx)
    return integral_sum

def main(req: func.HttpRequest) -> func.HttpResponse:
    interval_lower = 0.0
    interval_upper = np.pi
    N = [10, 100, 1000, 10000, 100000, 1000000]
    integrals = []
    string = ""

    for n in N:
        integral = numIntegration(interval_lower, interval_upper, n)
        integrals.append(integral)
        string += f"N = {n}: {integral} <br>"
        print(f"N = {n}: {integral}")

    return func.HttpResponse(f"<p>{string}</p>", mimetype="text/html")
