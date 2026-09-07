from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
app=FastAPI()
import json

class User(BaseModel):
    id:str
    name:str
    email:str
class post(BaseModel):
    id:str
    post:str
class comment(BaseModel):
   id:str
   comment:str
    


def user_data():
    with open('bloggers.json','r')as f:
        userdata=json.load(f)
        return userdata

def save_user(data):
    with open('bloggers.json','w') as f:
        json.dump(data,f)

def post_data():
    with open('posts.json','r')as f:
        postdata=json.load(f)
        return postdata
def save_post(data):
    with open('posts.json','w') as f:
        json.dump(data,f)
def comment_data():
    with open('comments.json','r')as f:
        commentdata=json.load(f)
        return commentdata
def save_comment(data):
    with open('comments.json','w') as f:
        json.dump(data,f)

@app.get('/')
def root():
    return {"message": "Blog Backend API is running"}
@app.get('/user')
def users():
    data=user_data()
    return data

@app.get('/post')
def posts():
    data=post_data()
    return data
@app.get('/comments')
def comments():
    data=comment_data()
    return data


@app.post('/cruser')
def create_user(user:User):
    data=user_data()
    if user.id in data:
        raise HTTPException(status_code=400,detail="User already exist")
    data[user.id]=user.model_dump(exclude=['id'])
    save_user(data)

    return JSONResponse(status_code=201,content={"Message":'User created successfully'})

@app.post('/crpost')
def create_post(post:post):
    data=post_data()
    if post.id in data:
        raise HTTPException(status_code=400,detail="User already exist")
    data[post.id]=post.model_dump(exclude=['id'])
    save_post(data)

    return JSONResponse(status_code=201,content={"Message":'Post created successfully'})

@app.post('/crcomment')
def create_comment(comment:comment):
    data=comment_data()
    if comment.id in data:
        raise HTTPException(status_code=400,detail="User already exist")
    data[comment.id]=post.model_dump(exclude=['id'])
    save_comment(data)

    return JSONResponse(status_code=201,content={"Message":'Comment send successfully'})


