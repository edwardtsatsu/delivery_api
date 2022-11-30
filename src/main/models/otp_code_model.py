import uuid

from sqlalchemy.dialects.postgresql import UUID

from ...extensions import db


class OtpCode(db.Model):

    __tablename__ = "otp_codes"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = db.Column(db.String(80), unique=False, nullable=False)
    verified = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    phone_number = db.Column(db.String, unique=False, nullable=False)
    generated_at = db.Column(db.DateTime, unique=False, nullable=False)
