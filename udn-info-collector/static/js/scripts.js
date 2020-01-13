function simpleSearch() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("userInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("participantTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}

function newInput(inputType) {
    console.log("Adding a " + inputType);
    var $new_element = $("." + inputType + "").children().last().clone();
    var arrVars = $new_element.prop("id").split("_");
    var lastVar = arrVars.pop();
    lastVar++;
    // Set new id and append to html
    $new_element.prop("id", "div_id_" + inputType + "_" + lastVar);
    $new_element.appendTo($("." + inputType + ""))
    // Label for input
    $label = $($new_element.contents()[1]);
    $label.text(lastVar);
    $label.attr('for', "id_" + inputType + "_" + lastVar);
    // Text area for input
    $text_area = $("." + inputType + "_textarea").last();
    $text_area.attr("name", inputType + "_" + lastVar).attr("id", "id_" + inputType + "_" + lastVar).val("");
}