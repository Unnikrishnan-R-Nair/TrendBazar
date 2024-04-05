window.addEventListener('resize', function(e){
    if (window.innerWidth >= 1024) {
      document.querySelector('.mobile-navbar-links').classList.remove('active');
      document.querySelector('.mobile-navbar-links').classList.add('hidden');
    }
  })

  document.querySelector('.hamburger-btn').addEventListener('click', function(e){
    document.querySelector('.mobile-navbar-links').classList.toggle('hidden');
    document.querySelector('.mobile-navbar-links').classList.add('active');
  })