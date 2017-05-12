var url = window.location.href;
console.log(url);

var master_pw;

var pwd_field = $(':password');
pwd_field.css( "background-color", "green" );
var form = pwd_field.closest("form");
form.css( "background-color", "blue" );
var usr_field = form.find("input[type='email'],input[name='email']");
//if we can't find via email, use regex to find name similar to user
if (!usr_field.length) {
	usr_field = form.find("input[name*='user'],input[name*='usr']");
}
usr_field.css( "background-color", "red" );

pwd_field.on('input',function() {
	master_pw = pwd_field.val();
	//console.log(master_pw);
	$.ajax({
		url: "http://127.0.0.1:5000/test",
		type: "GET",
		data: {master_pw: master_pw, url: url},
		dataType: "json",
		success: function (data) {
			//console.log("status",data["status"]);
			if (data["status"]=="success") {
				var username = data["username"];
				var password = data["password"];
				console.log(username,password);

				pwd_field.val(password);
				usr_field.val(username);	
			}

		}
	});
});
