// from data.js
var tableData = data;

// YOUR CODE HERE!
//table grid
var table = d3.select("table")
//bootstrap - stripe
table.attr("class", "table table-striped");

// <button id="filter-btn" type="button" class="btn btn-default">Filter Table</button>
var btn = d3.select("#filter-btn");
// <input class="form-control" id="datetime" type="text" placeholder="1/11/2011">
var inputDt = d3.select("#datetime");


// double click on text box and clear data
inputDt.on('dblclick', () => {
    document.getElementById("datetime").value ="";

});


//refresh reset date time to placehoder value
window.onload = function() {
    document.getElementById("datetime").value ="";

}

// table data to web
function tblData(tableData){
    //<tbody></tbody>
    var tbody = d3.select("tbody");
    tbody.html("");

    tableData.forEach((data) => {
        var row= tbody.append("tr");
        Object.entries(data).forEach(([key,value]) => {
            //append data to td in html
            var rs =row.append("td");
            rs.text(value);
        });
    });

};


// button click to filter data by datetime
btn.on("click", function(){
     
    var inputValue = inputDt.property("value");
    var filterData = tableData.filter(function(event){
        if(inputValue !== null && inputValue !== ""  ){
            return event.datetime === inputValue.trim();};
        return event.datetime;
        });
    tblData(filterData);

});



