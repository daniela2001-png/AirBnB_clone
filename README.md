# 0x00. AirBnB clone - The console

------------
<a href="https://ibb.co/hfv1q1B"><img src="https://i.ibb.co/tX5PdPq/CLON1.png" alt="CLON1" border="0"></a>

------------

# The console 

* **interactive** mode  😯:

------------

`

	$ ./console.py
	(hbnb) help

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit

	(hbnb) 
	(hbnb) 
	(hbnb) quit
	$`

------------

* **non-interactive** mode 😌:  

------------
`


	$ echo "help" | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$
	$ cat test_help
	help
	$
	$ cat test_help | ./console.py
	(hbnb)

	Documented commands (type help <topic>):
	========================================
	EOF  help  quit
	(hbnb) 
	$`



------------
# The general project 👋

------------
[![image general](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T154544Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ea1fa15ce7eafa6a77037f793682f22eb8b6685d7f018551ca63a54abe72d4a1 "image general")](http://https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T154544Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ea1fa15ce7eafa6a77037f793682f22eb8b6685d7f018551ca63a54abe72d4a1 "image general")


------------

* **Explanation**:  In the previous image we can see the struct of all our project with **Airbnb**, we done the first part of this that is the console, this console is made for the developer, here we can manage the **commands **:

------------

	👉 create
	👉 update
	👉 show
	👉 all
	👉 destroy

------------

And also the next part to this great scheme is use the miniframework of Python called **Flask  (back-end)**, We think that in this step, we will be manage Users related with the different amenitys of each room or house and then do the part of the **front-end**

------------
## Our classes 🙌🏻

------------

* **State**: 🌆
	Public class attributes:
	**name:** will be the name of teh state to

------------

* **City**: 🏙
	Public class attributes:
	**state_id**: string - empty string: it will be the State.id
	**name**: string - empty string

------------

* **Amenity** : ⭐️
	Public class attributes:
	**name**: string - empty string

------------


* **Place:** 🌎
	Public class attributes:
	**city_id:** string - empty string: it will be the City.id
	**user_id:** string - empty string: it will be the User.id
	**name:** string - empty string
	**description:** string - empty string
	**number_rooms:** integer - 0
	**number_bathrooms:** integer - 0
	**max_guest:** integer - 0
	**price_by_night:** integer - 0
	**latitude**: float - 0.0
	**longitude**: float - 0.0
	**amenity_ids**: list of string - empty list: it will be the list of Amenity.id later

------------


* **Review:** ✅
	Public class attributes:
	**place_id:** string - empty string: it will be the Place.id
	**user_id:** string - empty string: it will be the User.id
	**text:** string - empty string


------------
## Manage of the console 🌈:

------------

* **Example**: as you can see we manage the commands like this

<a href="https://ibb.co/Gk4wKSW"><img src="https://i.ibb.co/92kXF5b/ARIBNBIMAGETAVO.png" alt="ARIBNBIMAGETAVO" border="0"></a>

------------

## Unittests ✅
To run the unittests
```bash
./run_test.sh
```

------------

## By: <a href="https://github.com/daniela2001-png">Daniela Morales 🙋‍♀️</a>  & <a href="https://github.com/Athesto"> Gustavo Mejía 🙋‍♂️</a>

------------

