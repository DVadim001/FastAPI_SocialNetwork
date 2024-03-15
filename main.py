from fastapi import FastAPI, Depends
from database.jwtservice import get_current_user

from api.user_api.users import user_router
from api.post_api.posts import post_router
from api.comment_api.comments import comment_router

# from database import Base, engine

app = FastAPI(
    title="Social Network",
    docs_url='/')
# Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(post_router)
app.include_router(comment_router)


@app.get('/home')
async def home():
    return "This is home page"


@app.post('/register')
async def register():
    return 'Register page'


@app.post('/login')
async def login():
    return 'Login page'


@app.get("/secure-data")
async def secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": "This data is secure", "user": current_user}
