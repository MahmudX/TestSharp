(function(){
    function clickHandler(message){
        alert(`Hi ${message}!`);
    }
    let myButton = document.getElementById('myButton');
    myButton.addEventListener('click', function(){clickHandler('Mahmud')});
})();