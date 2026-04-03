# Indexing

## We use index for faster searching and retrieval of data. An index is a data structure that allows us to quickly locate and access the data in a database table. It works like a book index, where you can quickly find the page number of a specific topic.

To create an index in a database, we can use the following syntax:

```sql
CREATE INDEX index_name ON table_name (column_name);
```

We use explain query plan select to see how the database engine is executing a query and whether it is using an index or not. This command provides insights into the query execution plan, which can help us optimize our queries for better performance.

Syntax for explain query plan:

```sql
EXPLAIN QUERY PLAN SELECT * FROM table_name WHERE column_name = value;
```
This will show us whether the query is using an index or performing a full table scan, and we can use this information to make informed decisions about indexing and query optimization.
 