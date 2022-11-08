var modal = document.getElementById('id01');
  // When the user clicks anywhere outside of the modal, close it
  window.onclick = (event) => 
   event.target == modal ? 
      modal.style.display = "none" : undefined;

  window.onload = function () {
   var seconds = 00; 
   var tens = 00; 
   var appendTens = document.getElementById("tens")
   var appendSeconds = document.getElementById("seconds")
   var buttonStart = document.getElementById('button-start');
   var buttonStop = document.getElementById('button-stop');
   var buttonReset = document.getElementById('button-reset');
   var Interval ;
   var time = seconds + tens;

   function onclckfn() {
      clearInterval(Interval);
      Interval = setInterval(startTimer, 10);
   }

   buttonStop.onclick = () => 
      clearInterval(Interval);

   buttonReset.onclick = function() {
      clearInterval(Interval);
      tens = "00";
      seconds = "00";
      appendTens.innerHTML = tens;
      appendSeconds.innerHTML = seconds;
   }

   function startTimer () {
      tens++; 

      if(tens <= 9)
         appendTens.innerHTML = "0" + tens;

      if (tens > 9)
         appendTens.innerHTML = tens;

      if (tens > 99) {
         console.log("seconds");
         seconds++;
         appendSeconds.innerHTML = "0" + seconds;
         tens = 0;
         appendTens.innerHTML = "0" + 0;
      }

      if (seconds > 9)
         appendSeconds.innerHTML = seconds;
   }
}
