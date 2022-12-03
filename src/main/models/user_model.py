import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from src.extensions import db

association_table = db.Table(
    "user_roles",
    db.metadata,
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True,index=True),
    db.Column("role_id", db.ForeignKey("roles.id"), primary_key=True,index=True),
)


class User(db.Model):
    """User Model for storing user related details"""

    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,index=True)
    email = db.Column(db.String(255), unique=True, nullable=False,index=True)
    phone_number = db.Column(db.String(100), unique=True, nullable=False,index=True)
    username = db.Column(db.String(50), unique=False,index=True)
    password = db.Column(db.String(255), nullable=False,index=True)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        index=True,
    )
    roles = db.relationship("Role", secondary=association_table, back_populates="users")


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,index=True)
    role_name = db.Column(db.String(100), unique=True, nullable=False,index=True)
    users = db.relationship("User", secondary=association_table, back_populates="roles")
