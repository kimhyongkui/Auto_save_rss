from fastapi import FastAPI

import uvicorn

app = FastAPI(title="item-analysis")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        reload=True,
        port=8050
    )


@app.get("/")
def main():
    result = "hello"
    return result
