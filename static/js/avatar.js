$(document).ready(function() {
	$('#upavatar').live('change' ,function(){  
        var ie = !-[1,];
        if(ie) {  
        	alert("not support");
        } else {
        	PreviewImage();
        }
        $('#upload-submit').removeAttr("style");
	});
	var angle = 0
	$('#rotateRight').click(function(){
		angle += 90;
		$('#uploadPreview').rotate(angle);
		$('#uploadPreview-140').rotate(angle);
		$('#uploadPreview-50').rotate(angle);
		$('#hideAngle').val(angle);
	});
	$('#rotateLeft').click(function(){
		angle -= 90;
		$('#uploadPreview').rotate(angle);
		$('#uploadPreview-140').rotate(angle);
		$('#uploadPreview-50').rotate(angle);
		$('#hideAngle').val(angle);
	});
});

function PreviewImage() {
    oFReader = new FileReader();
    oFReader.readAsDataURL(document.getElementById("upavatar").files[0]);

    oFReader.onload = function (oFREvent) {
        document.getElementById("uploadPreview").src = oFREvent.target.result;
        document.getElementById("uploadPreview-140").src = oFREvent.target.result;
        document.getElementById("uploadPreview-50").src = oFREvent.target.result;
    };
};