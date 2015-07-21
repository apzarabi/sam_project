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

    add_button.click(function(){
        console.log("in");
        var e ="<li>"+  "تعداد=" + $("#count").val() + " قیمت=" + $("#price").val() + "</li>";
        target.append(e);
    });
}
