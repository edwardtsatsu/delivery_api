import uuid

from sqlalchemy.dialects.postgresql import UUID

from ...extensions import db


class OtpCode(db.Model):

    __tablename__ = "otp_codes"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"))
    code = db.Column(db.String(80), unique=False, nullable=False)
    generated_at = db.Column(db.DateTime, unique=False, nullable=False)
