const loadData = function({url, data, method,header={}}){

    let resultData = {};
    $.ajax({
        url: url,
        type:method,
        data:data,
        headers: header,
        async: false, // 동기식으로 동작
        success:function(response){
            resultData = response;    
        },
        error:function(){
            alert("오류발생");
        }
    });
    return resultData;
}

