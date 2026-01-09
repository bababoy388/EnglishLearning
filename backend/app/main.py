from fastapi import FastAPI
from api.routers import courses,users
import uvicorn


app = FastAPI()

app.include_router(courses.router, prefix="/api/courses", tags=['courses'] )
app.include_router(users.router, prefix="/api/users", tags=['users'])


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3333)
