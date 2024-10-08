import os

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from core.database import Base


from dotenv import load_dotenv
from app.user import models
from app.game_character import models
from app.friend import models
from app.point import models
from app.activity import models
from app.social_media import models


load_dotenv()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

section = config.config_ini_section
# LOCAL
# config.set_section_option(section, "DB_USER", os.environ.get("DB_USER") or "")
# config.set_section_option(section, "DB_PASS", os.environ.get("DB_PASS") or "")
# config.set_section_option(section, "DB_PORT", os.environ.get("DB_PORT") or "")
# config.set_section_option(section, "DB_NAME", os.environ.get("DB_NAME") or "")
# config.set_section_option(section, "DB_HOST", os.environ.get("DB_HOST") or "")

# REMOTE
config.set_section_option(section, "TIDB_USER", os.environ.get("TIDB_USER") or "")
config.set_section_option(section, "TIDB_PASS", os.environ.get("TIDB_PASS") or "")
config.set_section_option(section, "TIDB_PORT", os.environ.get("TIDB_PORT") or "")
config.set_section_option(section, "TIDB_NAME", os.environ.get("TIDB_NAME") or "")
config.set_section_option(section, "TIDB_HOST", os.environ.get("TIDB_HOST") or "")

# Interpret the config file for Python logging.
# This line sets up loggers basically.
# if config.config_file_name is not None:
#     fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
target_metadata = [Base.metadata]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
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
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()