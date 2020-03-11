anychart.onDocumentReady(function() {
 
    // set the data
    var data = {
        header: ["Name", "Total Homeless"],
        rows: [
          ["1995", 36951],
          ["2000", 47587],
          ["2005", 51174],
          ["2010", 56922],
          ["2015", 62718]
    ]};

    // create the chart
    var chart = anychart.column();

    // add the data
    chart.data(data);

    // set the chart title
    chart.title("Total made homeless between 1995-2015");

    // draw
    chart.container("bar");
    chart.draw();
  });