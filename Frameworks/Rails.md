# Rails

## CLI

Scaffold a User model and controllers

    rails generate scaffold User first_name:string last_name:string email:string

Generate a an Article with Comments

    rails generate model Article title:string text:text 
    rails generate model Comment commenter:string body:text article:references