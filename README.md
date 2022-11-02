# test_login

This is a test example, it should not be considered for a real project, since it has security problems and bad practices.

Usage

## Step 1

## Run Image
```
docker run --rm -it -p 8000:8000 -p 8080:8080 -p 9080:9080 dgraph/standalone:v20.11.0
```

## Step 2 - Add a GraphQL Schema
standing on /schema run
```
curl -X POST localhost:8080/admin/schema --data-binary '@schema.graphql'
```

## Step 3 - Install playground
https://github.com/graphql/graphql-playground


## Step 4 - Create mutation in Graphql

Open playground with point http://localhost:8080/graphql and have mutation:

```
mutation {
  adduser(input: [
    {name: "Isa Navas", password: "Hola12", email: "correo@correo.com"},
  ]) {
    numUids
    user {
      name
      userID
    }
  }
}
```

## Step 5 run python
### 5.1.Create environment
```
python3 -m venv venv
```

### 5.2.Activate environment
Unix or MacOS:
```
source venv/bin/activate
```

Windows:
```
source venv/Scripts/activate.bat
```

### 5.3.Install `requirements.txt`
```
pip3 install -r requirements.txt
```

### 5.4.Start App
```
python3 menu.py
```