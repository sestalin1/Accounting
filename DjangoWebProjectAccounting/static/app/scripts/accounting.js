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

/* accountTypes */

  var accountTypesLoadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-accountType").modal("show");
      },
      success: function (data) {
        $("#modal-accountType .modal-content").html(data.html_form);
      }
    });
  };

  var accountTypesSaveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#accountType-table tbody").html(data.html_accountType_list);
          $("#modal-accountType").modal("hide");
        }
        else {
          $("#modal-accountType .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create
  $(".js-create-accountType").click(accountTypesLoadForm);
  $("#modal-accountType").on("submit", ".js-accountType-create-form", accountTypesSaveForm);

  // Update 
  $("#accountType-table").on("click", ".js-update-accountType", accountTypesLoadForm);
  $("#modal-accountType").on("submit", ".js-accountType-update-form", accountTypesSaveForm);

  // Delete 
  $("#accountType-table").on("click", ".js-delete-accountType", accountTypesLoadForm);
  $("#modal-accountType").on("submit", ".js-accountType-delete-form", accountTypesSaveForm);






});