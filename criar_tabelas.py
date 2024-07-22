from core.configs import settings
from core.database import engine
import asyncio

async def create_tables() -> None:
    import models.__all_models  # Certifique-se de que este caminho está correto
    print('Criando as tabelas')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    
    print('Tabelas criadas com sucesso')

async def main():
    await create_tables()
    await engine.dispose()  # Certifique-se de que o engine é fechado corretamente

if __name__ == '__main__':
    asyncio.run(main())
