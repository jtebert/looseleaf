//The template for adding delete buttons

$(function () {
    var options = {};


    $('.grid-stack').gridstack(options);

    off = 0;
    on = 1;
    maxId = 0;

    changeHand = on;

    /*==============================================================
     IMPORTANT:
     This looks like some initialization data for the boxes,
     this would need to be stored somewhere on our server and called
     to initialize the sizes and positions of the user's notes
     ================================================================*/
    this.serializedData = [
        {x: 0, y: 0, width: 2, height: 2, id: 1, color: 'F00', content_html: 'Cats'},

    ];





    //This just calls gridstack for the page
    this.grid = $('.grid-stack').data('gridstack');





    this.addBox = function (params) {
        changeHand = off;

        $('.grid-stack').gridstack();

        var grid = $('.grid-stack').data('gridstack');
        this.grid.addWidget($('<div><div id="' + params.id + '" class="grid-stack-item-content" style=" color: #000000; text-align: center; background-color: #'+params.color+';" /><div/>'), params.x, params.y, params.width, params.height, true, null, null, null, null, params.id);


        console.log('Saving Grid');
        this.saveGridADD(params);

        console.log('Loading Grid');
        this.loadGrid();

        changeHand = on;


        return false;
    }.bind(this);


    this.deleteBox = function (item) {
        self.widgets.remove(item);
        return false;
    };





    this.loadGrid = function () {
        console.log('Adding 1 Box');
        changeHand = off;

        console.log('Removing All Grids');
        this.grid.removeAll();

        var grid = $('.grid-stack').data('gridstack');
        grid.setAnimation(true);

        console.log('Rebuilding All Grids');
        var items = GridStackUI.Utils.sort(this.serializedData);
        _.each(items, function (node) {
//NEW STUFF HERE FOR THE DELETION BUTON!!!!!!!!!!!!!!!!!1111111
            this.grid.addWidget($('<div><div id="' + node.id + '" class="grid-stack-item-content"' +
                'style="color: #2c3e50; text-align: center; background-color: #'+node.color+';">' +
				'<button type="button" id="'+node.id+'" onclick="delete-note">Delete</button>'+
				'<button type="button" id="'+node.id+'" onclick="edit-note">Edit</button>'+
				'<br>'+node.content_html +
                '<div/><div/>'), node.x, node.y, node.width, node.height, false, null, null, null, null, node.id);
            console.log(node)
            /*
             if (Number(node.id)>maxId){
             maxId=Number(node.id);
             }
             */

        }, this);

        console.log('maxId = '+maxId.toString());

        changeHand = on;

        return false;
    }.bind(this);





    this.saveGrid = function () {
		
		NewData = [];
		Coords = [];
		
		
		gridDataVec = _.map($('.grid-stack > .grid-stack-item:visible'), function (el) {
							el = $(el);
							var node = el.data('_gridstack_node');
							return {
								x: node.x,
								y: node.y,
								width: node.width,
								height: node.height,
								id: node.id
							};
						}, this);

		var items = GridStackUI.Utils.sort(this.serializedData);
		
				_.each(items, function (node) {
			  
			   _.each(gridDataVec, function(gridData){				
					if (gridData.id==node.id){
						
						NewData.push({
							x: gridData.x,
							y: gridData.y,
							width: gridData.width,
							height: gridData.height,
							id: gridData.id,
							color: node.color,
							content_html: node.content_html
						});
						
						Coords.push({
							xVec: gridData.x,
							yVec: gridData.y,
							widthVec: gridData.width,
							heightVec: gridData.height,
							idVec=: gridData.id
						});
					}			   
			   }, this);
			}, this);
			this.serializedData=NewData;
			
			//TODO: Send out the new serialized data along with new coords.
			
			$('#saved-data').val(JSON.stringify(this.serializedData, null, '    '));
			
			modify_post(Coords);
			
			return false;
		}.bind(this);




    this.saveGridADD = function (params) {
            this.serializedData.push({
                x: params.x,
                y: params.y,
                width: params.width,
                height: params.height,
                id: params.id,
                color: params.color,
                content_html: params.content_html
            });
        $('#saved-data').val(JSON.stringify(this.serializedData, null, '    '));
        return false;
    }.bind(this);





    this.clearGrid = function () {
        changeHand = off;
        this.grid.removeAll();
        changeHand = on;
        return false;
    }.bind(this);





    $('#save-grid').click(this.saveGrid);
    $('#load-grid').click(this.loadGrid);
    $('#clear-grid').click(this.clearGrid);
	
	   $('#delete-note').click(delete_note(this.id));
	   $('#edit-note').click(edit_get(this.id));
	   $('#edit-note-submit').click(edit_post(this.id));

    $('#add-box').click(this.addBox);

    _this=this;




    $('.grid-stack').on('change', function (event, ui) {

        console.log('Boxes Were Changed');
        console.log('________' + changeHand.toString())
        if (changeHand == 1) {
            this.saveGrid();
        }
    }.bind(this));


    this.loadGrid();

    // Submit post on submit
    $('#note-form').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        console.log($('input[name="color"]:checked').val());
        console.log("form submitted!")  // sanity check
        create_post();
    });

	
	
	
	
    // AJAX for posting
    function create_post() {
        $.ajax({
            url: "/add_note/", // the endpoint
            type: "POST", // http method
            data: {
                content_raw: $('#id_content').val(),
                color: $('input[name="color"]:checked').val(),
                notebook: $('.notebook-id').attr('id'),
                // TODO: Add position/size
            }, // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#id_content').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                _this.addBox(json);
                console.log("success"); // another sanity check
            }.bind(this),

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

	
//DELETE NOTES - GET FUNCTION RIGHT HERE!!!!=======================================================================================
//==============================================================================================================================	
	
	    function delete_note(id) {
        $.ajax({
            url: "/delete_note/", // the endpoint
            type: "POST", // http method
            data: {
				id: id,
                notebook: $('.notebook-id').attr('id')
                // TODO: Add position/size
            }, // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#id_content').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
 
				var items = GridStackUI.Utils.sort(_this.serializedData);
				_.each(items, function (node,i) {
					if(id==node.id){
						_this.serializedData = items.splice(i, 1);
					}
				
				});

                _this.loadGrid();
                console.log("success"); // another sanity check
            }.bind(this),

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
//EDIT NOTES - GET FUNCTION RIGHT HERE!!!!=======================================================================================
//==============================================================================================================================	
		
	
	
		    function edit_post(id) {
        $.ajax({
            url: "/edit_note/", // the endpoint
            type: "POST", // http method
            data: {
				id: id,
                notebook: $('.notebook-id').attr('id')
                // TODO: Add position/size
            }, // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#id_content').val(''); // remove the value from the input
                 
				var items = GridStackUI.Utils.sort(_this.serializedData);
				_.each(items, function (node,i) {
					if(id==node.id){
						_this.serializedData[i] = json;
						_this.loadGrid();
					}
				
				});
				
                console.log("success"); // another sanity check
            }.bind(this),

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

	
	
	function edit_get(id) {
        $.ajax({
            url: "/edit_note/", // the endpoint
            type: "POST", // http method
            data: {
				id: id,
                // TODO: Add position/size
            }, // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#id_content').val(''); // remove the value from the input
                 
				//CREATE POPUP MODAL

				
                console.log("success"); // another sanity check
            }.bind(this),

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

	
	
//==============================================================================================================================	
//==============================================================================================================================	
	
	
	
	
	
	
	
	    function modify_post(Coords) {
        $.ajax({
            url: "/mod_note/", // the endpoint
            type: "POST", // http method
            data: Coords, // data sent with the post request

            // handle a successful response
            success: function (json) {
                 console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
	
	
	
	
//GET NOTES - GET FUNCTION RIGHT HERE!!!!=============================================================================================
//==============================================================================================================================	
	
		    function get_note(params) {
        $.ajax({
            url: "/mod_note/", // the endpoint
            type: "GET", // http method
            data: $('.notebook-id').attr('id'), // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#id_content').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
				_this.serializedData = json;
                _this.loadGrid();
                console.log("success"); // another sanity check
            }.bind(this),

            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
	
//==============================================================================================================================	
//==============================================================================================================================	
	
	
	
    $(function () {
        // This function gets cookie with a given name
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        var csrftoken = getCookie('csrftoken');

        /*
         The functions below will create a header with csrftoken
         */

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        function sameOrigin(url) {
            // test that a given url is a same-origin URL
            // url could be relative or scheme relative or absolute
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                    // Send the token to same-origin, relative URLs only.
                    // Send the token only if the method warrants CSRF protection
                    // Using the CSRFToken value acquired earlier
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    });



});