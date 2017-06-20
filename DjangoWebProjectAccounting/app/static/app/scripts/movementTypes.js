
$(function () {

/* movementTypes */

  var movementTypesLoadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-movementType").modal("show");
      },
      success: function (data) {
        $("#modal-movementType .modal-content").html(data.html_form);
      }
    });
  };

  var movementTypesSaveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          alert("Operacion Exitosa!");
          $("#movementType-table tbody").html(data.html_movementType_list);
          $("#modal-movementType").modal("hide");
        }
        else {
          $("#modal-movementType .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create
  $(".js-create-movementType").click(movementTypesLoadForm);
  $("#modal-movementType").on("submit", ".js-movementType-create-form", movementTypesSaveForm);

  // Update 
  $("#movementType-table").on("click", ".js-update-movementType", movementTypesLoadForm);
  $("#modal-movementType").on("submit", ".js-movementType-update-form", movementTypesSaveForm);

  // Delete 
  $("#movementType-table").on("click", ".js-delete-movementType", movementTypesLoadForm);
  $("#modal-movementType").on("submit", ".js-movementType-delete-form", movementTypesSaveForm);






});