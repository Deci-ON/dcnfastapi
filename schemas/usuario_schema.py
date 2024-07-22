from typing import Optional, List
from pydantic import BaseModel, EmailStr, ValidationError, Field
from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        from_attributes = True
        
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]
    
class UsuarioSchemaUp(BaseModel):
    nome: Optional[str] = Field(default=None)
    sobrenome: Optional[str] = Field(default=None)
    email: Optional[EmailStr] = Field(default=None)
    senha: Optional[str] = Field(default=None)
    eh_admin: Optional[bool] = Field(default=None)

    class Config:
        from_attributes = True

