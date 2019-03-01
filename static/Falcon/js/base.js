function toggleRightMenu() {
    navMenuStatus = document.getElementById('mySidenav').style.width;
    if ( navMenuStatus == '0px' ) {
      document.getElementById('mySidenav').style.width = '321px';
      document.getElementById('magic_btn').style.display = 'none';
      document.getElementById("main").style.marginLeft = "321px";


    } else {
      document.getElementById('mySidenav').style.width = '0px';
      document.getElementById('magic_btn').style.display = 'block';
      document.getElementById("main").style.marginLeft = "0px";


    }
  }
