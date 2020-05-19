# Today I Learned

## 2020/05/19

Given the `zero_downtime_migrations` gem is installed <br>
And I need to reset the database <br>
And redo my last 3 migrations

```bash
bin/rails db:drop db:create
SAFETY_ASSURED=1 bin/rails db:migrate --trace
bin/rails db:migrate:redo STEP=3
```

Given I have blog post records <br>
And I have a boolean column with a `NULL` values <br>
And I need to set all the `NULL` values to `FALSE`

```sql
UPDATE blog_posts
SET published = FALSE
WHERE published IS NULL
```