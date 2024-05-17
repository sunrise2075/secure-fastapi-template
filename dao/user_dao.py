from datetime import datetime
from typing import Optional

import mysql.connector
from mysql.connector import errorcode

from dao.base_dao import BaseDao
from models.user_model import User, UserInDB

"""
    middleware for accessing the user database and performing CRUD operations on the user table
"""


class UserDAO(BaseDao):

    def create_user(self, user: User):
        cursor = self.cnx.cursor()
        add_user = ("INSERT INTO users "
                    "(id, username, email, is_admin, hashed_password) "
                    "VALUES (%s, %s, %s, %s, %s)")
        data_user = (user.id, user.username, user.email, user.is_admin, user.hashed_password)
        cursor.execute(add_user, data_user)
        self.cnx.commit()
        cursor.close()

    def get_user_by_username(self, username: str) -> Optional[UserInDB]:
        cursor = self.cnx.cursor()
        query = ("SELECT id, username, email, is_admin, hashed_password "
                 "FROM users "
                 "WHERE username = %s")
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return None
        return UserInDB(**dict(zip(['id', 'username', 'email', 'is_admin', 'hashed_password'], row)))

    def get_last_user_id(self) -> int:
        cursor = self.cnx.cursor()
        query = "SELECT MAX(id) FROM users"
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return 0
        return row[0]

    def blacklist_token(self, token: str):
        """
        Add a token to the blacklist table with the current timestamp
        """
        try:
            cursor = self.cnx.cursor()
            query = "INSERT INTO blacklist (token, blacklist_on) VALUES (%s, %s)"
            timestamp = datetime.now()

            cursor.execute(query, [token, timestamp])

            self.cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(err)

    def is_token_blacklisted(self, token: str) -> bool:
        """
        Check if a token exists in the blacklist table
        """
        try:
            cursor = self.cnx.cursor()
            query = "SELECT COUNT(*) FROM blacklist WHERE token = %s"
            values = (token,)
            cursor.execute(query, values)
            result = cursor.fetchone()[0]
            cursor.close()
            return result > 0
        except mysql.connector.Error as err:
            print(err)
            return False
