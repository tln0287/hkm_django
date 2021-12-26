function getsevanameamt(name, amt, dontnurl){
	//alert(name);
	if(amt == 'otheramt'){
		$('#donation_title').val(name);
		$('#donation_url').val(dontnurl);
		$('.otheramount').show();
		$('#donation_amount').hide();
		$('#sevaname').html('Other Seva');
		$('#donationotheramount').show();
		$('#donation_amount').hide();
	}else{
            var value = amt.replace(",", '');
            var value = value.replace(",", '');
		$('#sevaname').html(name);
		$('#donation_amount').val(value);
		$('#donation_title').val(name);
		$('#donation_url').val(dontnurl);
		$('#donation_amount').show();
		$('#donationotheramount').hide();
	}
}
function getsevanameamt1(name, i, dontnurl){
    var str = "seva_amt" + i;
    var seva_amt = document.querySelector('input[name='+str+']:checked').value;
    var value = seva_amt.replace(",", '');
	if(seva_amt == ''){
		$('#donation_title_mandir_seva').val(name);
		$('#donation_url_mandir_seva').val(dontnurl);
		$('.otheramount_mandir_seva').show();
		$('#donation_amount_mandir_seva').hide();
		$('#sevaname_mandir_seva').html('Other Seva');
		$('#donationotheramount_mandir_seva').show();
		$('#donation_amount_mandir_seva').hide();
	}else{
		$('#sevaname_mandir_seva').html(name);
		$('#donation_amount_mandir_seva').val(value);
		$('#donation_title_mandir_seva').val(name);
		$('#donation_url_mandir_seva').val(dontnurl);
		$('#donation_amount_mandir_seva').show();
		$('#donationotheramount_mandir_seva').hide();
	}
}
function getsevanameamt_seva(name, amt, dontnurl){
	//alert(amt);
	if(amt == 'otheramt'){
		$('#donation_title_seva').val(name);
		$('#donation_url_seva').val(dontnurl);
		$('.otheramount_seva').show();
		$('#donation_amount_seva').hide();
		$('#sevaname_seva').html('Other Seva');
		$('#donationotheramount_seva').show();
		$('#donation_amount').hide();
	}else{
		$('#sevaname_seva').html(name);
		//$('#donation_amount_seva').val(amt);
		$('#donation_title_seva').val(name);
		$('#donation_url_seva').val(dontnurl);
		$('#donation_amount_seva').show();
		$('#donationotheramount_seva').hide();
	}
}
;