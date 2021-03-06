﻿
# Django

## Requirements
Build and deploy a web application representing Dogs and Cats. 
* Each dog and cat must have a name and birthday, and be linked to an Owner.
* Owners should be able to access dogs and cats via an API and carry out CRUD operations on their Dog and Cat.
* Owners should also be able to access dogs and cats via an admin interface.

## Postman - User Guide
1. Download Postman from https://www.getpostman.com/apps
2. Once Postman is launched, on the first page, click the link at the bottom that says `Take me straight to the app...`
![postman_skip_signup](http://i68.tinypic.com/sothuh.png)


3. Close any popup window that appears that will lead you to the screen as shown below. ![postman_home](http://i66.tinypic.com/24v71wz.png)

4. Copy any link from the section below as it is and paste it in the textfield that says `Enter request URL`. Note the request method (GET/POST/PUT/DELETE) against each link and ensure that the same method is selected from the dropdown. Click the `Send` button to get the response. Request to get all animals for user id 2 is as follows:
![postman_get_request](http://i66.tinypic.com/2ir241z.png)

5. This point and the next point will explain the usage of `POST/PUT/DELETE` requests. In case of `POST/PUT/DELETE` requests, once a method is selected from the dropdown, some additional options will appear. For all `POST/PUT/DELETE` requests, set `Content-Type : application/json` under the `Headers` section as shown below.
![postman_header](http://i64.tinypic.com/172y68.png)

6. Lastly, set the request body as described in the section below, for example, if you want to create an animal, set the request body as shown below:
![postman_body](http://i68.tinypic.com/vmvlp3.png)
Note that the `raw` radio button is selected prior to entering the request body. Sample request body for each type of method has been given in the **Using this Application** section below. Please ensure that the date format is exactly as shown there. 

7. Press the `Send` button to receive the response. Currently active ids of users are 2 and 3. Id of admin is 1. You can play around with the APIs to get ids of animals in order to perform update and delete operations.
8. **Changes made via the APIs will also be reflected in the admin panel**
## Using this Application
Navigate to http://crowdbotics-django-demo.herokuapp.com/ and login. Inside the admin panel if you're logged in as an admin, you can create a new user and assign them permissions to perform CRUD operations on an animal. 

Furthermore, if you're logged in as a user, you can directly perform CRUD operations on Animal.

## Using the APIs

Though the requirements mention creating APIs for the admin panel, the CRUD functionality has been handled directly via Django admin panel without the need of any additional APIs. 

However, they have been created as an additional task and can be used as follows by using postman. Please use `Content-Type = application/json` in the header and create raw request bodies for `POST`/`PUT`/`DELETE` requests:

* **GET**  `http://crowdbotics-django-demo.herokuapp.com/api/animals/<owner_id>/`
This api returns all the animals created by a user.

* **POST** `http://crowdbotics-django-demo.herokuapp.com/api/animals/create/`
This api allows the user to create a new animal. Sample request body can be as follows:
```
{	
	"owner_id":3,
	"animal_type":"dog",
	"birthday":"2018-03-24",
	"name":"super dog"
}
```

* **PUT** `http://crowdbotics-django-demo.herokuapp.com/api/animals/update/`
This api allows the user to update their animal. Sample request body can be as follows:
```
{	
	"animal_id":3,
	"animal_type":"cat",
	"birthday":"2017-02-20",
	"name":"supercat"
}
```

* **DELETE**  `http://crowdbotics-django-demo.herokuapp.com/api/animals/delete/`
This api allows the user to delete an animal. The sample request body can be as follows:
```
{	
	"animal_id":3
}
```
