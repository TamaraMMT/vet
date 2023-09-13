document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
  
    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', function () {
        mobileMenu.classList.toggle('hidden');
      });
    }
  });

  
  import {
    Ripple,
    Input,
    initTE,
  } from "tw-elements";
  
  initTE({ Ripple, Input });