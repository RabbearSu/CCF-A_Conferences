var papers = document.getElementsByClassName("paper-item");

// console.log(papers.length);

for (var i =0;i<papers.length;i++){
    // console.log(papers[i].innerText);
    var emObj = papers[i].getElementsByTagName("em")[0];
    var brObj = papers[i].getElementsByTagName("br")[0];
    //删除作者
    papers[i].removeChild(emObj);
    //删除换行
    papers[i].removeChild(brObj);
    console.log(papers[i].innerText);
}