eel.expose(set_readed);
function set_readed(userName, state){
  if (state == "in") {
    document.getElementById("idm").textContent = userName + "さん、お帰りなさい！";
  } else {
    document.getElementById("idm").textContent = userName + "さん、また今度！";
  }
  document.getElementById("status").classList.remove("icono-sync");
  document.getElementById("status").classList.add("icono-check");
}

eel.expose(remove_readed);
function remove_readed(){
  document.getElementById("idm").textContent = "カード待機中...";
  document.getElementById("status").classList.remove("icono-check");
  document.getElementById("status").classList.add("icono-sync");
}

eel.expose(set_not_found);
function set_not_found(){
  document.getElementById("idm").textContent = "未登録のカードです";
  document.getElementById("status").classList.remove("icono-sync");
  document.getElementById("status").classList.add("icono-cross");
}

eel.expose(remove_not_found);
function remove_not_found(){
  document.getElementById("idm").textContent = "カード待機中...";
  document.getElementById("status").classList.remove("icono-cross");
  document.getElementById("status").classList.add("icono-sync");
}

eel.start_read()
