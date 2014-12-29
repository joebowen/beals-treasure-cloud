importScripts("BigInt.js");
importScripts("bigInteger.js");
importScripts("js-inflate.js");
importScripts("js-unzip.js");
importScripts("lz-string.min.js");

function pow(base, exp)
{
  var answer = base;
  for (var i = 0; i < exp; i++)
  {
    answer = mult(answer, base);
  }
  return answer;
}

function hashCode(s){
  return s.split("").reduce(function(a,b){a=((a<<5)-a)+b.charCodeAt(0);return a&a},0);              
}

function gcd(x, y) {
  while (y != 0) {
    var z = x % y;
    x = y;
    y = z;
  }
  return x;
}

function gcd_big(x, y) {
  while (!BigInteger.isZero(y)) {
    var z = x.modPow(BigInteger(1), y);
    x = y;
    y = z;
  }
  return x;
}

function doRequest(url) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.open("GET", url, false);
    xmlhttp.timeout = 400000;
    xmlhttp.ontimeout = function () { postMessage({console: "Timeout error"}); }
    xmlhttp.send(null);
    return xmlhttp.responseText;
}

function httpGetandParse(exp, table, backwards)
{
  var date = new Date().getTime();

  response = doRequest("/data/" + exp + ".txt?date=" + date);

  data = LZString.decompressFromBase64(response);

  var lines = data.match(/^.*((\r\n|\n|\r)|$)/gm);

  var arrayLength = lines.length;
  for (var i = 0; i < arrayLength; i++)
  {
    result = lines[i].split(",");
    if (result[0] && result[1])
    {
      if (backwards)
      {
        table[result[1].replace(/\n/g,'')] = result[0].replace(/\n/g,'');
        //postMessage({console: "ztable[" + result[1].replace(/\n/g,'') + "] = " + table[result[1].replace(/\n/g,'')]});
      }
      else
      {
        table[result[0].replace(/\n/g,'')] = result[1].replace(/\n/g,'');
        //postMessage({console: "table[" + result[0].replace(/\n/g,'') + "] = " + table[result[0].replace(/\n/g,'')]});
      }
    }
  }

  //postMessage({console: "ztable[91] = " + table[91]});

  return table;
}

postMessage({resultval: -2, A: "-", B: "-", result: "-", progress: "-", progress_calc: "-"});

var data_loaded = 0;
var max_loaded = 2;
var ztable = {};

onmessage = function (oEvent) {
  var max_basei = 10000;
  var xi = oEvent.data.x;
  var yi = oEvent.data.y;

  var powx = httpGetandParse(xi, {}, false);
  var powy = httpGetandParse(yi, {}, false);

  if ((data_loaded == 0) || (max_loaded < Math.max(xi,yi)+10))
  {
    for ( var i = max_loaded + 1; i < Math.max(xi,yi)+10; i++)
    { 
      ztable = httpGetandParse(i, ztable, true);
      postMessage({resultval: -2, A: "-", B: "-", result: "Downloading Data...", progress: Math.round(((i-max_loaded) / (Math.max(xi,yi)+10-max_loaded))*100), progress_calc: "-"});
    }
    max_loaded = Math.max(xi,yi)+10;
    data_loaded = 1;
  }

  //postMessage({console: "ztable[91] = " + ztable[91]});

  var cnt = 0;
  postMessage({resultval: -2, A: "-", B: "-", result: "Calculating...", progress: "100", progress_calc: "0"});

  for (var A_cnt = 3; A_cnt <= max_basei; A_cnt++)
  {
    var A_pow = BigInteger(Number(powx[A_cnt]));
    for (var B_cnt = 3; B_cnt <= A_cnt; B_cnt++)
    {
      if(gcd(A_cnt, B_cnt)==1)
      {
        var Cz = BigInteger.add(A_pow,BigInteger(Number(powy[B_cnt])));
        if (ztable[Cz.toString()])
        {
          if ((gcd_big(BigInteger(A_cnt),Cz)==1)&&(gcd_big(BigInteger(B_cnt),Cz)==1))
          {
            postMessage({console: "ztable[Cz.toString()] = " + ztable[Cz.toString()]});
            postMessage({console: "Cz = " + Cz});
            postMessage({console: "B_cnt = " + BigInteger(B_cnt)});
            postMessage({console: "A_cnt = " + BigInteger(A_cnt)});
            postMessage({console: "gcd = " + gcd_big(BigInteger(A_cnt),Cz) + " " + gcd_big(BigInteger(B_cnt),Cz)});
            postMessage({id: oEvent.data.id ,resultval: 1, A: A_cnt, B: B_cnt, x: xi, y: yi, m: A_cnt, n:B_cnt, result: "Please contact us, you may have found a solution."});
            exit;
          }
        }
      }
    }
    if (A_cnt % (max_basei / 100) == 0)
    {
      cnt++;
    }
    if (A_cnt % 5 == 0)
    {
      postMessage({resultval: -2, A: A_cnt, B: "0 to " + max_basei, result: "Calculating...", progress: "100", progress_calc: cnt});
    }

  }

  postMessage({resultval: -1, A: max_basei, B: max_basei, progress: "100", progress_calc: "100", result: "-"});

};

