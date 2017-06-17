/* accounting */
$(function () {

  /* functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-account").modal("show");
      },
      success: function (data) {
        $("#modal-account .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#account-table tbody").html(data.html_account_list);
          $("#modal-account").modal("hide");
        }
        else {
          $("#modal-account .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create
  $(".js-create-account").click(loadForm);
  $("#modal-account").on("submit", ".js-account-create-form", saveForm);

  // Update 
  $("#account-table").on("click", ".js-update-account", loadForm);
  $("#modal-account").on("submit", ".js-account-update-form", saveForm);

  // Delete 
  $("#account-table").on("click", ".js-delete-account", loadForm);
  $("#modal-account").on("submit", ".js-account-delete-form", saveForm);




});