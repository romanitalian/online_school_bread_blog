

;(function() {
	$(function() {
		const $el = $('h1');
		$el.append("<div><button class='show-new-text'>Show new page text</button></div>");
		const ratesUrl = "http://127.0.0.1:8000/api/v1/rates2/";

		const $button = $el.find('.show-new-text');
		const $page_container = $('#page-text');
		const $imgEl = $('img[alt="bread"]');
		const catImgUrl = "https://http.cat/100";

		$button.click(function() {
		    var newImage = $('<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/Purple_circle_100%25.svg" alt="loader" width="30px">');
		   $(this).append(newImage);

			$.get(ratesUrl, function(data, status){
					$page_container.hide();
					$page_container.empty();
					$.each(data, function(index, value){
						$page_container.append(`<p>${index}# sale: ${value.sale}; buy: ${value.buy}; currency: ${value.currency}; get_source_display: ${value.get_source_display}</p>`);
					});
					$button.find('img').hide(3000);
					console.log($button.find('img'))
					// $page_container.show(5000);
					$page_container.fadeIn(5000);
			});
		})

		$im = $('img[alt="bread"]');
		$imgURL = "https://http.cat/100";

		$im.click(function(e) {
			e.preventDefault();
			$im
				.fadeOut(400, function() {
					$im.attr('src', $imgURL);
				})
				.fadeIn(5000);
					return false;
		});

	});
})()



