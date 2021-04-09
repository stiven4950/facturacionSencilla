$(document).ready(main);

let count = 0;

function main(argument){
    $('.menu-bar').click(function(){
        if(count == 1){
            $('nav').animate({
                left: '0'
            });
            count = 0;
        } else {
            count = 1;
            $('nav').animate({
                left: '-100%'
            });
        }
    });

    $('.submenu').click(function(){
        $(this).children('.children').slideToggle();
    });

    /* $('#login-form').mdbAutocomplete({
        dataColor: 'green',
        inputFocus: '2px solid orange',
        inputBlur: '1px solid green',
        inputFocusShadow: '0 1px 0 0 green',
        inputBlurShadow: ''
    }); */
}