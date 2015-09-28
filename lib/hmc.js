// hmctgmls: How many challenges to get the my lovely ship ?
// 
// hmctgmls is a short script to get the number of trials to win 
// a rare drop item.
// 
// Copyright (c) 2015 IMAI Toshiyuki
// 
// Author: 2015 IMAI Toshiyuki
// 
// This software is released under the MIT License.
// http://opensource.org/licenses/mit-license.php

function calculate() {
    var drop_rate = document.getElementById('DROP_RATE').value;

    if (isNaN(drop_rate) || drop_rate == '') {
	alert('must be a numerical number.');
	return;
    }

    if (drop_rate <= 0) {
	alert('must be higher than 0.');
	return;
    }

    var rate = drop_rate / 100;

    var chance = 100;
    var result = {'20p': 0,
		  '50p': 0,
		  '80p': 0,
		  '90p': 0,
		  '95p': 0,
		  '98p': 0,
		  '99p': 0,
		  '99_999p': 0};

    var count = 0;
    while (chance > 0.001) {
	count += 1;
	chance -= chance * rate;
	if (chance <= 80 && result['20p'] == 0) result['20p'] = count;
	if (chance <= 50 && result['50p'] == 0) result['50p'] = count;
	if (chance <= 20 && result['80p'] == 0) result['80p'] = count;
	if (chance <= 10 && result['90p'] == 0) result['90p'] = count;
	if (chance <= 5 && result['95p'] == 0) result['95p'] = count;
	if (chance <= 2 && result['98p'] == 0) result['98p'] = count;
	if (chance <= 1 && result['99p'] == 0) result['99p'] = count;
	if (chance <= 0.001 && result['99_999p'] == 0) result['99_999p'] = count;
    }

    for (key in result) {
	var result_field = document.getElementById(key.toUpperCase() + '_RESULT');
	var textNode = document.createTextNode(result[key]);
	result_field.replaceChild(textNode, result_field.childNodes.item(0));
    }


}
