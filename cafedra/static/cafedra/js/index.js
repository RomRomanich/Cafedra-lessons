$('#login-button').click(function(){
  $('#login-button').fadeOut("slow",function(){
    $("#container").fadeIn();
    TweenMax.from("#container", .4, { scale: 0, ease:Sine.easeInOut});
    TweenMax.to("#container", .4, { scale: 1, ease:Sine.easeInOut});
  });
});

$(".close-btn").click(function(){
  TweenMax.from("#container", .4, { scale: 1, ease:Sine.easeInOut});
  TweenMax.to("#container", .4, { left:"0px", scale: 0, ease:Sine.easeInOut});
  $("#container, #forgotten-container").fadeOut(800, function(){
    $("#login-button").fadeIn(800);
  });
});

/* Forgotten Password */
$('#forgotten').click(function(){
  $("#container").fadeOut(function(){
    $("#forgotten-container").fadeIn();
  });
});


// preloder ======================

window.addEventListener('load',function(){
  document.querySelector('body').classList.add("loaded")
});


// Akardion ===========================


var accordion = document.getElementById('accordion');
		accordion.addEventListener('click', change);
		function change(event) {
			var targ = event.target;
			if (targ.tagName !== 'H3') return;
			if (targ.classList.contains('select')) {
				hideAll();
			} else {
				hideAll();
				targ.classList.add('select');
				showText(targ.nextElementSibling);
			}
		}
		function hideAll() {
			var h3El = accordion.querySelectorAll('h3');
			var divEl = accordion.querySelectorAll('div');
			for (var i = 0; i < h3El.length; i++) {
				h3El[i].classList.remove('select');
			}
			for (var i = 0; i < divEl.length; i++) {
				divEl[i].style.height = '0';
			}
		}
		function showText(textEl) {
			textEl.style.height = textEl.scrollHeight + 'px';
		}

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
      more.click(function(){
        th.toggleClass("content-block-text-shadow content-block-text-open");
        more.text(more.text() == "Yopish" ? "Ochish" : "Yopish");
      });
  }
});

	
