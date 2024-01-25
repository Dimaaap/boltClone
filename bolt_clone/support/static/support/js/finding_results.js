$(document).ready(function () {
    $("#search-form").on("input", function (e) {
        e.preventDefault();
        $.ajax({
            type: "GET",
            url: $(this).attr('action'),
            data: $(this).serialize(),
            beforeSend: function(xhr, settings) {
                if(!this.crossDomain) {
                    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");
                }
            },
            success: function(data) {
                $("#search-results").empty();
                if("error" in data) {
                    console.error(data.error);
                } else {
                    for(let i = 0; i < data.length; i++) {
                        let resultElement = $("<div class='result-item'></div>");
                        resultElement.append("<p>"+ data[i].title + data[i].content + "</p>")
                        $("#search-results").append(resultElement)
                    }
                }
            }
        })
    })
})