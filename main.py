from fastapi import FastAPI
from routers import parsing, posting, access_token
from routers.post import rss_url
import uvicorn

app = FastAPI(title="auto-save-rss")

app.include_router(parsing.router, prefix="/parsing")
app.include_router(posting.router, prefix="/posting")
app.include_router(access_token.router, prefix="/access")
app.include_router(rss_url.router, prefix="/posting")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        reload=True,
        port=8080
    )


@app.get("/")
def main():
    result = "RSS 피드"
    return result
