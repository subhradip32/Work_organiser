//Adding visible and not visisble feature to the btn main content
const list_of_object = ['create_task_maincontent','task_list_maincnt','analyse_task_maincnt'];
function togglebuttons(id){
    list_of_object.forEach(ele => {
        if(list_of_object.indexOf(ele) == id){
            document.getElementById(list_of_object[id]).style.display = "block";
        }else{
            document.getElementById(ele).style.display = "none";
        }
    });
}
document.getElementById("create_Task_btn").addEventListener('click',()=>{
    togglebuttons(0); 
});
document.getElementById("list_task_btn").addEventListener('click',()=>{
    togglebuttons(1);
});
document.getElementById("alz_task_btn").addEventListener('click',()=>{
    togglebuttons(2);
});

// preventing the form from auto submitting 
if ( window.history.replaceState ) {
    window.history.replaceState( null, null, window.location.href );
}