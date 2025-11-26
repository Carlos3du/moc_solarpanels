from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from datetime import datetime
import uvicorn
import os 


# Métricas:
# 	Irradiação
# 	Eficiência
# 	Área da placa
# 	Custo estimado
# 	Energia gerada

history = [] 
MAX_HISTORY_SIZE = 30
 
app = FastAPI()

# Permite que o Grafana acesse a API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def check():
    return {"status": "running"}

@app.get("/clear_history")
def clear_history():
    global history
    history = []
    return {"message": "cleared"}

@app.get("/metrics")
def get_metrics():
    # Simulação dos dados
    irradiacao = random.uniform(800, 1000)
    eficiencia = random.uniform(50, 100) / 100
    area = 1.60
    custo = 500
    potencia = random.uniform(600, 1000)
    time_now = datetime.now().isoformat()

    curr_metrics = {
        "irr_wm2": round(irradiacao, 2),
        "eff_pct": round(eficiencia, 2),
        "area_m2": area,
        "cost_brl": round(custo, 2),
        "power_w": round(potencia, 2),
        "time_now": time_now
    }
    
    # 4. Limpeza (Buffer Circular): Se passar do limite, remove o mais antigo
    if len(history) > MAX_HISTORY_SIZE:
        history.pop(0) # Remove o primeiro item da lista
    
    history.append(curr_metrics)
    return history


if __name__ == "__main__":
    # Pega a porta do Railway ou usa 8000 se for local
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)