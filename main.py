from fastapi import FastAPI
from routers.get import parsing, access_token
from routers.post import rss_url, posting
from routers.delete import feed
import uvicorn

app = FastAPI(title="Tistory Rss 피드 자동 포스팅")

app.include_router(parsing.router, prefix="/parsing")
app.include_router(posting.router, prefix="/posting")
app.include_router(access_token.router, prefix="/access")
app.include_router(rss_url.router, prefix="/posting")
app.include_router(feed.router, prefix="/delete")

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
