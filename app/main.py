from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from datetime import datetime
import uvicorn


# Métricas:
# 	Irradiação
# 	Eficiência
# 	Área da placa
# 	Custo estimado
# 	Energia gerada
 
app = FastAPI()

# Permite que o Grafana acesse a API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/metrics")
def get_metrics():
    # Simulação dos dados
    irradiacao = random.uniform(0, 1000)
    eficiencia = 0.25
    area = 1.60
    custo = 500
    potencia = random.uniform(0, 1000)
    time_now = datetime.now().isoformat()

    return {
        "irr_wm2": round(irradiacao, 2),
        "eff_pct": round(eficiencia, 2),
        "area_m2": area,
        "cost_brl": round(custo, 2),
        "power_w": round(potencia, 2),
        "time_now": time_now
    }

# if __name__ == "__main__":
#     # Roda na porta 8000
#     uvicorn.run(app, host="0.0.0.0", port=8000)