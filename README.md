![Codecov](https://img.shields.io/codecov/c/github/tamarammt/vet)

## Project Title: 

### **Veterinary Clinic Website**

## Project Description:

This project is a website designed for a veterinary clinic. It encompasses several key features:

**About Us Section:** This section offers insights into the clinic's background, mission, and team, helping users get to know the clinic better.

**Contact Section:** Users can easily reach out to the clinic by sending emails or inquiries through the contact section.

**Services Description:** The website provides a comprehensive section that details the range of services offered by the veterinary clinic, making it easier for visitors to understand what's available.

##**Blog:** The website offers veterinarians the ability to register and log in, providing them with access to a dedicated blog platform. Within this blog, veterinarians can create, edit, and delete their posts, each of which can be categorized for better organization. Additionally, veterinarians are provided with individual profiles that feature biographical information, and a user-friendly dashboard where they can efficiently manage their blog posts.

Additional information for GitHub project description:

This project is built using a variety of web development technologies, including Django, Tailwind CSS and JavaScript.
To contribute to the project, please fork the repository and create a pull request with your changes.



## Getting Started

### Step 1: Fork / Clone


```
mkdir -p ~/vet
cd ~/vet
```


Fork or clone this repo:

```
git clone https://github.com/TamaraMMT/vet.git
```


### Step 2: Create a Virtual Environment

```
python3.10 -m venv venv
```

- You can use _any_ virtual environment manager (poetry, pipenv, virtualenv, etc)



### Step 3: Activate Virtual Environment
_macOS/Linux_

```
source venv/bin/activate
```

_Windows_

```
.\venv\Scripts\activate
```



### Step 4: Install Requirements


```
$(venv): python -m pip install pip --upgrade
$(venv): python -m pip install -r requirements.txt
```

- `$(venv)` is merely denoting the virtual environment is activated




### Step 5: Setup your `.env`

```
DJANGO_SECRET_KEY = 123456


#  0 = false       1 = True
DEBUG = 0


# setup emails contact
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '*************'
EMAIL_HOST_PASSWORD = '*************'
EMAIL_PORT = '8888'

EMAIL_TO =[input your email for send the emails]
```


## Welcome Contributions!

We value and appreciate **contributions** from the community. If you have suggestions to improve this project, please feel free to open a pull request.

> Please submit your pull request to the develop branch.
Thank you for helping to make this project better!


## Project Status

This project is still under construction.



<img src="https://github.com/TamaraMMT/vet/blob/main/images%20README/contact.png?raw=true" height="120" width="120" >
<img src="https://github.com/TamaraMMT/vet/blob/main/images%20README/dashboard.png?raw=true" height="120" width="120" >
<img src="https://github.com/TamaraMMT/vet/blob/main/images%20README/logged%20out.png?raw=true" height="120" width="120" >
<img src="https://github.com/TamaraMMT/vet/blob/main/images%20README/services.png?raw=true" height="120" width="120" >


