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
    var target = $("#sam-ticket-types");
    var num = 0;
    add_button.click(function(){
        console.log("in");
        var name = '<input class="form-control" name="ticket-name-' + num + '"  type="text" value="' + $("#ticket-name").val() +'" >';
        var price = '<input class="form-control" name="ticket-price-' + num + '"  type="number" value="' + $("#price").val() +'" >';
        var count = '<input class="form-control" name="ticket-num-' + num + '"  type="number" value="' + $("#count").val() +'" >';
        var date = '<input class="form-control" name="ticket-date-' + num + '"  type="date" value="' + $("#ticket-date").val() +'" >';
        var outer_div = '<div class="form-inline">';
        var name_label = '<label for="ticket-name-' + num + '"> نام</label>';
        var price_label = '<label for="ticket-price-' + num + '"> قیمت</label>';
        var count_label = '<label for="ticket-num-'+num+ '"> تعداد</label>';
        var date_label = '<label for="ticket-date-' + num + '"> تاریخ</label>';
        num++;
        var elem = "<br>" + outer_div + name_label + name + price_label + price + count_label + count + date_label + date + "</div>";
        target.append(elem);
    });
}

