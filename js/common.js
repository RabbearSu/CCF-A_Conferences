/**
 * 根据id获取元素
 * @param id 元素的id
 * @returns {HTMLElement} 相应的元素
 */
function my$(id) {
    return document.getElementById(id)
}

/**
 * 创建鼠标进入事件，进入时根据li名称搜索论文标题并展示在创建的div中
 * @param allPapers 所有论文的对象
 */
function mouseOverHandle() {
    //获取关键字并找到关键字对应的论文列表
    var liName = this.innerText;

    if (my$(liName + "div")) {
        my$("box").removeChild(my$(liName + "div"));
    }
    var paperList = allPapers[liName];

    //创建div对象
    var divObj = document.createElement("div");
    divObj.className = "childBox";
    divObj.id = liName + "div";
    //限定显示的论文数量不超过15
    var paperLength = paperList.length < 15 ? paperList.length : 15;
    //遍历论文列表，为每一个标题创建一个p标签
    for (var i = 0; i < paperLength; i++) {
        var pObj = document.createElement("p");
        divObj.appendChild(pObj);
        //将关键字首字母大写
        var liNameUpper = liName.replace(liName[0], liName[0].toUpperCase());
        // 获取标题中关键词的位置
        var title = paperList[i];
        var start = title.toLowerCase().indexOf(liName);
        var end = start + liName.length;
        //将标题分割为三个部分
        var spanObj1 = document.createElement("span");
        spanObj1.innerText = title.slice(0, start);
        var spanObj2 = document.createElement("span");
        spanObj2.innerText = title.slice(end, title.length);
        var emObj = document.createElement("em");
        emObj.innerText = title.indexOf(liName) > 0 ? liName : liNameUpper;
        //添加入p标签
        pObj.appendChild(spanObj1);
        pObj.appendChild(emObj);
        pObj.appendChild(spanObj2);
    }
    my$("box").appendChild(divObj);
}

/**
 * 鼠标离开时删除创建的div
 */
function mouseOutHandle() {
    var liName = this.innerText;
    if (my$(liName + "div")) {
        my$("box").removeChild(my$(liName + "div"));
    }
}