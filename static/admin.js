$(function(){
	//登录模态框
	$('button.smodal').click(function(){
		$('#signin').modal('show');
	});
	
	//评论模态框
	$('button.vmodal').click(function(){
		$('#submit-views').modal('show');
	});
	
	like_i = 0;
	unlike_i = 0;
	
	//推荐	
	$('button#like').click(function(){
		val = parseInt($('span.count1').html());
		if(val < 0){
			val = 0;
			$('span.count1').html(val);
		}
		if(like_i % 2 == 0 && unlike_i % 2 == 0){
			val = parseInt($('span.count1').html()) + 1;
			$('span.count1').html(val);
			$(this).css({'background':'#1caaea','color':'white'});
		}else if(val == 0){
			$(this).css({'background':'white','color':'#1caaea'});
		}
		else{
			val = parseInt($('span.count1').html()) - 1;
			$('span.count1').html(val);
			$(this).css({'background':'white','color':'#1caaea'});
		}
		like_i++;			
	});
	
	//不推荐	
	$('button#unlike').click(function(){
		val = parseInt($('span.count2').html());
		if(val < 0){
			val = 0;
			$('span.count2').html(val);
		}
		if(unlike_i % 2 == 0 && like_i % 2 == 0){
			val +=  1;
			$('span.count2').html(val);
			$(this).css({'background':'#1caaea','color':'white'});
		}else if(val == 0){			
			$(this).css({'background':'white','color':'#1caaea'});
		}else{
			val = parseInt($('span.count2').html()) - 1;
			$('span.count2').html(val);
			$(this).css({'background':'white','color':'#1caaea'});
		}
		unlike_i++;
	});	
	
	//星级评分
	$('#star-rate1 span.star1').click(function(){
		for(var i = 0; i < 5; i++){
			$('span.star1').eq(i).addClass('blue');
		}
		num = $(this).attr("rel");
		for(var i = num; i < 5; i++){
			$('span.star1').eq(i).removeClass('blue');
		}
		$('span.rate1').html(num*20 + '%');
		$('.rate1-num').attr('value',num*2);
	});
	
	$('#star-rate2 span.star2').click(function(){
		for(var i = 0; i < 5; i++){
			$('span.star2').eq(i).addClass('blue');
		}
		num = $(this).attr("rel");
		for(var i = num; i < 5; i++){
			$('span.star2').eq(i).removeClass('blue');
		}
		$('span.rate2').html(num*20 + '%');
		$('.rate2-num').attr('value',num*2);
	});
	
	$('#star-rate3 span.star3').click(function(){
		for(var i = 0; i < 5; i++){
			$('span.star3').eq(i).addClass('blue');
		}
		num = $(this).attr("rel");
		for(var i = num; i < 5; i++){
			$('span.star3').eq(i).removeClass('blue');
		}
		$('span.rate3').html(num*20 + '%');
		$('.rate3-num').attr('value',num*2);
	});

	//追加评论
	$('#view-div button').click(function(){				
		val = parseInt($(this).attr("num"));
		
		if(val % 2 == 0){
			str = $('#message-text').text();
			$('#message-text').text(str + " " + $(this).text());
		}
		else{
			$('#message-text').text(str);
		}
		val++;
		$(this).attr('num',val);
	});
	
	//上传头像
	function getObjectURL(file) {
		var url = null ;
		if (window.createObjectURL!=undefined) { // basic
			url = window.createObjectURL(file) ;
		} else if (window.URL!=undefined) { // mozilla(firefox)
			url = window.URL.createObjectURL(file) ;
		} else if (window.webkitURL!=undefined) { // webkit or chrome
			url = window.webkitURL.createObjectURL(file) ;
		}
		return url ;
	}

	$('#thumbnail').change(function() {
		$(this).parent().prev().prev().attr('src',getObjectURL($(this)[0].files[0]));
		$(this).parent().prev().prev().attr('class','avatar-lg circle');
	});
	
	//用户名下拉列表
	$('.user').mouseenter(function(){
		$(this).find('i').addClass('glyphicon-chevron-up').removeClass('glyphicon-chevron-down');
		$(this).find('.usertop').css({'background':'#FFF'});
		$(this).find('.mydropdown').show();
	});
	$('.user').mouseleave(function(){
		$(this).find('i').addClass('glyphicon-chevron-down').removeClass('glyphicon-chevron-up');
		$(this).find('.usertop').css({'background':'#f8f8f8'});
		$(this).find('.mydropdown').hide();
	});	
	

});
