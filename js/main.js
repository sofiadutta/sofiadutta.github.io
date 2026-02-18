;(function () {
	
	'use strict';



	var isMobile = {
		Android: function() {
			return navigator.userAgent.match(/Android/i);
		},
			BlackBerry: function() {
			return navigator.userAgent.match(/BlackBerry/i);
		},
			iOS: function() {
			return navigator.userAgent.match(/iPhone|iPad|iPod/i);
		},
			Opera: function() {
			return navigator.userAgent.match(/Opera Mini/i);
		},
			Windows: function() {
			return navigator.userAgent.match(/IEMobile/i);
		},
			any: function() {
			return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows());
		}
	};

	// Helper: Debounce function to limit the rate at which a function can fire.
	var debounce = function(func, wait, immediate) {
		var timeout;
		return function() {
			var context = this, args = arguments;
			var later = function() {
				timeout = null;
				if (!immediate) func.apply(context, args);
			};
			var callNow = immediate && !timeout;
			clearTimeout(timeout);
			timeout = setTimeout(later, wait);
			if (callNow) func.apply(context, args);
		};
	};

	var fullHeight = function() {

		if ( !isMobile.any() ) {
			$('.js-fullheight').css('height', $(window).height());
			// Optimization: Debounce resize event to reduce layout thrashing
			$(window).resize(debounce(function(){
				$('.js-fullheight').css('height', $(window).height());
			}, 250));
		}

	};


	var counter = function() {
		$('.js-counter').countTo({
			 formatter: function (value, options) {
	      return value.toFixed(options.decimals);
	    },
		});
	};


	var counterWayPoint = function() {
		if ($('#colorlib-counter').length > 0 ) {
			$('#colorlib-counter').waypoint( function( direction ) {
										
				if( direction === 'down' && !$(this.element).hasClass('animated') ) {
					setTimeout( counter , 400);					
					$(this.element).addClass('animated');
				}
			} , { offset: '90%' } );
		}
	};

	// Animations
	var contentWayPoint = function() {
		var i = 0;
		$('.animate-box').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('animated') ) {
				
				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .animate-box.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn animated');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft animated');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight animated');
							} else {
								el.addClass('fadeInUp animated');
							}

							el.removeClass('item-animate');
						},  k * 200, 'easeInOutExpo' );
					});
					
				}, 100);
				
			}

		} , { offset: '85%' } );
	};


	var burgerMenu = function() {

		$('.js-colorlib-nav-toggle').on('click', function(event){
			event.preventDefault();
			var $this = $(this);

			if ($('body').hasClass('offcanvas')) {
				$this.removeClass('active');
				$('body').removeClass('offcanvas');	
			} else {
				$this.addClass('active');
				$('body').addClass('offcanvas');	
			}
		});



	};

	// Click outside of offcanvass
	var mobileMenuOutsideClick = function() {

		$(document).click(function (e) {
	    var container = $("#colorlib-aside, .js-colorlib-nav-toggle");
	    if (!container.is(e.target) && container.has(e.target).length === 0) {

	    	if ( $('body').hasClass('offcanvas') ) {

    			$('body').removeClass('offcanvas');
    			$('.js-colorlib-nav-toggle').removeClass('active');
			
	    	}
	    	
	    }
		});

		$(window).scroll(function(){
			if ( $('body').hasClass('offcanvas') ) {

    			$('body').removeClass('offcanvas');
    			$('.js-colorlib-nav-toggle').removeClass('active');
			
	    	}
		});

	};

	var clickMenu = function() {

		$('#navbar a:not([class="external"])').click(function(event){
			var section = $(this).data('nav-section'),
				navbar = $('#navbar');

				if ( $('[data-section="' + section + '"]').length ) {
			    	$('html, body').animate({
			        	scrollTop: $('[data-section="' + section + '"]').offset().top - 55
			    	}, 500);
			   }

		    if ( navbar.is(':visible')) {
		    	navbar.removeClass('in');
		    	navbar.attr('aria-expanded', 'false');
		    	$('.js-colorlib-nav-toggle').removeClass('active');
		    }

		    event.preventDefault();
		    return false;
		});


	};

	// Reflect scrolling in navigation
	var navActive = function(section) {

		var $el = $('#navbar > ul');
		$el.find('li').removeClass('active');
		$el.each(function(){
			$(this).find('a[data-nav-section="'+section+'"]').closest('li').addClass('active');
		});

	};

	var navigationSection = function() {

		var $section = $('section[data-section]');
		
		$section.waypoint(function(direction) {
		  	
		  	if (direction === 'down') {
		    	navActive($(this.element).data('section'));
		  	}
		}, {
	  		offset: '150px'
		});

		$section.waypoint(function(direction) {
		  	if (direction === 'up') {
		    	navActive($(this.element).data('section'));
		  	}
		}, {
		  	offset: function() { return -$(this.element).height() + 155; }
		});

	};






	var sliderMain = function() {
		
	  	$('#colorlib-hero .flexslider').flexslider({
			animation: "fade",
			slideshowSpeed: 5000,
			directionNav: true,
			start: function(){
				setTimeout(function(){
					$('.slider-text').removeClass('animated fadeInUp');
					$('.flex-active-slide').find('.slider-text').addClass('animated fadeInUp');
				}, 500);
			},
			before: function(){
				setTimeout(function(){
					$('.slider-text').removeClass('animated fadeInUp');
					$('.flex-active-slide').find('.slider-text').addClass('animated fadeInUp');
				}, 500);
			}

	  	});

	};

	var stickyFunction = function() {

		var h = $('.image-content').outerHeight();

		if ($(window).width() <= 992 ) {
			$("#sticky_item").trigger("sticky_kit:detach");
		} else {
			$('.sticky-parent').removeClass('stick-detach');
			$("#sticky_item").trigger("sticky_kit:detach");
			$("#sticky_item").trigger("sticky_kit:unstick");
		}

		// Optimization: Debounce resize event
		$(window).resize(debounce(function(){
			var h = $('.image-content').outerHeight();
			$('.sticky-parent').css('height', h);


			if ($(window).width() <= 992 ) {
				$("#sticky_item").trigger("sticky_kit:detach");
			} else {
				$('.sticky-parent').removeClass('stick-detach');
				$("#sticky_item").trigger("sticky_kit:detach");
				$("#sticky_item").trigger("sticky_kit:unstick");

				if ($.fn.stick_in_parent) {
					$("#sticky_item").stick_in_parent();
				}
			}
			

			

		}, 250));

		$('.sticky-parent').css('height', h);

		if ($.fn.stick_in_parent) {
			$("#sticky_item").stick_in_parent();
		}

	};

	var lazyLoadBackgrounds = function() {
		var lazyBackgrounds = [].slice.call(document.querySelectorAll("[data-bg]"));

		if ("IntersectionObserver" in window) {
			var lazyBackgroundObserver = new IntersectionObserver(function(entries, observer) {
				entries.forEach(function(entry) {
					if (entry.isIntersecting) {
						entry.target.style.backgroundImage = "url('" + entry.target.getAttribute('data-bg') + "')";
						lazyBackgroundObserver.unobserve(entry.target);
					}
				});
			});

			lazyBackgrounds.forEach(function(lazyBackground) {
				lazyBackgroundObserver.observe(lazyBackground);
			});
		} else {
			// Fallback for older browsers
			lazyBackgrounds.forEach(function(lazyBackground) {
				lazyBackground.style.backgroundImage = "url('" + lazyBackground.getAttribute('data-bg') + "')";
			});
		}
	};

	var updateCopyrightYear = function() {
		if ($('#copyright-year').length > 0) {
			$('#copyright-year').text(new Date().getFullYear());
		}
	};

	var initCopyEmail = function() {
		function fallbackCopyTextToClipboard(text, onSuccess, onError) {
			var textArea = document.createElement("textarea");
			textArea.value = text;
			textArea.style.position = "fixed";  // Avoid scrolling to bottom
			document.body.appendChild(textArea);
			textArea.focus();
			textArea.select();

			try {
				var successful = document.execCommand('copy');
				if (successful) {
					onSuccess();
				} else {
					onError(new Error('Copy command failed'));
				}
			} catch (err) {
				onError(err);
			}
			document.body.removeChild(textArea);
		}

		function copyTextToClipboard(text, onSuccess, onError) {
			if (!navigator.clipboard) {
				fallbackCopyTextToClipboard(text, onSuccess, onError);
				return;
			}
			navigator.clipboard.writeText(text).then(function() {
				onSuccess();
			}, function(err) {
				// Fallback if async copy fails
				fallbackCopyTextToClipboard(text, onSuccess, onError);
			});
		}

		function showCopySuccess($btn) {
			var $icon = $btn.find('i');
			var $text = $btn.find('.btn-text');
			// Store original state if not already stored
			if (!$btn.data('original-icon')) {
				$btn.data('original-icon', $icon.attr('class'));
				$btn.data('original-text', $text.text());
			}

			// Clear any existing timeout to prevent race conditions
			if ($btn.data('timeout')) {
				clearTimeout($btn.data('timeout'));
			}

			$icon.removeClass().addClass('icon-tick');
			$text.text('Copied!');
			$btn.removeClass('btn-primary').addClass('btn-success');

			// Revert after 2 seconds
			var timeoutId = setTimeout(function() {
				$icon.removeClass().addClass($btn.data('original-icon'));
				$text.text($btn.data('original-text'));
				$btn.removeClass('btn-success').addClass('btn-primary');
				$btn.removeData('timeout');
			}, 2000);

			$btn.data('timeout', timeoutId);
		}

		$('.js-email-copy-btn').on('click', function(e) {
			e.preventDefault();
			var $btn = $(this);
			var user = $btn.data('user');
			var domain = $btn.data('domain');
			var email = user + '@' + domain;

			copyTextToClipboard(email, function() {
				showCopySuccess($btn);
			}, function(err) {
				console.error('Could not copy text: ', err);
			});
		});
	};

	// Document on load.
	$(function(){
		fullHeight();
		counter();
		counterWayPoint();
		contentWayPoint();
		burgerMenu();

		clickMenu();
		// navActive();
		navigationSection();
		// windowScroll();


		mobileMenuOutsideClick();
		sliderMain();
		stickyFunction();
		lazyLoadBackgrounds();
		updateCopyrightYear();
		initCopyEmail();
	});


}());