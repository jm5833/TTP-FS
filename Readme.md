**Tech Talent Pipeline Stage 2: Portfolio App**

**Features**
- Portfolio tracking based on real-time data provided by IEX
- Detailed transaction data useful for performing audits
- Account creation in order to manage your portfolio
- Purchasing of stocks to grow your portfolio

**Technologies Used:**  
- Linux  
- Django 
- Python    
- Crispy Forms
- IEX Api
- Bootstrap

**Installing/Running**
- Use `git clone https://github.com/jm5833/TTP-FS` to pull the project
- Run `python manage.py createsuperuser` to create an admin account
- Run `python manage.py runserver` to start the server
- *** Note: by default the server goes up at localhost:8000 ***

**Available Pages**
- login : log into an existing account
- register : create a new account 
- portfolio : view your portfolio of stocks as well as purchase new stocks
- transactions : view a list of all transactions ever made on the authenticated account
