# How to add or edit words/sentences
To add the new words/sentences or edit the registered words/sentences, follow the steps below.

## 1. Login to admin page
Access `"System URL" + /admin/` from a browser.

- If the "System URL" is "http://127.0.0.1:8000/" (Development Environment), access to the URL below.
```
http://127.0.0.1:8000/admin/
```

- Login with the username and password which specified at the system installation


## 2. Get the registered data & add or edit
Get the registered data (by exporting tables), and add or edit words/sentences.
If you already have the data to register (such as sample data), you can go to the next step.

1. Export the tables that need to be added or edited on the admin page  
<img src ="https://user-images.githubusercontent.com/42882840/80270765-ed9fbe00-86f5-11ea-9b75-14d4c7edd064.png" alt="export 01" width="250"> > 
<img src ="https://user-images.githubusercontent.com/42882840/80270767-ee385480-86f5-11ea-92fb-ca19a18f074b.png" alt="export 02" width="250"> > 
<img src ="https://user-images.githubusercontent.com/42882840/80270768-eed0eb00-86f5-11ea-8ac0-a9a67df2058a.png" alt="export 03" width="250"> 


2. Add or edit the exported files
- For the details about the contents of the files, see [Database](./database.md)


## 3. Register data
Import the data in the following order.
You may skip the registration step if the data is unchanged.

1. Register "WordClass" table  
<img src ="https://user-images.githubusercontent.com/42882840/80270793-0e681380-86f6-11ea-8804-5045e35f0fd3.png" alt="import 01" width="250"> > 
<img src ="https://user-images.githubusercontent.com/42882840/80270795-0f00aa00-86f6-11ea-8e47-b45a8a7bfc63.png" alt="import 02" width="250"> > 
<img src ="https://user-images.githubusercontent.com/42882840/80270796-0f994080-86f6-11ea-8e60-13772c2a17f1.png" alt="import 03" width="250"> > 
<img src ="https://user-images.githubusercontent.com/42882840/80270797-0f994080-86f6-11ea-9669-30d2d01bcceb.png" alt="import 04" width="250"> 

2. Register "Tag" table
    * Same as above

3. Register "Word" table
    * Same as above

4. Click "UPDATE_SYS_WORD_TABLES" button on the "Word" table  
<img src ="https://user-images.githubusercontent.com/42882840/80270814-39eafe00-86f6-11ea-9a9a-c37c644de894.png" alt="Update_Sys_Word_Tables 01" width="300">

5. Register "Example" table
    * Same as above

6. Register "Constituents" table
    * Same as above
