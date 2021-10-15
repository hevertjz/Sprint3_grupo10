
//searhbox

const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const inputBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");
let linkTag = searchWrapper.querySelector("a") //pendiente que hay varios a en el archivo//
let webLink;

inputBox.onkeyup = (e)=>{
    let userData= e.target.value;
    let emptyArray = [];
    if(userData){
        icon.onclick = () =>{
            webLink ="https://www.google.com/search?q=${userData}";
            linkTag.setAttribute ("herf", webLink)
            linkTag.click();
        }
        emptyArray = suggestions.filter((data) =>{
            return
            data.toLocalLowerCase().startsWith(userData.toLocalLowerCase());
        
        });
        emptyArray = emptyArray.map((data)=>{
            return data= "<li>${data}</li>"
        });

        searchWrapper.classList.add("active");
        showSuggestions(emptyArray);
        let allList = suggBox.querySelectorAll("li");
        for (let i=0; i< allList.length; i++){
            allList[i].setAttribute("onclick", "select(this)");
        }
        
        
    }else{
        searchWrapper.classList.remove("active");}

    function select(element){
        let selectData = element.texContent;
        inputBox.value = selectData;
        icon.onclick = ()=>{
            webLink = "https://www.google.com/search?q=${userData}";
            linkTag.setAttribute("href", webLink);
            linkTag.click();
        }
        searchWrapper.classList.remove("active");
    }


    function showSuggestions(list){
        let listData;
        if(!list.length){
            userValue = inputBox.value;
            listData = "<li>${userValue}</li>";
        }else{
            listData=list.join("")
        }
        suggBox.innerHTML=listData; //min9:16
    }
}

