function csvToString(){
    var fs = require('fs');
	address = __dirname + '/../csv_files/test_figures.csv';
	const csvFile = fs.readFileSync(address);
    const csvData = csvFile.toString();
    return csvData;
}
function getData() {
    csvData=csvToString();
    var csvLines=csvData.split('\n');
    var finalData=[];
    for (var i=0;i<csvLines.length;i++) {
        var tempData=csvLines[i].split(',');
        finalData.push(tempData);
    }
    // Shuffle array
    const shuffled = finalData.sort(() => 0.5 - Math.random());

    // Get sub-array of first n elements after shuffled
    let selected = shuffled.slice(0, 10);
    return selected;
}

module.exports = {getData}

