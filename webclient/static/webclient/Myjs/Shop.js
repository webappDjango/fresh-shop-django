$("#addtocart").one("click", function (e) { 
    e.preventDefault();
    productid = $(this).find("#addingProduct").html();
    $.ajax({
        type: "GET",
        url: "AddtoCart",
        data: { product_id: productid},
        success: function(respone) {
            $("#message").html(respone);
        }
    })
});
