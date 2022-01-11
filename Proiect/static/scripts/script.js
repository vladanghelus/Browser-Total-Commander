function createFileButton(side){
    let fileName = prompt("Numele fisierului:");
    if(fileName!=null && fileName!=''){
        $.ajax({
            url: '/create',
            type: 'POST',
            data: {
                fileName : fileName,
                side : side,
                type : 'file'
            },
            success: function (response) {
                setTimeout(
                    function() 
                    {
                       location.replace("/");
                    }, 0001);    
            },
            error: function (response) {
                
            }
        });
    }
}

function createFolderButton(side){
    let folderName = prompt("Numele folderului:");
    if(folderName!=null && folderName!=''){
        $.ajax({
            url: '/create',
            type: 'POST',
            data: {
                fileName : folderName,
                side : side,
                type : 'folder'
            },
            success: function (response) {
                setTimeout(
                    function() 
                    {
                       location.replace("/");
                    }, 0001);    
            },
            error: function (response) {
                
            }
        });
    }
}

function back(side){
    let path = ''
    if(side == 'A'){
        path = document.getElementById('caleA').innerHTML;
    }
    else if (side == 'B'){
        path = document.getElementById('caleB').innerHTML;
    }
    if(path == "Files")
        alert("Nu puteti merge inapoi!");
    else{
        $.ajax({
            url: '/back',
            type: 'POST',
            data: {
                side : side
            },
            success: function (response) {
                setTimeout(
                    function() 
                    {
                        location.replace("/");
                    }, 0001);    
            },
            error: function (response) {
                
            }
        });
    }
}

function setCheckboxId(){
    let list = document.getElementById('listA').getElementsByTagName('input');
    let i = 0;
    for(i=0; i<list.length; ++i){
        list[i].setAttribute("id", (i+1).toString()+'A');
    }
    list = document.getElementById('listB').getElementsByTagName('input');
    for(i=0; i<list.length; ++i){
        list[i].setAttribute("id", (i+1).toString() +'B');
    }
    // set an id almost identical for <a> tag to be able to get file's name
    list = document.getElementById('listA').getElementsByTagName('a');
    for(i=0; i<list.length; ++i){
        list[i].setAttribute("id", (i+1).toString() +'AF');
    }

    list = document.getElementById('listB').getElementsByTagName('a');
    for(i=0; i<list.length; ++i){
        list[i].setAttribute("id", (i+1).toString() +'BF');
    }
}

function deleteSelection(side){
    // check if it is at least one checkbox checked
    let checkboxList = document.getElementById('list'+side).getElementsByTagName('input');
    let ctchecked = 0;
    let forDeletingList=[];
    for(i=0; i<checkboxList.length; ++i)
        if(checkboxList[i].checked == true){
            ctchecked++;
            forDeletingList[ctchecked] = document.getElementById(checkboxList[i].getAttribute('id') + 'F').innerHTML;
        }
    if(ctchecked == 0)
        alert("Selectati cel putin un element pentru a-l sterge!");
    else{
        $.ajax({
            url: '/delete',
            type: 'POST',
            data: {
                side : side,
                listToDelete : forDeletingList 
            },
            success: function (response) {
                setTimeout(
                    function() 
                    {
                        location.replace("/");
                    }, 0001);    
            },
            error: function (response) {
                
            }
        });
    }
}

function copySelection(side){
    let checkboxList = document.getElementById('list'+side).getElementsByTagName('input');
    let ctchecked = 0;
    let forCopyList=[];
    for(i=0; i<checkboxList.length; ++i)
        if(checkboxList[i].checked == true){
            ctchecked++;
            forCopyList[ctchecked] = document.getElementById(checkboxList[i].getAttribute('id') + 'F').innerHTML;
        }
    if(ctchecked == 0)
        alert("Selectati cel putin un element pentru a-l copia!");
    else{
        $.ajax({
            url: '/copy',
            type: 'POST',
            data: {
                side : side,
                listToCopy : forCopyList 
            },
            success: function (response) {
                setTimeout(
                    function() 
                    {
                        location.replace("/");
                    }, 0001);    
            },
            error: function (response) {
                
            }
        });
    }
}

function moveSelection(side){
    let checkboxList = document.getElementById('list'+side).getElementsByTagName('input');
    let ctchecked = 0;
    let oldName = '';
    let forCopyList=[];
    for(i=0; i<checkboxList.length; ++i)
        if(checkboxList[i].checked == true){
            ctchecked++;
            forCopyList[ctchecked] = document.getElementById(checkboxList[i].getAttribute('id') + 'F').innerHTML;
        }
    if(ctchecked == 0)
        alert("Selectati cel putin un element pentru a-l muta!");
    else if (ctchecked == 1){
        oldName = forCopyList[1]
        forCopyList[1] = prompt("Noul nume:", forCopyList[1]);
    }
    if(ctchecked != 0 ){
        $.ajax({
            url: '/move',
            type: 'POST',
            data: {
                side : side,
                listToCopy : forCopyList,
                oldName : oldName
            },
            success: function (response) {
                setTimeout(
                    function() 
                    {
                        location.replace("/");
                    }, 0001);    
            },
            error: function (response) {
                
            }
        });
    }
}

function edit(side){
    let checkboxList = document.getElementById('list'+side).getElementsByTagName('input');
    let ctchecked = 0;
    let fileName
    for(i=0; i<checkboxList.length; ++i)
        if(checkboxList[i].checked == true){
            ctchecked++;
            fileName = document.getElementById(checkboxList[i].getAttribute('id') + 'F').innerHTML;
        }
    if(ctchecked == 0)
        alert("Selectati un fisier text!");
    else if(ctchecked > 1)
        alert("Nu se poate edita mai mult de un fisier")
    else{
        $.ajax({
            url: '/edit',
            type: 'POST',
            data: {
                side : side,
                fileName : fileName
            },
            success: function(response){
                document.getElementById("inputEdit").innerHTML = response;
                document.getElementById("inputEdit").setAttribute('style', 'display:block');
            },
            error: function(response){
                console.log(response)
            }
        });
    }
}