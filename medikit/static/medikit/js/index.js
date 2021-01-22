function activateFirstKit () {
  const kitsPanel = $('#v-pills-tab');
  const drugsListPanel = $('#v-pills-tabContent');

  kitsPanel.children(':first').addClass('active');
  drugsListPanel.children(':first').addClass('active');
}

$(document).ready(function () {
  activateFirstKit();
});
