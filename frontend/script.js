// let createUser=document.querySelector("#createUserBtn");
// let userid=document.querySelector("#userId");
// let username=document.querySelector("#userName");
// let usermail=document.querySelector("#userEmail");
// createUser.addEventListener("click",()=>{
//     const postUser = async (url = '', data = {}) => {
//     const response = await fetch(url, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//     });
//     return response.json();
// };

// postUser('http://127.0.0.1:8000/cruser',{
//     id:userid.value,
//     name:username.value,
//     email:usermail.value
// })
// .then(data=>{
//     console.log(data);
// })
// .catch(error => {
//         console.error('Error:', error);
//     });
// });


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