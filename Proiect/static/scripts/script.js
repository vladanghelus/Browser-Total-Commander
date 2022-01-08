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