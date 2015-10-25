
$(document).ready(function(){
	hideslide();
	slide();
	changeslidetext();
	changezan();
})

function hideslide(){
	$(".share-content").hide();
}

function slide(){
	$(".share").click(function(){
    	$(".share-content").slideToggle("slow");
  	}
  );
}

function changeslidetext(){
	var clicktimes = 0;
	$(".share").click(function(){
		switch (clicktimes){
			case 0:
			$("#slidetext").html("收起");
			clicktimes = 1;
			break;

			case 1:
			$("#slidetext").html("点击此处分享趣事");
			clicktimes = 0;
			break;
		}
	})
}
$(".listzan").attr("src","../static/img/zan-2.png")
function changezan(){
	var clicktimes = 0;
	$(".listzan").click(function(){
		switch (clicktimes){
			case 0:
			$(this).attr("src","../static/img/zan-2.png");
			clicktimes = 1;
			break;

			case 1:
			$(this).attr("src","../static/img/zan-1.png");
			clicktimes = 0;
			break;
		}
	})
}
