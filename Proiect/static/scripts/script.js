function createButton(side){
    let fileName = prompt("Numele fisierului pe care vreti sa il creati");
    if(fileName!=null && fileName!=''){
        $.ajax({
            url: '/create',
            type: 'POST',
            data: {
                fileName : fileName,
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