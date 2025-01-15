$(function () {
    function bind_captcha_btn_click() {
        $("#captcha-btn").click(function (event) {
            let $this = $(this);
            let email = $("input[name='email']").val();
            if (!email) {
                alert("Please input your email");
            } else {
                // disable the button
                $this.off('click');

                // ajax
                $.ajax({
                    url: '/auth/send_email_captcha/',
                    type: 'POST',
                    data: {email: email},  // Data to be sent in the request
                    success: function (response) {
                        alert("Please input your email");

                        console.log("Response from server:", response);
                    },
                    error: function (xhr, status, error) {

                        console.error("Request failed:", error);
                    }
                });


                // countdown
                let countdown_second = 5
                let timer = setInterval(function () {
                    if (countdown_second <= 0) {
                        $this.text("Get captcha");
                        //Don't count down
                        clearInterval(timer);

                        //enable the button
                        bind_captcha_btn_click();
                    } else {
                        $this.text(countdown_second + "s")
                        countdown_second--;
                    }
                }, 1000)
            }
        })
    }

    bind_captcha_btn_click();
});