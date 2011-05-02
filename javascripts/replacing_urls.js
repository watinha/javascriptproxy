window.onload = function(event){

  var script_elements = document.getElementsByTagName("script");
  var link_elements = document.getElementsByTagName("link");
  var image_elements = document.getElementsByTagName("img");
  var style_elements = document.getElementsByTagName("style");

  var url_parts = window.location.search.substring(5).split("/");
  var real_url = "";
  for (var cont = 0; cont < url_parts.length - 1; cont++)
    real_url += url_parts[cont] + "/"
  var local_url = window.location.protocol + "//" + window.location.host;
  
  for (var cont = 0; cont < link_elements.length; cont++){
    if (link_elements[cont].href.search(local_url) == 0)
      link_elements[cont].href = link_elements[cont].href.replace(local_url, real_url);
  }

  for (var cont = 0; cont < img_elements.length; cont++){
    if (img_elements[cont].src.search(local_url) == 0)
      img_elements[cont].src = img_elements[cont].src.replace(local_url, real_url);
  }

  for (var cont = 0; cont < script_elements.length; cont++){
    if (script_elements[cont].src.search(local_url) == 0)
      script_elements[cont].src = script_elements[cont].src.replace(local_url, real_url);
  }
};
