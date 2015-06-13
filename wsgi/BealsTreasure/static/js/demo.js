var worker = 0;
var killvar = 0;
var calculating = 0;     
var blockcnt = 0;
var uuid = 0;
var attempt_id = 0;
var worker = new Worker("/static/js/worker2.js?date="+ new Date().getTime());
var form_sv = 0;
var email = 0;

var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-42067175-1']);

worker.onmessage = function (event) {
  document.getElementById("A").innerHTML = event.data.A;
  document.getElementById("B").innerHTML = event.data.B;
  document.getElementById("status").innerHTML = event.data.result;
  document.getElementById("progress1").innerHTML = event.data.progress;
  document.getElementById("progress2").innerHTML = event.data.progress_calc;
  document.getElementById("prize").innerHTML = event.data.prize;
  
  if (event.data.console)
  {
    console.log("console message: " + event.data.console);
  }

  if (event.data.resultval > -2)
  {
    _gaq.push(['_trackPageview', '/beal-track/']);
    if (event.data.resultval == 1)
    {
      var x = event.data.x;
      var m = event.data.m;
      var y = event.data.y;
      var n = event.data.n;
      document.getElementById("prize").innerHTML = event.data.id;
      httpGet("/savework?&result=true&x=" + x + "&m=" + m + "&y=" + y + "&n=" + n);
      return;
    }  
    httpGet("/savework?result=false&memory=0&uuid=" + uuid + "&attemptid=" + attempt_id);
    blockcnt = blockcnt + 1;
    start();
  }
}

function start()
{
  var date = new Date().getTime();
  var result = httpGet("/getwork?username="+ email + "&date=" + date).split(",");
  document.getElementById("solved").innerHTML = blockcnt;

  var x = result[0];
  var y = result[1];
  uuid = result[2];

  if (x == "") x = 1;
  if (y == "") y = 1;

  document.getElementById("x").innerHTML = x;
  document.getElementById("y").innerHTML = y;
  document.getElementById("A").innerHTML = "-";
  document.getElementById("B").innerHTML = "-";
  document.getElementById("status").innerHTML = "Loading...";

  worker.postMessage({id: uuid, x: x, y: y});
}

function autocalculateForm(form) 
{
  if (calculating == 1) return;

  calculating = 1;

  _gaq.push(['_trackPageview', '/beal-track-start/']);

  start();
}

function stopCalc(form) {
  calculating = 0;
  document.getElementById("A").innerHTML = "-";
  document.getElementById("B").innerHTML = "-";
  document.getElementById("status").innerHTML = "-";
  document.getElementById("progress1").innerHTML = "-";
  document.getElementById("progress2").innerHTML = "-";
}

function httpGet(theUrl)
{
  var xmlHttp = null;

  xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", theUrl, false );
  xmlHttp.send( );
  
  var result = xmlHttp.responseText;

  return result;
}
