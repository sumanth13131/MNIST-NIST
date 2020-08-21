//While Running the .ipynb in colab use this below lines to avoid connection error while Training(for long time in Tunning)

function ClickConnect(){
console.log("Working"); 
document
  .querySelector('#top-toolbar > colab-connect-button')
  .shadowRoot.querySelector('#connect')
  .click() 
}
setInterval(ClickConnect,60000)
