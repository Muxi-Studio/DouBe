var clicktimes = 0;
$(document).ready(function(){
	hideimg();
	showimg1();
	showimg2();
	showimg3();
	showimg4();
	showlogin();
});

function hideimg(){
	$("#dou").hide();
	$("#bi").hide();
	$("#text_1").hide();
	$("#text_2").hide();
	$(".login").hide();
	$(".img-word").hide();
}

function showimg1(){
	$("#black").click(function(){
		$("#dou").show(2000);
	});	
}

function showimg2(){
	$("#dou").click(function(){
		$("#bi").show(2000);
	})
}

function showimg3(){
	$("#bi").click(function(){
		$("#text_1").show(2000);
	})
}

function showimg4(){
	$("#text_1").click(function(){
		$("#text_2").show(2000);
	})
}

function showlogin(){
	$("#text_2").click(function(){
		$("#dou").hide();
		$("#bi").hide();
		$("#text_1").hide();
		$("#text_2").hide();
		$(".login").hide();
		$(".img-word").show();
		$(".login").show();
	})
}