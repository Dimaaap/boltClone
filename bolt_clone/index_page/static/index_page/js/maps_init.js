function initAutocomplete() {
    let autocomplete = new google.maps.places.Autocomplete(
        document.getElementById("partner-address-field"),
        {types: ["geocode"]}
    );
    autocomplete.addListener("place_changed", () => {
        let place = autocomplete.getPlace();
        console.log(place);

        let postalCode = getPostalCode(place);
        document.getElementById("partner-postal-code-field").value = postalCode;
    })
}

function getPostalCode(place) {
    for (let component of place.address_components) {
        for(let type of component.types){
            if(type === "postal_code"){
                return component.long_name;
            }
        }
    }
    return "";
}

document.addEventListener("DOMContentLoaded", () => {
    initAutocomplete();
})