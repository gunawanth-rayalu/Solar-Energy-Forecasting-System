from fastapi import FastAPI, HTTPException, Query
import pandas as pd
import tensorflow as tf
import datetime
import uvicorn 

app = FastAPI()

# Loading model
model = tf.keras.models.load_model(r"D:\projects\solar power prediction\backend\models\lstm.weights.h5")



df = pd.read_csv("solar_energy_forecasting_smarttrak.csv") 
df['timestamp'] = pd.to_datetime(df['timestamp_edge']).dt.hour


@app.get("/api/predict")
async def predict(datetime_str: str = Query(...)): 
        selected_datetime = pd.to_datetime(datetime_str)
        
        closest_row = df.iloc[(df['timestamp'] - selected_datetime).abs().argsort()[:1]]


        if closest_row.empty:
            raise HTTPException(status_code=404, detail="No data found for the selected datetime.")

        input_data = pd.DataFrame([closest_row.drop(columns='timestamp').to_dict('records')[0]])
        prediction = model.predict(input_data)[0]


        return {"prediction": prediction, **closest_row.drop(columns='timestamp').to_dict('records')[0]}



@app.get("/api/historical_data")
async def get_historical_data():
    return df.to_dict('records')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)