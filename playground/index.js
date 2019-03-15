
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

cropFields.addEventListener('click',(e)=>{
e.preventDefault();
console.log("hello");
var cropper = new Cropper(image,{
    aspectRatio:NaN,
    crop(event){

    },
    zoomOnWheel:false,
    cropBoxResizable:true,
    modal:true,
    initialAspectRatio:20,
    minCanvasWidth:200,
    background:true
})
})
