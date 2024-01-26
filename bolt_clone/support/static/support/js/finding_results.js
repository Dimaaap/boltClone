$(document).ready(function () {
    $("#search-form").on("input", function (e) {
        e.preventDefault();
        let searchQuery = $(this).find("input[name='q']").val();
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
                if(data.length === 0) {
                     $("#search-results").html(`<h3 class='find-results'>Результати пошуку</h3><p class='find-desc'>0 запис
                     (-ів) було знайдено за запитом ${searchQuery} </p>`);
                } else {
                    if(data.length) {
                        $("#search-results").append(`<h3 class='find-results'>
                        Результати пошуку</h3><p class='find-desc'>${data.length} запис
                         (-ів) було знайдено за запитом ${searchQuery} </p>`)
                    }
                    for(let i = 0; i < data.length; i++) {
                        let resultElement = $("<div class='result-item'></div>");
                        resultElement.append("<a href='" + data[i].url + "'>" + "<h3>"+ data[i].title + "</h3>" +
                        "<small>" +  "Підтримка" + " >" + " Для кур'єрів" + " > " + data[i].category + "</small>" +
                         "<p>" + data[i].content + "</p>" +"</a>");
                         $("#search-results").append(resultElement)
                    }
                }
            }
        })
    })
})