#! /usr/bin/env python3

import json


async def initialise_database(self) -> None:
    """
    Database function which initialises the PostgreSQL database.

    :param self: -
        Represents this object.

    :return: (None)
    """

    with open("schema.json", "r") as f:
        schema = json.load(f)

    async with self.database.acquire() as conn:
        for table_name, fields in schema.items():
            definitions = []
            for field_name, field_info in fields.items():
                constraint = field_info.get("constraints", "").strip()
                definitions.append(
                    f"{field_name} {field_info['type']} {constraint}"
                )
            table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(definitions)});"
            await conn.execute(table_query)


async def populate_experience_table(self, experience_table: dict) -> None:
    """
    Database function which populates the `experience_table`.

    :param self: -
        Represents this object.

    :return: (None)
    """

    async with self.database.acquire() as conn:
        for i in experience_table:
            await conn.execute(
                """
                INSERT INTO experience_table (level, total_experience, experience_difference)
                VALUES ($1, $2, $3)
                ON CONFLICT (level) DO NOTHING
                """,
                i["level"],
                i["total_experience"],
                i["experience_difference"]
            )
