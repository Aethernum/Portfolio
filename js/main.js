var _doc = document,
	_window = window,
	Home = _doc.getElementById('showcase'),
	About = _doc.getElementById('Ye'),
  	Work = _doc.getElementById('Yee'),
  	Educ = _doc.getElementById('Yeee'),
  	Ref = _doc.getElementById('Yeeee'),
  	Hport= _doc.getElementById('Hport'),
	parallax1=_doc.getElementById("parallax1"),
	parallax2=_doc.getElementById("parallax2"),
	parallax3=_doc.getElementById("parallax3");


document.getElementById('NavHome').onclick = function () {Home.scrollIntoView({
  behavior: 'smooth',
  block : "start"
}); };
document.getElementById('NavAbout').onclick = function () { About.scrollIntoView({
  block : "start",
  behavior: 'smooth'
});};
document.getElementById('NavWork').onclick = function () { Work.scrollIntoView({
  block : "start",
  behavior: 'smooth'
});};
document.getElementById('NavEduc').onclick = function () { Educ.scrollIntoView({
  block : "start",
  behavior: 'smooth'
});};
document.getElementById('NavRef').onclick = function () { Ref.scrollIntoView({
  block : "start",
  behavior: 'smooth'
});};
	

window.onscroll = function(){
        //TOP
        if(document.getElementById("Ye").getBoundingClientRect().top <= 0){
            document.getElementById("title").style = "display: none";
            
        }
        if(document.getElementById("Ye").getBoundingClientRect().top >= 0){
            document.getElementById("title").style = "display: block";
        }
    }
function resize (){
  if (window.innerWidth <= 1155){
    var x= _doc.getElementsByClassName('scroll');
    for (var i = 0; i < x.length; i++) {
        x[i].style.fontSize="15px";
    }
    Hport.style.fontSize="24px";
    _doc.getElementById("nav").style.marginTop="0";
    _doc.getElementById('headmenu').style.marginLeft="5%";
    
  }
  else{
    var x= _doc.getElementsByClassName('scroll');
    for (var i = 0; i < x.length; i++) {
        x[i].style.fontSize="24.96px";
    }
    Hport.style.fontSize="32px";
    _doc.getElementById("nav").style.marginTop="5px";
    _doc.getElementById('headmenu').style.marginLeft="10%";
  }
}


document.addEventListener("DOMContentLoaded", function() {
	let body = document.querySelector("body");
	let html = document.querySelector("html");
	//
	//projects
	let cardsProjects = document.querySelectorAll(".card");
	let container = document.getElementById("project-container");
	let details = document.getElementById("project-details");
	let name = document.getElementById("project-name");
	let subname = document.getElementById("project-subname");
	let description = document.getElementById("project-description");
	let technoList = document.getElementById("technos-list");
	let imagesList = document.getElementById("images-list");

	///// CALLS /////
	AOS.init();
	displayModalProjects();
	slideWithMouse();

	///// FUNCTIONS /////

	function displayModalProjects(){
		for (let i = 0; i < cardsProjects.length; ++i) {
			cardsProjects[i].addEventListener('click',function(e){
				e.preventDefault(); 
				const id = cardsProjects[i].getAttribute('id');
				if(projectsData[id] != null && typeof projectsData[id] != undefined){
					if(!cardsProjects[i].classList.contains("selected")) {
						displayProjectDetails(id);
						cardsProjects.forEach(card => {
							card.classList.remove("selected");
						});
						cardsProjects[i].classList.add("selected");
					} else {
						cardsProjects[i].classList.remove("selected");
						hideProjectDetails();
					}
				}
			});
		}
	}

	function hideProjectDetails() {
		container.style.opacity = 0;
		technoList.innerHTML = null;
		imagesList.innerHTML = null;
		name.innerText = null;
		subname.innerText = null;
		description.innerHTML = null;
		updateProjectContainer();
	}

	function displayProjectDetails(id) {
		const project = projectsData[id];

		technoList.innerHTML = null;
		imagesList.innerHTML = null;

		name.innerText = project.name;
		subname.innerText = project.subname;
		description.innerHTML = project.description;

		project.technos.forEach(value => {
			const li = document.createElement("li");
			li.innerText = value;
			technoList.appendChild(li);
		});

		project.images.forEach(value => {
			const a = document.createElement("a");
			a.href = "images/" + value;
			a.classList.add("img-lightbox-link");
			a.rel = "lightbox";
			a.setAttribute('aria-hidden', 'true');
			const img = document.createElement("img");
			img.src = "images/" + value;
			a.appendChild(img);
			imagesList.appendChild(a);
		});

		(function (root) {
			"use strict";
			if (root.imgLightbox) {
				imgLightbox("img-lightbox-link", {
					onCreated: function () {
						/* show your preloader */
					},
					onLoaded: function () {
						/* hide your preloader */
					},
					onError: function () {
						/* hide your preloader */
					},
					onClosed: function () {
						/* hide your preloader */
					},
					rate: 500 /* default: 500 */ ,
					touch: false /* default: false - use with care for responsive images in links on vertical mobile screens */
				});
			}
		})("undefined" !== typeof window ? window : this);

		container.style.opacity = 1;
		updateProjectContainer();
	}

	function updateProjectContainer() {
		container.style.height = details.clientHeight + 'px';
	}

	function slideWithMouse(){
		const slider = document.querySelector('.scrolling-wrapper');
		let isDown = false;
		let startX;
		let scrollLeft;

		slider.addEventListener('mousedown', (e) => {
			isDown = true;
			startX = e.pageX - slider.offsetLeft;
			scrollLeft = slider.scrollLeft;
		});
		slider.addEventListener('mouseleave', () => {
			isDown = false;
		});
		slider.addEventListener('mouseup', () => {
			isDown = false;
		});
		slider.addEventListener('mousemove', (e) => {
			if(!isDown) return;
			e.preventDefault();
			const x = e.pageX - slider.offsetLeft;
			const walk = (x - startX) * 2; //scroll-fast
			slider.scrollLeft = scrollLeft - walk;
		});
	}
});




