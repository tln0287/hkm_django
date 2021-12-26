$(document).ready(function () {
    $.validator.addMethod("customemail",
            function (value, element) {
                return /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(value);
            },
            "Please enter ealid Email-Id"
            );

    $.validator.addMethod("lettersonly",
            function (value, element) {
                return this.optional(element) || /^[a-z\s]+$/i.test(value);
            },
            "Please enter valid name"
            );

    $.validator.addMethod("Mobileno",
            function (value, element) {
                return this.optional(element) || value.length === 10;
            },
            "Please enter valid phone number"
            );

    $('#form_donation').validate({
        debug: false,
        rules: {
            first_name: {
                required: true,
                minlength: 2,
                maxlength: 50,
                lettersonly: true,
            },
            email: {
                required: true,
                email: true,
                customemail: true,
            },
            phone: {
                required: true,
                digits: true,
                Mobileno: true,
            },
            other_donation_amount: {
                required: true,
                digits: true,
            }
        },
        submitHandler: function () {
            //$("#step2").css("display", "block");
            form.submit();
        }

    });
    $('#form_donation_seva').validate({
        debug: false,
        rules: {
            first_name: {
                required: true,
                minlength: 2,
                maxlength: 50,
                lettersonly: true,
            },
            email: {
                required: true,
                email: true,
                customemail: true,
            },
            phone: {
                required: true,
                digits: true,
                Mobileno: true,
            },
            donation_amount: {
                required: true,
                digits: true,
            },
            other_donation_amount: {
                required: true,
                digits: true,
            }
        },
        submitHandler: function () {
            //$("#step2").css("display", "block");
            form.submit();
        }

    });
    $('#form_donation_mandir_seva').validate({
        debug: false,
        rules: {
            first_name: {
                required: true,
                minlength: 2,
                maxlength: 50,
                lettersonly: true,
            },
            email: {
                required: true,
                email: true,
                customemail: true,
            },
            phone: {
                required: true,
                digits: true,
                Mobileno: true,
            },
            donation_amount: {
                required: true,
                digits: true,
            },
            other_donation_amount: {
                required: true,
                digits: true,
            }
        },
        submitHandler: function () {
            //$("#step2").css("display", "block");
            form.submit();
        }

    });
    $('#form_donation_kartik_seva').validate({
        debug: false,
        rules: {
            first_name: {
                required: true,
                minlength: 2,
                maxlength: 50,
                lettersonly: true,
            },
            email: {
                required: true,
                email: true,
                customemail: true,
            },
            phone: {
                required: true,
                digits: true,
                Mobileno: true,
            },
            donation_amount: {
                required: true,
                digits: true,
            },
            address: {
                required: true,
            },
            other_donation_amount: {
                required: true,
                digits: true,
            }
        },
        submitHandler: function () {
            //$("#step2").css("display", "block");
            form.submit();
        }

    });

});
function changeamt(val)
{
    var value = val.replace("\u20b9 ", '');
    var value = value.replace(",", '');
    //var myvar = value[1];
    $('#donation_amount_seva').val(value);
}

function mylinkfunction(val, val1, val2)
{
    window.location.href = "onlinedonations#sevas";

    if (val2 == 'other') {
        document.getElementById("donation_amount_seva").readOnly = false;
        $('#donation_amount_name').val('');
        $('#donation_amount_seva').val('');
        $('#donation_amount_name1').val(val);
    } else {
        $('#donation_amount_name1').val(val);
        $('#donation_amount_name').val(val1);
        $('#donation_amount_seva').val(val2);
    }
}
