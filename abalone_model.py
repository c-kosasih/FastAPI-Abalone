from pydantic import BaseModel

class abalone(BaseModel):
    Sex : str
    Length : float
    Diameter : float
    Height : float
    Whole_weight : float
    Whole_weight_1 : float
    Whole_weight_2 : float
    Shell_weight : float 

    