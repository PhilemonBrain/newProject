# Micro API New Frontend

New fromtend repository for static files of the microAPI v2 project. Please read all instructions carefully as pull requests will be carefully accessed before being merged

### Folder Structure

The project consists of the main pages, the layout page and also an asset folder at the root directory. The layout contains the site header, footer and sidebars so please ensure your get the header and footer codes from there before proceeding.

In the assets folder, we have an images folder where all images should be sent to, there is a js folder containing js files for each page (the nav.js file is for the header/footer layout), there is also a fonts folder contains our custom fonts and most importantly, we have an SCSS folder and a CSS folder. All files in the SCSS folder compiles to one single minified css file which is located inside the CSS folder. The CSS folder and it's content SHOULD NEVER be touched or edited. 

### Contribution guide

1. Fork the repository
2. Clone and then open it up on your code editor
3. Open terminal and set upsream branch: ```git remote add upstream https://github.com/hngi/microAPI-v2.0-frontend```
4. Pull upstream ```git pull upstream develop```
5. Create a new branch for the task your are doing eg: ```git checkout -b home-page```
6. After making changes, do ```git add .```
7. Commit your changes with a descriptive commit message```git commit -m "commit message"```
8. To make sure there are no conflicts: ```git pull upstream develop```
9. Push changes to your new branch: ```git push origin your-current-branch-name```
10. Create a pull request to the develop branch