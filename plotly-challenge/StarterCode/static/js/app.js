
//1. Use the D3 library to read in `samples.json`.

//Initializes the page with a default plot
function init() {
    // drop downlist of IDs
    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selDataset");
    // get the names from samples
    d3.json("samples.json").then((importData) => {
      var lstID = importData.names;
          lstID.forEach((sample) => {
          // dropdown options and attributes
          dropdownMenu
            .append("option")
            .text(sample)
            .property("value", sample);
        });
  
        //default the 1st OIU name.
        const lstNames = lstID[0]; 
        //pass in the OIU ID in horizontalBar function
        horizontalBar(lstNames);
        bubbleChart(lstNames);
        metadataSample(lstNames);
  
  
   });
  };
  
  // 2. Create a horizontal bar chart with a dropdown menu to display the top 10 OTUs found in that individual.
  function horizontalBar(sample){
    // sample data
     d3.json("samples.json").then((importedData) => {
       // console.log(importedData);
       var dataSamples = importedData.samples;
       var arrLst = dataSamples.filter(s_Object => s_Object.id == sample);
       var rs = arrLst [0];
       console.log(rs);
  
      // {"id": "943", "otu_ids": [1795], "sample_values": [2], "otu_labels": ["Bacteria;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus"]}, 
      // * Use `sample_values` as the values for the bar chart.
      var sValues = rs.sample_values;
      // * Use `otu_ids` as the labels for the bar chart.
      var otuIDs  = rs.otu_ids;
      // * Use `otu_labels` as the hovertext for the chart.
      var lbls = rs.otu_labels;  
      //   ![bar Chart](Images/hw01.png)
      // create the trace
        var trace = {
            // Slice the first 10 objects for plotting and reverse get top 10
            x: data = sValues.slice(0, 10).reverse(),
            y: otuIDs.slice(0, 10).map(ids => `OTU ${ids}`),
            text: lbls.slice(0.10).reverse(),
            type: "bar",
            orientation: "h", //bar gragh horizontal
          };
  
        // data
        var chartData = [trace];
  
        // Apply the group bar mode to the layout
          var layout = {
            title: "Top 10 OTU"
      };
  
      // Render the plot to the div tag with id "bar" in the html file
      Plotly.newPlot("bar", chartData, layout);
       
     });
  };
  
  // 3. Create a bubble chart that displays each sample.
  function bubbleChart(sample){
    d3.json("samples.json").then((importedData) => {
      var dataSamples = importedData.samples;
      var arrLst = dataSamples.filter(s_Object => s_Object.id == sample);
      var rs = arrLst [0];
      //console.log(rs);
  
    // {"id": "943", "otu_ids": [1795], "sample_values": [2], "otu_labels": ["Bacteria;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus"]}, 
     var otuID  = rs.otu_ids;
     var sValues = rs.sample_values;
     var lbls = rs.otu_labels
  // ![Bubble Chart](Images/bubble_chart.png)
  // * Use `otu_ids` for the x values.
  // * Use `sample_values` for the y values.
  // * Use `sample_values` for the marker size.
  // * Use `otu_ids` for the marker colors.
  // * Use `otu_labels` for the text values.
  
      var trace ={
        x: otuID,
        y: sValues,
        mode: 'markers',
        text: lbls,
        marker : {
          color: otuID,
          size: sValues
  
        }
      }
      var chartData = [trace];
  
      var layout = {
        xaxis: {title: "OTU ID"} 
  };
    Plotly.newPlot('bubble', chartData, layout);
  });
  
  }
  
  // 4. Display the sample metadata, i.e., an individual's demographic information.
  //"metadata":[{"id": 940, "ethnicity": "Caucasian", "gender": "F", "age": 24.0, "location": "Beaufort/NC", "bbtype": "I", "wfreq": 2.0}
  function metadataSample(sample){
  
    d3.json("samples.json").then((importedData) => {
      var dataMeta = importedData.metadata;
      var arrLst = dataMeta.filter(s_Object => s_Object.id == sample);
      var rs = arrLst [0];
      console.log(rs);
      var p = d3.select("#sample-metadata").html("");
  
  // 5. Display each key-value pair from the metadata JSON object somewhere on the page.
  // Object.entries() returns an array whose elements are arrays corresponding to the enumerable 
  // string-keyed property [key, value] pairs found directly upon object. The ordering of 
  // the properties is the same as that given by looping over the property values of the object manually.
  // ![hw](Images/hw03.png)
  // interate through the an object
   // reset key values data in panel
    
    Object.entries(rs).forEach(([key, value]) => {
      p.append('h5').text(key+ ': ' + value);
      });
    });
  
  };
  
  // 6. Update all of the plots any time that a new sample is selected.
  // Additionally, you are welcome to create any layout that you would like for your dashboard. An example dashboard is shown below:
  // ![hw](Images/hw02.png)
  
  function optionChanged(ID){
    horizontalBar(ID);
    bubbleChart(ID);
    metadataSample(ID);
  
  }
  
  
  init();
  
  // ## Deployment
  
  // * Deploy your app to a free static page hosting service, such as GitHub Pages. Submit the links to your deployment and your GitHub repo.
  
  // * Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file
  
  // ## Hints
  
  // * Use `console.log` inside of your JavaScript code to see what your data looks like at each step.
  
  // * Refer to the [Plotly.js documentation](https://plot.ly/javascript/) when building the plots.
  
  // ### About the Data
  
  // Hulcr, J. et al.(2012) _A Jungle in There: Bacteria in Belly Buttons are Highly Diverse, but Predictable_. Retrieved from: [http://robdunnlab.com/projects/belly-button-biodiversity/results-and-data/](http://robdunnlab.com/projects/belly-button-biodiversity/results-and-data/)
  