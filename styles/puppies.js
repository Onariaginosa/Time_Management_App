const content = document.querySelector("section");
const company = document.querySelector("header");
const menuItems = document.querySelectorAll("nav li");

menuItems.forEach(item => item.addEventListener('click', show));

function show(event) {
  const sectionName = event.target.innerHTML;
 document.querySelector("#" + sectionName);
 section.style.display = "block";
}
