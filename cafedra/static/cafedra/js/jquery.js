jQuery('#datetimepicker3')
.datetimepicker({
  format:'d.m.Y H:i',
  inline:true,
  lang:'ru'
});

$(document).ready(function() {
  $(".show-hide-btn").click(function() {
    var id = $(this).data("id");
    $("#half-" + id).toggle();//hide/show..
    $("#full-" + id).toggle();
  })
});

$(".content-block-text").each(function() {
    let th = $(this);
    if (th.prop('scrollHeight') > th.height()) {
    let more = th.next(".show-all-container").find(".show-all");
        th.next(".show-all-container").show();
        th.addClass("content-block-text-shadow");
        more.click(function() {
            th.toggleClass("content-block-text-shadow content-block-text-open");
            more.text(more.text() == "Скрыть" ? "Показать полностью" : "Скрыть");
        });
    }
});
