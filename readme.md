### basic setup info for the backend 
1. make sure there is python on the device `pip3 --version`
2. download the requirements `pip3 install -r requirements.txt`
3. make sure to install `uvicorn` by doing `pip3 install uvicorn`
4. navigate to backend/src folder 
5. run the server `uvicorn main:app --reload`