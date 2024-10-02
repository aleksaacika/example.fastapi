from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings




#models.Base.metadata.create_all(bind=engine) od kad radimo sa alembicom, ovaj dio koda nam ne treba


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)





'''@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()
    
    print(posts)
    return {"data": "succesful"}''' # ovo je testni sqlalchemy pa smo zakomentarisali



@app.get('/')
def root():
    return {"message": "hello wordl"}