// // ////////////////////////////
// // Javascript for Posts page
// // ////////////////////////////

$(function () { // Executed when js-men-icon js clicked
    $('.js-menu-icon').click(function () {
        // $(this) : Self element, namely div.js-menu-icon
        // next() : to div.js-menu-icon, namely div.menu
        // toggle () : SWitch show and hide
        $(this).next().toggle();
    })
})
