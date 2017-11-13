from yoyo import step

step(
    "ALTER TABLE foo ADD COLUMN name text",
    "ALTER TABLE foo DROP COLUMN name"
)

