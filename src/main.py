from fastapi import FastAPI

app = FastAPI()


@app.get("/weather")
def get_weather() -> dict[str, str]:
    return {"forecast": "晴れ"}
