from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel, Field, EmailStr

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=['bcrypt'], deprecated = "auto")

#SECRETS that has not to shared on the github and has to stored in .env file only
SECRET_KEY = "thissecretkeyisnottobeshared"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 30


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#dependancey
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()        

# ------------------Schemas for data validation---------------------

class Post(BaseModel):
    caption: str = ""
    desc: str = Field(min_length=5, max_length=500)
    likes : int = Field(gt=-1)
    author_id: int 
    
class UserCreate(BaseModel):
    username : str = Field(min_length=3, max_length=50)  
    email : EmailStr
    hashedpassword: str = Field(min_length=6, max_length=255)
    

# -------------Functions for authentication---------------------------------------------------------------------------------------------------
def get_user_by_username(username: str, db:Session):
    return db.query(models.User).filter(models.User.username  == username).first()

def create_user(user: UserCreate, db:Session):
    hashedpassword = pwd_context.hash(user.hashedpassword)  # Plain password from the frontend
    try:
        user_model = db.query(models.User).filter(models.User.username == user.username or models.User.email == user.email).first()
        
        if user_model is not None: return JSONResponse(status_code=400, content={"msg":f"User with similar username or mail already exists"})
        
        user_model = models.User(username = user.username, email=user.email, hashedpassword=hashedpassword)
        db.add(user_model)
        db.commit()
        return JSONResponse(status_code=200, content={"msg":f"User created successfully with username: {user.username}"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    
def authenticate_user(username: str, password: str, db:Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user : return False
    if not pwd_context.verify(password, user.hashedpassword) : return False
    return user

def create_access_token(data: dict, expire_delta: timedelta | None = None):
    to_encode = data.copy()
    if expire_delta : expire = datetime.now(timezone.utc) + expire_delta
    else: expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str = Depends(oauth2_scheme)):
    try:
        print(token)
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None: raise HTTPException(status_code=403, detail=f"Token is invalid or expired")
        return payload
    except Exception as e:
        raise HTTPException(status_code=403, detail=f"{e}")

# ------------------------------------------------------------------------------------------------------------------------

# "/userdata" : if user is: return its data else: raise HTTPException stating that you are not authorized with status code 401

# ----------------------------------------------Auth Routes---------------------------------
@app.post("/register")
def register_user(user: UserCreate,  db:Session = Depends(get_db)):
    user_model = get_user_by_username(user.username, db)
    if user_model is not None: return JSONResponse(status_code=400, content={"msg":f"User with similar username or mail already exists"})
    return create_user(user, db)

@app.post("/token")
def login_for_accesstoken(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(username=form_data.username, password = form_data.password, db=db)
    if not user: raise HTTPException(status_code=401, detail=f"Incorrect password or username")
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
    access_token = create_access_token(data={"sub": user.username}, expire_delta= access_token_expire)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/verifytoken/{token}")
def verify_user_token(token: str):
    verify_token(token)
    return {"message": "Token is Valid"}
        
#-------------------------Routes--------------------------------------  
@app.post("/createuser")  # Older one just for practice
def createuser(user: UserCreate, db:Session = Depends(get_db)):
    try:
        user_model = db.query(models.User).filter(models.User.username == user.username or models.User.email == user.email).first()
        
        if user_model is not None: return JSONResponse(status_code=400, content={"msg":f"User with similar username or mail already exists"})
        
        user_model = models.User(username = user.username, email=user.email, password=user.hashedpassword)
        db.add(user_model)
        db.commit()
        return JSONResponse(status_code=200, content={"msg":f"User created successfully with username: {user.username}"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    
    

@app.get(path="/readuser")  # Read
def readuser(db:Session = Depends(get_db)):
    return db.query(models.User).all()



@app.delete("/deleteuser/{id}")  # Older one just for practice
def deleteuser(id:int, request: Request, db:Session = Depends(get_db)):
    user_model = db.query(models.User).filter(models.User.id == id).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail=f"User with id: {id} is not found")
    
    db.query(models.User).filter(models.User.id == id).delete()
    db.commit()
    return JSONResponse(status_code=200, content={"msg":f"User with {id} deleted successfully"})



@app.get(path="/")  # Get all posts
def read(db:Session = Depends(get_db)):
    return db.query(models.Posts).all()

@app.post("/create") # Older one just for practice
async def createpost(post:Post, db:Session = Depends(get_db)):
    try:
        post_model = models.Posts()
        post_model.caption = post.caption
        post_model.desc = post.desc
        post_model.likes = post.likes
        post_model.author_id = post.author_id
        db.add(post_model)
        db.commit()
        return JSONResponse(status_code=200, content={"msg":"Post created successfully"})
    except:
        raise HTTPException(status_code=400, detail=f"Something went wrong")

@app.put("/update/{id}")  # Older one just for practice
def updatepost(id:int, post:Post, db: Session = Depends(get_db)):
    post_model = db.query(models.Posts).filter(models.Posts.id == id).first()
    if post_model is None:
        raise HTTPException(status_code=404, detail=f"Post with id: {id} is not found")
    post_model.author_id = post.author_id
    post_model.caption = post.caption
    post_model.desc = post.desc
    post_model.likes = post.likes
    
    db.add(post_model)
    db.commit()
    
    return post

@app.delete("/delete/{id}")  # Older one just for practice
def deletepost(id:int, db:Session = Depends(get_db)):
    post_model = db.query(models.Posts).filter(models.Posts.id == id).first()
    if post_model is None:
        raise HTTPException(status_code=404, detail=f"Post with id: {id} is not found")
    
    db.query(models.Posts).filter(models.Posts.id == id).delete()
    db.commit()
    return JSONResponse(status_code=200, content={"msg":f"Post with {id} deleted successfully"})

if __name__ == "__main__":
    uvicorn.run(app=app)
    