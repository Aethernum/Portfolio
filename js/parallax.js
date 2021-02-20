// ------------- VARIABLES ------------- //
var ticking = false;
var isFirefox = (/Firefox/i.test(navigator.userAgent));
var isIe = (/MSIE/i.test(navigator.userAgent)) || (/Trident.*rv\:11\./i.test(navigator.userAgent));
var scrollSensitivitySetting = 50; //Increase/decrease this number to change sensitivity to trackpad gestures (up = less sensitive; down = more sensitive) 
var slideDurationSetting = 700; //Amount of time for which slide is "locked"
var currentSlideNumber = 0;
var totalSlideNumber = document.querySelectorAll('.background').length;

console.log(totalSlideNumber);
// ------------- DETERMINE DELTA/SCROLL DIRECTION ------------- //
function parallaxScroll(evt) {
    
  if (isFirefox) {
    //Set delta for Firefox
    delta = evt.detail * (-120);
  } else if (isIe) {
    //Set delta for IE
    delta = -evt.deltaY;
  } else {
    //Set delta for all other browsers
    delta = evt.wheelDelta;
  }

  if (ticking != true) {
    if (delta <= -scrollSensitivitySetting) {
      //Down scroll
      ticking = true;
      if (currentSlideNumber !== totalSlideNumber - 1) {
        currentSlideNumber++;
        nextItem();
      }
      slideDurationTimeout(slideDurationSetting);
    }
    if (delta >= scrollSensitivitySetting) {
      //Up scroll
      ticking = true;
      if (currentSlideNumber !== 0) {
        currentSlideNumber--;
      }
      previousItem();
      slideDurationTimeout(slideDurationSetting);
    }
  }
}


function SlideTo(dest){
    console.log("ooof");
    var goTo = setInterval(function(){  

        console.log(currentSlideNumber);
        if (currentSlideNumber < dest) {
        
            if (currentSlideNumber !== totalSlideNumber - 1) {
                currentSlideNumber++;
                nextItem();
            }
            
        }
        else if(currentSlideNumber > dest){
            if (currentSlideNumber !== 0) {
                currentSlideNumber--;
            }
            previousItem();
        }
        else{
            clearInterval(goTo);
        }
    
    }, 100);
}

// ------------- SET TIMEOUT TO TEMPORARILY "LOCK" SLIDES ------------- //
function slideDurationTimeout(slideDuration) {
  setTimeout(function() {
    ticking = false;
  }, slideDuration);
}

// ------------- ADD EVENT LISTENER ------------- //
var mousewheelEvent = isFirefox ? "DOMMouseScroll" : "wheel";
window.addEventListener(mousewheelEvent, parallaxScroll);


// ------------- SLIDE MOTION ------------- //
function nextItem() {
  var $previousSlide = $(".background").eq(currentSlideNumber - 1);
  $previousSlide.removeClass("up-scroll").addClass("down-scroll");
}

function previousItem() {
  var $currentSlide = $(".background").eq(currentSlideNumber);
  $currentSlide.removeClass("down-scroll").addClass("up-scroll");
}




document.addEventListener("DOMContentLoaded", function() {
	let body = document.querySelector("body");
	let html = document.querySelector("html");
	//
	//projects
	let cardsProjects = document.querySelectorAll(".card");
	let container = document.getElementById("project-container");
	let details = document.getElementById("project-details");
	let name = document.querySelector("#project-name a");
	let subname = document.getElementById("project-subname");
	let description = document.getElementById("project-description");
	let technoList = document.getElementById("technos-list");
	

	///// CALLS /////
	AOS.init();
	displayModalProjects();
	slideWithMouse();
    createFallingStar(26);
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
		name.innerText = null;
		subname.innerText = null;
		description.innerHTML = null;
		updateProjectContainer();
	}

	function displayProjectDetails(id) {
		const project = projectsData[id];

		technoList.innerHTML = null;
		if(project.name == "My portfolio")
			name.innerHTML = project.name;
		else
			name.innerHTML = project.name+' <i class="fas fa-download"></i>';
		subname.innerText = project.subname;
		description.innerHTML = project.description;

		project.technos.forEach(value => {
			const li = document.createElement("li");
			li.innerText = value;
			technoList.appendChild(li);
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




function createFallingStar(nbstar){
    var night = document.querySelector(".night");
    for (let index = 0; index < nbstar; index++) {
        const fall = document.createElement('div');
        fall.className = "shooting_star";
        topRand=Math.random()*800;
        leftRand=Math.random()*night.offsetWidth/2;

        fall.style.top= night.offsetHeight/2 - topRand+"px";
        fall.style.left= leftRand-300+"px";
        fall.style.animationDelay = Math.random()*8000+"ms";
        night.appendChild(fall);
    }
    for (let index = nbstar/2; index < nbstar; index++) {
        const fall = document.createElement('div');
        fall.className = "shooting_star";
        topRand=Math.random()*800;
        leftRand=Math.random()*night.offsetWidth/2+night.offsetWidth/2;

        fall.style.top= night.offsetHeight/2 - topRand+"px";
        fall.style.left= leftRand-300+"px";
        fall.style.animationDelay = Math.random()*8000+"ms";
        night.appendChild(fall);
    }
}