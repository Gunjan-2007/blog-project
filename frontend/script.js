let createUser = document.querySelector("#createUserBtn");
let userid = document.querySelector("#userId");
let username = document.querySelector("#userName");
let usermail = document.querySelector("#userEmail");

createUser.addEventListener("click", () => {
    const postUser = async (url = '', data = {}) => {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        console.log("Status:",response.status);
        return response.json();
    };

    postUser('http://127.0.0.1:8000/cruser', {
        id: userid.value,
        name: username.value,
        email: usermail.value
    })
    .then(data => {
        console.log(data);
    })
     .catch(error => {
        console.error('Error:', error);
    });
});


let createPost=document.querySelector("#createPostBtn");
let postid=document.querySelector("#postId");
let postcontent=document.querySelector("#postContent");
createPost.addEventListener("click", ()=>{
    const post=async (url,data={})=>{
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return response.json();
    };
     post('http://127.0.0.1:8000/crpost',{
        id:postid.value,
        post:postcontent.value
     })
     .then(data=>{
        console.log(data);
     })
     .catch(error=>{
        console.log('error:',error)
     });
});

console.log("script Loaded!");

let showpost=document.querySelector("#getPostsBtn");
let postdisplay=document.querySelector("#posts p");
showpost.addEventListener("click",()=>{
    console.log("Button Clicked");
    const post_list=async (url)=>{
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        return response.json();
    };
    post_list('http://127.0.0.1:8000/post')
    .then(data=>{
        
        for(let id in data){
            postdisplay.innerText+=data[id].post +"\n";
        }
        
    })
    .catch(error=>{
        console.log("error:",error)
    });

    }

    
);