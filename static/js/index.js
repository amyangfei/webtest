$(document).ready(function() {
	$('#link_submit').click(function (evt) {
		evt.preventDefault();
        $.post("/index/register", $("#register-form").serialize(), function(res) {
        	var resJson = JSON.parse(res);
        	if(resJson.status == "success") {
        		window.location.href = window.location.origin + "/index/signup/success";
        	}
        	else {
        		var tip_id = new Array();
        		tip_id[0] = "tip_username";
        		tip_id[1] = "tip_email";
        		tip_id[2] = "tip_password1";
        		tip_id[3] = "tip_password2";
        		for(var i in resJson.wrong_tips) {
        			if(resJson.wrong_tips[i] != "") {
        				$(('#')+tip_id[i]).html(resJson.wrong_tips[i]);
        				$(('#')+tip_id[i]).attr('class','f-red');
        			}
        	    }
        	}
        });
    });
    //$('.link_submit').closest('form').append('<input style="position:absolute;left:-1000px" type="submit" value="" />');
	
	$("#id_email").blur(function(){
		$.getJSON('/index/gravatar', $("#id_email").serialize(), function(res){
			$('#tip_email').html(res.info);
			if(res.status == 'error') {
				$('#tip_email').attr('class','f-red');
			}
			else {
				$('#gravatar').attr('src', res.gravatar_url);
				$('#tip_email').attr('class','f-green');
			}
		})
	});
});