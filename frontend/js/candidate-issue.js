function drawCandidateIssue(candidate, issue) {
  $('#overview').css('display', 'none');
  $('#candidate-issue').css('display', 'block');
  // use svg vis2
  if (candidate == 'trump' && issue == 'immigration') {
    d3.select('#candidate-zoom').text('Donald Trump');
    d3.select('#issue-zoom').text('Immigration');
    d3.json('../json/trump-immigration.json', function(error, data) {
      data.elements.forEach(function(element, index, array) {
        $('.list-group').append('<li class="list-group-item">' + element + "</li>");
      });
    });
  }
}