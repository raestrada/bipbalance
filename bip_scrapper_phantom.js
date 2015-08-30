var page = require('webpage').create();
page.open('http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('example.png');
  }
  phantom.exit();
});
