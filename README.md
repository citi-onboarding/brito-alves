# brito-alves

# Symvoulos

[![CITi](https://imgur.com/Hnsy4U6.png)](http://citi.org.br)

Sýmvoulos is a credit consulting company and the goal of this project is to make a website that will bring more visibility to the business and, eventually, more customers.

## Links
+ [Mockup and visual ID]()
+ [Mockup Assets]()
+ [Google Drive]()
+ [Backlog]()

## Accounts


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have virtualenv installed on your machine. For that, simply run:

```
pip install virtualenv
```

### Installing

To run the project for the **first** time you must follow this steps:

Clone the GitHub repository

```
git clone https://github.com/citi-onboarding/balb.git
```

On the same folder, create a virtualenv environment

```
virtualenv -p python3 venv
```

Start the virtualenv

```
source venv/bin/activate
```

Enter the project folder

```
cd Symvoulos
```

Install the riquirements for the project

```
pip install -r requirements.txt
```

create **.env** file and copy


Now, create the migrations

```
python manage.py makemigrations
```

Then apply migrations

```
python manage.py migrate
```

Now, You are able to run the server
```
python manage.py runserver
```

Now, you can see the app running at [localhost:8000](http://localhost:8000)

## Running the project

To run the project (if already installed), just follow this simple commands:

First start the _virtualenv_

```
source venv/bin/activate
```

Then run the app with

```
python manage.py makemigrations
```

```
python manage.py migrate
```

```
python manage.py runserver
```

## Deployment

The project is deployed on Heroku with continuous deploy of branch _master_ and _develop_.

Production app: <https://symvoulos.herokuapp.com/>

Development app: <https://symvoulos-teste.herokuapp.com/>

## Built With

* **Django** - _for back-end_.
* **HTML, CSS, JS** - for _front-end_.

## GitHub

### Branches
They can be:


Their names must follow this template: `feature/branch-name`

### Commits
Must begin with the name of the branch you developed on, following the model: _“Feature(name-of-feature) rest of commit…”._

Must be simple and show briefly what you just did.

Ex: `git commit -m “Feature(banner-parallax) Added the parallax effect to the background”`

### Pull Requests
First, proceed with _rebase_:
1. _commit_ the changes on your branch
2. Go to the original branch (develop ou master) with `git checkout develop` (or master)
3. Run `git pull`
4. Go back to your branch with `git checkout "your-branch"`
5. Run `git rebase develop` (or master)
6. Follow the steps to conclude the _rebase_, solving conflicts and running `git add .` and then `git rebase --continue`
7. Whan finished rebasing, run `git push -f origin "your-branch"`. Now your Pull Request can be opened on GitHub.

If possible, use this template for the pull request body:
```
### Issue Name
**What I did:**

- First thing I did...

- Second thing I did...

**How I did:**

- Brief notes on how the issue was solved (technically)
