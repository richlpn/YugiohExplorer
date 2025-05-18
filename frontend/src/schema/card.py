from pydantic import BaseModel, Field

class CardImages(BaseModel):
    """
    A class representing the images of a Yu-Gi-Oh! card.
    Attributes:
        id (str): The ID of the image.
        image_url (str): The URL of the image.
        image_url_small (str): The small version of the image URL.
    """
    id : int = Field(..., description="The ID of the image.")
    image_url : str = Field(..., description="The URL of the image.")
    image_url_small : str = Field(..., description="The small version of the image URL.")
    image_url_cropped : str = Field(..., description="The cropped version of the image URL.")

class Card (BaseModel):
    """
    A class representing a Yu-Gi-Oh! card.
    Attributes:
        name (str): The name of the card.
        description (str): A description of the card.
        image_urls (CardImages): The URL of the card's images.
    """
    name : str = Field(..., description="The name of the card.")
    desc : str = Field(..., description="A description of the card.")
    image_url : list[CardImages] = Field(..., description="The URL of the card's images.")
