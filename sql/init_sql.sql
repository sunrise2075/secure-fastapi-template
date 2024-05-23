GRANT ALL PRIVILEGES ON DATABASE fastapi TO fastapi_user;

-- Switch to the fastapi database
\c fastapi

-- Create tables
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(256),
    email VARCHAR(256),
    is_admin BOOLEAN DEFAULT FALSE,
    hashed_password VARCHAR(512)
);

CREATE TABLE IF NOT EXISTS blacklist (
    token VARCHAR(512) NOT NULL,
    blacklist_on TIMESTAMP,
    id BIGSERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS task (
    task_id SERIAL PRIMARY KEY,
    task VARCHAR(250) NOT NULL,
    status VARCHAR(30) NOT NULL
);

-- Insert initial data into the task table
INSERT INTO task (task, status) VALUES ('Read an article on React.js', 'Done');
INSERT INTO task (task, status) VALUES ('Organize a meeting', 'Pending');