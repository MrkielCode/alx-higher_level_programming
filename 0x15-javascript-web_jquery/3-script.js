/* global $ */
/**
 * adding class 'red'
 */
$(document).ready(function () {
  $('DIV#red_header').on('click', function () {
    $('header').addClass('red');
  });
});
