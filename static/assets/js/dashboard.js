// toggle butons

let toggle = document.querySelectorAll('.api__box .p-switch');
let check = document.querySelectorAll('.api__box .p-toggle input')

toggle.forEach((tug, index) => {
  tug.addEventListener('click', (e) => {
    check[index].click();
  })
})


// drag drop events

// Make box draggable
$('.dragBox').draggable({
  revert: 'invalid',
  cursor: "move",
  cursorAt: { top: 50, left: 50 },
   drag: function(event, ui) {
      $('.dropBox')
   }
});

// allow drop on section
$( '.dropBox' ).droppable({
   accept: '.dragBox',
   drop: function(event, ui) {
    $(this)
    .append(ui.draggable.css({
      position: 'relative',
      left: '5px',
      top: '0px',
   }))
 }
});