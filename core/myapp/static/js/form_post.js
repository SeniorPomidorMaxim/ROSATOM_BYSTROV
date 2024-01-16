document.addEventListener('DOMContentLoaded', function() {
    var defaultDivisionId = document.getElementById('id_division').value;
    sendAjaxRequest(defaultDivisionId);
    document.getElementById('id_division').addEventListener('change', function() {
        var divisionId = this.value;
        sendAjaxRequest(divisionId);
    });
});


function sendAjaxRequest(divisionId) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/get_companies/?division_id=' + divisionId, true);


    xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 400) {
            var companiesData = JSON.parse(xhr.responseText);
            var companiesDropdown = document.getElementById('id_company');
            companiesDropdown.innerHTML = '';  
            if (companiesData.length > 0) {
                companiesData.forEach(function(company) {
                    var option = document.createElement('option');
                    option.value = company.id;
                    option.text = company.name;
                    companiesDropdown.add(option);
                });
               console.log('Received companies data:', companiesData);
            } 
        } 
    };
    xhr.onerror = function() {
        console.error('Request failed');
    };
    xhr.send();
}