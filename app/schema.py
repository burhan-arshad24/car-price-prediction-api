from enum import Enum

from pydantic import BaseModel, Field


class FuelType(str, Enum):
    petrol = "Petrol"
    diesel = "Diesel"
    cng = "CNG"


class SellerType(str, Enum):
    individual = "Individual"
    dealer = "Dealer"


class TransmissionType(str, Enum):
    manual = "Manual"
    automatic = "Automatic"


class CarFeatures(BaseModel):
    Car_Name: str = Field(
        ...,
        min_length=1,
        example="alto 800"
    )

    Year: int = Field(
        ...,
        example=2014
    )

    Present_Price: float = Field(
        ...,
        ge=0,
        example=5.5
    )

    Kms_Driven: float = Field(
        ...,
        ge=0,
        example=2184
    )

    Fuel_Type: FuelType

    Seller_Type: SellerType

    Transmission: TransmissionType

    Owner: int = Field(
        ...,
        ge=0,
        le=10,
        example=1
    )


class PredictionResponse(BaseModel):
    prediction_price: float