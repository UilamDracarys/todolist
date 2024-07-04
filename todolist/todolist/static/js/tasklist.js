window.onload = init 


function init() {

    const btnNew = document.querySelector("#btnNew");
    btnNew.addEventListener('click', function(e) {
        const taskModal = document.querySelector("#taskModal");
        const action = 'New'
        const title = taskModal.querySelector("#action");
        title.textContent = action;

        const actionType = document.querySelector("[name='action']");
        actionType.value = action;

        $("#taskModal").modal("show");
    });



    
    const btnSave = document.querySelector("#btnSave");
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
                    refreshTable();
                    showCustomToast(data.message, 'green');
                    $("#taskModal").modal("hide");
                })
        }

    })

    const btnCancel = document.querySelector("#btnCancel");
    btnCancel.addEventListener('click', function(e) {
        e.preventDefault();
        $("#taskModal").modal("hide");
    });

    const btnCancelDelete = document.querySelector("#btnCancelDelete");
    btnCancelDelete.addEventListener('click', function(e) {
        e.preventDefault();
        $("#deleteModal").modal("hide");
    });

    const taskTable = document.querySelector("#taskTable");
    taskTable.addEventListener('click', function(e) {
        if (e.target.closest('#btnEdit')) {
            const action = 'Edit';
            const row = e.target.parentElement.parentElement;

            const taskId = row.children[0].textContent.trim();
            const taskTitle = row.children[1].textContent.trim();
            const taskDesc = row.children[2].textContent.trim();
            const taskCategory = row.children[3].textContent.trim();

            const taskForm = document.querySelector("#taskForm");

            taskForm.querySelector("[name='action']").value = action;
            taskForm.querySelector("[name='taskId']").value = taskId;
            taskForm.querySelector("#title").value = taskTitle;
            taskForm.querySelector("#description").value = taskDesc;
            taskForm.querySelector("#category").value = taskCategory;

            const taskModal = document.querySelector('#taskModal');
            taskModal.querySelector("#action").textContent = action;

            $("#taskModal").modal("show");
        } else if (e.target.closest("#btnDelete")) {
            const row = e.target.parentElement.parentElement;

            const taskId = row.children[0].textContent.trim();
            const taskTitle = row.children[1].textContent.trim();

            const deleteForm = document.querySelector("#deleteForm");

            deleteForm.querySelector("[name='taskId']").value = taskId;
            deleteForm.querySelector("#taskId").textContent = taskId;
            deleteForm.querySelector("#taskTitle").textContent = taskTitle;

            $("#deleteModal").modal("show");
        }
    })

    const btnDeleteTask = document.querySelector("#btnDeleteTask");
    btnDeleteTask.addEventListener("click", function(e) {
        e.preventDefault();
        deleteTask();
    })
}

function deleteTask() {
    let url = '/tasks/delete_task'
    const form = document.querySelector("#deleteForm");
    const formData = new FormData(form);

    fetch(url, {
        method: "POST",
        body: formData,
    })
        .then((res) => {
            return res.json()
        })
        .then((data) => {
            $("#deleteModal").modal('hide');
            refreshTable();
            showCustomToast(data.message, 'green');
        })
        .catch((error) => {
            showCustomToast(error.message, 'red');
        })
}

function refreshTable() {
    let url = '/tasks/refresh_table'
    const taskTable = document.querySelector("#taskTable");

    fetch(url, {
        method: "GET"
    })
        .then((res) => {
            if (!res.ok) {
                throw new Error(res.statusText);
            }

            return res.text();
        })
        .then((data) => {
            taskTable.innerHTML = data;
        })
        .catch((error) => {
            console.error(error.message);
        })
}