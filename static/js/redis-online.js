/**
 * Created by lenovo on 2017/2/15.
 */
 $(document).ready(function(){
      $("#select").click(function(){
        var a = $("#a").val();
        var b = $("#b").val();
        var c = $("#c").val();
        $.get("/redis/",{'a':a,'b':b,'c':c}, function(ret){
            $('#result').html(ret)
        })
      });
    });