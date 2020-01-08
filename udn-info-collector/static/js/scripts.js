function getFullAssayModel(pk) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {   // XMLHttpRequest.DONE == 4
            if (xmlhttp.status == 200) {
                visualize(JSON.parse(xmlhttp.responseText))
            } else if (xmlhttp.status == 400) {
                alert('There was an error 400');
            } else {
                alert('something else other than 200 was returned');
            }
        }
    };

    xmlhttp.open("GET", "/model/" + pk, true);
    xmlhttp.send();
}


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
    var lastInput = $("input[id*=" + inputType + "]").slice(-1)[0];
    console.log($("input[id*=" + inputType + "]").slice(-1)[0]);
    console.log($(lastInput).id);
    if ($(lastInput).val() === '') {
        console.log("Empty" + $(lastInput).val())
    } else {
        console.log("not empty!" + $(lastInput).val())
    }
}


// $('.environmental-list-new').on('input', function () {
//     var $this = $(this);
//     var $clone = $this.clone();
//     console.log($($clone))
//     var name = $clone.attr("name");
//     console.log($("input[name*='envexposure']"))
//     var lastEnvExposure = $("input[name^='envexposure']").slice(-1)[0];
//     console.log($(lastEnvExposure).attr('name').split("_")[1]);
//
//     let n = parseInt($(lastEnvExposure).attr('name').split("_")[1]) + 1;
//     name = 'envexposure_' + n;
//     console.log("new input name is " + name);
//     $clone.val('').end();
//     $clone.attr('name', name);
//     $clone.appendTo($this.parent());
//     $clone.val('')
//     $this.removeClass('environmental-list-new');
//     $this.off('input', arguments.callee);
//     $clone.on('input', arguments.callee)
// });
