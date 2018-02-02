## Update

```sh
# Update a client document's redirecturi
db.clients.updateOne({"_id" : "1234"}, {$set: {"redirecturi": "http://localhost:14000/appauth/token"} })
```
