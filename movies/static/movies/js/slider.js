const slider = document.querySelector('.slider');
const sliderImages = document.querySelectorAll('.slider__image');
const sliderLine = document.querySelector('.slider__line');

const sliderBtnNext = document.querySelector('.slider__btn-next');
const sliderBtnPrev = document.querySelector('.slider__btn-prev');

let sliderCount = 0;
let sliderWidth = slider.offsetWidth;

sliderBtnNext.addEventListener('click', nextSlide);
sliderBtnPrev.addEventListener('click', prevSlide);

function nextSlide() {
    sliderCount++;
    console.log(sliderCount);
    console.log(sliderImages.length);
    if (sliderCount >= sliderImages.length) {
    sliderCount = 0;
    }

    rollSlider()
}

function prevSlide() {
    sliderCount--;
    console.log(sliderCount);
    console.log(sliderImages.length);

    if (sliderCount < 0) {
    sliderCount = sliderImages.length - 1;
    }

    rollSlider()
}

function rollSlider() {
    sliderLine.style.transform = `translateX(${-sliderCount * sliderWidth}px)`;
}

setInterval(() => {
    nextSlide()
}, 7000);