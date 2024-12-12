from sqlalchemy import Column, String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Meter(Base):
    __tablename__ = 'meter'

    business_partner_id = Column(String(25), ForeignKey('mandate.business_partner_id'), nullable=True)
    connection_ean_code = Column(String(50), unique=True, nullable=True)
    grid_company_code = Column(String(25), nullable=True)
    oda_code = Column(String(25), nullable=True)
    meter_number = Column(String(25), primary_key=True)
    smart_collectable = Column(Enum('0', '1', name='smart_collectable_types_enum'), nullable=True)
    brand = Column(String(25), nullable=False)
    sjv1 = Column(String(25), nullable=True)
    sjv2 = Column(String(25), nullable=True)
    installation = Column(String(25), nullable=True)
    division = Column(String(25), nullable=True)
    move_out_date = Column(TIMESTAMP, nullable=True)
    row_create_datetime = Column(TIMESTAMP, nullable=False)
    move_in_date = Column(TIMESTAMP, nullable=False)

