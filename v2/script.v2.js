
addEventListener("py:ready",function(){
    const submit=document.getElementById("submit");
    const input=document.querySelector("#input");
    const load_prompt=document.getElementById("banner");
    load_prompt.innerHTML="<code>py:ready</code> has triggered. You are ready to go!";
    load_prompt.setAttribute("class","bg-green-400 bg-opacity-40 rounded-md shadow-md font-extralight");
    submit.setAttribute("class","bg-transparent hover:scale-110 hover:bg-indigo-400 hover:bg-opacity-20 rounded-lg px-3 py-1.5 transition cursor-pointer");
    submit.removeAttribute("disabled");
    input.removeAttribute("disabled");
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

