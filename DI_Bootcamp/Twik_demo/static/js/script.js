// Navbar
let navbar = document.querySelector('#nav');

div_nav = document.createElement('div');
a_link_1 = document.createElement('a');
a_link_2 = document.createElement('a');
h2_header = document.createElement('h2')

div_nav.id = 'div_nav';
a_link_1.classList.add('a_nav_link');
a_link_2.classList.add('a_nav_link');
a_link_1.setAttribute('href', '#main');
a_link_2.setAttribute('href', '#content_1');
h2_header.id = 'h2_nav';

a_link_1.innerHTML = 'Maps';
a_link_2.innerHTML = 'Content';
h2_header.innerHTML = 'Achim Goral'

navbar.appendChild(div_nav);
div_nav.appendChild(a_link_1);
div_nav.appendChild(a_link_2);
div_nav.appendChild(h2_header);

// Content_1
let img = document.querySelector('#content_1');

img_content_1 = document.createElement('img');

img_content_1.id = 'img_content_1';
img_content_1.setAttribute('src', 'img/Hipster-Developer-Dice-1200x750.jpg')
img_content_1.setAttribute('alt', 'twik logo');

img.appendChild(img_content_1);

// Content_2
let content_2 = document.querySelector('#content_2');

div_content_2 = document.createElement('div');
h4_content_2 = document.createElement('h4');
p_content_2 = document.createElement('p');
a_content_2 = document.createElement('a');
button_content_2 = document.createElement('button');

div_content_2.id = 'div_content_2';
h4_content_2.id = 'h4_content_2';
p_content_2.id = 'p_content_2';
a_content_2.classList.add('a_content');
a_content_2.setAttribute('href', '#');
button_content_2.id = 'button_content_2';
button_content_2.setAttribute('onclick', 'hideAndShow()');

h4_content_2.innerHTML = 'This could be your header';
p_content_2.innerHTML = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
button_content_2.innerHTML = 'Show and hide';

content_2.appendChild(div_content_2);
div_content_2.appendChild(h4_content_2);
div_content_2.appendChild(p_content_2);
div_content_2.appendChild(a_content_2);

content_2.appendChild(button_content_2);

let x = document.getElementById('div_content_2');
function hideAndShow() {
    x.style.display === 'none' ? x.style.display = 'block' : x.style.display = 'none';
}

// Content_3
let content_3 = document.querySelector('#content_3');

iframe = document.createElement('iframe');
iframe.setAttribute('width', '100%');
iframe.setAttribute('height', '100%');
iframe.setAttribute('src', 'https://www.youtube.com/embed/ocwnns57cYQ');
iframe.setAttribute('title', 'YouTube video player');
iframe.setAttribute('frameborder', '0');
iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
iframe.setAttribute('allowfullscreen', '');

content_3.appendChild(iframe);

// Footer
let footer = document.querySelector('#footer');

h6_footer = document.createElement('h6');
i_footer = document.createElement('i');

h6_footer.id = 'h6_footer';
i_footer.setAttribute('class', 'far fa-copyright');

h6_footer.innerHTML = 'Copyright 2021';

footer.appendChild(i_footer);
footer.appendChild(h6_footer);