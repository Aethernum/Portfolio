<!DOCTYPE html>
<html>
    <head>
    <meta charset="utf-8">
    <title>Skowron Martin</title>
    <link rel="stylesheet" type="text/css" href="css/swiper.css">
    <link rel="stylesheet" type="text/css" href="css/star.css">
    <link rel="stylesheet" type="text/css" href="css/starfall.css">
    <link rel="stylesheet" href="css/parallax.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css">
    <link rel="shortcut icon" type="image/png" href="picture/resume.png"/>
    </head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/3.10.1/lodash.min.js"></script>
    <script src="https://code.jquery.com/jquery-2.1.4.min.js"></script>
    

    <body>
        <header>
        <div id="headmenu" class="container">
            <h1 id="Hport"> Martin Skowron </h1>
            <div id="nav">
            <ul>
                <li><a id="NavParallax1" class="scroll" onclick="SlideTo(0)">Home</a></li>
                <li><a id="NavParallax2" class="scroll" onclick="SlideTo(1)">About</a></li>
                <li><a id="NavParallax3" class="scroll" onclick="SlideTo(2)">Projects</a></li>
                <li><a id="NavParallax4" class="scroll" onclick="SlideTo(3)">Education</a></li>
                <li><a href="CV_SKOWRON_Martin.pdf" target="_blank" class="ic">CV<i class="fas fa-file-download" style="padding-left:10px"></i></a></li>
            </ul>
            </div>
        </div>
        </header>
        <div class="container">
            <section class="background" id="parallax1">
                <div id="showcase">
                    <div  class="myPara">
                        <div id='stars'></div>
                        <div id='stars2'></div>
                        <div id='stars3'></div>
                        <div id='title' class="container">
                        <span>
                            Martin Skowron
                        </span>
                        <br>
                        <span>
                            IT Student
                        </span>
                        
                        </div>
                    </div>
                </div>
            </section>
            <section class="background" id="parallax2">
                <div id="about">
                
                    <h1 class="about-title">Who I am </h1>
                    <p class="about-text">I'm an IT student based in France and Québec, my relatives consider me to be an optimist and motivated person in all situations. I am someone who communicates a lot with the people around me and I have a great sense of humor. I encourage my colleagues to give their best. In future, I'd like to continue my studies in the field of video games or the development of VR applications, I still have a strong interest in website development.<br></br> 
                                            In the future I hope to have the opportunity to train as a stuntman, it's a very physical job that requires great rigour and strong nerves. Indeed, a stuntman must ensure the quality and safety of the equipment used. He or she assesses the risks and is recognised for the reliability of these feats. <br></br>
                                            Miscellaneous : Very sporty, extreme sports fan, I played rugby 🏉 in clubs for 12 years, and I have been playing American Football 🏈 for 2 years. I love video games, video editing and surfing on Youtube. </p>

                    <div class="night">
                        <div class="shooting_star"></div>
                    </div>
                    <h1 class="about-title">My skills</h1>
                    <div id="container_skill">
                        <div id="Skill-Web" class="skill-card">
                            <header class="skill-card__header" id="Header_Web"><img class="skill-card__icon" src="picture/Web.png" alt="HTML5 Logo"/></header>
                            <div class="skill-card__body">
                                <h2 class="skill-card__title">Web</h2><span class="skill-card__duration">HTML, CSS, JS, PHP<br>LARAVEL, PHPMyAdmin</span>
                                <p class="skill-card__star">
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star-half-alt"></span>
                                </p>
                            </div>
                        </div>
                        <div id="Skill-OOP" class="skill-card">
                            <header class="skill-card__header" id="Header_Oop"><img class="skill-card__icon" src="picture/OOP.png" alt="CSS3 Logo"/></header>
                            <div class="skill-card__body">
                                <h2 class="skill-card__title">OOP</h2><span class="skill-card__duration">C#, C++, JAVA, PYTHON, PHP </span>
                                <p class="skill-card__star">
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="far fa-star"></span>
                                </p>
                            </div>
                        </div>
                        <div id="Skill-DB" class="skill-card">
                            <header class="skill-card__header" id="Header_Db"><img class="skill-card__icon" src="picture/DB.png" alt="HTML5 Logo"/></header>
                            <div class="skill-card__body">
                                <h2 class="skill-card__title">DataBase</h2><span class="skill-card__duration">DBMS, SQL - PL/SQL, UML, MERISE</span>
                                <p class="skill-card__star">
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="far fa-star"></span>
                                <span class="far fa-star"></span>
                                </p>
                            </div>
                        </div>
                        <div id="Skill-Com" class="skill-card">
                            <header class="skill-card__header" id="Header_Com"><img class="skill-card__icon_Com" src="picture/communication.png" alt="PHP Logo"/></header>
                            <div class="skill-card__body">
                                <h2 class="skill-card__title">Communication</h2><span class="skill-card__duration">SPHINX, Office 365, Photoshop, Adobe Illustrator</span>
                                <p class="skill-card__star">
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="far fa-star"></span>
                                </p>
                            </div>
                        </div>
                        <div id="Skill-Lang" class="skill-card">
                            <header class="skill-card__header" id="Header_MSql"><img class="skill-card__icon_Com" src="picture/langue.png" alt="MySql Logo"/></header>
                            <div class="skill-card__body">
                                <h2 class="skill-card__title">Language</h2><span class="skill-card__duration">Français (Native), English(B2-C1), Español (A2), Pусский (A2)</span>
                                <p class="skill-card__star">
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star"></span>
                                <span class="fa fa-star-half-alt"></span>
                                <span class="far fa-star"></span>
                                </p>
                            </div>
                        </div>
                    </div>  
                </div>
            </section>
            <section class="background" id="parallax3">
                <div id="projects" data-aos="fade-up" class="aos-init aos-animate ">
                    <h1 class="title"> My projects</h1>
                    <h2 class="subtitle">Explore my school and personal projects :</h2>
                    <div class="scrolling-wrapper">
                        <div class="card first-card" id="moonstone"></div>
                        <div class="card" id="gladiaball"></div>
                        <div class="card" id="blowbug"></div>
                        <div class="card" id="purge"></div>
                        <div class="card" id="portfolio"></div>
                        <div class="card" id="hopital"></div>
                        <div id="last-card"></div>
                    </div>
                    <lottie-player src="https://assets2.lottiefiles.com/packages/lf20_zROQ4H.json" background="transparent" speed="0.8" style="width: 100px; height: 100px; margin-top: -60px; position: absolute; right: 0;" loop="" autoplay="">
                    </lottie-player>

                    <div id="project-container">
                        <div id="project-details">
                            <h2 id="project-name"><a href=""></a></h2>
                            <h3 id="project-subname"></h3>
                            <p id="project-description"></p>
                            <div id="technos">
                                <ul id="technos-list"></ul>
                            </div>
                        </div>
                    </div>
                </div>
            </section>


            <section class="background" id="parallax4">
                <div id="education" class="sectionClass">
                    <h1>Education</h1>
                    <div class="fullWidth eight columns">
                       
                        <div class="uk-section uk-section-muted uk-preserve-color" id="parcours">
                            <div class="uk-container">
                                <ul class="timeline">
                                    <li>
                                        <div class="direction-r">
                                            <div class="flag-wrapper">
                                                <span class="hexa"></span>
                                                <span class="flag">UQAC</span>
                                                <span class="time-wrapper"><span class="time">Jan 2021 -> Now</span></span>
                                            </div>
                                            <div class="desc">Maitrise en Informatique avec Majeur en Jeux vidéo</br> 
                                                Formation Bac +5 développeur informatique spécialisé dans la création et le développement des jeux vidéo 
                                            </div>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="direction-l">
                                            <div class="flag-wrapper">
                                                <span class="hexa"></span>
                                                <span class="flag">UQAC</span>
                                                <span class="time-wrapper"><span class="time">Sept 2019 -> May 2020</span></span>
                                            </div>
                                            <div class="desc">Baccalauréat en Informatique avec Majeur en Jeux vidéo </br>
                                                Diplome Bac +3 qui vise l'acquisition des connaissances essentielles pour concevoir et développer des jeux vidéo et des compétences pratiques de travail d'équipe.
                                            </div>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="direction-r">
                                            <div class="flag-wrapper">
                                                <span class="hexa"></span>
                                                <span class="flag">USMB</span>
                                                <span class="time-wrapper"><span class="time">Sept 2017 -> June 2019</span></span>
                                            </div>
                                            <div class="desc">DUT Informatique</br>
                                                Formation d'informatique en vue d'apprendre la conception et création d’application et site web, la gestion de base de données ou encore la gestion de projet. 
                                            </div>
                                        </div>
                                    </li>
                                </ul>
                                <div class="uk-text-center uk-margin-large">
                                    <a class="uk-button button-primary" href="PDF/Youness_Chetoui.pdf" target="_blank">mon cv pdf</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </body>
    
    <script src="js/parallax.js"></script>
    <script type="text/javascript" src="js/lottie-player.js" ></script>
    <script type="text/javascript" src="js/projects_data.js" ></script>
    <script type="text/javascript" src="js/aos.js" ></script>
</html>
