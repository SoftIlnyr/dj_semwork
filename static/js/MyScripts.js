/**
 * Created by softi on 01.06.2016.
 */

$(document).ready(function () {
    var array = window.location.href.split("/");
    var id = array[array.length - 1];
    var url = id + "/checklike";
    var csrftoken = getCookie("csrftoken");

    console.log(url);
    $.ajax({
        url: url,
        method: 'POST',
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        data: {csrftoken: csrftoken},
        dataType: "json",
        success: function f(resp) {
            console.log('success');
            console.log(resp.status);
            if (resp.status == "yes") {
                obj = $("#" + id + "-like-yes");
                obj.id = id + "-like-" + "no";
                $(obj).removeClass('link-black').addClass('link-orange');
            }
        }
    });
});

function checkFollow(id) {
    console.log('invoke checkFollow');
    var oldurl = window.location.href.split("/");
    var newurlarray = oldurl.slice(0, 3);
    var url = newurlarray.join("/");
    url = url + "/users/" + id + "/checkfollow";
    var csrftoken = getCookie("csrftoken");
    console.log(url);
        $.ajax({
        url: url,
        method: 'POST',
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        data: {csrftoken: csrftoken},
        dataType: "json",
        success: function f(resp) {
            console.log('success');
            console.log('chechFollow: ' + resp.status);
            return resp;
        }
    });
}

$(document).ready(function () {
    console.log('follow by a');
    var obj = $("a[name='follow']");
    console.log(obj);
    id = obj.attr('id').split("-")[0];
    var resp = checkFollow(id);
    console.log('after checkFollow: ' + resp);
    //var oldurl = window.location.href.split("/");
    //console.log(oldurl);
    //var newurlarray = oldurl.slice(0, 3);
    //var url = newurlarray.join("/");
    //url = url + "/users/" + id + "/checkfollow";
    //console.log(url);
    //var csrftoken = getCookie("csrftoken");
    //
    //console.log(url);
    //$.ajax({
    //    url: url,
    //    method: 'POST',
    //    beforeSend: function (xhr, settings) {
    //        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //        }
    //    },
    //    data: {csrftoken: csrftoken},
    //    dataType: "json",
    //    success: function f(resp) {
    //        console.log('success');
    //        console.log(resp.status);
    //        if (resp.status == "yes") {
    //            obj.id = id + "-follow-" + "no";
    //            $(obj).removeClass('link-black');
    //        }
    //    }
    //});
});

$(document).ready(function () {
    var array = window.location.href.split("/");
    var id = array[array.length - 1];
    var url = id + "/checkfollow";
    var csrftoken = getCookie("csrftoken");

    console.log(url);
    $.ajax({
        url: url,
        method: 'POST',
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        data: {csrftoken: csrftoken},
        dataType: "json",
        success: function f(resp) {
            console.log('success');
            console.log(resp.status);
            if (resp.status == "yes") {
                obj = $("#" + id + "-follow-yes");
                obj.id = id + "-follow-" + "no";
                $(obj).removeClass('btn-soundcloud').addClass('btn-primary');
                $(obj).text("Following")
            }
        }
    });
});

function follow_button(obj) {
    console.log(obj.id);
    var user_id = obj.id.split("-")[0];
    var do_action = obj.id.split("-")[2];
    var csrftoken = getCookie("csrftoken");
    console.log(csrftoken);

    console.log(user_id);
    console.log(do_action);
    if (do_action == "yes") {
        var url = '/users/' + user_id + "/follow";

        $.ajax({
            url: url,
            method: 'POST',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: {csrftoken: csrftoken},
            dataType: "json",
            success: function f(resp) {
                console.log('success');
                console.log(resp);
                obj.id = user_id + "-follow-" + "no";
                $(obj).removeClass('btn-soundcloud').addClass('btn-primary');
                $(obj).text("Following")
            }
        });
    } else if (do_action == "no") {
        url = '/users/' + user_id + "/unfollow";
        $.ajax({
            url: url,
            method: 'POST',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: {csrftoken: csrftoken},
            dataType: "json",
            success: function f(resp) {
                console.log('success');
                console.log(resp["status"]);
                obj.id = user_id + "-follow-" + "yes";
                $(obj).removeClass('btn-primary').addClass('btn-soundcloud');
                $(obj).text("Follow")
            }
        });
    }
}

function follow_a(obj) {
    console.log(obj.id);
    var user_id = obj.id.split("-")[0];
    var do_action = obj.id.split("-")[2];
    var csrftoken = getCookie("csrftoken");
    console.log(csrftoken);

    console.log(user_id);
    console.log(do_action);
    if (do_action == "yes") {
        var url = '/users/' + user_id + "/follow";

        $.ajax({
            url: url,
            method: 'POST',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: {csrftoken: csrftoken},
            dataType: "json",
            success: function f(resp) {
                console.log('success');
                console.log(resp);
                obj.id = user_id + "-follow-" + "no";
                $(obj).removeClass('link-black');
            }
        });
    } else if (do_action == "no") {
        url = '/users/' + user_id + "/unfollow";
        $.ajax({
            url: url,
            method: 'POST',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: {csrftoken: csrftoken},
            dataType: "json",
            success: function f(resp) {
                console.log('success');
                console.log(resp["status"]);
                obj.id = user_id + "-follow-" + "yes";
                $(obj).addClass('link-black');
            }
        });
    }
}

function like(obj) {
    console.log(obj.id);
    var artwork_id = obj.id.split("-")[0];
    var do_action = obj.id.split("-")[2];
    var csrftoken = getCookie("csrftoken");
    console.log(csrftoken);

    console.log(artwork_id);
    console.log(do_action);
    if (do_action == "yes") {
        var url = '/artworks/' + artwork_id + "/like";

        $.ajax({
            url: url,
            method: 'POST',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: {csrftoken: csrftoken},
            dataType: "json",
            success: function f(resp) {
                console.log('success');
                console.log(resp);
                obj.id = artwork_id + "-follow-" + "no";
                $(obj).removeClass('link-black').addClass('link-orange');
            }
        });
    } else if (do_action == "no") {
        url = '/artworks/' + artwork_id + "/unlike";
        $.ajax({
            url: url,
            method: 'POST',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: {csrftoken: csrftoken},
            dataType: "json",
            success: function f(resp) {
                console.log('success');
                console.log(resp["status"]);
                obj.id = artwork_id + "-follow-" + "yes";
                $(obj).removeClass('link-orange').addClass('link-black');
            }
        });
    }
}


// using jQuery
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

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
