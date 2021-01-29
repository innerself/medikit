function activateFirstKit () {
  const kitsPanel = $('#v-pills-tab');
  const medicinesListPanel = $('#v-pills-tabContent');

  kitsPanel.children(':first').addClass('active');
  medicinesListPanel.children(':first').addClass('active');
}

$(document).ready(function () {
  activateFirstKit();
});
