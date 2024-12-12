from sqlalchemy import Column, String, Enum, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MeterReadings(Base):
    __tablename__ = 'meter_readings'

    account_id = Column(String(25), primary_key=True)
    brand = Column(String(25), nullable=False)
    connection_ean_code = Column(String(50), ForeignKey('meter.connection_ean_code'), nullable=True)
    energy_type = Column(Enum('GAS', 'ELECTRICITY', name='energy_types_enum'), nullable=True)
    meter_number = Column(String(25), unique=True, nullable=True)
    reading_date = Column(Date, nullable=False)
    reading_electricity = Column(String(250), nullable=True)
    reading_gas = Column(String(250), nullable=True)
    rejection = Column(String(250), nullable=True)
    validation_status = Column(String(25), nullable=True)
