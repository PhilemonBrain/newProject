// toggle butons

let toggle = document.querySelectorAll('.api__box .p-switch input');
let check = document.querySelectorAll('.api__box .p-toggle input')

toggle.forEach((tug, index) => {
  tug.addEventListener('click', (e) => {
    check[index].click();
  })
})

// set inner text and class for api boxes
document.querySelector('body').addEventListener('mousemove', changeApiBtns)

function changeApiBtns() {

  let configBtn = document.querySelectorAll('.active-row .api__box__buttons a button');
  let addBtn = document.querySelectorAll('.inactive-row .api__box .api__box__buttons a button');

  // console.log(addBtn)

  if (addBtn) {
    addBtn.forEach(btn => {
      
      btn.innerHTML = "+ Add API";
      btn.className = "secondary-btn";
    })
  }

  if (configBtn) {
    configBtn.forEach(btn => {
      btn.innerHTML =  "Configure";
      btn.className =  "primary-btn";
    })
    
  }

}

// drag drop events

// Make box draggable
$('.dragBox').draggable({
  revert: 'invalid',
  cursor: "move",
  cursorAt: { top: 50, left: 50 },
  //  drag: function(event, ui) {
  //     // $('.dropBox')
  //  }
});

// allow drop on section
$( '.dropBox' ).droppable({
   accept: '.dragBox',
   drop: function(event, ui) {


    $(this)
    .append(ui.draggable.css({
      position: 'relative',
      left: '0px',
      top: '0px',
    }))
   
  }
});


// show empty for no content
let activeApiBox = document.querySelector('#container .active-row');
let apiPresent = document.querySelector('#container .active-row dragBox');

document.querySelector('body').addEventListener('mousemove', () => {

  if (!apiPresent) {
    activeApiBox.innerHTML = 
    /*html*/`
      <div class="empty-api" style="display:flex; flex-direction:column; justify-content:center; align-items:center; width: 100%">
      <div className="icon">
      <span class="material-icons" style="font-size: 65px; color: lightgrey">cloud_off</span>
      </div>

      <div className="text" style="text-align:center;">
      <h4 style="color: #9c9c9c">There's nothing here</h4>
      <p style="color: #9c9c9c;">Drag from available APIs or use the add button to add new API</p>
      </div>
      </div>
    `
  }
})


