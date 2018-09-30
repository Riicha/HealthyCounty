function addUserPreferenceSelection(){
 //If parent option is changed

    $("#Preference1").change(function() {
        var parent = $(this).val(); //get option value from parent
        list("#Preference1", '#Preference2', parent);
        list('#Preference2', '#Preference3', parent);
        list('#Preference3', '#Preference4', parent);
    });



    $("#Preference2").change(function () {
        var parent = $(this).val(); //get option value from parent
        list("#Preference2", '#Preference3', parent);
        list("#Preference3", '#Preference4', parent);
    });



    $("#Preference3").change(function () {
        var parent = $(this).val(); //get option value from parent
        list("#Preference3", '#Preference4', parent);
    });

}

function remove(array, element) {
    return array.filter(function (x) {
        return x.value != element
    });

}



//function to populate child select box
function list(parentOption, dependentChild, removeItem)
{
    var options = $(parentOption +' option');
    var values = $.map(options, function (option) {
    return { display: option.innerText, value: option.value };
    });



    $(dependentChild).empty(); //reset child options
    var childArray = remove(values, removeItem);
    $(childArray).each(function (i) { //populate child options
    $(dependentChild).append("<option value=\"" + childArray[i].value + "\">" + childArray[i].display + "</option>");

    });



}

addUserPreferenceSelection()