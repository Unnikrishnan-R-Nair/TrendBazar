
document.querySelectorAll('.title-text').forEach((eachTitle)=>{

    let title = eachTitle.innerHTML.toLowerCase()

    if (title.length > 30) {
        
        let newtitle = title.slice(0, 26) + '...';
        eachTitle.innerHTML = newtitle;
        
    }else {

        eachTitle.innerHTML = title;

    }
    
    eachTitle.style.textTransform = 'capitalize';  

});
