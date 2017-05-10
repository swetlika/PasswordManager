$.ajax({
	url: "http://127.0.0.1:5000/test",
	type: "GET",
	dataType: "json",
	success: function (data) {
		//alert(data[0]);
		var username = data["username"];
		var password = data["password"];
		console.log(username,password);
		//debugger;
		var pwd_field = $(':password');
		pwd_field.val(password);
		pwd_field.css( "background-color", "green" );

		var form = pwd_field.closest("form");
		form.css( "background-color", "blue" );

		var usr_field = form.find("input[type='email']");
		//if we can't find via email, use regex to find name similar to user
		if (!usr_field.length) {
			usr_field = form.find("input[name*='user'],input[name*='usr']");
		}
		/*
		var usr_field = pwd_field.prevAll(':input').first();
		if (!usr_field.length) {
			usr_field = pwd_field.parent().prev().find(':input');
		}
		*/
		
		usr_field.css( "background-color", "red" );
		usr_field.val(username);
		

		/*
		$('#email').val(username);
		$(':password').val(password);*/
	}
});