"use strict";


var editingWishlistName = false; //indicates if the name should be displayed in a text input or a header

$(document).ready(function() {

    $("#wishlistNameInput").hide(); //input is initially hidden

    //toggles editing of wishlist name
    $("#changeNameButton").click(function() {

        editingWishlistName = !editingWishlistName;
        $(this).text(editingWishlistName ? "Save" : "Change");

        //name should be an input field if editing is enabled
        if(editingWishlistName) {

            $("#wishlistName").hide();
            $("#wishlistNameInput").show();

            //show current title in input box
            let wishlistName = $("#wishlistName").text();
            $("#wishlistNameInput").val(wishlistName);

        }
        else {

            $("#wishlistName").show();
            $("#wishlistNameInput").hide();

            //set header to display new title
            let wishlistName = $("#wishlistNameInput").val();
            $("#wishlistName").text(wishlistName);

        }

    });

});