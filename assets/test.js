
const field = document.getElementById("field");
const button = document.getElementById("send");
let parent = null;
button.addEventListener("click", () => {
    if(parent === null) {
        return;
        alert("msh");
    }

    const text = field.value;
    parent.postMessage(text);
    alert("msh");
});
const text = field.value;
//parent.postMessage(text);
if(parent == null){
    alert("null");
}

document.getElementById("field").innerHTML = "Hello JavaScript!";
    

