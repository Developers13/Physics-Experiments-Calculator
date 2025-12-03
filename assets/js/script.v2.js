
addEventListener("py:ready",function(){
    const submit=document.getElementById("submit");
    const input=document.querySelector("#input");
    const load_prompt=document.getElementById("banner");
    const acquirebtn=document.getElementById("order");
    const varsfield=document.getElementById("defvars");
    load_prompt.innerHTML="<code>py:ready</code> has triggered. You are ready to go!";
    load_prompt.setAttribute("class","bg-green-400 bg-opacity-40 rounded-md shadow-md font-extralight p-3");
    submit.classList.remove("cursor-not-allowed");
    submit.classList.add("cursor-pointer");
    acquirebtn.classList.remove("cursor-not-allowed");
    acquirebtn.classList.add("cursor-pointer");
    acquirebtn.removeAttribute("disabled");
    input.removeAttribute("disabled");
    varsfield.removeAttribute("disabled");
    //out animation
    const transition=setTimeout(function(){
        load_prompt.style.transition="all 3s";
        load_prompt.style.opacity=0;
    },2000);
    
    
    const remove_prompt_timeout=setTimeout(function(){load_prompt.remove();},3000);
    clearTimeout(remove_prompt_timeout);
    
    
    
});
function reset() {
    document.querySelector("#input").value="";
    document.getElementById('data').value="";
    document.getElementById('uncertainty').value="";
    document.getElementById('data').setAttribute("disabled",true);
    document.getElementById('uncertainty').setAttribute("disabled",true);
}

