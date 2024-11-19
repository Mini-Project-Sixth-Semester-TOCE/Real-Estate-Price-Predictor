function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft").value;
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    console.log("Inputs: Sqft:", sqft, "BHK:", bhk, "Bath:", bathrooms, "Location:", location);

    var url = https://real-estate-price-predictor-6bbh.onrender.com/predict_home_price";

    $.post(url, {
        total_sqft: parseFloat(sqft),
        bhk: bhk,
        bath: bathrooms,
        location: location
    }, function (data, status) {
        console.log("Response from server:", data);
        if (data.estimated_price) {
            estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
        } else {
            estPrice.innerHTML = "<h2>Error in prediction</h2>";
        }
    }).fail(function (error) {
        console.error("Error in request:", error);
        estPrice.innerHTML = "<h2>Server Error</h2>";
    });
}
  
  function onPageLoad() {
    console.log("document loaded");
    var url = "https://real-estate-price-predictor-6bbh.onrender.com/get_location_names";
    $.get(url, function(data, status) {
        console.log("Got response for get_location_names request:", data);
        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for (var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
}
window.onload = onPageLoad;
