(function(){
  $(document).ready(function() {
    var baseHost = document.location.host;
    $('a[href]').each(function() {
      if (this.host == baseHost) {
        // Local link
        return;
      }
      $(this).attr('target', '_blank');
      $(this).addClass('external-link');
    });
  });
})();
