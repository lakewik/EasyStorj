//alert(window.location.search.substring(1));
 if (window.location.pathname == "/buckets_list") {
    $("#buckets_list_table_content").load("buckets_list_table");
 } else if (window.location.pathname.indexOf("/files_manager/") >= 0) {

        var splitted = window.location.pathname.split('files_manager/');

    $("#files_list_table_content").load("/files_table/" + splitted[1]);

 } else if (window.location.pathname.indexOf("/playlist_tracks_manager/") >= 0) {

        var splitted = window.location.pathname.split('playlist_tracks_manager/');

    $("#playlist_tracks_table_area").load("/playlist_tracks_table_data/" + splitted[1]);

 } else if (window.location.pathname.indexOf("/playlist_manager") >= 0) {

    $("#playlist_table_area").load("/playlist_table_data");

 } else if (window.location.pathname.indexOf("/node_details") >= 0) {

        var getSubstring =  window.location.search.substring(1);
        var splitted = getSubstring.split('nodeID=');

    $("#node_details_tab").load("/node_details_data/" + splitted[1]);
 } else if (window.location.pathname.indexOf("/file_mirrors/") >= 0) {

        var splitted = window.location.pathname.split('file_mirrors/');

    $("#available").load("/available_file_mirrors/" + splitted[1]);
    $("#established").load("/established_file_mirrors/" + splitted[1]);

 }

function measureNodeLatency(node_address, node_port) {
    var start = new Date().getTime();
    $('#junkOne').attr('src', 'http://'+node_address+':'+node_port).error(function () {
        var end = new Date().getTime();
        console.error("test");
        console.error (end-start);
           return end - start;
    });
}

setInterval(measureNodeLatency("192.168.1.189", "80"), 40);

measureNodeLatency("192.168.1.189", "80");

$( document ).ajaxComplete(function() {
  initNodePingChart();
});


     function httpGet_async(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.addEventListener("load", function(event) {

 //something_async(function(responseText) {
        callback(xmlHttp.responseText);
  //  });



}, false);
    xmlHttp.open( "GET", theUrl, true ); // false for synchronous request
    xmlHttp.send( null );
   // return xmlHttp.responseText;
}

function refresh_files_list(bucket_id="", mode="0") {

console.log(bucket_id);

//bucket_id = ""; # get bucket id from select list

var files_table_content = document.getElementById("files_list_table_content");

files_table_content.innerHTML= "<center> <img src='/static/assets/loader1.gif'> </center>";

var splitted = window.location.pathname.split('/');

if (mode != "0") {
 slash = "/";
 } else if (splitted[3] != "") {
slash = "/";
 mode = splitted[3];
 }
 else
 {
 slash = "";
 mode = "";

 }

$("#files_list_table_content").load("/files_table/" + bucket_id + slash + mode ); // add parameter 3 to enable public file features

}


function x (x="") {

}

function make_all_files_public(bucket_id, callback=x) {

httpGet_async("/make_all_files_public/"+bucket_id, function(x) {

callback();

});

}


function insert_all_files_to_playlist (bucket_id, playlist_id="", callback=x) {



httpGet_async("/insert_all_files_to_playlist/"+bucket_id+"/"+playlist_id, function(x) {

callback();

});

}


function make_file_public(bucket_id, file_id, file_name, file_size, file_upload_date, filestable_display_mode="") {

httpGet_async("/make_file_public?file_id="+file_id+"&bucket_id="+bucket_id+"&file_name="+file_name+"&file_size="+file_size+"&file_upload_date="+file_upload_date, function(x) {

refresh_files_list(bucket_id, filestable_display_mode);

});


}

    //live chart for ping

        //container.empty();
        // Determine how many data points to keep based on the placeholder's initial size;
        // this gives us a nice high-res plot while avoiding more than one point per pixel.
var container = $("#live-node-ping-chart");
container.empty();
        var maximum = container.outerWidth() / 10 || 100;

        //

        var data = [];

        function getRandomData() {

            if (data.length) {
                data = data.slice(1);
            }

            while (data.length < maximum) {
                var previous = data.length ? data[data.length - 1] : 50;
                var y = previous + Math.random() * 10 - 5;
                data.push(y < 0 ? 0 : y > 100 ? 100 : y);
            }

            // zip the generated y values with the x values

            var res = [];
            for (var i = 0; i < data.length; ++i) {
                res.push([i, data[i]])
            }

            return res;
        }



        function pingStorjNode() {

        var data = [];

            if (data.length) {
                data = data.slice(1);
            }

            while (data.length < maximum) {
                var previous = data.length ? data[data.length - 1] : 50;
                var y = previous + Math.random() * 10 - 5;
                data.push(y < 0 ? 0 : y > 100 ? 100 : y);
            }

            // zip the generated y values with the x values

            var res = [];
            for (var i = 0; i < data.length; ++i) {
                res.push([i, data[i]])
            }

            return res;
        }

       function initNodePingChart() {



        var node_address_div = document.getElementById('node_address');
        var node_address = node_address_div.innerHTML;

        series = [{
            data: pingStorjNode(),
            lines: {
                fill: true
            }
        }];


        var plot = $.plot(container, series, {
            grid: {

                color: "#999999",
                tickColor: "#D4D4D4",
                borderWidth:0,
                minBorderMargin: 20,
                labelMargin: 10,
                backgroundColor: {
                    colors: ["#ffffff", "#ffffff"]
                },
                margin: {
                    top: 8,
                    bottom: 20,
                    left: 20
                },
                markings: function(axes) {
                    var markings = [];
                    var xaxis = axes.xaxis;
                    for (var x = Math.floor(xaxis.min); x < xaxis.max; x += xaxis.tickSize * 2) {
                        markings.push({
                            xaxis: {
                                from: x,
                                to: x + xaxis.tickSize
                            },
                            color: "#fff"
                        });
                    }
                    return markings;
                }
            },
            colors: [config.chart.colorPrimary.toString()],
            xaxis: {
                tickFormatter: function() {
                    return "";
                }
            },
            yaxis: {
                min: 0,
                max: 110
            },
            legend: {
                show: true
            }
        });

         // Update the random dataset at 25FPS for a smoothly-animating chart

        setInterval(function pingNode() {
            series[0].data = pingStorjNode();
            plot.setData(series);
            plot.draw();
        }, 40);

        }


$('#morris-donut-chart').empty();

        Morris.Donut({
            element: 'morris-donut-chart',
            data: [{ label: "Download Sales", value: 12 },
                { label: "In-Store Sales", value: 30 },
                { label: "Mail-Order Sales", value: 20 } ],
            resize: true,
            colors: [
                tinycolor(config.chart.colorPrimary.toString()).lighten(10).toString(),
                tinycolor(config.chart.colorPrimary.toString()).darken(10).toString(),
                config.chart.colorPrimary.toString()
            ],
        });

