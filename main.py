from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

class DeviceInfo(BaseModel):
    kullanici_id: str
    marka: str
    model: str
    versiyon: str

@app.get("/")
def anasayfa():
    return {"mesaj": "API çalışıyor"}

@app.post("/cihaz-bilgisi")
def cihaz_bilgisi_gonder(payload: DeviceInfo):
    print(f"[{datetime.now()}] Gelen cihaz bilgisi:", payload.dict())
    return {"durum": "başarılı", "mesaj": "Cihaz bilgisi alındı"}
