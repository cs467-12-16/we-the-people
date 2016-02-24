$(document).ready(function() {
  drawOverview('json/overview.json');
  $('#overall').on('click', function() {
    drawOverview('json/overview.json');
  });
  $('#facebook-overview').on('click', function() {
    drawOverview('json/facebook-data-filtered/totals-comments.json');
  });
  $('#twitter-overview').on('click', function() {
    drawOverview('json/twitter-data-filtered/totals-tweets.json');
  });
});