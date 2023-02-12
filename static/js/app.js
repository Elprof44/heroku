
function demo(led,idm)
{   console.log(led)
    console.log(idm)
    var et = document.getElementById(led);
    var col = document.getElementById(idm);

    if (et.innerHTML=='OFF')
    {
        var xhttp = new XMLHttpRequest();
        xhttp.open('GET','login/'+led+'/1/led',true);
        xhttp.send();

        et.innerHTML='ON';
        col.setAttribute("src","static/img/alumer.png")
    }else{

        var xhttp = new XMLHttpRequest();
        xhttp.open('GET','login/'+led+'/0/led',true);
        xhttp.send();

        et.innerHTML='OFF';
        col.setAttribute("src","static/img/eteindre.png")

    }
}
function Onbtm()
{}



// setInterval( load(),2000)

// function load()
// {
//     window.location.reload();
// }