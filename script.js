const form = document.querySelector('#dataform') 
//Add a submit event listener to the form
form.addEventListener('submit', function(event){
    event.preventDefault();
    //Retrieve the value of the distribution
    var dist=form.querySelector('#distribution').value;
    //Confidence
    var conf=form.querySelector('#confidence').value;
    //uncertainty B
    var uncer=form.querySelector('#uncertainty').value;
})
