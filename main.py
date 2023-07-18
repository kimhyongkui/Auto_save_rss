from fastapi import FastAPI
from routers.get import parsing, access_token, category
from routers.post import posting
from routers import rss_url

import uvicorn

app = FastAPI(title="Tistory Rss 피드 자동 포스팅")

app.include_router(parsing.router, prefix="/parsing")
app.include_router(category.router, prefix="/category")
app.include_router(posting.router, prefix="/posting")
app.include_router(access_token.router, prefix="/access")
app.include_router(rss_url.router, prefix="/posting")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        reload=True,
        port=8060
    )


@app.get("/")
def main():
    result = "RSS 피드"
    return result
