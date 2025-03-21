let currentIndex = 0;

function showNextSlide() {
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;

    slides[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % totalSlides;
    slides[currentIndex].classList.add('active');

    const carouselInner = document.querySelector('.carousel-inner');
    carouselInner.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Cambiar de slide cada 3 segundos
setInterval(showNextSlide, 3000);