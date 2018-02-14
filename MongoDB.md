## Database

```sh
# View current database
db

# Use database named "test"
use test
```

## Create

```sh
# Create a new user
db.users.insert({"email": "a", "password": "asdfasdf"})
```

## Read

```sh
# Find all users
db.users.find()
```

## Update

```sh
# Update a client document's redirecturi
db.clients.updateOne({"_id" : "1234"}, {$set: {"redirecturi": "http://localhost:14000/appauth/token"} })
```

# Delete

```sh
# Delete all users. BE CAREFUL!!!
# db.users.remove({})
```
