<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <meta name="Description" content="Enter your description here" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/all.min.css">
  <link rel="stylesheet" href="assets/css/style.min.css">
  <title>Micro Api - Documentation</title>
</head>
<body id="documentation">
  <header>
    <div class="container">
      <div class="row pt-4 pb-4 header__wrapper">
        <div class="col-lg-2 col-md-6 col-sm-6 logo__container">
          <a href="index.html" class="logo"><img src="./assets/img/logo.svg" alt="site logo"></a>
        </div>
        <nav class="col-lg-6">
          <ul class="nav__menu">
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About us</a></li>
            <li><a href="contact.html">Contact us</a></li>
            <li><a href="docs.html">Documentation</a></li>
          </ul>
        </nav>
        <div class="col-lg-4 menu__button__container">
          <a href="signin1.html"><button class="secondary-btn">Sign In</button></a>
          <a href="signup-1.html"><button class="primary-btn">Sign Up</button></a>
        </div>
        <div class="mobile__nav">
          <div class="hamburger">
            <div></div>
            <div></div>
            <div></div>
          </div>
          <div class="mobile__menu">
            <nav class="nav">
              <div class="search__form">
                <label for="search">
                  <input type="text" name="search" placeholder="Search...">
                </label>
                <div class="search__icon">
                  <i class="fas fa-search"></i>
                </div>
              </div>
              <ul class="mobile__nav__menu">
                <li><a href="index.html"><b>Home</b></a></li>
                <li><a href="about.html"><b>About us</b></a></li>
                <li><a href="contact.html"><b>Contact us</b></a></li>
                <li><a href="docs.html"><b>Documentation</b></a></li>
                <li><a href="signin1.html"><b>Sign in</b></a></li>
                <li><a href="signup-1.html"><b>Sign Up</b></a></li>
                <li>
                  <a href="#"><i class="fab fa-facebook-f"></i></a>
                  <a href="#"><i class="fab fa-instagram"></i></a>
                  <a href="#"><i class="fab fa-twitter"></i></a>
                </li>
              </ul>
              <div class="menu__logo">
                <a href="#"><img src="./assets/img/logo.svg" alt=""></a>
              </div>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </header>
  <!-- Main body goes here -->
  <main id="comment_main">
    <div class="container-fluidx">
      <div class="row top-row ">
        <div class="col-lg-8 col-md-7 col-sm-12">
          <div class="rowx no-wrap">
            <div class="message-icon">
              <svg width="50" height="50" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M23.4167 39.5834V39.0834H22.9167H14.5834C13.6109 39.0834 12.6783 38.6971 11.9906 38.0094C11.303 37.3218 10.9167 36.3892 10.9167 35.4167V14.5834C10.9167 13.6109 11.303 12.6783 11.9906 11.9906C12.6783 11.303 13.6109 10.9167 14.5834 10.9167H43.75C44.7225 10.9167 45.6551 11.303 46.3428 11.9906C47.0304 12.6783 47.4167 13.6109 47.4167 14.5834V35.4167C47.4167 36.3892 47.0304 37.3218 46.3428 38.0094C45.6551 38.6971 44.7225 39.0834 43.75 39.0834H35.2084H35.0009L34.8543 39.2303L27.151 46.9544C26.8231 47.2639 26.4257 47.4167 26.0417 47.4167H25C24.5801 47.4167 24.1774 47.2499 23.8805 46.953C23.5835 46.656 23.4167 46.2533 23.4167 45.8334V39.5834ZM33.7071 35.9167H43.75H44.25V35.4167V14.5834V14.0834H43.75H14.5834H14.0834V14.5834V35.4167V35.9167H14.5834H26.5834V41.8334V43.0405L27.4369 42.1869L33.7071 35.9167ZM5.75004 6.25004V30.75H2.58337V6.25004C2.58337 5.27758 2.96968 4.34495 3.65732 3.65732C4.34495 2.96968 5.27758 2.58337 6.25004 2.58337H39.0834V5.75004H6.25004H5.75004V6.25004Z"
                  fill="#121215" stroke="white" />
              </svg>
            </div>
            <div class="comment-api-content">
              <h1 class="commentapi-title">
                Comment MicroAPI
              </h1>
              <p class="comentapi-subtitle">
                Updated 10 June 2020
              </p>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-md-5 col-sm-12">
          <div class="row no-wrap">
            <div class="col-lg-4 col-md-4 col-sm-5">
              <p class="user-title">
                Users
              </p>
              <h3 class="user-number">
                2340
              </h3>
            </div>
            <div class="v-divider"></div>
            <div class="col-lg-4 col-md-4 col-sm-5">
              <p class="rating-title">
                Ratings
              </p>
              <h3 class="rating-number">
                <span class="star">
                  <!-- <svg width="25" height="24" viewBox="0 0 25 24" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M11.515 1.6268C11.7081 0.523385 13.2919 0.523387 13.485 1.62681L14.8018 9.14856C14.8948 9.68013 15.3929 10.042 15.9272 9.96622L23.4877 8.89417C24.5968 8.73691 25.0862 10.2431 24.0965 10.7678L17.3498 14.3444C16.873 14.5972 16.6827 15.1827 16.9199 15.6674L20.2758 22.5266C20.7681 23.5329 19.4868 24.4637 18.682 23.6846L13.1955 18.3733C12.8078 17.998 12.1922 17.998 11.8045 18.3733L6.31801 23.6846C5.51316 24.4637 4.23191 23.5329 4.72421 22.5266L8.08012 15.6674C8.31729 15.1827 8.12705 14.5972 7.65025 14.3444L0.903533 10.7678C-0.0861902 10.2431 0.403209 8.73691 1.51231 8.89417L9.07282 9.96622C9.60713 10.042 10.1052 9.68013 10.1982 9.14856L11.515 1.6268Z"
                                    fill="#121215" />
                            </svg> -->
                  <svg width="31" height="29" viewBox="0 0 31 29" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                      d="M14.5489 0.927048C14.8483 0.0057373 16.1517 0.00573993 16.4511 0.927051L19.2045 9.40122C19.3384 9.81324 19.7223 10.0922 20.1555 10.0922L29.0658 10.0922C30.0345 10.0922 30.4373 11.3318 29.6536 11.9012L22.445 17.1385C22.0945 17.3932 21.9479 17.8446 22.0818 18.2566L24.8352 26.7308C25.1345 27.6521 24.0801 28.4182 23.2963 27.8488L16.0878 22.6115C15.7373 22.3568 15.2627 22.3568 14.9122 22.6115L7.70365 27.8488C6.91994 28.4182 5.86546 27.6521 6.16481 26.7307L8.91824 18.2566C9.05211 17.8446 8.90545 17.3932 8.55497 17.1385L1.34641 11.9012C0.562692 11.3318 0.96547 10.0922 1.93419 10.0922L10.8445 10.0922C11.2777 10.0922 11.6616 9.81324 11.7955 9.40122L14.5489 0.927048Z"
                      fill="#121215" />
                  </svg>
                </span>
                <span class="number">
                  4.6
                </span>
              </h3>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="ms-links-div">
      <div class="row1">
        <a href="#" class="ms-links">Introduction</a>
        <a href="./documentation.html" class="ms-links">API Reference</a>
      </div>
      <div class="row2">
        <a href="#" class="ms-links">Video Guide</a>
        <a href="#" class="ms-links active">Tutorial</a>
      </div>
    </div>
    <div class="row no-wrap second-menu">
      <button class="menu__btn" id="bugger" onclick="showMoreLinks(event, 'other__links_div', 'more__links_div')">
        <span></span>
        <span></span>
        <span></span>
      </button>
      <!-- <button id="more__links" onclick="showMoreLinks(event,'more__links_div', 'other__links_div')">
        More <span></span>
    </button> -->
      <div class="col-lg-9 col-md-9 col-sm-12 m-hide">
        <!-- <div class="containr"> -->
        <ul class="links">
          <li class="s-links "><a href="#">Introduction</a></li>
          <li class="s-links "><a href="./documentation.html">API Reference</a></li>
          <li class="s-links "><a href="#">Video Guide</a></li>
          <li class="s-links active"><a href="#">Tutorial</a></li>
        </ul>
        <!-- </div> -->
      </div>
      <div class="col-lg-2 col-md-3 col-sm-12 m-hidex">
        <a href="hire_consultant.html" class="hire">Hire a Consultant</a>
      </div>
    </div>
  </main>
  <div class="d-flex my-5">
    <section class="side__nav">
      <div class="input__div">
        <i class="fa fa-search"></i>
        <input type="search" name="search" placeholder="Search">
      </div>
      <p class="mt-3" data-toggle="collapse" data-target="#get_started" aria-expanded="false"
        aria-controls="collapseExample">
        Get Started
      </p>
      <div class="collapse" id="get_started">
        <ul>
          <li><a href="#">How To Use</a></li>
          <li><a href="#">Terms of service</a></li>
          <li><a href="#">API Support - Website</a></li>
          <li><a href="#">Send email to API support</a></li>
          <li><a href="#">MIT</a></li>
        </ul>
      </div>
      <p><a href="#">Microservice Admins</a></p>
      <p><a href="#">Organizations</a></p>
      <p><a href="#">Admins</a></p>
      <p><a href="#">Applications</a></p>
      <p data-toggle="collapse" data-target="#comments__replies" aria-expanded="false" aria-controls="collapseExample">
        Comments & Replies
      </p>
      <div class="collapse" id="comments__replies">
        <ul>
          <li><a href="#">Schema</a></li>
        </ul>
      </div>
      <p><a href="#">Trouble Shooting/Security</a></p>
      <p><a href="#">Tutorials</a></p>
    </section>
    <section class="container">
      <section>
        <div>
          <h2>API Reference</h2>
          <p>
            The Comment API gives the developer access to built-in functionalities for when they want to
            implement comments and replies within their own application. Basic functionalities are available
            for creation, update, and deletion of comments and replies while ensuring that only users
            authorized are allowed to use such functionalities. Additionally, there are extra features such
            as filtering, sorting, voting, and flagging available.
            <br><br>
            You can use the Comment MicroApi in test mode,
            which does not affect your live data. The API key you use to authenticate
            the request determines whether the request is in live mode or test mode. The Comment MicroApi differs
            for every account as we release new versions and tailor functionality. Log in to see docs
            customized to your version of the API, with your test key and data.<br><br>
          </p>
        </div>
        <div class="signup__steps">
          <h5>Ready to use the Comment Microapi? <span><a href="#"> Sign up for a free MicroApi account.</a></span></h5>
          <ol>
            <li>1. First, sign up with your email after which a temporary login code will be sent to your inbox. Use
              this code to complete registration.</li>
            <li>2. Next, once your setup is complete, you would be redirected to your API dashboard where you can find
              all our list of APIs and link them to your project.</li>
          </ol>
          <h5>
            Was this section helpful?
            <span><a href="#">Yes?</a></span>
            <span><a href="#">No?</a></span>
          </h5>
        </div>
      </section>
      <section class="get__started">
        <h3>Get Started</h3>
        <h5>How To Use</h5>
        <p>Create new Organization to get token. (On creating a new organization, a new admin account is created).</p>
        <p>All Administration related endpoints requires the <span><a href="#">orgToken</a></span> (i.e
          organziations,admins. & application endpoints)</p>
        <p>Create a new Application that Comments and Replies will be tied to.</p>
        <p>Use <span><a href="#">appToken</a></span> generated when creating application on all Comments and Repies
          endpoints</p>
      </section>
      <section>
        <h3>Video Guide</h3>
        <p>The Comment API gives the developer access to built-in functionalities for when they want to implement
          comments and replies within
          their own application. Basic functionalities are available for creation, update, and deletion of
          comments and replies while ensuring that only users authorized are allowed to use such functionalities.
          Additionally, there are extra features such as filtering, sorting, voting, and flagging available.
        </p>
        <video width="100%" controls>
          <source src="" type="video/mp4">
          <source src="" type="video/ogg">
          Your browser does not support the video tag.
        </video>
      </section>
      <section class="my-4">
        <h3>Tutorial</h3>
        <p>
          The Comment API gives the developer access to built-in functionalities for when they want to implement
          comments and replies within their own application. Basic functionalities are available for creation,
          update, and deletion of comments and replies while ensuring that only users authorized are allowed to
          use such functionalities. Additionally, there are extra features such as filtering, sorting, voting, and
          flagging available.<br><br>
          The Comment API gives the developer access to built-in functionalities for when they want to implement
          comments and replies within their own application. Basic functionalities are available for creation,
          update, and deletion of comments and replies while ensuring that only users authorized are allowed to
          use such functionalities. Additionally, there are extra features such as filtering, sorting, voting, and
          flagging available.<br><br>
          The Comment API gives the developer access to built-in functionalities for when they want to implement
          comments and replies within their own application. Basic functionalities are available for creation,
          update, and deletion of comments and replies while ensuring that only users authorized are allowed to
          use such functionalities. Additionally, there are extra features such as filtering, sorting, voting, and
          flagging available.
        </p>
      </section>
    </section>
  </div>
  </main>
  <footer>
    <!-- Write footer here -->
    <div class="container pt-5 pb-5 footer__wrapper">
      <div class="footer__logo__container">
        <div class="footer__logo">
          <a href="#"><img src="./assets/img/logo.svg" alt="footer logo"></a>
        </div>
      </div>
      <div class="footer__menus__container">
        <div>
          <h6>Product</h6>
          <ul>
            <li><a href="#">Authentication API</a></li>
            <li><a href="#">Models</a></li>
            <li><a href="faq.html">FAQ</a></li>
          </ul>
        </div>
        <div>
          <h6>Collaboration</h6>
          <ul>
            <li><a href="setup-comment-api.html">Comments</a></li>
            <li><a href="#">Track Changes</a></li>
          </ul>
        </div>
        <div>
          <h6>Explore</h6>
          <ul>
            <li><a href="contact.html">Contact Us</a></li>
            <li><a href="about.html">About Us</a></li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.slim.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/js/bootstrap.min.js"></script>
  <script src="assets/js/nav.js"></script>
  <script src="assets/js/setup-comment-api.js"></script>
</body>
</html>