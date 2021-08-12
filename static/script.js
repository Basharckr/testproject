// ------------Add player---------------------
function addPlayers() {

  $("#formAddplayer").validate({
    rules: {
      name: {
        required: true,
        minlength: 3,
      },
      email: {
        required: true,
        email: true,
      },
      country: {
        required: true,
      },
      game: {
        required: true,
      },
      score: {
        required: true,
      },
    },
    messages: {
      name: {
        required: "Please enter player name",
      },
      email: {
        required: "Please enter email address",
      },
      country: {
        required: "Enter country name",
      },
      game: {
        required: "Enter game name",
      },
      score: {
        required: "Enter score",
      },
    },
    submitHandler: (formAddplayer, e) => {
      e.preventDefault();
      $.ajax({
        url: "/addplayer/",
        data: $("#formAddplayer").serialize(),
        method: "post",

        success: function (response) {

          if (response == "success") {
         
            // $('#formAddplayer')[0].reset();

            $("#addPlayer").modal("hide");
            $("#tablediv").load(" #tablediv");
          }
        },
      });
    },
  });
}


// -----------Delete player------------
function deletePlayer(id) {
    var pk = id
  $.ajax({
    url: "/deleteplayer/"+pk+"/",
    method: "get",

    success: function (response) {

      if (response == "success") {
        console.log("delete success");
        $("#tablediv").load(" #tablediv");
      }
    },
  });
}
