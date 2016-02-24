//https://bl.ocks.org/mbostock/7607535
function drawOverview(datafile) {
  d3.select('#vis').selectAll('*').remove();
  var margin = 0,
  diameter = 500;

  function color(depth, d) {
    if (depth === 0) {
      return d3.rgb(255, 255, 255);
    } else if (depth === 1) {
      return d3.rgb('#eeeeee');
    } else {
      if (d.name === 'sanders' || d.name === 'clinton') {
        return d3.rgb('#2e4272');
      } else if (d.name === 'unknown') {
        return d3.rgb('#659933');
      } else {
        return d3.rgb('#aa3939');
      }
    }
  }

  var pack = d3.layout.pack()
  .padding(2)
  .size([diameter - margin, diameter - margin])
  .value(function(d) { return d.size; });

  var svg = d3.select('#vis')
  .attr('width', diameter)
  .attr('height', diameter)
  .append('g')
  .attr('transform', 'translate(' + diameter / 2 + ',' + diameter / 2 + ')');

  d3.json(datafile, function(error, root) {
    if (error) throw error;

    var focus = root,
    nodes = pack.nodes(root),
    view;

    var circle = svg.selectAll('circle')
    .data(nodes)
    .enter().append('circle')
    .attr('class', function(d) { return d.parent ? d.children ? 'node' : 'node node--leaf' : 'node node--root'; })
    .style('fill', function(d) { return color(d.depth, d); })
    .on('click', function(d) { if (focus !== d) { zoom(d); } d3.event.stopPropagation(); });

    var text = svg.selectAll('text')
    .data(nodes)
    .enter().append('text')
    .attr('class', 'label')
    .style('fill-opacity', function(d) { return d.parent === root ? 1 : 0; })
    .style('display', function(d) { return d.parent === root ? 'inline' : 'none'; })
    .text(function(d) { return d.name; })
    .on('click', function(d) { console.log('clicked! ' + d.name); });

    var node = svg.selectAll('circle,text');

    d3.select('body')
    .on('click', function() { zoom(root); });

    zoomTo([root.x, root.y, root.r * 2 + margin]);

    function zoom(d) {
      var focus0 = focus; focus = d;

      var transition = d3.transition()
      .duration(d3.event.altKey ? 7500 : 750)
      .tween('zoom', function(d) {
        var i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 2 + margin]);
        return function(t) { zoomTo(i(t)); };
      });

      transition.selectAll('text')
      .filter(function(d) { return d.parent === focus || this.style.display === 'inline'; })
      .style('fill-opacity', function(d) { return d.parent === focus ? 1 : 0; })
      .each('start', function(d) { if (d.parent === focus && d.size > 0) this.style.display = 'inline'; })
      .each('end', function(d) { if (d.parent !== focus) this.style.display = 'none'; });
    }

    function zoomTo(v) {
      var k = diameter / v[2]; view = v;
      node.attr('transform', function(d) { return 'translate(' + (d.x - v[0]) * k + ',' + (d.y - v[1]) * k + ')'; });
      circle.attr('r', function(d) { return d.r * k; });
    }
  });

  d3.select(self.frameElement).style('height', diameter + 'px');
}