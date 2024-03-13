frappe.listview_settings['Fees'] = {
    filters: [["status", "!=", "Cancelled"]],
  get_indicator: function(doc) {
    if(doc.status==="Submitted") {
      return [__("Unpaid"), "orange", "status,=,Unpaid"];
    } else {
      return [__(doc.status), {
        "Draft": "red",
        "Unpaid": "orange",
        "Partly-paid": "yellow",
        "Paid": "green",
        "Cancelled": "red"
      }[doc.status], "status,=," + doc.status];
    }
  }//*/
  };