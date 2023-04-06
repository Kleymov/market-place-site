console.log("Hello, world");
// import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@9/swiper-bundle.esm.browser.min.js'

new Swiper(".image-slider", {
  navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
  },
  pagination: {
      el: ".swiper-pagination",
      clickable: true,
  },
  loop: true,
  // autoHeight: true,
  slidesPerView: 1,
  autoplay: {
    delay: 2000, 
    disableOnInteraction: false,
  }, 
  // speed: 1100, 
  effect: 'fade',
  fadeEffect: {
    crossFade: true,
  }
});

// {
    // spaceBetween: 100,
    // 
    // 
    // keyboard: true,
// }