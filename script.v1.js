
const p = document.getElementById("prompt");
const ph = document.querySelector("#phead");
const pc = document.querySelector("#pcontent");
const submit = document.querySelector("#submit");
const confidence= document.getElementById("confidence");
const distribution = document.getElementById("distribution");
const timebar=document.getElementById("time_bar");
document.getElementById("loadpy").addEventListener("mpy:ready", function () {
  document.querySelector("#load").remove();
  submit.setAttribute(
      "class",
      "cursor-pointer bg-transparent hover:bg-blue-500 hover:scale-110 bg-opacity-30  rounded-full  px-2  py-1  my-2   transition "
    );
  p.setAttribute(
    "class",
    "bg-green-500  bg-opacity-50 my-4  mx-3  p-2 rounded-sm  shadow-sm transition-all "
  );
  
  ph.innerText = "You are all set!";
  pc.innerHTML = "<code>py:ready</code> has triggered.You are ready to go!";
  
  const transition=setTimeout(function(){
    p.style.transition="all 3s";
    p.style.opacity=0;
},3000);
  const removePrompt=setTimeout(()=>{p.remove();},5000);
  }
);
//Out Transition



//Clear button

  document.querySelector("#clear").addEventListener("click", function () {
    document.querySelector("#input").value = "";
  });

//Processing transition


submit.addEventListener("click", function () {
  submit.setAttribute(
    "class",
    "cursor-progress bg-indigo-300 scale-x-110 rounded-full px-2 py-1 my-2 transition"
  );

  setTimeout(() => (submit.innerText = "Processing..."), 500);
  setTimeout(()=>{
    if (submit.innerText='Processing...'){
      submit.innerText = "Submit";
      submit.setAttribute('class',
        'cursor-pointer bg-transparent hover:bg-blue-500 hover:scale-110 bg-opacity-30  rounded-full  px-2  py-1  my-2   transition '
      );
    }
  },3000) ; 
});


//Handle error box
submit.addEventListener("click",()=>{
  
  let ErrorBoxHandler = function(){
    const errorboxcollection=document.getElementsByClassName("py-error");
    if (typeof(errorboxcollection)!=(null || undefined)){
      timebar.classList.add("w-full");
      const vanishTimeout=setTimeout(()=>{
        errorboxcollection[errorboxcollection.length-1].remove();
      },5100);
      const timebarTransition=setTimeout(()=>{
        timebar.style.transition="all linear 5s";
        timebar.classList.remove('w-full');
        timebar.classList.add('w-0');
        clearTimeout(timebarTransition);
      },0);
      setTimeout(()=>{timebar.removeAttribute("style");},5500);
    }
  };
  
  ErrorBoxHandler();

})