window.onscroll = function() {
    shrinkNavOnScroll();
    scrollFunction();
};

function shrinkNavOnScroll() {
    var header = document.querySelector('.header-nav');
    if (window.scrollY > 50) {
        header.classList.add('smaller-nav');
    } else {
        header.classList.remove('smaller-nav');
    }
}

function scrollFunction() {
    let topButton = document.getElementById("topButton");
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        topButton.style.display = "block";
    } else {
        topButton.style.display = "none";
    }
}

function scrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}
