use fastapi;

create table if not exists users
(
    id              int auto_increment
        primary key,
    username        varchar(256)         null,
    email           varchar(256)         null,
    is_admin        tinyint(1) default 0 null,
    hashed_password varchar(512)         null
);

create table if not exists blacklist
(
    token        varchar(512) not null,
    blacklist_on datetime     null
);

create table if not exists task
(
    task_id int auto_increment
        primary key,
    task    varchar(250) not null,
    status  varchar(30)  not null
);

INSERT INTO fastapi.task (task_id, task, status) VALUES (1, 'Read an article on React.js', 'Done');
INSERT INTO fastapi.task (task_id, task, status) VALUES (2, 'Organize a meeting', 'Pending');
