
// 각 항목 컨텐츠 수
var Today_number =  1;
var Tomorrow_number = 1;
var Trouble_number = 1;

  function Today_button(){
    var id = "Today_text_";
    id += Today_number;
    var appendrow = "<tr><td>";
    appendrow += Today_number;
    appendrow += "</td>";
    appendrow += "<td><input  class='form-control' style='width : 100%;' type='text' name=";
    appendrow += "dc_content";
    appendrow += "> </td></tr>";

    $('#today_tbody').append(appendrow);
    Today_number += 1
  }

  function Today_delete(){
    $('#today_tbody > tr:last').remove();
    if(Today_number > 1){
      Today_number -= 1
    }
  }

    function Tomorrow_button(){
      var id = "Tomorrow_text_";
      id += Tomorrow_number;
      var appendrow = "<tr><td>";
      appendrow += Tomorrow_number;
      appendrow += "</td>";
      appendrow += "<td><input  class='form-control' style='width : 100%;' type='text' name=";
      appendrow += "tw_content";
      appendrow += "> </td></tr>";

      $('#tomorrow_tbody').append(appendrow);
      Tomorrow_number += 1
    }

    function Tomorrow_delete(){
      $('#tomorrow_tbody > tr:last').remove();
      if(Tomorrow_number > 1){
        Tomorrow_number -= 1
      }
    }

      function Trouble_button(){
        var id = "Trouble_text_";
        id += Trouble_number;
        var appendrow = "<tr><td>";
        appendrow += Trouble_number;
        appendrow += "</td>"
        appendrow += "<td><input class='form-control' style='width : 100%;' type='text' name=";
        appendrow += "s_content";
        appendrow += "> </td></tr>";

        $('#trouble_tbody').append(appendrow);
        Trouble_number += 1
      }

      function Trouble_delete(){
        $('#trouble_tbody > tr:last').remove();
        if(Trouble_number > 1){
          Trouble_number -= 1
        }
      }
    
    var selected_user = "";


$(document).on("click", "#choice-addressee-btn", function(){

    var w = w || window.open('/document/userlist', 'userlist', 'width=500, height=500');
})

function setUserInfo(obj)
{
  selected_user = JSON.parse(obj);
  $("#reciever").val(selected_user['name']);
  $("#reciever-name").html(selected_user['name']);
}



/* jy
  * 결재 완료
  * reportCompleleted
  * Description : 결재 완료 시 리포트 데이터 처리
  * input : none
  * output : none 
*/

$(document).on("click", "#submit-feedback-btn", reportCompleleted);
function reportCompleleted(){
  var status = $("input[name=dr_status]:checked").val();
  var feedback = $("#textarea-feedback").val();
  var pk = $(this).data('pk');
  var csrf = $(this).data('csrf');

  $.ajax({
    url : '/document/daily/read/' + pk,
    type : 'post',
    data : {
      'csrfmiddlewaretoken' : csrf,
      'pk' : pk,
      'feedback' : feedback,
      'status' : status
    }
  }).success(function(res){
    alert(res.msg);
    window.location.reload();
  });

  console.log(status, feedback, pk);
}

function reportWriteValidate(){
  if ( $("#reciever").val() == "" ){
    alert("수신자를 선택해 주세요.");
    $("#reciever").focus();
    return false; 
  }

  alert("일일 보고서 작성이 완료되었습니다.");
  return true;
}