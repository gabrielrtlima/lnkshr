from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from app.models.url import Base  # Importe seu modelo Base
from app.core.config import settings  # Importe suas configurações

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interprete a seção [alembic] no arquivo alembic.ini
# e substitua as configurações do sqlalchemy.url com a DATABASE_URL do settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL_NEW)

# Adicione seu modelo MetaData aqui
# para 'autogenerate' suportar a criação de tabelas
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
