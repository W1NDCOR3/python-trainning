from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy import create_engine
from alembic import context
import os

config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata object for autogenerate support (if using SQLAlchemy ORM models)
# from yourapp.models import Base
# target_metadata = Base.metadata
target_metadata = None

# Optionally set the SQLite URL dynamically if needed (e.g., via environment variable)
# DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./mydatabase.db')
# config.set_main_option('sqlalchemy.url', DATABASE_URL)

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
    # SQLite-specific engine configuration without pooling
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        connect_args={"check_same_thread": False},  # Necessary for SQLite in multi-threaded environments
        poolclass=pool.NullPool,  # Disable pooling for SQLite
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
