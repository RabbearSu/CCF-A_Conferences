var main = document.getElementById("main-container");

var entrys = main.getElementsByTagName("strong");

var papers = [];
for (var i=0;i<entrys.length;i++){
    papers[papers.length] = entrys[i].innerText;
    console.log(entrys[i].innerText);
}

