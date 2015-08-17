/////////// FOR REPORT /////////

var select_report = $("div.form-inline>.form-group>#report-type");
if(select_report !== undefined ){
    var category = $("div.form-inline>.form-group>#category");
    var time_from = $("div.form-inline>.form-group>#from");
    var time_to = $("div.form-inline>.form-group>#to");

    select_report.change(function(){
        if(select_report.val() === "گزارش فروش زیردسته"){
            category.removeAttr('disabled');
            time_from.attr('disabled', true);
            time_to.attr('disabled', true);
        }
        else if(select_report.val() === "گزارش فروش بر حسب زمان"){
            category.attr('disabled', true);
            time_from.removeAttr('disabled');
            time_to.removeAttr('disabled');
        }
        else if(select_report.val() === "گزارش فروش کل"){
            category.attr('disabled', true);
            time_from.attr('disabled', true);
            time_to.attr('disabled', true);
        }
        else if(select_report.val() === "گزارش فروش دسته"){
            category.attr('disabled', true);
            time_from.attr('disabled', true);
            time_to.attr('disabled', true);
        }
        console.log(select_report.val());
        console.log(category);
        console.log(time_from);
        console.log(time_to);
    });
}



////////////// FOR CREATING EVENT //////////////

var add_button = $("#add-ticket-type");
if(add_button !== undefined){
    var target2 = $("#sam-ticket-types");
    var num = 0;
    add_button.click(function(){
        console.log("in");
        var start_div = "<div class='col-md-3'>";
        var end_div = "</div>";
        var name = '<input class="form-control" name="ticket-name-' + num + '"  type="text" value="" >';
        var price = '<input class="form-control" name="ticket-price-' + num + '"  type="number" value="" >';
        var count = '<input class="form-control" name="ticket-num-' + num + '"  type="number" value="" >';
        var date = '<input class="form-control" name="ticket-date-' + num + '"  type="date" value="" >';
        var outer_div = '<div class="form-inline">';
        var name_label = '<label for="ticket-name-' + num + '"> نام</label>';
        var price_label = '<label for="ticket-price-' + num + '"> قیمت</label>';
        var count_label = '<label for="ticket-num-'+num+ '"> تعداد</label>';
        var date_label = '<label for="ticket-date-' + num + '"> تاریخ</label>';
        num++;
        var elem = "<div class='row'><br>" + outer_div + start_div + name_label +name + end_div + start_div + price_label + price + end_div + start_div+ count_label + count + end_div + start_div + date_label + date + end_div + "</div></div>";
        target2.append(elem);
    });
}

var map =
[
"&\#1632;","&\#1633;","&\#1634;","&\#1635;","&\#1636;",
"&\#1637;","&\#1638;","&\#1639;","&\#1640;","&\#1641;"
];

function getArabicNumbers(str)
{
    var newStr = "";

    str = String(str);

    for(i=0; i<str.length; i++)
    {
        newStr += map[parseInt(str.charAt(i))];
    }

    return newStr;
}

var add_button2 = $("#add-picture");
if(add_button2 !== undefined){
    var target = $("#sam-pictures");
    var num2 = 0;
    add_button2.click(function(){
        console.log("in2");
        var start_div = "<div class='col-md-3'>";
        var end_div = "</div>";
        var pic = '<input class="form-control" name="picture-' + num2 + '"  type="file" value="" size = "50">';
        var outer_div = '<div class="form-inline">';
        var pic_label = '<label for="picture-' + num2 + '">' + 'تصویر' + getArabicNumbers((num2+1).toString()) + '</label>';
        num2++;
        var elem = "<div class='row'><br>" + outer_div + start_div + pic_label + pic + end_div + "</div></div>";
        target.append(elem);
    });
}

