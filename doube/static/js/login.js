$(document).ready(function(){
	hideimg();
	showimg();
})

function hideimg(){
	$("#black").hide();
	$("#dou").hide();
	$("#bi").hide();
	$("#text_1").hide();
	$("#text_2").hide();
	$(".login").hide();
	$(".img-word").hide();
}

function showimg(){
	var clicktimes = 0;
	$(document).click(
		function(){
			switch (clicktimes){
			case 0:
			$("#dou").show(1200);
			clicktimes++;
			break;
			case 1:
			$("#bi").show(1200);
			clicktimes++;
			break;
			case 2:
			$("#text_1").show(1200);
			clicktimes++;
			break;s
			case 3:
			$("#text_2").show(1200);
			clicktimes++;
			break;
			case 4:
			$("#dou").hide(1000);
			$("#bi").hide(1000);
			$("#text_1").hide(1000);
			$("#text_2").hide(1000);
			$(".login").show(1000);
			$(".img-word").show(1000);
			clicktimes++;
			break;
			}
		}
	)
}
