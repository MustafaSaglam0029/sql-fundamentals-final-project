from sqlalchemy import Column, Enum, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mandate(Base):
    __tablename__ = 'mandate'

    business_partner_id = Column(String(25), unique=True, nullable=True)
    mandate_status = Column(Enum('Y', 'N', 'R', name='mandate_status_types_enum'), nullable=True)
    collection_frequency = Column(Enum('D', 'I', 'W', 'M', name='collection_frequency_types_enum'), nullable=True)
    brand = Column(Text, nullable=False)
    row_update_datetime = Column(TIMESTAMP, nullable=False)
    row_create_datetime = Column(TIMESTAMP, nullable=False)
    changed_by = Column(Text, nullable=True)
    mandate_id = Column(String(10), primary_key=True)
    collection_type = Column(String(5), nullable=False)
    metering_consent = Column(String(50), nullable=False)
