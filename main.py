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
class like(BaseModel):
    user_id:str
    post_id:str
    


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

def like_data():
    with open('likes.json','r')as f:
        likedata=json.load(f)
        return likedata
def save_like(data):
    with open('likes.json','w') as f:
        json.dump(data,f)


@app.get('/')
def root():
    return {"message": "Blog Backend API is running"}
@app.get('/user')
def users():
    data=user_data()
    return data

@app.get("/user/{user_id}")
def get_user(user_id:str):
    data=user_data()
    if user_id not in data:
        raise HTTPException(status_code=404,detail='User not found')
    return {
        "id":user_id,
        **data[user_id]
    }


@app.get('/post')
def posts():
    data=post_data()
    return data

@app.get('/post/{post_id}')
def get_post(post_id:str):
    data=post_data()
    if post_id not in data:
        raise HTTPException(status_code=404,detail="post not found")
    return{
        "id":post_id,
        **data[post_id]
    }
@app.get('/comment')
def comments():
    data=comment_data()
    return data
@app.get('/comment/{comment_id}')
def get_comment(comment_id:str):
    data=comment_data()
    if comment_id not in data:
        raise HTTPException(status_code=404,detail="Comment not found") 
    return{
        "id":comment_id,
        **data[comment_id]
    }
@app.get('/likes')
def likes():
    data = like_data()
    return data
@app.get('/likes/{like_id}')
def get_like(like_id: str):
    data = like_data()

    if like_id not in data:
        raise HTTPException(status_code=404, detail="Like not found")

    return {
        "id": like_id,
        **data[like_id]
    }



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
    data[comment.id]=comment.model_dump(exclude=['id'])
    save_comment(data)

    return JSONResponse(status_code=201,content={"Message":'Comment send successfully'})

@app.post('/crlike')
def create_like(like:like):
    data=like_data()
    like_id=str(len(data)+1)
    data[like_id]=like.model_dump()
    save_like(data)
    return{
        "id":like_id,
        **data[like_id]
    }
@app.put('/user/{user_id}')
def update_user(user_id: str, user: User):
    data = user_data()

    if user_id not in data:
        raise HTTPException(status_code=404, detail="User not found")

    data[user_id] = user.model_dump(exclude=['id'])

    save_user(data)

    return {
        "id": user_id,
        **data[user_id]
    }

@app.delete('/user/{user_id}')
def delete_user(user_id: str):
    data = user_data()

    if user_id not in data:
        raise HTTPException(status_code=404, detail="User not found")

    del data[user_id]

    save_user(data)

    return {
        "Message": "User deleted successfully"
    }

@app.put('/post/{post_id}')
def update_post(post_id: str, post: post):
    data = post_data()

    if post_id not in data:
        raise HTTPException(status_code=404, detail="Post not found")

    data[post_id] = post.model_dump(exclude=['id'])

    save_post(data)

    return {
        "id": post_id,
        **data[post_id]
    }

@app.delete('/post/{post_id}')
def delete_post(post_id: str):
    data = post_data()

    if post_id not in data:
        raise HTTPException(status_code=404, detail="Post not found")

    del data[post_id]

    save_post(data)

    return {
        "Message": "Post deleted successfully"
    }

@app.put('/comments/{comment_id}')
def update_comment(comment_id: str, comment: comment):
    data = comment_data()

    if comment_id not in data:
        raise HTTPException(status_code=404, detail="Comment not found")

    data[comment_id] = comment.model_dump(exclude=['id'])

    save_comment(data)

    return {
        "id": comment_id,
        **data[comment_id]
    }

@app.delete('/comments/{comment_id}')
def delete_comment(comment_id: str):
    data = comment_data()

    if comment_id not in data:
        raise HTTPException(status_code=404, detail="Comment not found")

    del data[comment_id]

    save_comment(data)

    return {
        "Message": "Comment deleted successfully"
    }

@app.delete('/likes/{like_id}')
def delete_like(like_id: str):
    data = like_data()

    if like_id not in data:
        raise HTTPException(status_code=404, detail="Like not found")

    del data[like_id]

    save_like(data)

    return {
        "Message": "Like deleted successfully"
    }




