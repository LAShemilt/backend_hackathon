
## Configure
This includes a setup.sh script that does the following:
- clones the main branch of scicat-backend-next
- Copies .env into scicat-backend-next, needed to configure mongo
- Copies funcitonalAccounts.json.example into root
- calls npm install

The functionalAccounts.json.example folder in the root of this project contains users and passwords. Please change the passwords. Save this and the setup.sh below will copy them.

To start, set setup.sh to executable and run it.

```
chmod +x setup.sh
./setup.sh
```

## Configure (Optional)
The hackathon will use jupyter and the httpx library. Many developers will have all they need in an environment, but just in case here are some commands to get people started

```
conda create -n 'hackathon' python=3.10
conda activate hackathon
conda install jupyterlab
pip install -r requirements.txt
```

Now that you have this setup, you can launch a jupyter with:
```
jupyter lab
```

## Launch 
Now cd into scicat-backend-next and run the server.

```
docker-compose up -d
cd scicat-backend-next
npm run start:dev
```

