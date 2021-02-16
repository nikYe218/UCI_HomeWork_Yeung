
// @TODO: YOUR CODE HERE!
// ### Core Assignment: D3 Dabbler (Required Assignment)
// ![4-scatter](Images/4-scatter.jpg)
// You need to create a scatter plot between two of the data variables such as `Healthcare vs. Poverty` or `Smokers vs. Age`.
// Using the D3 techniques we taught you in class, create a scatter plot that represents each state with circle elements. 
// You'll code this graphic in the `app.js` file of your homework directory—make sure you pull in the data from `data.csv` by using the `d3.csv` function. 
// Your scatter plot should ultimately appear like the image at the top of this section.
// * Include state abbreviations in the circles.
// * Create and situate your axes and labels to the left and b  ottom of the chart.
// * Note: You'll need to use `python -m http.server` to run the visualization. This will host the page at `localhost:8000` in your web browser.

//SETUP1 CHART PARAMETERS
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 80
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

//console.log("width:" + width);
//STEP2 SVG WRAPPER 
// Create an SVG wrapper, append an SVG group that will hold our chart,
// and shift the latter by left and top margins.
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight +20);

  // Append an SVG group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Retrieve data from the CSV file 
d3.csv("assets/data/data.csv").then(function(csv_Data, err) {
    if (err) throw err;
    //Parse data
    csv_Data.forEach(function(data) {
        if (err) throw err;
        data.poverty = +data.poverty
        data.healthcare= +data.healthcare

        });

// Initial Params
    var chosenXAxis = "poverty";
    var chosenYAxis = "healthcare";

    // scaling x and y axes
    var xLinearScale = d3.scaleLinear()
      .domain([d3.min(csv_Data, d => d[chosenXAxis]) * 0.8,
        d3.max(csv_Data, d => d[chosenXAxis]) * 1.2])
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([2, d3.max(csv_Data, d => d.healthcare)])
      .range([height, 0]);
    
  
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);


    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    // create the circle
    var circlesGroup = chartGroup.selectAll("circle")
      .data(csv_Data)
      .enter()
      .append("circle")
      .attr("cx", d => xLinearScale(d.poverty))
      .attr("cy", d => yLinearScale(d.healthcare))
      .attr("r", "15")
      .attr("fill", "lightblue")
      .style("text-anchor", "middle");

    // create the circle text
      var circlesGroup = chartGroup.selectAll()
      .data(csv_Data)
      .enter()
      .append("text")
      .attr("x", d => xLinearScale(d.poverty))
      .attr("y", d => yLinearScale(d.healthcare))
      .style("font-size", "10px")
      .style("text-anchor", "middle")
      .style('fill', 'white')
      .text(d => (d.abbr))


    // tool tip and data
    var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function (d) {
        return (`${d.state}<br>Poverty: ${d.poverty}<br>HealthCare: ${d.healthcare}`);
    });

    chartGroup.call(toolTip);

    //hover over to show tooltip data
    circlesGroup.on("mouseover", function(data) {
      toolTip.show(data, this);
    })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

     // append y axis
      chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 25)
      .attr("x", -50 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "aText")
      .text("Lacks Healthcare (%)");

      // append x axis
      chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top +25 })`) // xaxis label settings
      .attr("class", "aText")
      .text("In Poverty (%) ");
  }).catch(function(error) {
    console.log(error);
  });