
//supplier
$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-supplier').modal('show');
			},
			success: function(data){
				$('#modal-supplier .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#supplier-table tbody').html(data.supplier_list);
					$('#modal-supplier').modal('hide');
				} else {
					$('#modal-supplier .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create
$(".show-form").click(ShowForm);
$("#modal-supplier").on("submit",".create-form",SaveForm);

//update
$('#supplier-table').on("click",".show-form-update",ShowForm);
$('#modal-supplier').on("submit",".update-form",SaveForm)

//delete
$('#supplier-table').on("click",".show-form-delete",ShowForm);
$('#modal-supplier').on("submit",".delete-form",SaveForm)
    });


//stock
$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-stock').modal('show');
			},
			success: function(data){
				$('#modal-stock .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#stock-table tbody').html(data.stock_list);
					$('#modal-stock').modal('hide');
				} else {
					$('#modal-stock .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create
$(".show-form").click(ShowForm);
$("#modal-stock").on("submit",".create-form",SaveForm);

//update
$('#stock-table').on("click",".show-form-update",ShowForm);
$('#modal-stock').on("submit",".update-form",SaveForm)

//delete
$('#stock-table').on("click",".show-form-delete",ShowForm);
$('#modal-stock').on("submit",".delete-form",SaveForm)
    });


//users
$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-user').modal('show');
			},
			success: function(data){
				$('#modal-user .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#user-table tbody').html(data.user_list);
					$('#modal-user').modal('hide');
				} else {
					$('#modal-user .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

	// create
	$(".show-form").click(ShowForm);
	$("#modal-user").on("submit",".create-form",SaveForm);

	//update
	$('#user-table').on("click",".show-form-update",ShowForm);
	$('#modal-user').on("submit",".update-form",SaveForm)

	//delete
	$('#user-table').on("click",".show-form-delete",ShowForm);
	$('#modal-user').on("submit",".delete-form",SaveForm)
	});


//Item units
$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-unit').modal('show');
			},
			success: function(data){
				$('#modal-unit .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#unit-table tbody').html(data.unit_list);
					$('#modal-unit').modal('hide');
				} else {
					$('#modal-unit .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

// create
$(".show-form").click(ShowForm);
$("#modal-unit").on("submit",".create-form",SaveForm);

//update
$('#unit-table').on("click",".show-form-update",ShowForm);
$('#modal-unit').on("submit",".update-form",SaveForm)

//delete
$('#unit-table').on("click",".show-form-delete",ShowForm);
$('#modal-unit').on("submit",".delete-form",SaveForm)
});

//Products/items
$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-item ').modal('show');
			},
			success: function(data){
				$('#modal-item .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#item-table tbody').html(data.item_list);
					$('#modal-item').modal('hide');
				} else {
					$('#modal-item .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

	// create
	$(".show-form").click(ShowForm);
	$("#modal-item ").on("submit",".create-form",SaveForm);

	//update
	$('#item-table').on("click",".show-form-update",ShowForm);
	$('#modal-item').on("submit",".update-form",SaveForm)

	//delete
	$('#item-table').on("click",".show-form-delete",ShowForm);
	$('#modal-item ').on("submit",".delete-form",SaveForm)
	});

//category
$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-category').modal('show');
			},
			success: function(data){
				$('#modal-category .modal-content').html(data.html_form);
			}
		});
	};

	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#category-table tbody').html(data.category_list);
					$('#modal-category').modal('hide');
				} else {
					$('#modal-category .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}

	// create
	$(".show-form").click(ShowForm);
	$("#modal-category").on("submit",".create-form",SaveForm);

	//update
	$('#category-table').on("click",".show-form-update",ShowForm);
	$('#modal-category').on("submit",".update-form",SaveForm)

	//delete
	$('#category-table').on("click",".show-form-delete",ShowForm);
	$('#modal-category').on("submit",".delete-form",SaveForm)
	});
