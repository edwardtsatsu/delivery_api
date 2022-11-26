import uuid
from datetime import datetime

import  flask_bcrypt

from sqlalchemy.dialects.postgresql import UUID

from src.extensions import db

association_table = db.Table(
    "user_roles",
    db.metadata,
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True),
    db.Column("role_id", db.ForeignKey("roles.id"), primary_key=True),
)


class User(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_number = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=False)
    password_hash = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    roles = db.relationship("Role", secondary=association_table, back_populates="users")

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship("User", secondary=association_table, back_populates="roles")
