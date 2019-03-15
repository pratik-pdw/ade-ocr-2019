
var image = document.getElementById('image');

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            image.setAttribute('src',e.target.result)
        };
        reader.readAsDataURL(input.files[0]); 
    }
}


var cropFields = document.querySelector('#crop-fields');
var cropBoxData;
var cropper;
cropFields.addEventListener('click',(e)=>{
e.preventDefault();
console.log("hello");
cropper = new Cropper(image,{
    aspectRatio:NaN,
    crop(event){
        cropBoxData = cropper.getData(true);
        console.log(cropBoxData);
    },
    zoomOnWheel:false,
    cropBoxResizable:true,
    modal:true,
    initialAspectRatio:20,
    minCanvasWidth:200,
    background:true,
    viewMode:1
})
})


var dimensionArr = [];
var fieldname = document.querySelector('#field-name');
var addField = document.querySelector('#add-field')
addField.addEventListener('click',(e)=>{
    e.preventDefault();
    console.log("hello");
    console.log(cropBoxData);
    var fieldNameAndDimensions = {
        fieldName: fieldname.value,
        dimensions:{
            x: cropBoxData.x,
            y:cropBoxData.y,
            width:cropBoxData.width,
            height:cropBoxData.height
        }
    }
    dimensionArr.unshift(fieldNameAndDimensions)
    console.log(dimensionArr);
})



//Register the co-ordinates to the database...Send the co-ordinates to the server
var registerTemplate = document.querySelector('#register-template');
registerTemplate.addEventListener('click',(e)=>{
    e.preventDefault();
    fetch('http://127.0.0.1:5000',{
        method:"POST",
        mode: "cors", // no-cors, cors, *same-origin
        cache: "no-cache", // *def // include, same-origin, *omit
        headers: {
            "Content-Type": "application/json; charset=utf-8",
            // "Content-Type": "application/x-www-form-urlencoded",
        },
        body:JSON.stringify(dimensionArr)
    }).then((res)=>{return res.json()})
    .then((data)=>console.log(data));
})






var stopCrop = document.getElementById('stop-crop');
stopCrop.addEventListener('click',(e)=>{
e.preventDefault();
cropper.destroy()
})

