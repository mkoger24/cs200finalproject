
//     function drawOnImage(image = null) {
//     const canvasElement = document.getElementById("canvas");
    
//     const context = canvasElement.getContext("2d");
    
//     // if an image is present,
//     // the image passed as a parameter is drawn in the canvas
//     if (image) {
//         const imageWidth = image.width;
//         const imageHeight = image.height;
//         // rescaling the canvas element
//         canvasElement.width = imageWidth;
//         canvasElement.height = imageHeight;
//         context.drawImage(image, 0, 0, imageWidth, imageHeight);
//     }
    
//     let isDrawing;
//     canvasElement.onmousedown = (e) => {
//         isDrawing = true;
//         context.beginPath();
//         context.lineWidth = 10;
//         context.strokeStyle = "black";
//         context.lineJoin = "round";
//         context.lineCap = "round";
//         context.moveTo(e.clientX, e.clientY);
//     };
    
//     canvasElement.onmousemove = (e) => {
//         if (isDrawing) {      
//         context.lineTo(e.clientX, e.clientY);
//         context.stroke();      
//         }
//     };
    
//     canvasElement.onmouseup = function () {
//         isDrawing = false;
//         context.closePath();
//     };
//     }

//     const fileInput = document.querySelector("#upload");

// // enabling drawing on the blank canvas
// drawOnImage();
//     fileInput.addEventListener("change", async (e) => {
//     const [file] = fileInput.files;

//     // displaying the uploaded image
//     const image = document.createElement("img");
//     image.src = await fileToDataUri(file);

//     // enabling the brush after the image
//     // has been uploaded
//     image.addEventListener("load", () => {
//         drawOnImage(image);
//     });
  
//   return false;
// });

// function fileToDataUri(field) {
//   return new Promise((resolve) => {
//     const reader = new FileReader();
//     reader.addEventListener("load", () => {
//       resolve(reader.result);
//     });
//     reader.readAsDataURL(field);
//   });
// }

// const sizeElement = document.querySelector("#sizeRange");
// let size = sizeElement.value;
// sizeElement.oninput = (e) => {
//   size = e.target.value;
// };

// const colorElement = document.getElementsByName("colorRadio");
//     let color;
//     colorElement.forEach((c) => {
//     if (c.checked) color = c.value;
//     });
//     colorElement.forEach((c) => {
//     c.onclick = () => {
//         color = c.value;
//     };
// });

// function drawOnImage(image = null) {
//   const canvasElement = document.getElementById("canvas");
  
//   const context = canvasElement.getContext("2d");
  
//   // if an image is present,
//   // the image passed as parameter is drawn in the canvas
//   if (image) {
//     const imageWidth = image.width;
//     const imageHeight = image.height;
    
//     // rescaling the canvas element
//     canvasElement.width = imageWidth;
//     canvasElement.height = imageHeight;
    
//     context.drawImage(image, 0, 0, imageWidth, imageHeight);
//   }
  
//   const clearElement = document.getElementById("clear");
//   clearElement.onclick = () => {
//     context.clearRect(0, 0, canvasElement.width, canvasElement.height);
//   };
  
//   let isDrawing;
//   canvasElement.onmousedown = (e) => {
//     isDrawing = true;
//     context.beginPath();
//     context.lineWidth = size;
//     context.strokeStyle = color;
//     context.lineJoin = "round";
//     context.lineCap = "round";
//     context.moveTo(e.clientX, e.clientY);
//   };
  
//   canvasElement.onmousemove = (e) => {
//     if (isDrawing) {      
//       context.lineTo(e.clientX, e.clientY);
//       context.stroke();
//     }
//   };
  
//   canvasElement.onmouseup = function () {
//     isDrawing = false;
//     context.closePath();
//   };
// }


const MAIN_MOUSE_BUTTON = 0;

function prepareContext(canvasElement) {
  let dpr = window.devicePixelRatio || 1;
  let rect = canvasElement.getBoundingClientRect();
  canvasElement.width = rect.width * dpr;
  canvasElement.height = rect.height * dpr;
 
  let context = canvasElement.getContext("2d");
  context.scale(dpr, dpr);
  
  return context;
}

function setLineProperties(context) {
  context.lineWidth = 4;
  context.lineJoin = "round";
  context.lineCap = "round";
  return context;
}

let clearButton = document.getElementById("clearButton");
let theCanvas = document.getElementById("theCanvas");
let theContext = prepareContext(theCanvas);
let shouldDraw = false;

theCanvas.addEventListener("mousedown", start);
theCanvas.addEventListener("mouseup", end);
theCanvas.addEventListener("mousemove", move, false);

clearButton.addEventListener("click", event => {
  clearCanvas(theContext);
});

 
function clearCanvas(context) {
  context.clearRect(0, 0, context.canvas.width, context.canvas.height);  
}

function start(event) {
  if (event.button === MAIN_MOUSE_BUTTON) {
    shouldDraw = true;
    setLineProperties(theContext);
    theContext.beginPath();
    let elementRect = event.target.getBoundingClientRect();
    theContext.moveTo(event.clientX - elementRect.left, event.clientY - elementRect.top);
  }
}

function end(event) {
  if (event.button === MAIN_MOUSE_BUTTON) {
    shouldDraw = false;
  }
}

function move(event) {
  if (shouldDraw) {
    let elementRect = event.target.getBoundingClientRect();
    theContext.lineTo(event.clientX - elementRect.left, event.clientY - elementRect.top);
    theContext.stroke();
  }
}
