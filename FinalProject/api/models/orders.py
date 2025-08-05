from sqlalchemy import Column, ForeignKey, Float, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    customer_phone = Column(String(20))
    customer_address = Column(String(200))
    customer_email = Column(String(200))

    total_price = Column(Float)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))
    status = Column(String(50))
    tracking_number = Column(String(50), unique=True)

    order_details = relationship("OrderDetail", back_populates="order")