//http://codepen.io/superpikar/pen/xCeiu
function drawCandidateIssue(candidate, issue) {
  $('#overview').css('display', 'none');
  $('#candidate-issue').css('display', 'block');

  if (candidate == 'trump' && issue == 'immigration') {
    d3.select('#candidate-zoom').text('Donald Trump');
    d3.select('#issue-zoom').text('Immigration');

    d3.json('json/trump-immigration.json', function(error, data) {
      data.elements.forEach(function(element, index, array) {
        $('.list-group').append('<li class="list-group-item">' + element + "</li>");
      });
    });

    d3.json('json/trump-immigration-sentiment.json', function(error, data) {
      var percentagefromRight = (1 + Math.abs(data.mean)) / 2 * 100;
      d3.select('#mean').style('right', percentagefromRight + '%');
    });

    var margin = { top: 0, right: 30, bottom: 30, left: 40 };
    width = 450 - margin.left - margin.right;
    height = 500 - margin.top - margin.bottom;

    var x = d3.scale.ordinal().rangeRoundBands([0, width], 0.1);
    var y = d3.scale.linear().range([height, 0]);

    var svg = d3.select('#vis2')
    .attr('width', width + (2*margin.left) + margin.right)
    .attr('height', height + margin.top + margin.bottom);

    var xAxis = d3.svg.axis()
    .scale(x)
    .orient('bottom');

    var yAxis = d3.svg.axis()
    .scale(y)
    .orient('left');

    d3.json('json/location-d3-2.json', function(error, data) {

      x.domain(data.map(function(d) { return d.bin; }));
      y.domain([0, d3.max(data, function(d) { return d.size; }) + 1]);

      var bar = svg.selectAll('g')
      .data(data)
      .enter()
      .append('g')
      .attr("transform", function(d, i){
        return "translate("+x(d.bin)+", 0)";
      });

      bar.append("rect")
      .attr("y", function(d) {
        return y(d.size);
      })
      .attr("x", function(d,i){
        return x.rangeBand()-(margin.left/4);
      })
      .attr("height", function(d) {
        return height - y(d.size);
      })
      .attr("width", x.rangeBand());

      bar.append("text")
      .attr("x", x.rangeBand()+margin.left )
      .attr("y", function(d) { return y(d.size) -10; })
      .attr("dy", ".75em")
      .text(function(d) { return d.size; });

      svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate("+margin.left+","+ height+")")
      .call(xAxis);

      svg.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate("+margin.left+",0)")
      .call(yAxis)
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Number of Tweets");
    });
    function type(d) {
      d.size = +d.size; // coerce to number
      return d;
    }
  }
}