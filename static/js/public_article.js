window.onload = function (){
    $("#submit-btn").click(function (event){
       event.preventDefault();
        let title = $("input[name='title']").val();
        let category = $("#category-select").val();
        let content = quill.getSemanticHTML();
        $.ajax("/write/", {
            method: "POST",
            data: {
                title: title,
                category: category,
                content: content
            },
            success:function (result){
                if(result['code'] === 200){
                    let article_id = result['data']['article_id'];
                    console.log(article_id);
                    window.location = "/article/" + article_id;
                }else{
                    alert(result['message']);
                }
            }

        })
    });
}