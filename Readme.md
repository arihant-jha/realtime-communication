### Setting up the database

#### Creating Tables

Users Table
- id
- name

Channels Table
- id
- name

Messages Table
- id
- channel_id
- sender_id
- message
- ctime

Membership Table
- id
- user_id
- channel_id


What about DMs?

Let's say we do it this way:

Messages Table
...
- receiver_id

In this case if I want to get DMs b/w user 1 and user 2, I can do a query like this:

```sql
SELECT * FROM messages WHERE (sender_id = 1 AND receiver_id = 2) OR (sender_id = 2 AND receiver_id = 1);
```

but if we model DMs also as a channel, then we can do a query like this:

```sql
SELECT * FROM messages WHERE channel_id IN (SELECT id FROM channels WHERE id = channel_id);
```
which we anyways had to write.


#### Inserting Test Data

#### 