
// 暗色模式切换功能
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    
    if (!themeToggle || !sunIcon || !moonIcon) {
        console.error('暗色模式切换元素未找到');
        return;
    }
    
    // 检查本地存储的主题偏好
    const savedTheme = localStorage.theme;
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    // 设置初始主题
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.documentElement.classList.add('dark');
        sunIcon.classList.remove('hidden');
        moonIcon.classList.add('hidden');
    } else {
        document.documentElement.classList.remove('dark');
        sunIcon.classList.add('hidden');
        moonIcon.classList.remove('hidden');
    }
    
    // 切换主题事件
    themeToggle.addEventListener('click', () => {
        const isDark = document.documentElement.classList.contains('dark');
        
        if (isDark) {
            document.documentElement.classList.remove('dark');
            localStorage.theme = 'light';
            sunIcon.classList.add('hidden');
            moonIcon.classList.remove('hidden');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.theme = 'dark';
            sunIcon.classList.remove('hidden');
            moonIcon.classList.add('hidden');
        }
    });
}

// 页面加载完成后初始化所有功能
function initAll() {
    initResourceMonitor();
    initThemeToggle();
}

// 页面加载完成后初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
} else {
    initAll();
}

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
    "bg-green-500  bg-opacity-50 my-4  mx-3  p-2 rounded-sm  shadow-sm transition-all text-green-800 dark:text-green-100"
  );
  pc.setAttribute("class","mt-1 text-sm text-green-800 dark:text-green-100");
  ph.innerText = "You are all set!";
  pc.innerHTML = "<code class='text-green-900 dark:text-green-50 font-mono bg-green-200/30 dark:bg-green-800/30 px-1 rounded'>py:ready</code> has triggered.<br/>现在可以输入内容了。";
  
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


//Handle error box - 只在出现PyScript错误时执行
submit.addEventListener("click",()=>{
  
  let ErrorBoxHandler = function(){
    const errorboxcollection=document.getElementsByClassName("py-error");
    // 只有当确实存在错误框时才执行timebar动画（HTMLCollection.length > 0表示有匹配元素）
    if (errorboxcollection.length > 0){
      timebar.classList.add("w-screen");
      const vanishTimeout=setTimeout(()=>{
        errorboxcollection[errorboxcollection.length-1].remove();
      },5100);
      setTimeout(()=>{
        timebar.style.transition="all linear 5s";
        timebar.classList.remove('w-screen');
        timebar.classList.add('w-0');
      },100);
      setTimeout(()=>{timebar.removeAttribute("style");},5500);
    }
  };
  
  // 延迟执行，等待可能的错误框出现
  setTimeout(ErrorBoxHandler, 100);

})
//placeholder text handler
submit.addEventListener("click",()=>{
  const placeholdertext=document.getElementById("placeholder-text");
  if (placeholdertext){
    placeholdertext.remove();
  }
});
