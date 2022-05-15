from sqlalchemy import Integer, Text, Column
from .database import Base


class DefaultStyleImage(Base):
    __tablename__ = "default_style_images"

    id = Column(Integer, primary_key=True, index=True)
    img_code = Column(Text)
