(function() {
  // TODO: add acknowledgement
  var clickHandler = function(btn) {
    var divBox = $(this).closest('div.highlight');
    var codeBox = divBox.find('code');
    var codeText = codeBox.text();

    // Create a temporary text area
    var textArea = $('<textarea>');
    textArea.text(codeText);
    divBox.append(textArea);
    textArea.focus();
    textArea.select();
    document.execCommand("copy");
    textArea.remove();
  };
  $(document).ready(function() {
    $('code').each(function() {
      var divBox = $(this).closest('div.highlight');
      var copyBtn = $(
        '<button class="btn copy-btn"><i class="fas fa-copy"></i></button>');
      divBox.append(copyBtn);
      copyBtn.on("click", clickHandler);
    });
  });
})();
