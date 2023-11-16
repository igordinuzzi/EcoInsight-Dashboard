window.onscroll = function() {shrinkNavOnScroll()};

function shrinkNavOnScroll() {
    var header = document.querySelector('.header-nav');
    if (window.scrollY > 50) {
        header.classList.add('smaller-nav');
    } else {
        header.classList.remove('smaller-nav');
    }
}
