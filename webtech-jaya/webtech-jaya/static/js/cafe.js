var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-contents");

function opentab(tabname){
    const tablinks = document.getElementsByClassName("tab-links");
    for(tablink of tablinks){
        tablink.classList.remove("active-link");
    }
    for(tabcontent of tabcontents){
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
    const tabContents = document.getElementsByClassName('tab-contents');
    for(let c of tabContents){
        c.classList.remove('active-tab')
    }

    var activeContent = document.getElementById(tabname);
    activeContent.classList.add('active-tab')
}