window.onload = init 


function init() {
    const btnNew = document.querySelector("#btnNew");
    const btnSave = document.querySelector("#btnSave");
    btnNew.addEventListener('click', function(e) {
        $("#newTaskModal").modal("show");
    })

    btnSave.addEventListener('click', function(e) {
        e.preventDefault();

        const taskTable = document.querySelector("#taskTable");
        let url = taskTable.getAttribute("url-save-task");

        const taskForm = document.querySelector("#taskForm");
        if (taskForm.reportValidity()) {
            const formData = new FormData(taskForm);
            
            fetch(url, {
                method:"POST",
                body: formData
            })
                .then((res) => {
                    return res.json()
                })
                .then((data) => {
                    location.reload()
                })
        }
        
    })
}