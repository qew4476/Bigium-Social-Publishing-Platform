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
                if (result["code"] === 200){
                    console.log(result);
                }else {
                    console.log("error",result);
                    console.log(title)
                }
            }

        })
    });
}