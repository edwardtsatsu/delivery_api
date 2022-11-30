import uuid
from datetime import datetime

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
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )
    roles = db.relationship("Role", secondary=association_table, back_populates="users")


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_name = db.Column(db.String(100), unique=True, nullable=False)
    users = db.relationship("User", secondary=association_table, back_populates="roles")
