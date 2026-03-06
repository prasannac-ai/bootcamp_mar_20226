from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel


app = FastAPI()
app_v1 = APIRouter(prefix="/api/v1",tags=["v1"])

class IrrigationData(BaseModel):
    irrigation_id: str
    irrigation_status: str
    irrigation_duration: int
    

@app_v1.post("/irrigation-data")
def create_irrigation_data(irrigation_data: IrrigationData):
    return {"message": "Irrigation data created successfully"}


app.include_router(app_v1)