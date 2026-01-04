The app handles CRUD operations on tasks through views in apptodo.views: add new tasks via POST to /add/, mark complete at /complete/<int:task_id>/, delete at /delete/<int:task_id>/, and list completed ones at /completed/. Home.html renders a form for input, task list with status styling, and buttons for actions; Bootstrap ensures mobile responsiveness. 
Using this app, we can add y=our day to day to-do list and mark them completed if completed. Also we can check them in the ccompleted list. 


Set up project todo and app apptodo
In apptodo create a model task givenn title and status as fields. 
In Views: 
  Import Models
  In home it receeievss task
  add_task: using POST method the tite of the task is posted.
  delete_task: Using task id we can delete the task
  completed_task: All the completed tasks indicates all the items in Module (we use this since     we have already tagged the same in home)

We add home, adding task, deleting it completed task page will all be included in urls. 











  
