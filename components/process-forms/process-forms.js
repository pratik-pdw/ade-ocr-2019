const uploadImage = document.getElementById('uploadImage');
var getdata = document.getElementById('getdata');
var loader = document.getElementById('loader');
// var form = document.getElementById('form');
var formData = "";
let finalData = undefined;


uploadImage.addEventListener('submit', (e)=>{
    e.preventDefault();
    const fd = new FormData();
    fd.append('file', e.target.elements.file.files[0]);
    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        mode: 'no-cors',
        body: fd
    }).then((response)=>{
        return response.text();
    }).then((data)=>{
        console.log(data);
        console.log("done");
    })
    .catch((err)=>{
        console.log(err);
    })
}, false);


getdata.addEventListener('click',(e)=>{
    e.preventDefault();
    e.target.style.display = 'none';
    loader.style.display = 'block';
    fetch('http://127.0.0.1:5000',{
        method:"GET",
        mode:"cors",
        cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
        credentials: "same-origin", // include, same-origin, *omit
        headers: {
            "Content-Type": "application/json; charset=utf-8",
            // "Content-Type": "application/x-www-form-urlencoded",
        }
    })
    .then((res)=>{return res.json()})
    .then((data)=>{
        console.log(data);
       
        setTimeout(()=>{
        loader.style.display = 'none';
        showForm(data);   
        },2000)
         
    });
});

document.getElementById("storeData").addEventListener('click', (e)=>{
    e.preventDefault();
    fetch('http://127.0.0.1:5000/save',{
        method:"POST",
        mode: "cors", // no-cors, cors, *same-origin
        cache: "no-cache", // *def // include, same-origin, *omit
        headers: {
            "Content-Type": "application/json; charset=utf-8",
            // "Content-Type": "application/x-www-form-urlencoded",
        },
        body:JSON.stringify(finalData)
    }).then((res)=>{return res.json()})
    .then((data)=>console.log(data));
})





function showForm(data){
    console.log("called");
    getdata.style.display = "none";
    let keys = Object.keys(data);
    finalData = data;
    let imgSrc = "../../flask-api/";
    
    let form = document.getElementById("form");
    form.innerHTML += `<h2>Form Data</h2>`
    for(i=0; i<keys.length; i++){
        // imgSrc = imgSrc + keys[i] + ".jpg"; 
            form.innerHTML += `
                <div class="form-group">
                    <label for="${keys[i]}">${keys[i]}</label>
                    <img style="width: 500px;height: 35px;" src="${imgSrc+keys[i]+".jpg"}"><br><br>
                    <input type="text" name="${keys[i]}" value="${data[keys[i]]}" class="form-control" />
                   
                </div>
            `
    }
    form.innerHTML += `
        <button id="storeData" class="btn btn-success">Store Data</button>
    `    
}






