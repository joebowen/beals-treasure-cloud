var app = angular.module('bealsTreasure', ['ngCookies'])

app.controller('treasureFinder', ['$scope', 'getWork', function($scope, getWork) {
    $scope.finder = {
        A: '-',
        B: '-',
        x: '-',
        y: '-',
        status: '-',
        progress1: '-',
        progress2: '-',
        solved: '-',
        prize: '-'
    };
    
    $scope._gaq = _gaq || [];
    $scope._gaq.push(['_setAccount', 'UA-42067175-1']);
    
    $scope.calculating = false;
    
    $scope.uuid = '';
    
    $scope.username = '0';
    
    $scope.worker = new Worker("/static/js/worker2.js?date="+ new Date().getTime());
    
    $scope.start = function() {
        if ($scope.calculating) {
            return;
        }
        else {
            $scope.calculating = true;
            
            $scope._gaq.push(['_trackPageview', '/beal-track-start/']);
              
            var result = getWork($scope.username, function(result) {
                var x = result.x;
                var y = result.y;
                uuid = result.uuid;
                
                if (x == "") x = 3;
                if (y == "") y = 3;
                
                $scope.finder.x = x;
                $scope.finder.y = y;
                $scope.finder.A = "-";
                $scope.finder.B = "-";
                $scope.finder.status = "Loading...";
                
                $scope.worker.postMessage({id: uuid, x: x, y: y});
            });
        }
    };
    
    $scope.worker.onmessage = function (event) {
        $scope.finder.A = event.data.A;
        $scope.finder.B = event.data.B;
        $scope.finder.status = event.data.result;
        $scope.finder.progress1 = event.data.progress;
        $scope.finder.progress2 = event.data.progress_calc;
        $scope.finder.prize = event.data.prize;
        
        if (event.data.console)
        {
            console.log("console message: " + event.data.console);
        }
        
        if (event.data.resultval > -2)
        {
            $scope._gaq.push(['_trackPageview', '/beal-track/']);
            if (event.data.resultval == 1)
            {
                var x = event.data.x;
                var m = event.data.m;
                var y = event.data.y;
                var n = event.data.n;
                $scope.finder.prize = event.data.id;
                httpGet("/savework?&result=true&x=" + x + "&m=" + m + "&y=" + y + "&n=" + n);
                return;
            }  
    
            httpGet("/savework?result=false&memory=0&uuid=" + uuid + "&attemptid=" + attempt_id);
            $scope.finder.solved = $scope.finder.solved + 1;
            $scope.start();
        }
    };
}]);

function httpGet(theUrl)
{
  var xmlHttp = null;

  xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", theUrl, false );
  xmlHttp.send( );
  
  var result = xmlHttp.responseText;

  return result;
}

app.factory('getWork', function ($http, $cookies) {
    return function (username, callback) {
        $http({
            url: "/getwork?username="+ username + "&date=" + new Date().getTime(),
            method: "GET",
            headers: {'X-CSRFToken': $cookies['csrftoken']}
        }).success(function (response) {
            callback(response);
        });
    };
});


app.factory('httpPostFactory', function ($http, $cookies) {
    return function (file, data, callback) {
        $http({
            url: file,
            method: "POST",
            data: data,
            headers: {'Content-Type': undefined,
                      'X-CSRFToken': $cookies['csrftoken']}
        }).success(function (response) {
            callback(response);
        });
    };
});
