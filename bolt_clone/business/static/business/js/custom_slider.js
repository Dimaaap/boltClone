const adverts = [
    {
        count: 1,
        title: "Мальта",
        desc: `У партнерстві з компанією Buzzz Electric ми розгорнули сервіс виклику
        електричного триколісного електромобіля.`
    },
    {
        count: 2,
        title: "Країни Балтії",
        desc: `У партнерстві з Eleport ми встановили 750 пунктів зарядки електромобілів,
        а наша співпраця зі Swedbank та Luminor допомагає фінансувати розширення прокатного парку
        гібридних та електричних Bolt Drive.`
    },
    {
        count: 3,
        title: "Іспанія",
        desc: `Компанія Repsol стала нашим затвердженим постачальником електроенергії для нашої служби
        підзарядки, гарантуючи, що водії, які користуються автомобілями, заряджають свої
        автомобілі 100% відновлювальною електроенергією.`
    },
    {
        count: 4,
        title: "Великобританія",
        desc: `Ми співпрацюємо з компанією Weflex, що дозволяє водіям переходити
        на використання електромобілів за гнучкою схемою оренди з правом викупу. А
        наша пілотна програма зі Splend дозволяє 500 водіям таксі стати власниками електромобілів.
        `
    },
    {
        count: 5,
        title: "Нідерланди",
        desc: `Ми розпочали співпрацю з Shell, щоб надавати водіям знижки
        на зарядку електромобілів на їхніх станціях.`
    },
    {
        count: 6,
        title: "Кенія",
        desc: `Ми представили електричні тук-туки(вид ТЗ) та електровелосипеди
        на платформі доставлення їжі Bolt Food`
    }
];

document.addEventListener("DOMContentLoaded", function() {
    let currentIndex = 0;
    const images = [
        "../../../static/business/media/slide-1.webp",
        "../../../static/business/media/slide-2.webp",
        "../../../static/business/media/slide-3.webp",
        "../../../static/business/media/slide-4.webp",
        "../../../static/business/media/slide-5.webp",
        "../../../static/business/media/slide-6.webp"
    ];
    const advertContainer = document.querySelector(".advert");
    const pageNumContainer = document.querySelector(".page-num");
    const imageContainer = document.querySelector(".carousel");
    const progressBar = document.querySelector(".busy-selector");

    function updateCarousel() {
        const currentImage = images[currentIndex];
        const nextImage = images[(currentIndex + 1) % images.length];
        const hasNextSlide = currentIndex < images.length - 1;
        const hasPrevSlide = currentIndex > 0;

        imageContainer.innerHTML = `
            <img src="${currentImage}" class="images" style="width: 150%;" />
            ${hasNextSlide ? `<img src="${nextImage}" class="images next" />` : ''}
        `;
        advertContainer.innerHTML = `<h3>${adverts[currentIndex].title}</h3><p>${adverts[currentIndex].desc}</p>`;
        pageNumContainer.textContent = `${currentIndex + 1} / ${images.length}`;

        const progress = ((currentIndex + 1) / images.length) * 100;
        progressBar.style.width = `${progress}%`;

        const prevSlideBtn = document.getElementById("prev-slide");
        const nextSlideBtn = document.getElementById("next-slide");
        prevSlideBtn.style.display = hasPrevSlide ? 'block' : 'none';
        nextSlideBtn.style.display = hasNextSlide ? 'block' : 'none';
    }

    document.getElementById("prev-slide").addEventListener("click", function() {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });

    document.getElementById("next-slide").addEventListener("click", function() {
        if (currentIndex < images.length - 1) {
            currentIndex++;
            updateCarousel();
        }
    });

    updateCarousel();
});