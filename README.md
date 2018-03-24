# Django

## Requirements
Build and deploy a web application representing Dogs and Cats. 
* Each dog and cat must have a name and birthday, and be linked to an Owner.
* Owners should be able to access dogs and cats via an API and carry out CRUD operations on their Dog and Cat.
* Owners should also be able to access dogs and cats via an admin interface.

## Using this Application
Navigate to http://crowdbotics-python-demo.herokuapp.com/ and login. Inside the admin panel if you're logged in as an admin, you can create a new user and assign them permissions to perform CRUD operations on an animal. 

Furthermore, if you're logged in as a user, you can directly perform CRUD operations on Animal.

## Using the APIs

Though the requirements mention creating APIs for the admin panel, the CRUD functionality has been handled directly via Django admin panel without the need of any additional APIs. 

However, they have been created as an additional task and can be used as follows by using postman. Please use `Content-Type = application/json` in the header and create raw request bodies for `POST`/`PUT`/`DELETE` requests:

* **GET**  `/api/animals/<owner_id>`
This api returns all the animals created by a user.

* **POST** `/api/animals/create/`
This api allows the user to create a new animal. Sample request body can be as follows:
```
{	
	"owner_id":3,
	"animal_type":"dog",
	"birthday":"2018-03-24",
	"name":"super dog"
}
```

* **PUT** `/api/animals/update/`
This api allows the user to update their animal. Sample request body can be as follows:
```
{	
	"animal_id":3,
	"animal_type":"cat",
	"birthday":"2017-02-20",
	"name":"supercat"
}
```

* **DELETE**  `/api/animals/delete/`
This api allows the user to delete an animal. The sample request body can be as follows:
```
{	
	"animal_id":3
}
```
