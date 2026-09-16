from pydantic import BaseModel, Field


class CategoriaCriar(BaseModel):
    nome: str = Field(min_length=2, max_length=60, description="Nome único da categoria")
    descricao: str | None = Field(default=None, max_length=255, description="Descrição opcional")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nome": "Rede",
                "descricao": "Problema de conexão, Wi-fi, VPN e cabeamento"
            }
        }
    )