    
// var dimensionArr = [];

// const image = document.getElementById('image');

// const cropper = new Cropper(image,{
//     aspectRatio:NaN,
//     crop(event){
//         // console.log(`X: ${event.detail.x}`);
//         // console.log(`Y: ${event.detail.y}`);
//         // console.log(`Width: ${event.detail.width}`);
//         // console.log(`Height: ${event.detail.height}`);
//         // console.log(`Rotate: ${event.detail.rotate}`);
//         // console.log(`Scale X: ${event.detail.scaleX}`);
//         // console.log(`Scale Y: ${event.detail.scaleX}`);
//         // dimensions.x = event.detail.x;
//         // dimensions.y = event.detail.y;
//         // dimensions.width = event.detail.width;
//         // dimensions.height = event.detail.height;
//         // console.log(`Dimension X : ${dimensions.x}`);
//         // console.log(`Dimension Y : ${dimensions.y}`);
//         // console.log(`Dimension Width : ${dimensions.width}`);
//         // console.log(`Dimension Height : ${dimensions.height}`);
 
//     },
//     zoomOnWheel:false,
//     cropBoxResizable:true,
//     modal:true,
//     initialAspectRatio:20,
//     minCanvasWidth:200,
//     background:true
// })


// var fieldname = document.querySelector('#field-name');
// var submit = document.querySelector('#submit')

// submit.addEventListener('click',(e)=>{
//     e.preventDefault()
//     var cropBoxData = cropper.getData()
//     console.log(cropBoxData);
    
//     var fieldNameAndDimensions = {
//         fieldName: fieldname.value,
//         dimensions:{
//             x: cropBoxData.x,
//             y:cropBoxData.y,
//             width:cropBoxData.width,
//             height:cropBoxData.height
//         }
//     }

//     dimensionArr.unshift(fieldNameAndDimensions)
//     console.log(dimensionArr);
// })

// var registerTemplate = document.querySelector('#register-template');
// registerTemplate.addEventListener('click',(e)=>{
//     e.preventDefault();
//     fetch('http://127.0.0.1:5000',{
//         method:"POST",
//         mode: "cors", // no-cors, cors, *same-origin
//         cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
//         credentials: "same-origin", // include, same-origin, *omit
//         headers: {
//             "Content-Type": "application/json; charset=utf-8",
//             // "Content-Type": "application/x-www-form-urlencoded",
//         },
//         body:JSON.stringify(dimensionArr)
//     }).then((res)=>{return res.json()})
//     .then((data)=>console.log(data));
// })




