drop table if exists users;
    create table pm (
    id integer primary key autoincrement,
    domain text not null,
    username text not null,
    password text not null
);