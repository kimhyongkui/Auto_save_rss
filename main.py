from fastapi import FastAPI
from routers import parsing, posting
import uvicorn

app = FastAPI(title="auto-save-rss")

app.include_router(parsing.router, prefix="/parsing")
app.include_router(posting.router, prefix="/posting")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        reload=True,
        port=8050
    )


@app.get("/")
def main():
    result = "RSS 피드"
    return result
